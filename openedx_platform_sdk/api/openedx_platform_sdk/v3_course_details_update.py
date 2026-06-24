from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.course_details import CourseDetails
from ...types import UNSET, Response


def _get_kwargs(
    course_id: str,
    *,
    body: CourseDetails | CourseDetails | CourseDetails | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v3/course_details/{course_id}/".format(
            course_id=quote(str(course_id), safe=""),
        ),
    }

    if isinstance(body, CourseDetails):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, CourseDetails):
        _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, CourseDetails):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | CourseDetails | None:
    if response.status_code == 200:
        response_200 = CourseDetails.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | CourseDetails]:
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
    body: CourseDetails | CourseDetails | CourseDetails | Unset = UNSET,
) -> Response[Any | CourseDetails]:
    """Update a course's details

     Update the details for the specified course.

    Args:
        course_id (str):
        body (CourseDetails): Serializer for course details
        body (CourseDetails): Serializer for course details
        body (CourseDetails): Serializer for course details

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CourseDetails]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    course_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CourseDetails | CourseDetails | CourseDetails | Unset = UNSET,
) -> Any | CourseDetails | None:
    """Update a course's details

     Update the details for the specified course.

    Args:
        course_id (str):
        body (CourseDetails): Serializer for course details
        body (CourseDetails): Serializer for course details
        body (CourseDetails): Serializer for course details

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CourseDetails
    """

    return sync_detailed(
        course_id=course_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    course_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CourseDetails | CourseDetails | CourseDetails | Unset = UNSET,
) -> Response[Any | CourseDetails]:
    """Update a course's details

     Update the details for the specified course.

    Args:
        course_id (str):
        body (CourseDetails): Serializer for course details
        body (CourseDetails): Serializer for course details
        body (CourseDetails): Serializer for course details

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CourseDetails]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    course_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CourseDetails | CourseDetails | CourseDetails | Unset = UNSET,
) -> Any | CourseDetails | None:
    """Update a course's details

     Update the details for the specified course.

    Args:
        course_id (str):
        body (CourseDetails): Serializer for course details
        body (CourseDetails): Serializer for course details
        body (CourseDetails): Serializer for course details

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CourseDetails
    """

    return (
        await asyncio_detailed(
            course_id=course_id,
            client=client,
            body=body,
        )
    ).parsed
