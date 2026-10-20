from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.youtube_transcript_import_request import YoutubeTranscriptImportRequest
from ...models.youtube_transcript_import_result import YoutubeTranscriptImportResult
from ...types import UNSET, Response, Unset


def _get_kwargs(
    course_key: str,
    *,
    body: YoutubeTranscriptImportRequest
    | YoutubeTranscriptImportRequest
    | YoutubeTranscriptImportRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/authoring/v1/courses/{course_key}/youtube_transcript_imports/".format(
            course_key=quote(str(course_key), safe=""),
        ),
    }

    if isinstance(body, YoutubeTranscriptImportRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | YoutubeTranscriptImportResult | None:
    if response.status_code == 200:
        response_200 = YoutubeTranscriptImportResult.from_dict(response.json())

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
) -> Response[ErrorResponse | YoutubeTranscriptImportResult]:
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
    body: YoutubeTranscriptImportRequest
    | YoutubeTranscriptImportRequest
    | YoutubeTranscriptImportRequest
    | Unset = UNSET,
) -> Response[ErrorResponse | YoutubeTranscriptImportResult]:
    """Import a video's transcript from YouTube

     Downloads the transcript YouTube publishes for the video named in the request body and stores it
    against that video, replacing any transcript already stored.

    Args:
        course_key (str):
        body (YoutubeTranscriptImportRequest): Input identifying the video block to import a
            YouTube transcript into.
        body (YoutubeTranscriptImportRequest): Input identifying the video block to import a
            YouTube transcript into.
        body (YoutubeTranscriptImportRequest): Input identifying the video block to import a
            YouTube transcript into.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | YoutubeTranscriptImportResult]
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
    body: YoutubeTranscriptImportRequest
    | YoutubeTranscriptImportRequest
    | YoutubeTranscriptImportRequest
    | Unset = UNSET,
) -> ErrorResponse | YoutubeTranscriptImportResult | None:
    """Import a video's transcript from YouTube

     Downloads the transcript YouTube publishes for the video named in the request body and stores it
    against that video, replacing any transcript already stored.

    Args:
        course_key (str):
        body (YoutubeTranscriptImportRequest): Input identifying the video block to import a
            YouTube transcript into.
        body (YoutubeTranscriptImportRequest): Input identifying the video block to import a
            YouTube transcript into.
        body (YoutubeTranscriptImportRequest): Input identifying the video block to import a
            YouTube transcript into.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | YoutubeTranscriptImportResult
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
    body: YoutubeTranscriptImportRequest
    | YoutubeTranscriptImportRequest
    | YoutubeTranscriptImportRequest
    | Unset = UNSET,
) -> Response[ErrorResponse | YoutubeTranscriptImportResult]:
    """Import a video's transcript from YouTube

     Downloads the transcript YouTube publishes for the video named in the request body and stores it
    against that video, replacing any transcript already stored.

    Args:
        course_key (str):
        body (YoutubeTranscriptImportRequest): Input identifying the video block to import a
            YouTube transcript into.
        body (YoutubeTranscriptImportRequest): Input identifying the video block to import a
            YouTube transcript into.
        body (YoutubeTranscriptImportRequest): Input identifying the video block to import a
            YouTube transcript into.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | YoutubeTranscriptImportResult]
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
    body: YoutubeTranscriptImportRequest
    | YoutubeTranscriptImportRequest
    | YoutubeTranscriptImportRequest
    | Unset = UNSET,
) -> ErrorResponse | YoutubeTranscriptImportResult | None:
    """Import a video's transcript from YouTube

     Downloads the transcript YouTube publishes for the video named in the request body and stores it
    against that video, replacing any transcript already stored.

    Args:
        course_key (str):
        body (YoutubeTranscriptImportRequest): Input identifying the video block to import a
            YouTube transcript into.
        body (YoutubeTranscriptImportRequest): Input identifying the video block to import a
            YouTube transcript into.
        body (YoutubeTranscriptImportRequest): Input identifying the video block to import a
            YouTube transcript into.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | YoutubeTranscriptImportResult
    """

    return (
        await asyncio_detailed(
            course_key=course_key,
            client=client,
            body=body,
        )
    ).parsed
