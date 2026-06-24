"""A client library for accessing Authoring API"""

from .auth import OAuth2ClientCredentials
from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
    "OAuth2ClientCredentials",
)
