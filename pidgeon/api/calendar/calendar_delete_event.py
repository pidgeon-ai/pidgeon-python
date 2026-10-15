from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.calendar_delete_event_mode import CalendarDeleteEventMode
from ...models.calendar_delete_event_response_200 import CalendarDeleteEventResponse200
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    event_id: str,
    *,
    mode: CalendarDeleteEventMode | Unset = UNSET,
    if_match: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(if_match, Unset):
        headers["If-Match"] = if_match

    params: dict[str, Any] = {}

    json_mode: str | Unset = UNSET
    if not isinstance(mode, Unset):
        json_mode = mode.value

    params["mode"] = json_mode

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/identities/{id}/calendar/events/{event_id}".format(
            id=quote(str(id), safe=""),
            event_id=quote(str(event_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CalendarDeleteEventResponse200 | Error | None:
    if response.status_code == 200:
        response_200 = CalendarDeleteEventResponse200.from_dict(response.json())

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
) -> Response[CalendarDeleteEventResponse200 | Error]:
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
    mode: CalendarDeleteEventMode | Unset = UNSET,
    if_match: str | Unset = UNSET,
) -> Response[CalendarDeleteEventResponse200 | Error]:
    """Take it off the calendar

     On one date of a series this records that the date does not happen rather than removing a row — the
    rule still generates it, so a removal would bring it straight back. `mode=future` ends the series
    there and leaves every earlier date alone.

    Args:
        id (str):
        event_id (str):
        mode (CalendarDeleteEventMode | Unset):
        if_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CalendarDeleteEventResponse200 | Error]
    """

    kwargs = _get_kwargs(
        id=id,
        event_id=event_id,
        mode=mode,
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
    mode: CalendarDeleteEventMode | Unset = UNSET,
    if_match: str | Unset = UNSET,
) -> CalendarDeleteEventResponse200 | Error | None:
    """Take it off the calendar

     On one date of a series this records that the date does not happen rather than removing a row — the
    rule still generates it, so a removal would bring it straight back. `mode=future` ends the series
    there and leaves every earlier date alone.

    Args:
        id (str):
        event_id (str):
        mode (CalendarDeleteEventMode | Unset):
        if_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CalendarDeleteEventResponse200 | Error
    """

    return sync_detailed(
        id=id,
        event_id=event_id,
        client=client,
        mode=mode,
        if_match=if_match,
    ).parsed


async def asyncio_detailed(
    id: str,
    event_id: str,
    *,
    client: AuthenticatedClient | Client,
    mode: CalendarDeleteEventMode | Unset = UNSET,
    if_match: str | Unset = UNSET,
) -> Response[CalendarDeleteEventResponse200 | Error]:
    """Take it off the calendar

     On one date of a series this records that the date does not happen rather than removing a row — the
    rule still generates it, so a removal would bring it straight back. `mode=future` ends the series
    there and leaves every earlier date alone.

    Args:
        id (str):
        event_id (str):
        mode (CalendarDeleteEventMode | Unset):
        if_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CalendarDeleteEventResponse200 | Error]
    """

    kwargs = _get_kwargs(
        id=id,
        event_id=event_id,
        mode=mode,
        if_match=if_match,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    event_id: str,
    *,
    client: AuthenticatedClient | Client,
    mode: CalendarDeleteEventMode | Unset = UNSET,
    if_match: str | Unset = UNSET,
) -> CalendarDeleteEventResponse200 | Error | None:
    """Take it off the calendar

     On one date of a series this records that the date does not happen rather than removing a row — the
    rule still generates it, so a removal would bring it straight back. `mode=future` ends the series
    there and leaves every earlier date alone.

    Args:
        id (str):
        event_id (str):
        mode (CalendarDeleteEventMode | Unset):
        if_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CalendarDeleteEventResponse200 | Error
    """

    return (
        await asyncio_detailed(
            id=id,
            event_id=event_id,
            client=client,
            mode=mode,
            if_match=if_match,
        )
    ).parsed
