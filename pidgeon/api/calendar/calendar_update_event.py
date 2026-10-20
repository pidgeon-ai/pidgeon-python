from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.calendar_update_event_body import CalendarUpdateEventBody
from ...models.calendar_update_event_mode import CalendarUpdateEventMode
from ...models.calendar_update_event_response_200 import CalendarUpdateEventResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    event_id: str,
    *,
    body: CalendarUpdateEventBody,
    mode: CalendarUpdateEventMode | Unset = UNSET,
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
        "method": "patch",
        "url": "/identities/{id}/calendar/events/{event_id}".format(
            id=quote(str(id), safe=""),
            event_id=quote(str(event_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CalendarUpdateEventResponse200:
    if response.status_code >= 400:
        raise errors.PidgeonError.from_response(response)

    if response.status_code == 200:
        response_200 = CalendarUpdateEventResponse200.from_dict(response.json())

        return response_200

    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CalendarUpdateEventResponse200]:
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
    body: CalendarUpdateEventBody,
    mode: CalendarUpdateEventMode | Unset = UNSET,
    if_match: str | Unset = UNSET,
) -> Response[CalendarUpdateEventResponse200]:
    """Change an event

     An omitted field survives. `sequence` rises only when the change is one attendees see — the time,
    the title, the place, the status, the list. A `metadata` edit moves the `etag` and not the sequence,
    because nobody is ever told about it.

    Args:
        id (str):
        event_id (str):
        mode (CalendarUpdateEventMode | Unset):
        if_match (str | Unset):
        body (CalendarUpdateEventBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CalendarUpdateEventResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        event_id=event_id,
        body=body,
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
    body: CalendarUpdateEventBody,
    mode: CalendarUpdateEventMode | Unset = UNSET,
    if_match: str | Unset = UNSET,
) -> CalendarUpdateEventResponse200:
    """Change an event

     An omitted field survives. `sequence` rises only when the change is one attendees see — the time,
    the title, the place, the status, the list. A `metadata` edit moves the `etag` and not the sequence,
    because nobody is ever told about it.

    Args:
        id (str):
        event_id (str):
        mode (CalendarUpdateEventMode | Unset):
        if_match (str | Unset):
        body (CalendarUpdateEventBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CalendarUpdateEventResponse200
    """

    return sync_detailed(
        id=id,
        event_id=event_id,
        client=client,
        body=body,
        mode=mode,
        if_match=if_match,
    ).parsed


async def asyncio_detailed(
    id: str,
    event_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CalendarUpdateEventBody,
    mode: CalendarUpdateEventMode | Unset = UNSET,
    if_match: str | Unset = UNSET,
) -> Response[CalendarUpdateEventResponse200]:
    """Change an event

     An omitted field survives. `sequence` rises only when the change is one attendees see — the time,
    the title, the place, the status, the list. A `metadata` edit moves the `etag` and not the sequence,
    because nobody is ever told about it.

    Args:
        id (str):
        event_id (str):
        mode (CalendarUpdateEventMode | Unset):
        if_match (str | Unset):
        body (CalendarUpdateEventBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CalendarUpdateEventResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        event_id=event_id,
        body=body,
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
    body: CalendarUpdateEventBody,
    mode: CalendarUpdateEventMode | Unset = UNSET,
    if_match: str | Unset = UNSET,
) -> CalendarUpdateEventResponse200:
    """Change an event

     An omitted field survives. `sequence` rises only when the change is one attendees see — the time,
    the title, the place, the status, the list. A `metadata` edit moves the `etag` and not the sequence,
    because nobody is ever told about it.

    Args:
        id (str):
        event_id (str):
        mode (CalendarUpdateEventMode | Unset):
        if_match (str | Unset):
        body (CalendarUpdateEventBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CalendarUpdateEventResponse200
    """

    return (
        await asyncio_detailed(
            id=id,
            event_id=event_id,
            client=client,
            body=body,
            mode=mode,
            if_match=if_match,
        )
    ).parsed
