from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_course_enrollment_list import PaginatedCourseEnrollmentList
from ...models.v2_enrollment_list_view import V2EnrollmentListView
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: str | Unset = UNSET,
    page_size: str | Unset = UNSET,
    user: str | Unset = UNSET,
    view: V2EnrollmentListView | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["page_size"] = page_size

    params["user"] = user

    json_view: str | Unset = UNSET
    if not isinstance(view, Unset):
        json_view = view.value

    params["view"] = json_view

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/enrollment/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PaginatedCourseEnrollmentList | None:
    if response.status_code == 200:
        response_200 = PaginatedCourseEnrollmentList.from_dict(response.json())

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
) -> Response[Any | PaginatedCourseEnrollmentList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: str | Unset = UNSET,
    page_size: str | Unset = UNSET,
    user: str | Unset = UNSET,
    view: V2EnrollmentListView | Unset = UNSET,
) -> Response[Any | PaginatedCourseEnrollmentList]:
    """List enrollments for a user (paginated)

     Returns a paginated list of enrollments for the currently logged-in user, or for the user named by
    the 'user' query parameter. Staff/admin/api-key access is required to view another user's
    enrollments — otherwise the list is filtered to courses the requester staffs. Supports the ADR 0036
    ``?view=minimal`` preset (see parameter description).

    Args:
        page (str | Unset):
        page_size (str | Unset):
        user (str | Unset):
        view (V2EnrollmentListView | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PaginatedCourseEnrollmentList]
    """

    kwargs = _get_kwargs(
        page=page,
        page_size=page_size,
        user=user,
        view=view,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    page: str | Unset = UNSET,
    page_size: str | Unset = UNSET,
    user: str | Unset = UNSET,
    view: V2EnrollmentListView | Unset = UNSET,
) -> Any | PaginatedCourseEnrollmentList | None:
    """List enrollments for a user (paginated)

     Returns a paginated list of enrollments for the currently logged-in user, or for the user named by
    the 'user' query parameter. Staff/admin/api-key access is required to view another user's
    enrollments — otherwise the list is filtered to courses the requester staffs. Supports the ADR 0036
    ``?view=minimal`` preset (see parameter description).

    Args:
        page (str | Unset):
        page_size (str | Unset):
        user (str | Unset):
        view (V2EnrollmentListView | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PaginatedCourseEnrollmentList
    """

    return sync_detailed(
        client=client,
        page=page,
        page_size=page_size,
        user=user,
        view=view,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: str | Unset = UNSET,
    page_size: str | Unset = UNSET,
    user: str | Unset = UNSET,
    view: V2EnrollmentListView | Unset = UNSET,
) -> Response[Any | PaginatedCourseEnrollmentList]:
    """List enrollments for a user (paginated)

     Returns a paginated list of enrollments for the currently logged-in user, or for the user named by
    the 'user' query parameter. Staff/admin/api-key access is required to view another user's
    enrollments — otherwise the list is filtered to courses the requester staffs. Supports the ADR 0036
    ``?view=minimal`` preset (see parameter description).

    Args:
        page (str | Unset):
        page_size (str | Unset):
        user (str | Unset):
        view (V2EnrollmentListView | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PaginatedCourseEnrollmentList]
    """

    kwargs = _get_kwargs(
        page=page,
        page_size=page_size,
        user=user,
        view=view,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    page: str | Unset = UNSET,
    page_size: str | Unset = UNSET,
    user: str | Unset = UNSET,
    view: V2EnrollmentListView | Unset = UNSET,
) -> Any | PaginatedCourseEnrollmentList | None:
    """List enrollments for a user (paginated)

     Returns a paginated list of enrollments for the currently logged-in user, or for the user named by
    the 'user' query parameter. Staff/admin/api-key access is required to view another user's
    enrollments — otherwise the list is filtered to courses the requester staffs. Supports the ADR 0036
    ``?view=minimal`` preset (see parameter description).

    Args:
        page (str | Unset):
        page_size (str | Unset):
        user (str | Unset):
        view (V2EnrollmentListView | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PaginatedCourseEnrollmentList
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            page_size=page_size,
            user=user,
            view=view,
        )
    ).parsed
