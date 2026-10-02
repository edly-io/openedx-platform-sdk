from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_course_enrollments_api_list_list import PaginatedCourseEnrollmentsApiListList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    course_id: str | Unset = UNSET,
    course_ids: str | Unset = UNSET,
    course_key: str | Unset = UNSET,
    course_keys: str | Unset = UNSET,
    email: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    page: str | Unset = UNSET,
    page_size: str | Unset = UNSET,
    username: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["course_id"] = course_id

    params["course_ids"] = course_ids

    params["course_key"] = course_key

    params["course_keys"] = course_keys

    params["email"] = email

    params["ordering"] = ordering

    params["page"] = page

    params["page_size"] = page_size

    params["username"] = username

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/enrollments/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PaginatedCourseEnrollmentsApiListList | None:
    if response.status_code == 200:
        response_200 = PaginatedCourseEnrollmentsApiListList.from_dict(response.json())

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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | PaginatedCourseEnrollmentsApiListList]:
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
    course_ids: str | Unset = UNSET,
    course_key: str | Unset = UNSET,
    course_keys: str | Unset = UNSET,
    email: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    page: str | Unset = UNSET,
    page_size: str | Unset = UNSET,
    username: str | Unset = UNSET,
) -> Response[Any | PaginatedCourseEnrollmentsApiListList]:
    """List all course enrollments (admin-only, paginated)

     Admin-only paginated list of CourseEnrollment records, optionally filtered by course_key,
    course_keys, username, or email, and optionally ordered.

    Args:
        course_id (str | Unset):
        course_ids (str | Unset):
        course_key (str | Unset):
        course_keys (str | Unset):
        email (str | Unset):
        ordering (str | Unset):
        page (str | Unset):
        page_size (str | Unset):
        username (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PaginatedCourseEnrollmentsApiListList]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        course_ids=course_ids,
        course_key=course_key,
        course_keys=course_keys,
        email=email,
        ordering=ordering,
        page=page,
        page_size=page_size,
        username=username,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    course_id: str | Unset = UNSET,
    course_ids: str | Unset = UNSET,
    course_key: str | Unset = UNSET,
    course_keys: str | Unset = UNSET,
    email: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    page: str | Unset = UNSET,
    page_size: str | Unset = UNSET,
    username: str | Unset = UNSET,
) -> Any | PaginatedCourseEnrollmentsApiListList | None:
    """List all course enrollments (admin-only, paginated)

     Admin-only paginated list of CourseEnrollment records, optionally filtered by course_key,
    course_keys, username, or email, and optionally ordered.

    Args:
        course_id (str | Unset):
        course_ids (str | Unset):
        course_key (str | Unset):
        course_keys (str | Unset):
        email (str | Unset):
        ordering (str | Unset):
        page (str | Unset):
        page_size (str | Unset):
        username (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PaginatedCourseEnrollmentsApiListList
    """

    return sync_detailed(
        client=client,
        course_id=course_id,
        course_ids=course_ids,
        course_key=course_key,
        course_keys=course_keys,
        email=email,
        ordering=ordering,
        page=page,
        page_size=page_size,
        username=username,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    course_id: str | Unset = UNSET,
    course_ids: str | Unset = UNSET,
    course_key: str | Unset = UNSET,
    course_keys: str | Unset = UNSET,
    email: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    page: str | Unset = UNSET,
    page_size: str | Unset = UNSET,
    username: str | Unset = UNSET,
) -> Response[Any | PaginatedCourseEnrollmentsApiListList]:
    """List all course enrollments (admin-only, paginated)

     Admin-only paginated list of CourseEnrollment records, optionally filtered by course_key,
    course_keys, username, or email, and optionally ordered.

    Args:
        course_id (str | Unset):
        course_ids (str | Unset):
        course_key (str | Unset):
        course_keys (str | Unset):
        email (str | Unset):
        ordering (str | Unset):
        page (str | Unset):
        page_size (str | Unset):
        username (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PaginatedCourseEnrollmentsApiListList]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        course_ids=course_ids,
        course_key=course_key,
        course_keys=course_keys,
        email=email,
        ordering=ordering,
        page=page,
        page_size=page_size,
        username=username,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    course_id: str | Unset = UNSET,
    course_ids: str | Unset = UNSET,
    course_key: str | Unset = UNSET,
    course_keys: str | Unset = UNSET,
    email: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    page: str | Unset = UNSET,
    page_size: str | Unset = UNSET,
    username: str | Unset = UNSET,
) -> Any | PaginatedCourseEnrollmentsApiListList | None:
    """List all course enrollments (admin-only, paginated)

     Admin-only paginated list of CourseEnrollment records, optionally filtered by course_key,
    course_keys, username, or email, and optionally ordered.

    Args:
        course_id (str | Unset):
        course_ids (str | Unset):
        course_key (str | Unset):
        course_keys (str | Unset):
        email (str | Unset):
        ordering (str | Unset):
        page (str | Unset):
        page_size (str | Unset):
        username (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PaginatedCourseEnrollmentsApiListList
    """

    return (
        await asyncio_detailed(
            client=client,
            course_id=course_id,
            course_ids=course_ids,
            course_key=course_key,
            course_keys=course_keys,
            email=email,
            ordering=ordering,
            page=page,
            page_size=page_size,
            username=username,
        )
    ).parsed
