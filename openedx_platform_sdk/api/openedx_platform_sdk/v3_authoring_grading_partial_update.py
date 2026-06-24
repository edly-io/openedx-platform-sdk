from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.authoring_grading_course_grading_v0 import AuthoringGradingCourseGradingV0
from ...models.patchedauthoring_grading_course_grading_v0 import PatchedauthoringGradingCourseGradingV0
from ...types import UNSET, Response, Unset


def _get_kwargs(
    course_key: str,
    *,
    body: PatchedauthoringGradingCourseGradingV0
    | PatchedauthoringGradingCourseGradingV0
    | PatchedauthoringGradingCourseGradingV0
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v3/authoring_grading/{course_key}/".format(
            course_key=quote(str(course_key), safe=""),
        ),
    }

    if isinstance(body, PatchedauthoringGradingCourseGradingV0):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchedauthoringGradingCourseGradingV0):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, PatchedauthoringGradingCourseGradingV0):
        if not isinstance(body, Unset):
            _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | AuthoringGradingCourseGradingV0 | None:
    if response.status_code == 200:
        response_200 = AuthoringGradingCourseGradingV0.from_dict(response.json())

        return response_200

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


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | AuthoringGradingCourseGradingV0]:
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
    body: PatchedauthoringGradingCourseGradingV0
    | PatchedauthoringGradingCourseGradingV0
    | PatchedauthoringGradingCourseGradingV0
    | Unset = UNSET,
) -> Response[Any | AuthoringGradingCourseGradingV0]:
    """Update a course's grading settings

     Partially update the grading settings for the specified course.

    Args:
        course_key (str):
        body (PatchedauthoringGradingCourseGradingV0 | Unset): Serializer for course grading model
            data
        body (PatchedauthoringGradingCourseGradingV0 | Unset): Serializer for course grading model
            data
        body (PatchedauthoringGradingCourseGradingV0 | Unset): Serializer for course grading model
            data

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | AuthoringGradingCourseGradingV0]
    """

    kwargs = _get_kwargs(
        course_key=course_key,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    course_key: str,
    *,
    client: AuthenticatedClient | Client,
    body: PatchedauthoringGradingCourseGradingV0
    | PatchedauthoringGradingCourseGradingV0
    | PatchedauthoringGradingCourseGradingV0
    | Unset = UNSET,
) -> Any | AuthoringGradingCourseGradingV0 | None:
    """Update a course's grading settings

     Partially update the grading settings for the specified course.

    Args:
        course_key (str):
        body (PatchedauthoringGradingCourseGradingV0 | Unset): Serializer for course grading model
            data
        body (PatchedauthoringGradingCourseGradingV0 | Unset): Serializer for course grading model
            data
        body (PatchedauthoringGradingCourseGradingV0 | Unset): Serializer for course grading model
            data

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | AuthoringGradingCourseGradingV0
    """

    return sync_detailed(
        course_key=course_key,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    course_key: str,
    *,
    client: AuthenticatedClient | Client,
    body: PatchedauthoringGradingCourseGradingV0
    | PatchedauthoringGradingCourseGradingV0
    | PatchedauthoringGradingCourseGradingV0
    | Unset = UNSET,
) -> Response[Any | AuthoringGradingCourseGradingV0]:
    """Update a course's grading settings

     Partially update the grading settings for the specified course.

    Args:
        course_key (str):
        body (PatchedauthoringGradingCourseGradingV0 | Unset): Serializer for course grading model
            data
        body (PatchedauthoringGradingCourseGradingV0 | Unset): Serializer for course grading model
            data
        body (PatchedauthoringGradingCourseGradingV0 | Unset): Serializer for course grading model
            data

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | AuthoringGradingCourseGradingV0]
    """

    kwargs = _get_kwargs(
        course_key=course_key,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    course_key: str,
    *,
    client: AuthenticatedClient | Client,
    body: PatchedauthoringGradingCourseGradingV0
    | PatchedauthoringGradingCourseGradingV0
    | PatchedauthoringGradingCourseGradingV0
    | Unset = UNSET,
) -> Any | AuthoringGradingCourseGradingV0 | None:
    """Update a course's grading settings

     Partially update the grading settings for the specified course.

    Args:
        course_key (str):
        body (PatchedauthoringGradingCourseGradingV0 | Unset): Serializer for course grading model
            data
        body (PatchedauthoringGradingCourseGradingV0 | Unset): Serializer for course grading model
            data
        body (PatchedauthoringGradingCourseGradingV0 | Unset): Serializer for course grading model
            data

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | AuthoringGradingCourseGradingV0
    """

    return (
        await asyncio_detailed(
            course_key=course_key,
            client=client,
            body=body,
        )
    ).parsed
