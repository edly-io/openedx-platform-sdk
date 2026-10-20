from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.paginated_course_textbook_list import PaginatedCourseTextbookList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    course_key: str,
    *,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/authoring/v2/courses/{course_key}/textbooks/".format(
            course_key=quote(str(course_key), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | PaginatedCourseTextbookList | None:
    if response.status_code == 200:
        response_200 = PaginatedCourseTextbookList.from_dict(response.json())

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
) -> Response[ErrorResponse | PaginatedCourseTextbookList]:
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
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
) -> Response[ErrorResponse | PaginatedCourseTextbookList]:
    """List a course's PDF textbooks

     Returns one page of the course's PDF textbooks, each with its chapters, in the order the course
    stores them, which is also the order of the course's textbook tabs.

    Args:
        course_key (str):
        page (int | Unset):
        page_size (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PaginatedCourseTextbookList]
    """

    kwargs = _get_kwargs(
        course_key=course_key,
        page=page,
        page_size=page_size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    course_key: str,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
) -> ErrorResponse | PaginatedCourseTextbookList | None:
    """List a course's PDF textbooks

     Returns one page of the course's PDF textbooks, each with its chapters, in the order the course
    stores them, which is also the order of the course's textbook tabs.

    Args:
        course_key (str):
        page (int | Unset):
        page_size (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PaginatedCourseTextbookList
    """

    return sync_detailed(
        course_key=course_key,
        client=client,
        page=page,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    course_key: str,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
) -> Response[ErrorResponse | PaginatedCourseTextbookList]:
    """List a course's PDF textbooks

     Returns one page of the course's PDF textbooks, each with its chapters, in the order the course
    stores them, which is also the order of the course's textbook tabs.

    Args:
        course_key (str):
        page (int | Unset):
        page_size (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PaginatedCourseTextbookList]
    """

    kwargs = _get_kwargs(
        course_key=course_key,
        page=page,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    course_key: str,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
) -> ErrorResponse | PaginatedCourseTextbookList | None:
    """List a course's PDF textbooks

     Returns one page of the course's PDF textbooks, each with its chapters, in the order the course
    stores them, which is also the order of the course's textbook tabs.

    Args:
        course_key (str):
        page (int | Unset):
        page_size (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PaginatedCourseTextbookList
    """

    return (
        await asyncio_detailed(
            course_key=course_key,
            client=client,
            page=page,
            page_size=page_size,
        )
    ).parsed
