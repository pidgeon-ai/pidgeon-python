from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.calendar_create_event_body import CalendarCreateEventBody
from ...models.calendar_create_event_response_201 import CalendarCreateEventResponse201
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    body: CalendarCreateEventBody,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/identities/{id}/calendar/events".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CalendarCreateEventResponse201:
    if response.status_code >= 400:
        raise errors.PidgeonError.from_response(response)

    if response.status_code == 201:
        response_201 = CalendarCreateEventResponse201.from_dict(response.json())

        return response_201

    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CalendarCreateEventResponse201]:
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
    body: CalendarCreateEventBody,
    idempotency_key: str | Unset = UNSET,
) -> Response[CalendarCreateEventResponse201]:
    """Put something on the calendar

     `start` and `end` are **local wall times with no zone on them** — `2026-10-20T14:00:00` — and
    `timezone` is a field of its own. That pair is the truth; `starts_at` is the same moment as an
    instant, derived from it, and it is what survives a daylight-saving change. For an all-day event,
    `end` is the last day, inclusive.

    Args:
        id (str):
        idempotency_key (str | Unset):
        body (CalendarCreateEventBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CalendarCreateEventResponse201]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CalendarCreateEventBody,
    idempotency_key: str | Unset = UNSET,
) -> CalendarCreateEventResponse201:
    """Put something on the calendar

     `start` and `end` are **local wall times with no zone on them** — `2026-10-20T14:00:00` — and
    `timezone` is a field of its own. That pair is the truth; `starts_at` is the same moment as an
    instant, derived from it, and it is what survives a daylight-saving change. For an all-day event,
    `end` is the last day, inclusive.

    Args:
        id (str):
        idempotency_key (str | Unset):
        body (CalendarCreateEventBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CalendarCreateEventResponse201
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CalendarCreateEventBody,
    idempotency_key: str | Unset = UNSET,
) -> Response[CalendarCreateEventResponse201]:
    """Put something on the calendar

     `start` and `end` are **local wall times with no zone on them** — `2026-10-20T14:00:00` — and
    `timezone` is a field of its own. That pair is the truth; `starts_at` is the same moment as an
    instant, derived from it, and it is what survives a daylight-saving change. For an all-day event,
    `end` is the last day, inclusive.

    Args:
        id (str):
        idempotency_key (str | Unset):
        body (CalendarCreateEventBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CalendarCreateEventResponse201]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CalendarCreateEventBody,
    idempotency_key: str | Unset = UNSET,
) -> CalendarCreateEventResponse201:
    """Put something on the calendar

     `start` and `end` are **local wall times with no zone on them** — `2026-10-20T14:00:00` — and
    `timezone` is a field of its own. That pair is the truth; `starts_at` is the same moment as an
    instant, derived from it, and it is what survives a daylight-saving change. For an all-day event,
    `end` is the last day, inclusive.

    Args:
        id (str):
        idempotency_key (str | Unset):
        body (CalendarCreateEventBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CalendarCreateEventResponse201
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
