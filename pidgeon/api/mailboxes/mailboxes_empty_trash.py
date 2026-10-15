from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.mailboxes_empty_trash_response_200 import MailboxesEmptyTrashResponse200
from ...types import UNSET, Response


def _get_kwargs(
    folder: str,
    *,
    identity_id: UUID,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_identity_id = str(identity_id)
    params["identity_id"] = json_identity_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/mailboxes/{folder}".format(
            folder=quote(str(folder), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | MailboxesEmptyTrashResponse200 | None:
    if response.status_code == 200:
        response_200 = MailboxesEmptyTrashResponse200.from_dict(response.json())

        return response_200

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


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | MailboxesEmptyTrashResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    folder: str,
    *,
    client: AuthenticatedClient | Client,
    identity_id: UUID,
) -> Response[Error | MailboxesEmptyTrashResponse200]:
    """Empty the trash

     Only `trash`; every other folder refuses. Permanent, and it takes attachments and archived originals
    with it — there is no undo, because the snapshot `POST /messages/undo` replays is a set of column
    values and these rows are gone. `delete_forever` on `POST /messages/actions` does the same to a list
    you name, and caps at 200; this needs no ids.

    Args:
        folder (str):
        identity_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | MailboxesEmptyTrashResponse200]
    """

    kwargs = _get_kwargs(
        folder=folder,
        identity_id=identity_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    folder: str,
    *,
    client: AuthenticatedClient | Client,
    identity_id: UUID,
) -> Error | MailboxesEmptyTrashResponse200 | None:
    """Empty the trash

     Only `trash`; every other folder refuses. Permanent, and it takes attachments and archived originals
    with it — there is no undo, because the snapshot `POST /messages/undo` replays is a set of column
    values and these rows are gone. `delete_forever` on `POST /messages/actions` does the same to a list
    you name, and caps at 200; this needs no ids.

    Args:
        folder (str):
        identity_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | MailboxesEmptyTrashResponse200
    """

    return sync_detailed(
        folder=folder,
        client=client,
        identity_id=identity_id,
    ).parsed


async def asyncio_detailed(
    folder: str,
    *,
    client: AuthenticatedClient | Client,
    identity_id: UUID,
) -> Response[Error | MailboxesEmptyTrashResponse200]:
    """Empty the trash

     Only `trash`; every other folder refuses. Permanent, and it takes attachments and archived originals
    with it — there is no undo, because the snapshot `POST /messages/undo` replays is a set of column
    values and these rows are gone. `delete_forever` on `POST /messages/actions` does the same to a list
    you name, and caps at 200; this needs no ids.

    Args:
        folder (str):
        identity_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | MailboxesEmptyTrashResponse200]
    """

    kwargs = _get_kwargs(
        folder=folder,
        identity_id=identity_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    folder: str,
    *,
    client: AuthenticatedClient | Client,
    identity_id: UUID,
) -> Error | MailboxesEmptyTrashResponse200 | None:
    """Empty the trash

     Only `trash`; every other folder refuses. Permanent, and it takes attachments and archived originals
    with it — there is no undo, because the snapshot `POST /messages/undo` replays is a set of column
    values and these rows are gone. `delete_forever` on `POST /messages/actions` does the same to a list
    you name, and caps at 200; this needs no ids.

    Args:
        folder (str):
        identity_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | MailboxesEmptyTrashResponse200
    """

    return (
        await asyncio_detailed(
            folder=folder,
            client=client,
            identity_id=identity_id,
        )
    ).parsed
