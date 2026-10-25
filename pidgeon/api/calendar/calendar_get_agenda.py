import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.calendar_get_agenda_include_overlapping import CalendarGetAgendaIncludeOverlapping
from ...models.calendar_get_agenda_response_200 import CalendarGetAgendaResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    after: datetime.datetime | Unset = UNSET,
    before: datetime.datetime | Unset = UNSET,
    include_overlapping: CalendarGetAgendaIncludeOverlapping | Unset = UNSET,
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

    json_include_overlapping: str | Unset = UNSET
    if not isinstance(include_overlapping, Unset):
        json_include_overlapping = include_overlapping.value

    params["include_overlapping"] = json_include_overlapping

    params["limit"] = limit

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/identities/{id}/calendar/agenda".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CalendarGetAgendaResponse200:
    if response.status_code >= 400:
        raise errors.PidgeonError.from_response(response)

    if response.status_code == 200:
        response_200 = CalendarGetAgendaResponse200.from_dict(response.json())

        return response_200

    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CalendarGetAgendaResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    after: datetime.datetime | Unset = UNSET,
    before: datetime.datetime | Unset = UNSET,
    include_overlapping: CalendarGetAgendaIncludeOverlapping | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> Response[CalendarGetAgendaResponse200]:
    """What is on, in a window, in order

     `include_overlapping` defaults to true, which is the difference between *what starts today* and
    *what is on today*: a meeting that began last night and runs into this morning is on today, and a
    naive `starts_at between` misses it. Cancelled events are left out — an agenda is what you are
    doing.

    Args:
        id (str):
        after (datetime.datetime | Unset):
        before (datetime.datetime | Unset):
        include_overlapping (CalendarGetAgendaIncludeOverlapping | Unset):
        limit (int | Unset):
        cursor (str | Unset): From a previous page’s `next_cursor`. Opaque — do not parse it.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CalendarGetAgendaResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        after=after,
        before=before,
        include_overlapping=include_overlapping,
        limit=limit,
        cursor=cursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    after: datetime.datetime | Unset = UNSET,
    before: datetime.datetime | Unset = UNSET,
    include_overlapping: CalendarGetAgendaIncludeOverlapping | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> CalendarGetAgendaResponse200:
    """What is on, in a window, in order

     `include_overlapping` defaults to true, which is the difference between *what starts today* and
    *what is on today*: a meeting that began last night and runs into this morning is on today, and a
    naive `starts_at between` misses it. Cancelled events are left out — an agenda is what you are
    doing.

    Args:
        id (str):
        after (datetime.datetime | Unset):
        before (datetime.datetime | Unset):
        include_overlapping (CalendarGetAgendaIncludeOverlapping | Unset):
        limit (int | Unset):
        cursor (str | Unset): From a previous page’s `next_cursor`. Opaque — do not parse it.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CalendarGetAgendaResponse200
    """

    return sync_detailed(
        id=id,
        client=client,
        after=after,
        before=before,
        include_overlapping=include_overlapping,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    after: datetime.datetime | Unset = UNSET,
    before: datetime.datetime | Unset = UNSET,
    include_overlapping: CalendarGetAgendaIncludeOverlapping | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> Response[CalendarGetAgendaResponse200]:
    """What is on, in a window, in order

     `include_overlapping` defaults to true, which is the difference between *what starts today* and
    *what is on today*: a meeting that began last night and runs into this morning is on today, and a
    naive `starts_at between` misses it. Cancelled events are left out — an agenda is what you are
    doing.

    Args:
        id (str):
        after (datetime.datetime | Unset):
        before (datetime.datetime | Unset):
        include_overlapping (CalendarGetAgendaIncludeOverlapping | Unset):
        limit (int | Unset):
        cursor (str | Unset): From a previous page’s `next_cursor`. Opaque — do not parse it.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CalendarGetAgendaResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        after=after,
        before=before,
        include_overlapping=include_overlapping,
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    after: datetime.datetime | Unset = UNSET,
    before: datetime.datetime | Unset = UNSET,
    include_overlapping: CalendarGetAgendaIncludeOverlapping | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> CalendarGetAgendaResponse200:
    """What is on, in a window, in order

     `include_overlapping` defaults to true, which is the difference between *what starts today* and
    *what is on today*: a meeting that began last night and runs into this morning is on today, and a
    naive `starts_at between` misses it. Cancelled events are left out — an agenda is what you are
    doing.

    Args:
        id (str):
        after (datetime.datetime | Unset):
        before (datetime.datetime | Unset):
        include_overlapping (CalendarGetAgendaIncludeOverlapping | Unset):
        limit (int | Unset):
        cursor (str | Unset): From a previous page’s `next_cursor`. Opaque — do not parse it.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CalendarGetAgendaResponse200
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            after=after,
            before=before,
            include_overlapping=include_overlapping,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
