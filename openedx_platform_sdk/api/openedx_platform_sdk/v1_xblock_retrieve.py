from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.v1_xblock_retrieve_view import V1XblockRetrieveView
from ...models.xblock import Xblock
from ...types import UNSET, Response, Unset


def _get_kwargs(
    usage_key_string: str,
    *,
    fields: str | Unset = UNSET,
    view: V1XblockRetrieveView | Unset = UNSET,
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
        "url": "/v1/xblock/{usage_key_string}/".format(
            usage_key_string=quote(str(usage_key_string), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | Xblock | None:
    if response.status_code == 200:
        response_200 = Xblock.from_dict(response.json())

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
    fields: str | Unset = UNSET,
    view: V1XblockRetrieveView | Unset = UNSET,
) -> Response[Any | Xblock]:
    """Retrieve an xblock

     Retrieve an xblock (and, by default, its nested tree) by usage key. Supports ADR 0036
    ``?view=minimal`` to strip contextual fields, plus the legacy ``?fields=`` type-of-response
    selector.

    Args:
        usage_key_string (str):
        fields (str | Unset):
        view (V1XblockRetrieveView | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Xblock]
    """

    kwargs = _get_kwargs(
        usage_key_string=usage_key_string,
        fields=fields,
        view=view,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    usage_key_string: str,
    *,
    client: AuthenticatedClient | Client,
    fields: str | Unset = UNSET,
    view: V1XblockRetrieveView | Unset = UNSET,
) -> Any | Xblock | None:
    """Retrieve an xblock

     Retrieve an xblock (and, by default, its nested tree) by usage key. Supports ADR 0036
    ``?view=minimal`` to strip contextual fields, plus the legacy ``?fields=`` type-of-response
    selector.

    Args:
        usage_key_string (str):
        fields (str | Unset):
        view (V1XblockRetrieveView | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Xblock
    """

    return sync_detailed(
        usage_key_string=usage_key_string,
        client=client,
        fields=fields,
        view=view,
    ).parsed


async def asyncio_detailed(
    usage_key_string: str,
    *,
    client: AuthenticatedClient | Client,
    fields: str | Unset = UNSET,
    view: V1XblockRetrieveView | Unset = UNSET,
) -> Response[Any | Xblock]:
    """Retrieve an xblock

     Retrieve an xblock (and, by default, its nested tree) by usage key. Supports ADR 0036
    ``?view=minimal`` to strip contextual fields, plus the legacy ``?fields=`` type-of-response
    selector.

    Args:
        usage_key_string (str):
        fields (str | Unset):
        view (V1XblockRetrieveView | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Xblock]
    """

    kwargs = _get_kwargs(
        usage_key_string=usage_key_string,
        fields=fields,
        view=view,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    usage_key_string: str,
    *,
    client: AuthenticatedClient | Client,
    fields: str | Unset = UNSET,
    view: V1XblockRetrieveView | Unset = UNSET,
) -> Any | Xblock | None:
    """Retrieve an xblock

     Retrieve an xblock (and, by default, its nested tree) by usage key. Supports ADR 0036
    ``?view=minimal`` to strip contextual fields, plus the legacy ``?fields=`` type-of-response
    selector.

    Args:
        usage_key_string (str):
        fields (str | Unset):
        view (V1XblockRetrieveView | Unset):

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
            fields=fields,
            view=view,
        )
    ).parsed
