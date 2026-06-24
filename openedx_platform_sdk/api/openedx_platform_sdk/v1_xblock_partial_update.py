from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patched_xblock import PatchedXblock
from ...models.xblock import Xblock
from ...types import UNSET, Response, Unset


def _get_kwargs(
    usage_key_string: str,
    *,
    body: PatchedXblock | PatchedXblock | PatchedXblock | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/xblock/{usage_key_string}/".format(
            usage_key_string=quote(str(usage_key_string), safe=""),
        ),
    }

    if isinstance(body, PatchedXblock):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchedXblock):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, PatchedXblock):
        if not isinstance(body, Unset):
            _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Xblock | None:
    if response.status_code == 200:
        response_200 = Xblock.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Xblock]:
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
    body: PatchedXblock | PatchedXblock | PatchedXblock | Unset = UNSET,
) -> Response[Xblock]:
    """ViewSet for xblock CRUD operations (v1 — ADR 0028).

    Router-generated URLs:
      POST   /api/contentstore/v1/xblock/                      → create
      GET    /api/contentstore/v1/xblock/{usage_key_string}/   → retrieve
      PUT    /api/contentstore/v1/xblock/{usage_key_string}/   → update
      PATCH  /api/contentstore/v1/xblock/{usage_key_string}/   → partial_update
      DELETE /api/contentstore/v1/xblock/{usage_key_string}/   → destroy

    Query parameters (ADR 0036, GET only):
      ?view=minimal   Drop heavy / contextual fields from the response,
                      keeping only structural fields (id, display_name,
                      category, children, has_children, studio_url).
                      Default response is the full xblock payload.

    Args:
        usage_key_string (str):
        body (PatchedXblock | Unset): A serializer for xblocks that enforces strict validation.

            The serializer ensures:
            1. All top-level fields have the expected data types.
            2. No unexpected fields are passed in.

            Note: The current list of fields is not exhaustive. It is primarily designed
            to support the CMS API demo. While optional fields have been added, they were
            chosen based on ease of discovery, not comprehensiveness.
        body (PatchedXblock | Unset): A serializer for xblocks that enforces strict validation.

            The serializer ensures:
            1. All top-level fields have the expected data types.
            2. No unexpected fields are passed in.

            Note: The current list of fields is not exhaustive. It is primarily designed
            to support the CMS API demo. While optional fields have been added, they were
            chosen based on ease of discovery, not comprehensiveness.
        body (PatchedXblock | Unset): A serializer for xblocks that enforces strict validation.

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
        Response[Xblock]
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
    body: PatchedXblock | PatchedXblock | PatchedXblock | Unset = UNSET,
) -> Xblock | None:
    """ViewSet for xblock CRUD operations (v1 — ADR 0028).

    Router-generated URLs:
      POST   /api/contentstore/v1/xblock/                      → create
      GET    /api/contentstore/v1/xblock/{usage_key_string}/   → retrieve
      PUT    /api/contentstore/v1/xblock/{usage_key_string}/   → update
      PATCH  /api/contentstore/v1/xblock/{usage_key_string}/   → partial_update
      DELETE /api/contentstore/v1/xblock/{usage_key_string}/   → destroy

    Query parameters (ADR 0036, GET only):
      ?view=minimal   Drop heavy / contextual fields from the response,
                      keeping only structural fields (id, display_name,
                      category, children, has_children, studio_url).
                      Default response is the full xblock payload.

    Args:
        usage_key_string (str):
        body (PatchedXblock | Unset): A serializer for xblocks that enforces strict validation.

            The serializer ensures:
            1. All top-level fields have the expected data types.
            2. No unexpected fields are passed in.

            Note: The current list of fields is not exhaustive. It is primarily designed
            to support the CMS API demo. While optional fields have been added, they were
            chosen based on ease of discovery, not comprehensiveness.
        body (PatchedXblock | Unset): A serializer for xblocks that enforces strict validation.

            The serializer ensures:
            1. All top-level fields have the expected data types.
            2. No unexpected fields are passed in.

            Note: The current list of fields is not exhaustive. It is primarily designed
            to support the CMS API demo. While optional fields have been added, they were
            chosen based on ease of discovery, not comprehensiveness.
        body (PatchedXblock | Unset): A serializer for xblocks that enforces strict validation.

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
        Xblock
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
    body: PatchedXblock | PatchedXblock | PatchedXblock | Unset = UNSET,
) -> Response[Xblock]:
    """ViewSet for xblock CRUD operations (v1 — ADR 0028).

    Router-generated URLs:
      POST   /api/contentstore/v1/xblock/                      → create
      GET    /api/contentstore/v1/xblock/{usage_key_string}/   → retrieve
      PUT    /api/contentstore/v1/xblock/{usage_key_string}/   → update
      PATCH  /api/contentstore/v1/xblock/{usage_key_string}/   → partial_update
      DELETE /api/contentstore/v1/xblock/{usage_key_string}/   → destroy

    Query parameters (ADR 0036, GET only):
      ?view=minimal   Drop heavy / contextual fields from the response,
                      keeping only structural fields (id, display_name,
                      category, children, has_children, studio_url).
                      Default response is the full xblock payload.

    Args:
        usage_key_string (str):
        body (PatchedXblock | Unset): A serializer for xblocks that enforces strict validation.

            The serializer ensures:
            1. All top-level fields have the expected data types.
            2. No unexpected fields are passed in.

            Note: The current list of fields is not exhaustive. It is primarily designed
            to support the CMS API demo. While optional fields have been added, they were
            chosen based on ease of discovery, not comprehensiveness.
        body (PatchedXblock | Unset): A serializer for xblocks that enforces strict validation.

            The serializer ensures:
            1. All top-level fields have the expected data types.
            2. No unexpected fields are passed in.

            Note: The current list of fields is not exhaustive. It is primarily designed
            to support the CMS API demo. While optional fields have been added, they were
            chosen based on ease of discovery, not comprehensiveness.
        body (PatchedXblock | Unset): A serializer for xblocks that enforces strict validation.

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
        Response[Xblock]
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
    body: PatchedXblock | PatchedXblock | PatchedXblock | Unset = UNSET,
) -> Xblock | None:
    """ViewSet for xblock CRUD operations (v1 — ADR 0028).

    Router-generated URLs:
      POST   /api/contentstore/v1/xblock/                      → create
      GET    /api/contentstore/v1/xblock/{usage_key_string}/   → retrieve
      PUT    /api/contentstore/v1/xblock/{usage_key_string}/   → update
      PATCH  /api/contentstore/v1/xblock/{usage_key_string}/   → partial_update
      DELETE /api/contentstore/v1/xblock/{usage_key_string}/   → destroy

    Query parameters (ADR 0036, GET only):
      ?view=minimal   Drop heavy / contextual fields from the response,
                      keeping only structural fields (id, display_name,
                      category, children, has_children, studio_url).
                      Default response is the full xblock payload.

    Args:
        usage_key_string (str):
        body (PatchedXblock | Unset): A serializer for xblocks that enforces strict validation.

            The serializer ensures:
            1. All top-level fields have the expected data types.
            2. No unexpected fields are passed in.

            Note: The current list of fields is not exhaustive. It is primarily designed
            to support the CMS API demo. While optional fields have been added, they were
            chosen based on ease of discovery, not comprehensiveness.
        body (PatchedXblock | Unset): A serializer for xblocks that enforces strict validation.

            The serializer ensures:
            1. All top-level fields have the expected data types.
            2. No unexpected fields are passed in.

            Note: The current list of fields is not exhaustive. It is primarily designed
            to support the CMS API demo. While optional fields have been added, they were
            chosen based on ease of discovery, not comprehensiveness.
        body (PatchedXblock | Unset): A serializer for xblocks that enforces strict validation.

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
        Xblock
    """

    return (
        await asyncio_detailed(
            usage_key_string=usage_key_string,
            client=client,
            body=body,
        )
    ).parsed
