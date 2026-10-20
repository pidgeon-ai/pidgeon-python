from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.mailboxes_list_folder_response_200 import MailboxesListFolderResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    folder: str,
    *,
    identity_id: UUID,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    label_id: UUID | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_identity_id = str(identity_id)
    params["identity_id"] = json_identity_id

    params["limit"] = limit

    params["cursor"] = cursor

    json_label_id: str | Unset = UNSET
    if not isinstance(label_id, Unset):
        json_label_id = str(label_id)
    params["label_id"] = json_label_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/mailboxes/{folder}".format(
            folder=quote(str(folder), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> MailboxesListFolderResponse200:
    if response.status_code >= 400:
        raise errors.PidgeonError.from_response(response)

    if response.status_code == 200:
        response_200 = MailboxesListFolderResponse200.from_dict(response.json())

        return response_200

    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[MailboxesListFolderResponse200]:
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
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    label_id: UUID | Unset = UNSET,
) -> Response[MailboxesListFolderResponse200]:
    """List one folder

     A row is a conversation — the newest message in each thread — not a message. Paged by an opaque
    `cursor`, which is the `next_cursor` of the page before it: it carries a sort key and an id
    together, because several messages can share a millisecond. Do not construct one.

    Args:
        folder (str):
        identity_id (UUID):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset): From a previous page’s `next_cursor`. Opaque — do not parse it.
        label_id (UUID | Unset):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MailboxesListFolderResponse200]
    """

    kwargs = _get_kwargs(
        folder=folder,
        identity_id=identity_id,
        limit=limit,
        cursor=cursor,
        label_id=label_id,
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
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    label_id: UUID | Unset = UNSET,
) -> MailboxesListFolderResponse200:
    """List one folder

     A row is a conversation — the newest message in each thread — not a message. Paged by an opaque
    `cursor`, which is the `next_cursor` of the page before it: it carries a sort key and an id
    together, because several messages can share a millisecond. Do not construct one.

    Args:
        folder (str):
        identity_id (UUID):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset): From a previous page’s `next_cursor`. Opaque — do not parse it.
        label_id (UUID | Unset):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MailboxesListFolderResponse200
    """

    return sync_detailed(
        folder=folder,
        client=client,
        identity_id=identity_id,
        limit=limit,
        cursor=cursor,
        label_id=label_id,
    ).parsed


async def asyncio_detailed(
    folder: str,
    *,
    client: AuthenticatedClient | Client,
    identity_id: UUID,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    label_id: UUID | Unset = UNSET,
) -> Response[MailboxesListFolderResponse200]:
    """List one folder

     A row is a conversation — the newest message in each thread — not a message. Paged by an opaque
    `cursor`, which is the `next_cursor` of the page before it: it carries a sort key and an id
    together, because several messages can share a millisecond. Do not construct one.

    Args:
        folder (str):
        identity_id (UUID):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset): From a previous page’s `next_cursor`. Opaque — do not parse it.
        label_id (UUID | Unset):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MailboxesListFolderResponse200]
    """

    kwargs = _get_kwargs(
        folder=folder,
        identity_id=identity_id,
        limit=limit,
        cursor=cursor,
        label_id=label_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    folder: str,
    *,
    client: AuthenticatedClient | Client,
    identity_id: UUID,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    label_id: UUID | Unset = UNSET,
) -> MailboxesListFolderResponse200:
    """List one folder

     A row is a conversation — the newest message in each thread — not a message. Paged by an opaque
    `cursor`, which is the `next_cursor` of the page before it: it carries a sort key and an id
    together, because several messages can share a millisecond. Do not construct one.

    Args:
        folder (str):
        identity_id (UUID):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset): From a previous page’s `next_cursor`. Opaque — do not parse it.
        label_id (UUID | Unset):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MailboxesListFolderResponse200
    """

    return (
        await asyncio_detailed(
            folder=folder,
            client=client,
            identity_id=identity_id,
            limit=limit,
            cursor=cursor,
            label_id=label_id,
        )
    ).parsed
