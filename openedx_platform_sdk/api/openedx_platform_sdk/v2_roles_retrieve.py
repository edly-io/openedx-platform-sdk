from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.user_roles_response import UserRolesResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    course_id: str | Unset = UNSET,
    course_key: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["course_id"] = course_id

    params["course_key"] = course_key

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/roles/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | UserRolesResponse | None:
    if response.status_code == 200:
        response_200 = UserRolesResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | UserRolesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    course_id: str | Unset = UNSET,
    course_key: str | Unset = UNSET,
) -> Response[Any | UserRolesResponse]:
    """List the current user's course roles

     Returns the list of course-level roles held by the currently logged-in user, plus an is_staff flag.
    Optionally filters by course_key (or course_id, deprecated).

    Args:
        course_id (str | Unset):
        course_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | UserRolesResponse]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        course_key=course_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    course_id: str | Unset = UNSET,
    course_key: str | Unset = UNSET,
) -> Any | UserRolesResponse | None:
    """List the current user's course roles

     Returns the list of course-level roles held by the currently logged-in user, plus an is_staff flag.
    Optionally filters by course_key (or course_id, deprecated).

    Args:
        course_id (str | Unset):
        course_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | UserRolesResponse
    """

    return sync_detailed(
        client=client,
        course_id=course_id,
        course_key=course_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    course_id: str | Unset = UNSET,
    course_key: str | Unset = UNSET,
) -> Response[Any | UserRolesResponse]:
    """List the current user's course roles

     Returns the list of course-level roles held by the currently logged-in user, plus an is_staff flag.
    Optionally filters by course_key (or course_id, deprecated).

    Args:
        course_id (str | Unset):
        course_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | UserRolesResponse]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        course_key=course_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    course_id: str | Unset = UNSET,
    course_key: str | Unset = UNSET,
) -> Any | UserRolesResponse | None:
    """List the current user's course roles

     Returns the list of course-level roles held by the currently logged-in user, plus an is_staff flag.
    Optionally filters by course_key (or course_id, deprecated).

    Args:
        course_id (str | Unset):
        course_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | UserRolesResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            course_id=course_id,
            course_key=course_key,
        )
    ).parsed
