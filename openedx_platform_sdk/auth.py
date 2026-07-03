"""
OAuth2 authentication helpers for the OpenedX Authoring SDK.

OpenedX Studio uses JWT tokens obtained via the OAuth2 client_credentials flow.
The Authorization header must use the "JWT" prefix (not "Bearer").

Usage:
    from openedx_platform_sdk.auth import OAuth2ClientCredentials
    from openedx_platform_sdk import AuthenticatedClient

    auth = OAuth2ClientCredentials(
        lms_url="http://localhost:18000",
        client_id="your-client-id",
        client_secret="your-client-secret",
    )

    client = auth.get_client(studio_url="http://localhost:18010")

    # Use with context manager (recommended)
    with auth.get_client(studio_url="http://localhost:18010") as client:
        result = some_api.sync(client=client)

    # Token auto-refreshes on the next get_client() call once expired.
"""

import time
from typing import Optional

import httpx

from openedx_platform_sdk.client import AuthenticatedClient


class OAuth2ClientCredentials:
    """
    Fetches and caches a JWT token from the OpenedX LMS OAuth2 endpoint.
    Automatically refreshes when the token is within `refresh_buffer_seconds` of expiry.
    """

    TOKEN_ENDPOINT = "/oauth2/access_token"

    def __init__(
        self,
        lms_url: str,
        client_id: str,
        client_secret: str,
        refresh_buffer_seconds: int = 60,
        verify_ssl: bool = True,
    ):
        """
        Args:
            lms_url: Base URL of the LMS (e.g. "http://localhost:18000")
            client_id: OAuth2 client ID registered in the LMS
            client_secret: OAuth2 client secret
            refresh_buffer_seconds: Refresh the token this many seconds before it expires
            verify_ssl: Whether to verify SSL certificates
        """
        self.lms_url = lms_url.rstrip("/")
        self.client_id = client_id
        self.client_secret = client_secret
        self.refresh_buffer_seconds = refresh_buffer_seconds
        self.verify_ssl = verify_ssl

        self._token: Optional[str] = None
        self._expires_at: float = 0.0

    def _fetch_token(self) -> None:
        response = httpx.post(
            f"{self.lms_url}{self.TOKEN_ENDPOINT}",
            data={
                "grant_type": "client_credentials",
                "client_id": self.client_id,
                "client_secret": self.client_secret,
                "token_type": "jwt",
            },
            verify=self.verify_ssl,
        )
        response.raise_for_status()
        data = response.json()
        self._token = data["access_token"]
        expires_in = data.get("expires_in", 3600)
        self._expires_at = time.monotonic() + expires_in

    def get_token(self) -> str:
        """Return a valid JWT token, fetching or refreshing as needed."""
        if self._token is None or time.monotonic() >= (self._expires_at - self.refresh_buffer_seconds):
            self._fetch_token()
        return self._token  # type: ignore[return-value]

    def get_client(
        self,
        studio_url: str,
        raise_on_unexpected_status: bool = False,
        verify_ssl: Optional[bool] = None,
        **kwargs,
    ) -> AuthenticatedClient:
        """
        Return an AuthenticatedClient pre-configured with a valid JWT token.

        Args:
            studio_url: Base URL of Studio (e.g. "http://localhost:18010/api/contentstore")
            raise_on_unexpected_status: Raise on undocumented status codes
            verify_ssl: Override SSL verification for the Studio client
            **kwargs: Additional arguments forwarded to AuthenticatedClient
        """
        headers = kwargs.pop("headers", {})
        headers.setdefault("Accept", "application/json")
        return AuthenticatedClient(
            base_url=studio_url.rstrip("/"),
            token=self.get_token(),
            prefix="JWT",
            raise_on_unexpected_status=raise_on_unexpected_status,
            verify_ssl=verify_ssl if verify_ssl is not None else self.verify_ssl,
            headers=headers,
            **kwargs,
        )
