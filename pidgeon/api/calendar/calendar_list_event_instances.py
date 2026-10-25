import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.calendar_list_event_instances_response_200 import CalendarListEventInstancesResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    event_id: str,
    *,
    after: datetime.datetime | Unset = UNSET,
    before: datetime.datetime | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_after: str | Unset = UNSET
    if not isinstance(after, Unset):
        json_after = after.isoformat()
    params["after"] = json_after

    json_before: str | Unset = UNSET
    if not isinstance(before, Unset):
        json_before = before.isoformat()
    params["before"] = json_before

    params["limit"] = limit

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/identities/{id}/calendar/events/{event_id}/instances".format(
            id=quote(str(id), safe=""),
            event_id=quote(str(event_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CalendarListEventInstancesResponse200:
    if response.status_code >= 400:
        raise errors.PidgeonError.from_response(response)

    if response.status_code == 200:
        response_200 = CalendarListEventInstancesResponse200.from_dict(response.json())

        return response_200

    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CalendarListEventInstancesResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    event_id: str,
    *,
    client: AuthenticatedClient | Client,
    after: datetime.datetime | Unset = UNSET,
    before: datetime.datetime | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> Response[CalendarListEventInstancesResponse200]:
    """The dates a series actually happens

     Most of them have no row — they are expanded from the rule, which is what makes a weekly meeting
    cheap to store. An id here is `{seriesId}::{originalStart}`, derived rather than allocated, and it
    does **not** change when you edit that date. A date somebody edited comes back in place of the one
    the rule generated, under that id.

    Args:
        id (str):
        event_id (str):
        after (datetime.datetime | Unset):
        before (datetime.datetime | Unset):
        limit (int | Unset):
        cursor (str | Unset): From a previous page’s `next_cursor`. Opaque — do not parse it.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CalendarListEventInstancesResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        event_id=event_id,
        after=after,
        before=before,
        limit=limit,
        cursor=cursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    event_id: str,
    *,
    client: AuthenticatedClient | Client,
    after: datetime.datetime | Unset = UNSET,
    before: datetime.datetime | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> CalendarListEventInstancesResponse200:
    """The dates a series actually happens

     Most of them have no row — they are expanded from the rule, which is what makes a weekly meeting
    cheap to store. An id here is `{seriesId}::{originalStart}`, derived rather than allocated, and it
    does **not** change when you edit that date. A date somebody edited comes back in place of the one
    the rule generated, under that id.

    Args:
        id (str):
        event_id (str):
        after (datetime.datetime | Unset):
        before (datetime.datetime | Unset):
        limit (int | Unset):
        cursor (str | Unset): From a previous page’s `next_cursor`. Opaque — do not parse it.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CalendarListEventInstancesResponse200
    """

    return sync_detailed(
        id=id,
        event_id=event_id,
        client=client,
        after=after,
        before=before,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    id: str,
    event_id: str,
    *,
    client: AuthenticatedClient | Client,
    after: datetime.datetime | Unset = UNSET,
    before: datetime.datetime | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> Response[CalendarListEventInstancesResponse200]:
    """The dates a series actually happens

     Most of them have no row — they are expanded from the rule, which is what makes a weekly meeting
    cheap to store. An id here is `{seriesId}::{originalStart}`, derived rather than allocated, and it
    does **not** change when you edit that date. A date somebody edited comes back in place of the one
    the rule generated, under that id.

    Args:
        id (str):
        event_id (str):
        after (datetime.datetime | Unset):
        before (datetime.datetime | Unset):
        limit (int | Unset):
        cursor (str | Unset): From a previous page’s `next_cursor`. Opaque — do not parse it.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CalendarListEventInstancesResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        event_id=event_id,
        after=after,
        before=before,
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    event_id: str,
    *,
    client: AuthenticatedClient | Client,
    after: datetime.datetime | Unset = UNSET,
    before: datetime.datetime | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> CalendarListEventInstancesResponse200:
    """The dates a series actually happens

     Most of them have no row — they are expanded from the rule, which is what makes a weekly meeting
    cheap to store. An id here is `{seriesId}::{originalStart}`, derived rather than allocated, and it
    does **not** change when you edit that date. A date somebody edited comes back in place of the one
    the rule generated, under that id.

    Args:
        id (str):
        event_id (str):
        after (datetime.datetime | Unset):
        before (datetime.datetime | Unset):
        limit (int | Unset):
        cursor (str | Unset): From a previous page’s `next_cursor`. Opaque — do not parse it.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CalendarListEventInstancesResponse200
    """

    return (
        await asyncio_detailed(
            id=id,
            event_id=event_id,
            client=client,
            after=after,
            before=before,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
