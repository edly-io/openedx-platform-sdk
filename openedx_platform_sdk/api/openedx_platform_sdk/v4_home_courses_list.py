from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.course_home_tab_serializer_v2 import CourseHomeTabSerializerV2
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    active_only: str | Unset = UNSET,
    archived_only: str | Unset = UNSET,
    order: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    org: str | Unset = UNSET,
    page: str | Unset = UNSET,
    page_size: str | Unset = UNSET,
    search: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["active_only"] = active_only

    params["archived_only"] = archived_only

    params["order"] = order

    params["ordering"] = ordering

    params["org"] = org

    params["page"] = page

    params["page_size"] = page_size

    params["search"] = search

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v4/home/courses/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | list[CourseHomeTabSerializerV2] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = CourseHomeTabSerializerV2.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | list[CourseHomeTabSerializerV2]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    active_only: str | Unset = UNSET,
    archived_only: str | Unset = UNSET,
    order: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    org: str | Unset = UNSET,
    page: str | Unset = UNSET,
    page_size: str | Unset = UNSET,
    search: str | Unset = UNSET,
) -> Response[Any | list[CourseHomeTabSerializerV2]]:
    """List courses for the Studio home page (paginated)

     Returns a paginated list of all courses available to the logged-in user, with optional filtering and
    ordering. Supersedes ``GET /api/contentstore/v2/home/courses``.

    Args:
        active_only (str | Unset):
        archived_only (str | Unset):
        order (str | Unset):
        ordering (str | Unset):
        org (str | Unset):
        page (str | Unset):
        page_size (str | Unset):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[CourseHomeTabSerializerV2]]
    """

    kwargs = _get_kwargs(
        active_only=active_only,
        archived_only=archived_only,
        order=order,
        ordering=ordering,
        org=org,
        page=page,
        page_size=page_size,
        search=search,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    active_only: str | Unset = UNSET,
    archived_only: str | Unset = UNSET,
    order: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    org: str | Unset = UNSET,
    page: str | Unset = UNSET,
    page_size: str | Unset = UNSET,
    search: str | Unset = UNSET,
) -> Any | list[CourseHomeTabSerializerV2] | None:
    """List courses for the Studio home page (paginated)

     Returns a paginated list of all courses available to the logged-in user, with optional filtering and
    ordering. Supersedes ``GET /api/contentstore/v2/home/courses``.

    Args:
        active_only (str | Unset):
        archived_only (str | Unset):
        order (str | Unset):
        ordering (str | Unset):
        org (str | Unset):
        page (str | Unset):
        page_size (str | Unset):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[CourseHomeTabSerializerV2]
    """

    return sync_detailed(
        client=client,
        active_only=active_only,
        archived_only=archived_only,
        order=order,
        ordering=ordering,
        org=org,
        page=page,
        page_size=page_size,
        search=search,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    active_only: str | Unset = UNSET,
    archived_only: str | Unset = UNSET,
    order: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    org: str | Unset = UNSET,
    page: str | Unset = UNSET,
    page_size: str | Unset = UNSET,
    search: str | Unset = UNSET,
) -> Response[Any | list[CourseHomeTabSerializerV2]]:
    """List courses for the Studio home page (paginated)

     Returns a paginated list of all courses available to the logged-in user, with optional filtering and
    ordering. Supersedes ``GET /api/contentstore/v2/home/courses``.

    Args:
        active_only (str | Unset):
        archived_only (str | Unset):
        order (str | Unset):
        ordering (str | Unset):
        org (str | Unset):
        page (str | Unset):
        page_size (str | Unset):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[CourseHomeTabSerializerV2]]
    """

    kwargs = _get_kwargs(
        active_only=active_only,
        archived_only=archived_only,
        order=order,
        ordering=ordering,
        org=org,
        page=page,
        page_size=page_size,
        search=search,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    active_only: str | Unset = UNSET,
    archived_only: str | Unset = UNSET,
    order: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    org: str | Unset = UNSET,
    page: str | Unset = UNSET,
    page_size: str | Unset = UNSET,
    search: str | Unset = UNSET,
) -> Any | list[CourseHomeTabSerializerV2] | None:
    """List courses for the Studio home page (paginated)

     Returns a paginated list of all courses available to the logged-in user, with optional filtering and
    ordering. Supersedes ``GET /api/contentstore/v2/home/courses``.

    Args:
        active_only (str | Unset):
        archived_only (str | Unset):
        order (str | Unset):
        ordering (str | Unset):
        org (str | Unset):
        page (str | Unset):
        page_size (str | Unset):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[CourseHomeTabSerializerV2]
    """

    return (
        await asyncio_detailed(
            client=client,
            active_only=active_only,
            archived_only=archived_only,
            order=order,
            ordering=ordering,
            org=org,
            page=page,
            page_size=page_size,
            search=search,
        )
    ).parsed
