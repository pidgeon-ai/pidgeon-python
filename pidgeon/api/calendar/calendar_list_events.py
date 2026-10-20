from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.calendar_list_events_response_200 import CalendarListEventsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/identities/{id}/calendar/events".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CalendarListEventsResponse200:
    if response.status_code >= 400:
        raise errors.PidgeonError.from_response(response)

    if response.status_code == 200:
        response_200 = CalendarListEventsResponse200.from_dict(response.json())

        return response_200

    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CalendarListEventsResponse200]:
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
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> Response[CalendarListEventsResponse200]:
    """Everything on the calendar

     Ordered by when it last changed. `GET /agenda` is the other read and the one you usually want: this
    answers *what is on this calendar*, that answers *what is on between these two moments*.

    Args:
        id (str):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset): From a previous page’s `next_cursor`. Opaque — do not parse it.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CalendarListEventsResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
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
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> CalendarListEventsResponse200:
    """Everything on the calendar

     Ordered by when it last changed. `GET /agenda` is the other read and the one you usually want: this
    answers *what is on this calendar*, that answers *what is on between these two moments*.

    Args:
        id (str):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset): From a previous page’s `next_cursor`. Opaque — do not parse it.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CalendarListEventsResponse200
    """

    return sync_detailed(
        id=id,
        client=client,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> Response[CalendarListEventsResponse200]:
    """Everything on the calendar

     Ordered by when it last changed. `GET /agenda` is the other read and the one you usually want: this
    answers *what is on this calendar*, that answers *what is on between these two moments*.

    Args:
        id (str):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset): From a previous page’s `next_cursor`. Opaque — do not parse it.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CalendarListEventsResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> CalendarListEventsResponse200:
    """Everything on the calendar

     Ordered by when it last changed. `GET /agenda` is the other read and the one you usually want: this
    answers *what is on this calendar*, that answers *what is on between these two moments*.

    Args:
        id (str):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset): From a previous page’s `next_cursor`. Opaque — do not parse it.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CalendarListEventsResponse200
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
