import datetime
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
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    identity_id: UUID | Unset = UNSET,
    after: datetime.datetime | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["cursor"] = cursor

    params["type"] = type_

    json_identity_id: str | Unset = UNSET
    if not isinstance(identity_id, Unset):
        json_identity_id = str(identity_id)
    params["identity_id"] = json_identity_id

    json_after: str | Unset = UNSET
    if not isinstance(after, Unset):
        json_after = after.isoformat()
    params["after"] = json_after

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/events/stream",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | str | None:
    if response.status_code == 200:
        response_200 = response.text
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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    identity_id: UUID | Unset = UNSET,
    after: datetime.datetime | Unset = UNSET,
) -> Response[Error | str]:
    """Stream events as they happen

     The event log held open, for a caller that cannot host a webhook endpoint — a script on a laptop, a
    notebook, an agent runtime with no public address.

    **Server-sent events.** Each message carries the event as `data`, the event type as `event:`, and
    the cursor to resume from as `id:`. Authentication, filtering by `type` and `identity_id`, and the
    `after` cursor are all exactly as on `GET /events` — this is that read, held open.

    **Reconnection is automatic and lossless.** A compliant client resends the last `id:` it saw as
    `Last-Event-ID`, which is preferred over `after`, so a dropped connection resumes with no gap and no
    repeat. The connection closes itself after about 280 seconds so that the last thing you receive is a
    cursor rather than a socket error; reconnect and carry on.

    **It polls, every two seconds, on our side of the wire.** No push exists in the database. What this
    buys is one held connection instead of a request from your network on a timer, and being woken only
    when something happened.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset): From a previous page’s `next_cursor`. Opaque — do not parse it.
        type_ (str | Unset):
        identity_id (UUID | Unset):
        after (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | str]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
        type_=type_,
        identity_id=identity_id,
        after=after,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    identity_id: UUID | Unset = UNSET,
    after: datetime.datetime | Unset = UNSET,
) -> Error | str | None:
    """Stream events as they happen

     The event log held open, for a caller that cannot host a webhook endpoint — a script on a laptop, a
    notebook, an agent runtime with no public address.

    **Server-sent events.** Each message carries the event as `data`, the event type as `event:`, and
    the cursor to resume from as `id:`. Authentication, filtering by `type` and `identity_id`, and the
    `after` cursor are all exactly as on `GET /events` — this is that read, held open.

    **Reconnection is automatic and lossless.** A compliant client resends the last `id:` it saw as
    `Last-Event-ID`, which is preferred over `after`, so a dropped connection resumes with no gap and no
    repeat. The connection closes itself after about 280 seconds so that the last thing you receive is a
    cursor rather than a socket error; reconnect and carry on.

    **It polls, every two seconds, on our side of the wire.** No push exists in the database. What this
    buys is one held connection instead of a request from your network on a timer, and being woken only
    when something happened.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset): From a previous page’s `next_cursor`. Opaque — do not parse it.
        type_ (str | Unset):
        identity_id (UUID | Unset):
        after (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | str
    """

    return sync_detailed(
        client=client,
        limit=limit,
        cursor=cursor,
        type_=type_,
        identity_id=identity_id,
        after=after,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    identity_id: UUID | Unset = UNSET,
    after: datetime.datetime | Unset = UNSET,
) -> Response[Error | str]:
    """Stream events as they happen

     The event log held open, for a caller that cannot host a webhook endpoint — a script on a laptop, a
    notebook, an agent runtime with no public address.

    **Server-sent events.** Each message carries the event as `data`, the event type as `event:`, and
    the cursor to resume from as `id:`. Authentication, filtering by `type` and `identity_id`, and the
    `after` cursor are all exactly as on `GET /events` — this is that read, held open.

    **Reconnection is automatic and lossless.** A compliant client resends the last `id:` it saw as
    `Last-Event-ID`, which is preferred over `after`, so a dropped connection resumes with no gap and no
    repeat. The connection closes itself after about 280 seconds so that the last thing you receive is a
    cursor rather than a socket error; reconnect and carry on.

    **It polls, every two seconds, on our side of the wire.** No push exists in the database. What this
    buys is one held connection instead of a request from your network on a timer, and being woken only
    when something happened.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset): From a previous page’s `next_cursor`. Opaque — do not parse it.
        type_ (str | Unset):
        identity_id (UUID | Unset):
        after (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | str]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
        type_=type_,
        identity_id=identity_id,
        after=after,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    identity_id: UUID | Unset = UNSET,
    after: datetime.datetime | Unset = UNSET,
) -> Error | str | None:
    """Stream events as they happen

     The event log held open, for a caller that cannot host a webhook endpoint — a script on a laptop, a
    notebook, an agent runtime with no public address.

    **Server-sent events.** Each message carries the event as `data`, the event type as `event:`, and
    the cursor to resume from as `id:`. Authentication, filtering by `type` and `identity_id`, and the
    `after` cursor are all exactly as on `GET /events` — this is that read, held open.

    **Reconnection is automatic and lossless.** A compliant client resends the last `id:` it saw as
    `Last-Event-ID`, which is preferred over `after`, so a dropped connection resumes with no gap and no
    repeat. The connection closes itself after about 280 seconds so that the last thing you receive is a
    cursor rather than a socket error; reconnect and carry on.

    **It polls, every two seconds, on our side of the wire.** No push exists in the database. What this
    buys is one held connection instead of a request from your network on a timer, and being woken only
    when something happened.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset): From a previous page’s `next_cursor`. Opaque — do not parse it.
        type_ (str | Unset):
        identity_id (UUID | Unset):
        after (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | str
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            cursor=cursor,
            type_=type_,
            identity_id=identity_id,
            after=after,
        )
    ).parsed
