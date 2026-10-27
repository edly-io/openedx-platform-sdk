from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.library_tab import LibraryTab
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    is_migrated: bool | Unset = UNSET,
    org: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["is_migrated"] = is_migrated

    params["org"] = org

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/contentstore/v3/home/libraries/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | LibraryTab | None:
    if response.status_code == 200:
        response_200 = LibraryTab.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | LibraryTab]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    is_migrated: bool | Unset = UNSET,
    org: str | Unset = UNSET,
) -> Response[Any | LibraryTab]:
    """Get an object containing all libraries on home page.

    **Example Request**

        GET /api/contentstore/v3/home/libraries/

    Args:
        is_migrated (bool | Unset):
        org (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | LibraryTab]
    """

    kwargs = _get_kwargs(
        is_migrated=is_migrated,
        org=org,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    is_migrated: bool | Unset = UNSET,
    org: str | Unset = UNSET,
) -> Any | LibraryTab | None:
    """Get an object containing all libraries on home page.

    **Example Request**

        GET /api/contentstore/v3/home/libraries/

    Args:
        is_migrated (bool | Unset):
        org (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | LibraryTab
    """

    return sync_detailed(
        client=client,
        is_migrated=is_migrated,
        org=org,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    is_migrated: bool | Unset = UNSET,
    org: str | Unset = UNSET,
) -> Response[Any | LibraryTab]:
    """Get an object containing all libraries on home page.

    **Example Request**

        GET /api/contentstore/v3/home/libraries/

    Args:
        is_migrated (bool | Unset):
        org (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | LibraryTab]
    """

    kwargs = _get_kwargs(
        is_migrated=is_migrated,
        org=org,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    is_migrated: bool | Unset = UNSET,
    org: str | Unset = UNSET,
) -> Any | LibraryTab | None:
    """Get an object containing all libraries on home page.

    **Example Request**

        GET /api/contentstore/v3/home/libraries/

    Args:
        is_migrated (bool | Unset):
        org (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | LibraryTab
    """

    return (
        await asyncio_detailed(
            client=client,
            is_migrated=is_migrated,
            org=org,
        )
    ).parsed
