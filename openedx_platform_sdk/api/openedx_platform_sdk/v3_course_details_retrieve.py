from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.course_details import CourseDetails
from ...models.v3_course_details_retrieve_view import V3CourseDetailsRetrieveView
from ...types import UNSET, Response, Unset


def _get_kwargs(
    course_id: str,
    *,
    fields: str | Unset = UNSET,
    view: V3CourseDetailsRetrieveView | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["fields"] = fields

    json_view: str | Unset = UNSET
    if not isinstance(view, Unset):
        json_view = view.value

    params["view"] = json_view

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/course_details/{course_id}/".format(
            course_id=quote(str(course_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | CourseDetails | None:
    if response.status_code == 200:
        response_200 = CourseDetails.from_dict(response.json())

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
    fields: str | Unset = UNSET,
    view: V3CourseDetailsRetrieveView | Unset = UNSET,
) -> Response[Any | CourseDetails]:
    """Retrieve a course's details

     Get an object containing the course details for the specified course. Supports the ADR 0036
    ``?view=minimal`` preset and ``?fields=`` explicit field selection (see the parameter descriptions
    for details).

    Args:
        course_id (str):
        fields (str | Unset):
        view (V3CourseDetailsRetrieveView | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CourseDetails]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        fields=fields,
        view=view,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    course_id: str,
    *,
    client: AuthenticatedClient | Client,
    fields: str | Unset = UNSET,
    view: V3CourseDetailsRetrieveView | Unset = UNSET,
) -> Any | CourseDetails | None:
    """Retrieve a course's details

     Get an object containing the course details for the specified course. Supports the ADR 0036
    ``?view=minimal`` preset and ``?fields=`` explicit field selection (see the parameter descriptions
    for details).

    Args:
        course_id (str):
        fields (str | Unset):
        view (V3CourseDetailsRetrieveView | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CourseDetails
    """

    return sync_detailed(
        course_id=course_id,
        client=client,
        fields=fields,
        view=view,
    ).parsed


async def asyncio_detailed(
    course_id: str,
    *,
    client: AuthenticatedClient | Client,
    fields: str | Unset = UNSET,
    view: V3CourseDetailsRetrieveView | Unset = UNSET,
) -> Response[Any | CourseDetails]:
    """Retrieve a course's details

     Get an object containing the course details for the specified course. Supports the ADR 0036
    ``?view=minimal`` preset and ``?fields=`` explicit field selection (see the parameter descriptions
    for details).

    Args:
        course_id (str):
        fields (str | Unset):
        view (V3CourseDetailsRetrieveView | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CourseDetails]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        fields=fields,
        view=view,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    course_id: str,
    *,
    client: AuthenticatedClient | Client,
    fields: str | Unset = UNSET,
    view: V3CourseDetailsRetrieveView | Unset = UNSET,
) -> Any | CourseDetails | None:
    """Retrieve a course's details

     Get an object containing the course details for the specified course. Supports the ADR 0036
    ``?view=minimal`` preset and ``?fields=`` explicit field selection (see the parameter descriptions
    for details).

    Args:
        course_id (str):
        fields (str | Unset):
        view (V3CourseDetailsRetrieveView | Unset):

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
            fields=fields,
            view=view,
        )
    ).parsed
