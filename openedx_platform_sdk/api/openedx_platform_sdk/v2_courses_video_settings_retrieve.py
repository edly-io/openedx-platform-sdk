from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.course_video_settings import CourseVideoSettings
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    course_key: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/authoring/v2/courses/{course_key}/video_settings/".format(
            course_key=quote(str(course_key), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CourseVideoSettings | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = CourseVideoSettings.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CourseVideoSettings | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    course_key: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[CourseVideoSettings | ErrorResponse]:
    """Retrieve a course's video settings

     Returns the course's video upload limits, thumbnail image limits, transcript settings and the Studio
    addresses that act on them. The course's uploaded videos are listed by `GET
    /api/authoring/v1/courses/{course_key}/videos/`.

    Args:
        course_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CourseVideoSettings | ErrorResponse]
    """

    kwargs = _get_kwargs(
        course_key=course_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    course_key: str,
    *,
    client: AuthenticatedClient | Client,
) -> CourseVideoSettings | ErrorResponse | None:
    """Retrieve a course's video settings

     Returns the course's video upload limits, thumbnail image limits, transcript settings and the Studio
    addresses that act on them. The course's uploaded videos are listed by `GET
    /api/authoring/v1/courses/{course_key}/videos/`.

    Args:
        course_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CourseVideoSettings | ErrorResponse
    """

    return sync_detailed(
        course_key=course_key,
        client=client,
    ).parsed


async def asyncio_detailed(
    course_key: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[CourseVideoSettings | ErrorResponse]:
    """Retrieve a course's video settings

     Returns the course's video upload limits, thumbnail image limits, transcript settings and the Studio
    addresses that act on them. The course's uploaded videos are listed by `GET
    /api/authoring/v1/courses/{course_key}/videos/`.

    Args:
        course_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CourseVideoSettings | ErrorResponse]
    """

    kwargs = _get_kwargs(
        course_key=course_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    course_key: str,
    *,
    client: AuthenticatedClient | Client,
) -> CourseVideoSettings | ErrorResponse | None:
    """Retrieve a course's video settings

     Returns the course's video upload limits, thumbnail image limits, transcript settings and the Studio
    addresses that act on them. The course's uploaded videos are listed by `GET
    /api/authoring/v1/courses/{course_key}/videos/`.

    Args:
        course_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CourseVideoSettings | ErrorResponse
    """

    return (
        await asyncio_detailed(
            course_key=course_key,
            client=client,
        )
    ).parsed
