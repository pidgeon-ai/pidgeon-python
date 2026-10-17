from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    identity_id: UUID | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_identity_id: str | Unset = UNSET
    if not isinstance(identity_id, Unset):
        json_identity_id = str(identity_id)
    params["identity_id"] = json_identity_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/export",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | None:
    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    identity_id: UUID | Unset = UNSET,
) -> Response[Error]:
    """Export mail as mbox

     Every message the key can read, as one `application/mbox` file, streamed — or one address of it with
    `identity_id`. Each message carries `X-Pidgeon-Mailbox` so a file holding several addresses can be
    split again; originals are byte for byte where storage still holds them. Four an hour per workspace.

    Args:
        identity_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error]
    """

    kwargs = _get_kwargs(
        identity_id=identity_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    identity_id: UUID | Unset = UNSET,
) -> Error | None:
    """Export mail as mbox

     Every message the key can read, as one `application/mbox` file, streamed — or one address of it with
    `identity_id`. Each message carries `X-Pidgeon-Mailbox` so a file holding several addresses can be
    split again; originals are byte for byte where storage still holds them. Four an hour per workspace.

    Args:
        identity_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error
    """

    return sync_detailed(
        client=client,
        identity_id=identity_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    identity_id: UUID | Unset = UNSET,
) -> Response[Error]:
    """Export mail as mbox

     Every message the key can read, as one `application/mbox` file, streamed — or one address of it with
    `identity_id`. Each message carries `X-Pidgeon-Mailbox` so a file holding several addresses can be
    split again; originals are byte for byte where storage still holds them. Four an hour per workspace.

    Args:
        identity_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error]
    """

    kwargs = _get_kwargs(
        identity_id=identity_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    identity_id: UUID | Unset = UNSET,
) -> Error | None:
    """Export mail as mbox

     Every message the key can read, as one `application/mbox` file, streamed — or one address of it with
    `identity_id`. Each message carries `X-Pidgeon-Mailbox` so a file holding several addresses can be
    split again; originals are byte for byte where storage still holds them. Four an hour per workspace.

    Args:
        identity_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error
    """

    return (
        await asyncio_detailed(
            client=client,
            identity_id=identity_id,
        )
    ).parsed
