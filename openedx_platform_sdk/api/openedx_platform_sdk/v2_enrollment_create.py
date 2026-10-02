from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.course_enrollment import CourseEnrollment
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CourseEnrollment | CourseEnrollment | CourseEnrollment | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/enrollment/",
    }

    if isinstance(body, CourseEnrollment):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | CourseEnrollment | None:
    if response.status_code == 200:
        response_200 = CourseEnrollment.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

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
    *,
    client: AuthenticatedClient | Client,
    body: CourseEnrollment | CourseEnrollment | CourseEnrollment | Unset = UNSET,
) -> Response[Any | CourseEnrollment]:
    """Create or update an enrollment

     Enrolls a user in a course. Server-to-server calls may deactivate or modify the mode of existing
    enrollments; all other requests create or reactivate enrollments. The request body must include
    course_details.course_id.

    Args:
        body (CourseEnrollment): Serializes CourseEnrollment models

            Aggregates all data from the Course Enrollment table, and pulls in the serialization for
            the Course block and course modes, to give a complete representation of course enrollment.
        body (CourseEnrollment): Serializes CourseEnrollment models

            Aggregates all data from the Course Enrollment table, and pulls in the serialization for
            the Course block and course modes, to give a complete representation of course enrollment.
        body (CourseEnrollment): Serializes CourseEnrollment models

            Aggregates all data from the Course Enrollment table, and pulls in the serialization for
            the Course block and course modes, to give a complete representation of course enrollment.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CourseEnrollment]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: CourseEnrollment | CourseEnrollment | CourseEnrollment | Unset = UNSET,
) -> Any | CourseEnrollment | None:
    """Create or update an enrollment

     Enrolls a user in a course. Server-to-server calls may deactivate or modify the mode of existing
    enrollments; all other requests create or reactivate enrollments. The request body must include
    course_details.course_id.

    Args:
        body (CourseEnrollment): Serializes CourseEnrollment models

            Aggregates all data from the Course Enrollment table, and pulls in the serialization for
            the Course block and course modes, to give a complete representation of course enrollment.
        body (CourseEnrollment): Serializes CourseEnrollment models

            Aggregates all data from the Course Enrollment table, and pulls in the serialization for
            the Course block and course modes, to give a complete representation of course enrollment.
        body (CourseEnrollment): Serializes CourseEnrollment models

            Aggregates all data from the Course Enrollment table, and pulls in the serialization for
            the Course block and course modes, to give a complete representation of course enrollment.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CourseEnrollment
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CourseEnrollment | CourseEnrollment | CourseEnrollment | Unset = UNSET,
) -> Response[Any | CourseEnrollment]:
    """Create or update an enrollment

     Enrolls a user in a course. Server-to-server calls may deactivate or modify the mode of existing
    enrollments; all other requests create or reactivate enrollments. The request body must include
    course_details.course_id.

    Args:
        body (CourseEnrollment): Serializes CourseEnrollment models

            Aggregates all data from the Course Enrollment table, and pulls in the serialization for
            the Course block and course modes, to give a complete representation of course enrollment.
        body (CourseEnrollment): Serializes CourseEnrollment models

            Aggregates all data from the Course Enrollment table, and pulls in the serialization for
            the Course block and course modes, to give a complete representation of course enrollment.
        body (CourseEnrollment): Serializes CourseEnrollment models

            Aggregates all data from the Course Enrollment table, and pulls in the serialization for
            the Course block and course modes, to give a complete representation of course enrollment.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CourseEnrollment]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CourseEnrollment | CourseEnrollment | CourseEnrollment | Unset = UNSET,
) -> Any | CourseEnrollment | None:
    """Create or update an enrollment

     Enrolls a user in a course. Server-to-server calls may deactivate or modify the mode of existing
    enrollments; all other requests create or reactivate enrollments. The request body must include
    course_details.course_id.

    Args:
        body (CourseEnrollment): Serializes CourseEnrollment models

            Aggregates all data from the Course Enrollment table, and pulls in the serialization for
            the Course block and course modes, to give a complete representation of course enrollment.
        body (CourseEnrollment): Serializes CourseEnrollment models

            Aggregates all data from the Course Enrollment table, and pulls in the serialization for
            the Course block and course modes, to give a complete representation of course enrollment.
        body (CourseEnrollment): Serializes CourseEnrollment models

            Aggregates all data from the Course Enrollment table, and pulls in the serialization for
            the Course block and course modes, to give a complete representation of course enrollment.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CourseEnrollment
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
