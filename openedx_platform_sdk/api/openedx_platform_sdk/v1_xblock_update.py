from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.xblock import Xblock
from ...types import UNSET, Response, Unset


def _get_kwargs(
    usage_key_string: str,
    *,
    body: Xblock | Xblock | Xblock | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/xblock/{usage_key_string}/".format(
            usage_key_string=quote(str(usage_key_string), safe=""),
        ),
    }

    if isinstance(body, Xblock):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | Xblock | None:
    if response.status_code == 200:
        response_200 = Xblock.from_dict(response.json())

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

    if response.status_code == 406:
        response_406 = cast(Any, None)
        return response_406

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | Xblock]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    usage_key_string: str,
    *,
    client: AuthenticatedClient | Client,
    body: Xblock | Xblock | Xblock | Unset = UNSET,
) -> Response[Any | Xblock]:
    """Update an xblock

     Fully update an xblock identified by its usage key.

    Args:
        usage_key_string (str):
        body (Xblock | Unset): A serializer for xblocks that enforces strict validation.

            The serializer ensures:
            1. All top-level fields have the expected data types.
            2. No unexpected fields are passed in.

            Note: The current list of fields is not exhaustive. It is primarily designed
            to support the CMS API demo. While optional fields have been added, they were
            chosen based on ease of discovery, not comprehensiveness.
        body (Xblock | Unset): A serializer for xblocks that enforces strict validation.

            The serializer ensures:
            1. All top-level fields have the expected data types.
            2. No unexpected fields are passed in.

            Note: The current list of fields is not exhaustive. It is primarily designed
            to support the CMS API demo. While optional fields have been added, they were
            chosen based on ease of discovery, not comprehensiveness.
        body (Xblock | Unset): A serializer for xblocks that enforces strict validation.

            The serializer ensures:
            1. All top-level fields have the expected data types.
            2. No unexpected fields are passed in.

            Note: The current list of fields is not exhaustive. It is primarily designed
            to support the CMS API demo. While optional fields have been added, they were
            chosen based on ease of discovery, not comprehensiveness.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Xblock]
    """

    kwargs = _get_kwargs(
        usage_key_string=usage_key_string,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    usage_key_string: str,
    *,
    client: AuthenticatedClient | Client,
    body: Xblock | Xblock | Xblock | Unset = UNSET,
) -> Any | Xblock | None:
    """Update an xblock

     Fully update an xblock identified by its usage key.

    Args:
        usage_key_string (str):
        body (Xblock | Unset): A serializer for xblocks that enforces strict validation.

            The serializer ensures:
            1. All top-level fields have the expected data types.
            2. No unexpected fields are passed in.

            Note: The current list of fields is not exhaustive. It is primarily designed
            to support the CMS API demo. While optional fields have been added, they were
            chosen based on ease of discovery, not comprehensiveness.
        body (Xblock | Unset): A serializer for xblocks that enforces strict validation.

            The serializer ensures:
            1. All top-level fields have the expected data types.
            2. No unexpected fields are passed in.

            Note: The current list of fields is not exhaustive. It is primarily designed
            to support the CMS API demo. While optional fields have been added, they were
            chosen based on ease of discovery, not comprehensiveness.
        body (Xblock | Unset): A serializer for xblocks that enforces strict validation.

            The serializer ensures:
            1. All top-level fields have the expected data types.
            2. No unexpected fields are passed in.

            Note: The current list of fields is not exhaustive. It is primarily designed
            to support the CMS API demo. While optional fields have been added, they were
            chosen based on ease of discovery, not comprehensiveness.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Xblock
    """

    return sync_detailed(
        usage_key_string=usage_key_string,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    usage_key_string: str,
    *,
    client: AuthenticatedClient | Client,
    body: Xblock | Xblock | Xblock | Unset = UNSET,
) -> Response[Any | Xblock]:
    """Update an xblock

     Fully update an xblock identified by its usage key.

    Args:
        usage_key_string (str):
        body (Xblock | Unset): A serializer for xblocks that enforces strict validation.

            The serializer ensures:
            1. All top-level fields have the expected data types.
            2. No unexpected fields are passed in.

            Note: The current list of fields is not exhaustive. It is primarily designed
            to support the CMS API demo. While optional fields have been added, they were
            chosen based on ease of discovery, not comprehensiveness.
        body (Xblock | Unset): A serializer for xblocks that enforces strict validation.

            The serializer ensures:
            1. All top-level fields have the expected data types.
            2. No unexpected fields are passed in.

            Note: The current list of fields is not exhaustive. It is primarily designed
            to support the CMS API demo. While optional fields have been added, they were
            chosen based on ease of discovery, not comprehensiveness.
        body (Xblock | Unset): A serializer for xblocks that enforces strict validation.

            The serializer ensures:
            1. All top-level fields have the expected data types.
            2. No unexpected fields are passed in.

            Note: The current list of fields is not exhaustive. It is primarily designed
            to support the CMS API demo. While optional fields have been added, they were
            chosen based on ease of discovery, not comprehensiveness.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Xblock]
    """

    kwargs = _get_kwargs(
        usage_key_string=usage_key_string,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    usage_key_string: str,
    *,
    client: AuthenticatedClient | Client,
    body: Xblock | Xblock | Xblock | Unset = UNSET,
) -> Any | Xblock | None:
    """Update an xblock

     Fully update an xblock identified by its usage key.

    Args:
        usage_key_string (str):
        body (Xblock | Unset): A serializer for xblocks that enforces strict validation.

            The serializer ensures:
            1. All top-level fields have the expected data types.
            2. No unexpected fields are passed in.

            Note: The current list of fields is not exhaustive. It is primarily designed
            to support the CMS API demo. While optional fields have been added, they were
            chosen based on ease of discovery, not comprehensiveness.
        body (Xblock | Unset): A serializer for xblocks that enforces strict validation.

            The serializer ensures:
            1. All top-level fields have the expected data types.
            2. No unexpected fields are passed in.

            Note: The current list of fields is not exhaustive. It is primarily designed
            to support the CMS API demo. While optional fields have been added, they were
            chosen based on ease of discovery, not comprehensiveness.
        body (Xblock | Unset): A serializer for xblocks that enforces strict validation.

            The serializer ensures:
            1. All top-level fields have the expected data types.
            2. No unexpected fields are passed in.

            Note: The current list of fields is not exhaustive. It is primarily designed
            to support the CMS API demo. While optional fields have been added, they were
            chosen based on ease of discovery, not comprehensiveness.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Xblock
    """

    return (
        await asyncio_detailed(
            usage_key_string=usage_key_string,
            client=client,
            body=body,
        )
    ).parsed
