from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    usage_key_string: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/xblock/{usage_key_string}/".format(
            usage_key_string=quote(str(usage_key_string), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 204:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    usage_key_string: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any]:
    """ViewSet for xblock CRUD operations (v1 — ADR 0028).

    Router-generated URLs:
      POST   /api/contentstore/v1/xblock/                      → create
      GET    /api/contentstore/v1/xblock/{usage_key_string}/   → retrieve
      PUT    /api/contentstore/v1/xblock/{usage_key_string}/   → update
      PATCH  /api/contentstore/v1/xblock/{usage_key_string}/   → partial_update
      DELETE /api/contentstore/v1/xblock/{usage_key_string}/   → destroy

    Query parameters (ADR 0036, GET only):
      ?view=minimal   Drop heavy / contextual fields from the response,
                      keeping only structural fields (id, display_name,
                      category, children, has_children, studio_url).
                      Default response is the full xblock payload.

    Args:
        usage_key_string (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        usage_key_string=usage_key_string,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    usage_key_string: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any]:
    """ViewSet for xblock CRUD operations (v1 — ADR 0028).

    Router-generated URLs:
      POST   /api/contentstore/v1/xblock/                      → create
      GET    /api/contentstore/v1/xblock/{usage_key_string}/   → retrieve
      PUT    /api/contentstore/v1/xblock/{usage_key_string}/   → update
      PATCH  /api/contentstore/v1/xblock/{usage_key_string}/   → partial_update
      DELETE /api/contentstore/v1/xblock/{usage_key_string}/   → destroy

    Query parameters (ADR 0036, GET only):
      ?view=minimal   Drop heavy / contextual fields from the response,
                      keeping only structural fields (id, display_name,
                      category, children, has_children, studio_url).
                      Default response is the full xblock payload.

    Args:
        usage_key_string (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        usage_key_string=usage_key_string,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
