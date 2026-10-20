import datetime
from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.events_list_response_200 import EventsListResponse200
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
        "url": "/events",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> EventsListResponse200:
    if response.status_code >= 400:
        raise errors.PidgeonError.from_response(response)

    if response.status_code == 200:
        response_200 = EventsListResponse200.from_dict(response.json())

        return response_200

    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[EventsListResponse200]:
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
) -> Response[EventsListResponse200]:
    """List events

     The same events a webhook delivers, readable after the fact — so a missed delivery is recoverable
    without replaying anything.

    **Two directions.** `cursor` pages backwards through history, newest first, which is what a
    dashboard shows. `after` tails the log forwards, oldest first, which is what a caller that cannot
    receive a webhook does: ask for everything since the last event you saw, act on it, and keep the
    last `created_at` as the next cursor. Naming both is refused — they are different reads.

    **Starting from nothing: pass `after=1970-01-01T00:00:00Z`.** With neither parameter this answers
    newest first, so a first-time consumer that takes the last row as its high-water mark stores the
    *oldest* event in the log and never advances. Any timestamp at or before the oldest event you hold
    will do; the epoch is the one nobody has to think about.

    A forward page is ordered oldest first precisely so its **last** row is the high-water mark to
    resume from; `next_cursor` is that row either way.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset): From a previous page’s `next_cursor`. Opaque — do not parse it.
        type_ (str | Unset):
        identity_id (UUID | Unset):
        after (datetime.datetime | Unset):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EventsListResponse200]
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
) -> EventsListResponse200:
    """List events

     The same events a webhook delivers, readable after the fact — so a missed delivery is recoverable
    without replaying anything.

    **Two directions.** `cursor` pages backwards through history, newest first, which is what a
    dashboard shows. `after` tails the log forwards, oldest first, which is what a caller that cannot
    receive a webhook does: ask for everything since the last event you saw, act on it, and keep the
    last `created_at` as the next cursor. Naming both is refused — they are different reads.

    **Starting from nothing: pass `after=1970-01-01T00:00:00Z`.** With neither parameter this answers
    newest first, so a first-time consumer that takes the last row as its high-water mark stores the
    *oldest* event in the log and never advances. Any timestamp at or before the oldest event you hold
    will do; the epoch is the one nobody has to think about.

    A forward page is ordered oldest first precisely so its **last** row is the high-water mark to
    resume from; `next_cursor` is that row either way.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset): From a previous page’s `next_cursor`. Opaque — do not parse it.
        type_ (str | Unset):
        identity_id (UUID | Unset):
        after (datetime.datetime | Unset):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EventsListResponse200
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
) -> Response[EventsListResponse200]:
    """List events

     The same events a webhook delivers, readable after the fact — so a missed delivery is recoverable
    without replaying anything.

    **Two directions.** `cursor` pages backwards through history, newest first, which is what a
    dashboard shows. `after` tails the log forwards, oldest first, which is what a caller that cannot
    receive a webhook does: ask for everything since the last event you saw, act on it, and keep the
    last `created_at` as the next cursor. Naming both is refused — they are different reads.

    **Starting from nothing: pass `after=1970-01-01T00:00:00Z`.** With neither parameter this answers
    newest first, so a first-time consumer that takes the last row as its high-water mark stores the
    *oldest* event in the log and never advances. Any timestamp at or before the oldest event you hold
    will do; the epoch is the one nobody has to think about.

    A forward page is ordered oldest first precisely so its **last** row is the high-water mark to
    resume from; `next_cursor` is that row either way.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset): From a previous page’s `next_cursor`. Opaque — do not parse it.
        type_ (str | Unset):
        identity_id (UUID | Unset):
        after (datetime.datetime | Unset):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EventsListResponse200]
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
) -> EventsListResponse200:
    """List events

     The same events a webhook delivers, readable after the fact — so a missed delivery is recoverable
    without replaying anything.

    **Two directions.** `cursor` pages backwards through history, newest first, which is what a
    dashboard shows. `after` tails the log forwards, oldest first, which is what a caller that cannot
    receive a webhook does: ask for everything since the last event you saw, act on it, and keep the
    last `created_at` as the next cursor. Naming both is refused — they are different reads.

    **Starting from nothing: pass `after=1970-01-01T00:00:00Z`.** With neither parameter this answers
    newest first, so a first-time consumer that takes the last row as its high-water mark stores the
    *oldest* event in the log and never advances. Any timestamp at or before the oldest event you hold
    will do; the epoch is the one nobody has to think about.

    A forward page is ordered oldest first precisely so its **last** row is the high-water mark to
    resume from; `next_cursor` is that row either way.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset): From a previous page’s `next_cursor`. Opaque — do not parse it.
        type_ (str | Unset):
        identity_id (UUID | Unset):
        after (datetime.datetime | Unset):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EventsListResponse200
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
