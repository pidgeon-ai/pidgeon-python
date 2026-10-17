import datetime
from http import HTTPStatus
from typing import Any, cast
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
        "url": "/events/socket",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | Error | None:
    if response.status_code == 101:
        response_101 = cast(Any, None)
        return response_101

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | Error]:
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
) -> Response[Any | Error]:
    """Events over a WebSocket

     The event log over a WebSocket — `wss://pidgeon.ai/api/v1/events/socket` — with the same `type`,
    `identity_id` and `after` as `GET /events/stream`. All frames are JSON text.

    **Authenticate** with the `Authorization` header on the upgrade, or — from a browser, which cannot
    set one — send `{"type":"auth","api_key":"pgn_live_…"}` as the first message within ten seconds.
    Never put the key in the URL.

    **The server sends** `{"type":"ready","cursor"}`, then `{"type":"event","event":Event}` per event,
    oldest first. Before about 280 seconds it sends `{"type":"reconnect","cursor"}` and closes with
    4000: reconnect with `after` set to that cursor and nothing is missed. 4401 means no key or a bad
    one; 4500 means the read failed — reconnect with the last cursor you saw.

    Like the stream, it polls the log on our side of the wire every two seconds.

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
        Response[Any | Error]
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
) -> Any | Error | None:
    """Events over a WebSocket

     The event log over a WebSocket — `wss://pidgeon.ai/api/v1/events/socket` — with the same `type`,
    `identity_id` and `after` as `GET /events/stream`. All frames are JSON text.

    **Authenticate** with the `Authorization` header on the upgrade, or — from a browser, which cannot
    set one — send `{"type":"auth","api_key":"pgn_live_…"}` as the first message within ten seconds.
    Never put the key in the URL.

    **The server sends** `{"type":"ready","cursor"}`, then `{"type":"event","event":Event}` per event,
    oldest first. Before about 280 seconds it sends `{"type":"reconnect","cursor"}` and closes with
    4000: reconnect with `after` set to that cursor and nothing is missed. 4401 means no key or a bad
    one; 4500 means the read failed — reconnect with the last cursor you saw.

    Like the stream, it polls the log on our side of the wire every two seconds.

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
        Any | Error
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
) -> Response[Any | Error]:
    """Events over a WebSocket

     The event log over a WebSocket — `wss://pidgeon.ai/api/v1/events/socket` — with the same `type`,
    `identity_id` and `after` as `GET /events/stream`. All frames are JSON text.

    **Authenticate** with the `Authorization` header on the upgrade, or — from a browser, which cannot
    set one — send `{"type":"auth","api_key":"pgn_live_…"}` as the first message within ten seconds.
    Never put the key in the URL.

    **The server sends** `{"type":"ready","cursor"}`, then `{"type":"event","event":Event}` per event,
    oldest first. Before about 280 seconds it sends `{"type":"reconnect","cursor"}` and closes with
    4000: reconnect with `after` set to that cursor and nothing is missed. 4401 means no key or a bad
    one; 4500 means the read failed — reconnect with the last cursor you saw.

    Like the stream, it polls the log on our side of the wire every two seconds.

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
        Response[Any | Error]
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
) -> Any | Error | None:
    """Events over a WebSocket

     The event log over a WebSocket — `wss://pidgeon.ai/api/v1/events/socket` — with the same `type`,
    `identity_id` and `after` as `GET /events/stream`. All frames are JSON text.

    **Authenticate** with the `Authorization` header on the upgrade, or — from a browser, which cannot
    set one — send `{"type":"auth","api_key":"pgn_live_…"}` as the first message within ten seconds.
    Never put the key in the URL.

    **The server sends** `{"type":"ready","cursor"}`, then `{"type":"event","event":Event}` per event,
    oldest first. Before about 280 seconds it sends `{"type":"reconnect","cursor"}` and closes with
    4000: reconnect with `after` set to that cursor and nothing is missed. 4401 means no key or a bad
    one; 4500 means the read failed — reconnect with the last cursor you saw.

    Like the stream, it polls the log on our side of the wire every two seconds.

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
        Any | Error
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
