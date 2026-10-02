from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.enrollment_course import EnrollmentCourse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    course_id: str,
    *,
    include_expired: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["include_expired"] = include_expired

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/course/{course_id}".format(
            course_id=quote(str(course_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | EnrollmentCourse | None:
    if response.status_code == 200:
        response_200 = EnrollmentCourse.from_dict(response.json())

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
) -> Response[Any | EnrollmentCourse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    course_id: str,
    *,
    client: AuthenticatedClient | Client,
    include_expired: str | Unset = UNSET,
) -> Response[Any | EnrollmentCourse]:
    """Get enrollment details for a course

     Returns the course schedule and supported enrollment modes. No authentication required. Use
    ?include_expired=1 to include expired enrollment modes.

    Args:
        course_id (str):
        include_expired (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | EnrollmentCourse]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        include_expired=include_expired,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    course_id: str,
    *,
    client: AuthenticatedClient | Client,
    include_expired: str | Unset = UNSET,
) -> Any | EnrollmentCourse | None:
    """Get enrollment details for a course

     Returns the course schedule and supported enrollment modes. No authentication required. Use
    ?include_expired=1 to include expired enrollment modes.

    Args:
        course_id (str):
        include_expired (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | EnrollmentCourse
    """

    return sync_detailed(
        course_id=course_id,
        client=client,
        include_expired=include_expired,
    ).parsed


async def asyncio_detailed(
    course_id: str,
    *,
    client: AuthenticatedClient | Client,
    include_expired: str | Unset = UNSET,
) -> Response[Any | EnrollmentCourse]:
    """Get enrollment details for a course

     Returns the course schedule and supported enrollment modes. No authentication required. Use
    ?include_expired=1 to include expired enrollment modes.

    Args:
        course_id (str):
        include_expired (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | EnrollmentCourse]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        include_expired=include_expired,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    course_id: str,
    *,
    client: AuthenticatedClient | Client,
    include_expired: str | Unset = UNSET,
) -> Any | EnrollmentCourse | None:
    """Get enrollment details for a course

     Returns the course schedule and supported enrollment modes. No authentication required. Use
    ?include_expired=1 to include expired enrollment modes.

    Args:
        course_id (str):
        include_expired (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | EnrollmentCourse
    """

    return (
        await asyncio_detailed(
            course_id=course_id,
            client=client,
            include_expired=include_expired,
        )
    ).parsed
