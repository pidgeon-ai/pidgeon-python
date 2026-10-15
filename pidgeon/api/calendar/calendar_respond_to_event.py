from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.calendar_respond_to_event_body import CalendarRespondToEventBody
from ...models.calendar_respond_to_event_response_200 import CalendarRespondToEventResponse200
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    event_id: str,
    *,
    body: CalendarRespondToEventBody,
    if_match: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(if_match, Unset):
        headers["If-Match"] = if_match

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/identities/{id}/calendar/events/{event_id}/respond".format(
            id=quote(str(id), safe=""),
            event_id=quote(str(event_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CalendarRespondToEventResponse200 | Error | None:
    if response.status_code == 200:
        response_200 = CalendarRespondToEventResponse200.from_dict(response.json())

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
) -> Response[CalendarRespondToEventResponse200 | Error]:
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
    body: CalendarRespondToEventBody,
    if_match: str | Unset = UNSET,
) -> Response[CalendarRespondToEventResponse200 | Error]:
    """Answer a meeting from the calendar

     The same act as `POST /messages/{id}/invitation/respond`, reached from the other end — an agent
    working from an agenda holds an event id and not a message id. When the meeting came from mail and
    `send_reply` is true (the default), an iCalendar `REPLY` goes to the organiser and the answer is
    written onto the event. When it did not — a meeting this mailbox created itself — there is nobody to
    reply to, so the answer is recorded and `reply_sent` is false. One of this mailbox’s own addresses
    must be on the attendee list, including an address routed to it.

    Args:
        id (str):
        event_id (str):
        if_match (str | Unset):
        body (CalendarRespondToEventBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CalendarRespondToEventResponse200 | Error]
    """

    kwargs = _get_kwargs(
        id=id,
        event_id=event_id,
        body=body,
        if_match=if_match,
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
    body: CalendarRespondToEventBody,
    if_match: str | Unset = UNSET,
) -> CalendarRespondToEventResponse200 | Error | None:
    """Answer a meeting from the calendar

     The same act as `POST /messages/{id}/invitation/respond`, reached from the other end — an agent
    working from an agenda holds an event id and not a message id. When the meeting came from mail and
    `send_reply` is true (the default), an iCalendar `REPLY` goes to the organiser and the answer is
    written onto the event. When it did not — a meeting this mailbox created itself — there is nobody to
    reply to, so the answer is recorded and `reply_sent` is false. One of this mailbox’s own addresses
    must be on the attendee list, including an address routed to it.

    Args:
        id (str):
        event_id (str):
        if_match (str | Unset):
        body (CalendarRespondToEventBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CalendarRespondToEventResponse200 | Error
    """

    return sync_detailed(
        id=id,
        event_id=event_id,
        client=client,
        body=body,
        if_match=if_match,
    ).parsed


async def asyncio_detailed(
    id: str,
    event_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CalendarRespondToEventBody,
    if_match: str | Unset = UNSET,
) -> Response[CalendarRespondToEventResponse200 | Error]:
    """Answer a meeting from the calendar

     The same act as `POST /messages/{id}/invitation/respond`, reached from the other end — an agent
    working from an agenda holds an event id and not a message id. When the meeting came from mail and
    `send_reply` is true (the default), an iCalendar `REPLY` goes to the organiser and the answer is
    written onto the event. When it did not — a meeting this mailbox created itself — there is nobody to
    reply to, so the answer is recorded and `reply_sent` is false. One of this mailbox’s own addresses
    must be on the attendee list, including an address routed to it.

    Args:
        id (str):
        event_id (str):
        if_match (str | Unset):
        body (CalendarRespondToEventBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CalendarRespondToEventResponse200 | Error]
    """

    kwargs = _get_kwargs(
        id=id,
        event_id=event_id,
        body=body,
        if_match=if_match,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    event_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CalendarRespondToEventBody,
    if_match: str | Unset = UNSET,
) -> CalendarRespondToEventResponse200 | Error | None:
    """Answer a meeting from the calendar

     The same act as `POST /messages/{id}/invitation/respond`, reached from the other end — an agent
    working from an agenda holds an event id and not a message id. When the meeting came from mail and
    `send_reply` is true (the default), an iCalendar `REPLY` goes to the organiser and the answer is
    written onto the event. When it did not — a meeting this mailbox created itself — there is nobody to
    reply to, so the answer is recorded and `reply_sent` is false. One of this mailbox’s own addresses
    must be on the attendee list, including an address routed to it.

    Args:
        id (str):
        event_id (str):
        if_match (str | Unset):
        body (CalendarRespondToEventBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CalendarRespondToEventResponse200 | Error
    """

    return (
        await asyncio_detailed(
            id=id,
            event_id=event_id,
            client=client,
            body=body,
            if_match=if_match,
        )
    ).parsed
