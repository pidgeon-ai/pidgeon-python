from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.mailboxes_changes_response_200 import MailboxesChangesResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    identity_id: UUID,
    since: str,
    limit: int | Unset = 100,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_identity_id = str(identity_id)
    params["identity_id"] = json_identity_id

    params["since"] = since

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/mailboxes/changes",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MailboxesChangesResponse200:
    if response.status_code >= 400:
        raise errors.PidgeonError.from_response(response)

    if response.status_code == 200:
        response_200 = MailboxesChangesResponse200.from_dict(response.json())

        return response_200

    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[MailboxesChangesResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    identity_id: UUID,
    since: str,
    limit: int | Unset = 100,
) -> Response[MailboxesChangesResponse200]:
    """What changed since you last looked

     Per mailbox, not per folder: a message moving from the inbox to the archive is one event, and the
    row says where it went. Arrivals are included, so this is the only thing to poll. `since` is the
    `sync_cursor` from a listing or the `next_cursor` from a previous delta — **not** a page cursor,
    which walks a different order and is refused rather than guessed at. A cursor older than the window
    in which we keep the record of what was deleted returns `410 resync`, because an empty delta would
    be indistinguishable from "nothing changed".

    Args:
        identity_id (UUID):
        since (str):
        limit (int | Unset):  Default: 100.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MailboxesChangesResponse200]
    """

    kwargs = _get_kwargs(
        identity_id=identity_id,
        since=since,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    identity_id: UUID,
    since: str,
    limit: int | Unset = 100,
) -> MailboxesChangesResponse200:
    """What changed since you last looked

     Per mailbox, not per folder: a message moving from the inbox to the archive is one event, and the
    row says where it went. Arrivals are included, so this is the only thing to poll. `since` is the
    `sync_cursor` from a listing or the `next_cursor` from a previous delta — **not** a page cursor,
    which walks a different order and is refused rather than guessed at. A cursor older than the window
    in which we keep the record of what was deleted returns `410 resync`, because an empty delta would
    be indistinguishable from "nothing changed".

    Args:
        identity_id (UUID):
        since (str):
        limit (int | Unset):  Default: 100.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MailboxesChangesResponse200
    """

    return sync_detailed(
        client=client,
        identity_id=identity_id,
        since=since,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    identity_id: UUID,
    since: str,
    limit: int | Unset = 100,
) -> Response[MailboxesChangesResponse200]:
    """What changed since you last looked

     Per mailbox, not per folder: a message moving from the inbox to the archive is one event, and the
    row says where it went. Arrivals are included, so this is the only thing to poll. `since` is the
    `sync_cursor` from a listing or the `next_cursor` from a previous delta — **not** a page cursor,
    which walks a different order and is refused rather than guessed at. A cursor older than the window
    in which we keep the record of what was deleted returns `410 resync`, because an empty delta would
    be indistinguishable from "nothing changed".

    Args:
        identity_id (UUID):
        since (str):
        limit (int | Unset):  Default: 100.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MailboxesChangesResponse200]
    """

    kwargs = _get_kwargs(
        identity_id=identity_id,
        since=since,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    identity_id: UUID,
    since: str,
    limit: int | Unset = 100,
) -> MailboxesChangesResponse200:
    """What changed since you last looked

     Per mailbox, not per folder: a message moving from the inbox to the archive is one event, and the
    row says where it went. Arrivals are included, so this is the only thing to poll. `since` is the
    `sync_cursor` from a listing or the `next_cursor` from a previous delta — **not** a page cursor,
    which walks a different order and is refused rather than guessed at. A cursor older than the window
    in which we keep the record of what was deleted returns `410 resync`, because an empty delta would
    be indistinguishable from "nothing changed".

    Args:
        identity_id (UUID):
        since (str):
        limit (int | Unset):  Default: 100.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MailboxesChangesResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            identity_id=identity_id,
            since=since,
            limit=limit,
        )
    ).parsed
