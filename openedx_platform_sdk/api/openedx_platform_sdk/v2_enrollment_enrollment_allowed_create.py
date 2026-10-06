from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.course_enrollment_allowed import CourseEnrollmentAllowed
from ...models.paginated_course_enrollment_allowed_list import PaginatedCourseEnrollmentAllowedList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CourseEnrollmentAllowed | CourseEnrollmentAllowed | CourseEnrollmentAllowed | Unset = UNSET,
    email: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["email"] = email

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/enrollment/enrollment_allowed/",
        "params": params,
    }

    if isinstance(body, CourseEnrollmentAllowed):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | CourseEnrollmentAllowed | PaginatedCourseEnrollmentAllowedList | None:
    if response.status_code == 200:
        response_200 = PaginatedCourseEnrollmentAllowedList.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = CourseEnrollmentAllowed.from_dict(response.json())

        return response_201

    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if response.status_code == 409:
        response_409 = cast(Any, None)
        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | CourseEnrollmentAllowed | PaginatedCourseEnrollmentAllowedList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CourseEnrollmentAllowed | CourseEnrollmentAllowed | CourseEnrollmentAllowed | Unset = UNSET,
    email: str | Unset = UNSET,
) -> Response[Any | CourseEnrollmentAllowed | PaginatedCourseEnrollmentAllowedList]:
    """Manage CourseEnrollmentAllowed records (admin-only)

     GET lists allowed enrollments for an email; POST creates a new one; DELETE removes an existing one
    by email + course_id. Admin-only.

    Args:
        email (str | Unset):
        body (CourseEnrollmentAllowed): Serializes CourseEnrollmentAllowed model

            Aggregates all data from the CourseEnrollmentAllowed table, and pulls in the serialization
            to give a complete representation of course enrollment allowed.
        body (CourseEnrollmentAllowed): Serializes CourseEnrollmentAllowed model

            Aggregates all data from the CourseEnrollmentAllowed table, and pulls in the serialization
            to give a complete representation of course enrollment allowed.
        body (CourseEnrollmentAllowed): Serializes CourseEnrollmentAllowed model

            Aggregates all data from the CourseEnrollmentAllowed table, and pulls in the serialization
            to give a complete representation of course enrollment allowed.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CourseEnrollmentAllowed | PaginatedCourseEnrollmentAllowedList]
    """

    kwargs = _get_kwargs(
        body=body,
        email=email,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: CourseEnrollmentAllowed | CourseEnrollmentAllowed | CourseEnrollmentAllowed | Unset = UNSET,
    email: str | Unset = UNSET,
) -> Any | CourseEnrollmentAllowed | PaginatedCourseEnrollmentAllowedList | None:
    """Manage CourseEnrollmentAllowed records (admin-only)

     GET lists allowed enrollments for an email; POST creates a new one; DELETE removes an existing one
    by email + course_id. Admin-only.

    Args:
        email (str | Unset):
        body (CourseEnrollmentAllowed): Serializes CourseEnrollmentAllowed model

            Aggregates all data from the CourseEnrollmentAllowed table, and pulls in the serialization
            to give a complete representation of course enrollment allowed.
        body (CourseEnrollmentAllowed): Serializes CourseEnrollmentAllowed model

            Aggregates all data from the CourseEnrollmentAllowed table, and pulls in the serialization
            to give a complete representation of course enrollment allowed.
        body (CourseEnrollmentAllowed): Serializes CourseEnrollmentAllowed model

            Aggregates all data from the CourseEnrollmentAllowed table, and pulls in the serialization
            to give a complete representation of course enrollment allowed.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CourseEnrollmentAllowed | PaginatedCourseEnrollmentAllowedList
    """

    return sync_detailed(
        client=client,
        body=body,
        email=email,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CourseEnrollmentAllowed | CourseEnrollmentAllowed | CourseEnrollmentAllowed | Unset = UNSET,
    email: str | Unset = UNSET,
) -> Response[Any | CourseEnrollmentAllowed | PaginatedCourseEnrollmentAllowedList]:
    """Manage CourseEnrollmentAllowed records (admin-only)

     GET lists allowed enrollments for an email; POST creates a new one; DELETE removes an existing one
    by email + course_id. Admin-only.

    Args:
        email (str | Unset):
        body (CourseEnrollmentAllowed): Serializes CourseEnrollmentAllowed model

            Aggregates all data from the CourseEnrollmentAllowed table, and pulls in the serialization
            to give a complete representation of course enrollment allowed.
        body (CourseEnrollmentAllowed): Serializes CourseEnrollmentAllowed model

            Aggregates all data from the CourseEnrollmentAllowed table, and pulls in the serialization
            to give a complete representation of course enrollment allowed.
        body (CourseEnrollmentAllowed): Serializes CourseEnrollmentAllowed model

            Aggregates all data from the CourseEnrollmentAllowed table, and pulls in the serialization
            to give a complete representation of course enrollment allowed.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CourseEnrollmentAllowed | PaginatedCourseEnrollmentAllowedList]
    """

    kwargs = _get_kwargs(
        body=body,
        email=email,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CourseEnrollmentAllowed | CourseEnrollmentAllowed | CourseEnrollmentAllowed | Unset = UNSET,
    email: str | Unset = UNSET,
) -> Any | CourseEnrollmentAllowed | PaginatedCourseEnrollmentAllowedList | None:
    """Manage CourseEnrollmentAllowed records (admin-only)

     GET lists allowed enrollments for an email; POST creates a new one; DELETE removes an existing one
    by email + course_id. Admin-only.

    Args:
        email (str | Unset):
        body (CourseEnrollmentAllowed): Serializes CourseEnrollmentAllowed model

            Aggregates all data from the CourseEnrollmentAllowed table, and pulls in the serialization
            to give a complete representation of course enrollment allowed.
        body (CourseEnrollmentAllowed): Serializes CourseEnrollmentAllowed model

            Aggregates all data from the CourseEnrollmentAllowed table, and pulls in the serialization
            to give a complete representation of course enrollment allowed.
        body (CourseEnrollmentAllowed): Serializes CourseEnrollmentAllowed model

            Aggregates all data from the CourseEnrollmentAllowed table, and pulls in the serialization
            to give a complete representation of course enrollment allowed.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CourseEnrollmentAllowed | PaginatedCourseEnrollmentAllowedList
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            email=email,
        )
    ).parsed
