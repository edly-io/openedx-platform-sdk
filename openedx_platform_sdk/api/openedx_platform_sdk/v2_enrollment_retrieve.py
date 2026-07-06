from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.course_enrollment import CourseEnrollment
from ...types import Response


def _get_kwargs(
    username: str,
    course_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/enrollment/{username},{course_id}".format(
            username=quote(str(username), safe=""),
            course_id=quote(str(course_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | CourseEnrollment | None:
    if response.status_code == 200:
        response_200 = CourseEnrollment.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | CourseEnrollment]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    username: str,
    course_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | CourseEnrollment]:
    """Retrieve a user's enrollment in a course

     Returns the current user's enrollment for the specified course, or the named user's enrollment when
    invoked with the {username},{course_id} URL form (server-to-server or staff only).

    Args:
        username (str):
        course_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CourseEnrollment]
    """

    kwargs = _get_kwargs(
        username=username,
        course_id=course_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    username: str,
    course_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | CourseEnrollment | None:
    """Retrieve a user's enrollment in a course

     Returns the current user's enrollment for the specified course, or the named user's enrollment when
    invoked with the {username},{course_id} URL form (server-to-server or staff only).

    Args:
        username (str):
        course_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CourseEnrollment
    """

    return sync_detailed(
        username=username,
        course_id=course_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    username: str,
    course_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | CourseEnrollment]:
    """Retrieve a user's enrollment in a course

     Returns the current user's enrollment for the specified course, or the named user's enrollment when
    invoked with the {username},{course_id} URL form (server-to-server or staff only).

    Args:
        username (str):
        course_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CourseEnrollment]
    """

    kwargs = _get_kwargs(
        username=username,
        course_id=course_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    username: str,
    course_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | CourseEnrollment | None:
    """Retrieve a user's enrollment in a course

     Returns the current user's enrollment for the specified course, or the named user's enrollment when
    invoked with the {username},{course_id} URL form (server-to-server or staff only).

    Args:
        username (str):
        course_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CourseEnrollment
    """

    return (
        await asyncio_detailed(
            username=username,
            course_id=course_id,
            client=client,
        )
    ).parsed
