from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.studio_home import StudioHome
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    fields: str | Unset = UNSET,
    org: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["fields"] = fields

    params["org"] = org

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/home/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> StudioHome | None:
    if response.status_code == 200:
        response_200 = StudioHome.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[StudioHome]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    fields: str | Unset = UNSET,
    org: str | Unset = UNSET,
) -> Response[StudioHome]:
    """Get an object containing all courses and libraries on home page.

    **Example Request**

        GET /api/contentstore/v3/home/
        GET /api/contentstore/v3/home/?fields=courses,libraries  (ADR 0036)

    Args:
        fields (str | Unset):
        org (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StudioHome]
    """

    kwargs = _get_kwargs(
        fields=fields,
        org=org,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    fields: str | Unset = UNSET,
    org: str | Unset = UNSET,
) -> StudioHome | None:
    """Get an object containing all courses and libraries on home page.

    **Example Request**

        GET /api/contentstore/v3/home/
        GET /api/contentstore/v3/home/?fields=courses,libraries  (ADR 0036)

    Args:
        fields (str | Unset):
        org (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StudioHome
    """

    return sync_detailed(
        client=client,
        fields=fields,
        org=org,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    fields: str | Unset = UNSET,
    org: str | Unset = UNSET,
) -> Response[StudioHome]:
    """Get an object containing all courses and libraries on home page.

    **Example Request**

        GET /api/contentstore/v3/home/
        GET /api/contentstore/v3/home/?fields=courses,libraries  (ADR 0036)

    Args:
        fields (str | Unset):
        org (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StudioHome]
    """

    kwargs = _get_kwargs(
        fields=fields,
        org=org,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    fields: str | Unset = UNSET,
    org: str | Unset = UNSET,
) -> StudioHome | None:
    """Get an object containing all courses and libraries on home page.

    **Example Request**

        GET /api/contentstore/v3/home/
        GET /api/contentstore/v3/home/?fields=courses,libraries  (ADR 0036)

    Args:
        fields (str | Unset):
        org (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StudioHome
    """

    return (
        await asyncio_detailed(
            client=client,
            fields=fields,
            org=org,
        )
    ).parsed
