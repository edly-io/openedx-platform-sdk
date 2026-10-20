from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.youtube_transcript_check_result import YoutubeTranscriptCheckResult
from ...types import UNSET, Response


def _get_kwargs(
    course_key: str,
    *,
    data: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["data"] = data

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/authoring/v1/courses/{course_key}/youtube_transcript_checks/".format(
            course_key=quote(str(course_key), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | list[YoutubeTranscriptCheckResult] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = YoutubeTranscriptCheckResult.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

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
) -> Response[ErrorResponse | list[YoutubeTranscriptCheckResult]]:
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
    data: str,
) -> Response[ErrorResponse | list[YoutubeTranscriptCheckResult]]:
    """Report the transcript availability of a video

     Reports which transcripts exist for the video named by the `data` parameter, and whether the
    transcript published on YouTube differs from the stored one.

    Args:
        course_key (str):
        data (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | list[YoutubeTranscriptCheckResult]]
    """

    kwargs = _get_kwargs(
        course_key=course_key,
        data=data,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    course_key: str,
    *,
    client: AuthenticatedClient | Client,
    data: str,
) -> ErrorResponse | list[YoutubeTranscriptCheckResult] | None:
    """Report the transcript availability of a video

     Reports which transcripts exist for the video named by the `data` parameter, and whether the
    transcript published on YouTube differs from the stored one.

    Args:
        course_key (str):
        data (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | list[YoutubeTranscriptCheckResult]
    """

    return sync_detailed(
        course_key=course_key,
        client=client,
        data=data,
    ).parsed


async def asyncio_detailed(
    course_key: str,
    *,
    client: AuthenticatedClient | Client,
    data: str,
) -> Response[ErrorResponse | list[YoutubeTranscriptCheckResult]]:
    """Report the transcript availability of a video

     Reports which transcripts exist for the video named by the `data` parameter, and whether the
    transcript published on YouTube differs from the stored one.

    Args:
        course_key (str):
        data (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | list[YoutubeTranscriptCheckResult]]
    """

    kwargs = _get_kwargs(
        course_key=course_key,
        data=data,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    course_key: str,
    *,
    client: AuthenticatedClient | Client,
    data: str,
) -> ErrorResponse | list[YoutubeTranscriptCheckResult] | None:
    """Report the transcript availability of a video

     Reports which transcripts exist for the video named by the `data` parameter, and whether the
    transcript published on YouTube differs from the stored one.

    Args:
        course_key (str):
        data (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | list[YoutubeTranscriptCheckResult]
    """

    return (
        await asyncio_detailed(
            course_key=course_key,
            client=client,
            data=data,
        )
    ).parsed
