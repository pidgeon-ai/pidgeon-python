import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.calendar_free_time_response_200 import CalendarFreeTimeResponse200
from ...models.calendar_free_time_skip_weekends import CalendarFreeTimeSkipWeekends
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    identity_ids: str,
    after: datetime.datetime | Unset = UNSET,
    before: datetime.datetime | Unset = UNSET,
    duration_minutes: int | Unset = UNSET,
    day_start: str | Unset = UNSET,
    day_end: str | Unset = UNSET,
    timezone: str | Unset = UNSET,
    skip_weekends: CalendarFreeTimeSkipWeekends | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["identity_ids"] = identity_ids

    json_after: str | Unset = UNSET
    if not isinstance(after, Unset):
        json_after = after.isoformat()
    params["after"] = json_after

    json_before: str | Unset = UNSET
    if not isinstance(before, Unset):
        json_before = before.isoformat()
    params["before"] = json_before

    params["duration_minutes"] = duration_minutes

    params["day_start"] = day_start

    params["day_end"] = day_end

    params["timezone"] = timezone

    json_skip_weekends: str | Unset = UNSET
    if not isinstance(skip_weekends, Unset):
        json_skip_weekends = skip_weekends.value

    params["skip_weekends"] = json_skip_weekends

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/calendar/free-time",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CalendarFreeTimeResponse200:
    if response.status_code >= 400:
        raise errors.PidgeonError.from_response(response)

    if response.status_code == 200:
        response_200 = CalendarFreeTimeResponse200.from_dict(response.json())

        return response_200

    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CalendarFreeTimeResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    identity_ids: str,
    after: datetime.datetime | Unset = UNSET,
    before: datetime.datetime | Unset = UNSET,
    duration_minutes: int | Unset = UNSET,
    day_start: str | Unset = UNSET,
    day_end: str | Unset = UNSET,
    timezone: str | Unset = UNSET,
    skip_weekends: CalendarFreeTimeSkipWeekends | Unset = UNSET,
) -> Response[CalendarFreeTimeResponse200]:
    """When several addresses are all free

     The stretches in a window when every address in `identity_ids` is free, at least `duration_minutes`
    long. Busy is a timed event that is not cancelled and that the address has not declined; tentative
    counts as busy, all-day events do not. `day_start` and `day_end` limit it to working hours, read in
    `timezone` (the first address’s calendar zone by default), and each slot carries its wall times in
    that zone too. Needs `read` on every address. It books nothing.

    Args:
        identity_ids (str): The addresses that must all be free, comma-separated ids. Up to 10.
        after (datetime.datetime | Unset): Default now.
        before (datetime.datetime | Unset): Default a week after `after`; 31 days after it at
            most.
        duration_minutes (int | Unset): The shortest slot worth returning. Default 30.
        day_start (str | Unset): Only from this wall time each day, like `09:00`.
        day_end (str | Unset): Only until this wall time each day, like `17:30`.
        timezone (str | Unset): The zone `day_start`, `day_end` and the local times are in.
            Default the first address’s calendar zone.
        skip_weekends (CalendarFreeTimeSkipWeekends | Unset): Leave out Saturdays and Sundays in
            that zone.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CalendarFreeTimeResponse200]
    """

    kwargs = _get_kwargs(
        identity_ids=identity_ids,
        after=after,
        before=before,
        duration_minutes=duration_minutes,
        day_start=day_start,
        day_end=day_end,
        timezone=timezone,
        skip_weekends=skip_weekends,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    identity_ids: str,
    after: datetime.datetime | Unset = UNSET,
    before: datetime.datetime | Unset = UNSET,
    duration_minutes: int | Unset = UNSET,
    day_start: str | Unset = UNSET,
    day_end: str | Unset = UNSET,
    timezone: str | Unset = UNSET,
    skip_weekends: CalendarFreeTimeSkipWeekends | Unset = UNSET,
) -> CalendarFreeTimeResponse200:
    """When several addresses are all free

     The stretches in a window when every address in `identity_ids` is free, at least `duration_minutes`
    long. Busy is a timed event that is not cancelled and that the address has not declined; tentative
    counts as busy, all-day events do not. `day_start` and `day_end` limit it to working hours, read in
    `timezone` (the first address’s calendar zone by default), and each slot carries its wall times in
    that zone too. Needs `read` on every address. It books nothing.

    Args:
        identity_ids (str): The addresses that must all be free, comma-separated ids. Up to 10.
        after (datetime.datetime | Unset): Default now.
        before (datetime.datetime | Unset): Default a week after `after`; 31 days after it at
            most.
        duration_minutes (int | Unset): The shortest slot worth returning. Default 30.
        day_start (str | Unset): Only from this wall time each day, like `09:00`.
        day_end (str | Unset): Only until this wall time each day, like `17:30`.
        timezone (str | Unset): The zone `day_start`, `day_end` and the local times are in.
            Default the first address’s calendar zone.
        skip_weekends (CalendarFreeTimeSkipWeekends | Unset): Leave out Saturdays and Sundays in
            that zone.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CalendarFreeTimeResponse200
    """

    return sync_detailed(
        client=client,
        identity_ids=identity_ids,
        after=after,
        before=before,
        duration_minutes=duration_minutes,
        day_start=day_start,
        day_end=day_end,
        timezone=timezone,
        skip_weekends=skip_weekends,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    identity_ids: str,
    after: datetime.datetime | Unset = UNSET,
    before: datetime.datetime | Unset = UNSET,
    duration_minutes: int | Unset = UNSET,
    day_start: str | Unset = UNSET,
    day_end: str | Unset = UNSET,
    timezone: str | Unset = UNSET,
    skip_weekends: CalendarFreeTimeSkipWeekends | Unset = UNSET,
) -> Response[CalendarFreeTimeResponse200]:
    """When several addresses are all free

     The stretches in a window when every address in `identity_ids` is free, at least `duration_minutes`
    long. Busy is a timed event that is not cancelled and that the address has not declined; tentative
    counts as busy, all-day events do not. `day_start` and `day_end` limit it to working hours, read in
    `timezone` (the first address’s calendar zone by default), and each slot carries its wall times in
    that zone too. Needs `read` on every address. It books nothing.

    Args:
        identity_ids (str): The addresses that must all be free, comma-separated ids. Up to 10.
        after (datetime.datetime | Unset): Default now.
        before (datetime.datetime | Unset): Default a week after `after`; 31 days after it at
            most.
        duration_minutes (int | Unset): The shortest slot worth returning. Default 30.
        day_start (str | Unset): Only from this wall time each day, like `09:00`.
        day_end (str | Unset): Only until this wall time each day, like `17:30`.
        timezone (str | Unset): The zone `day_start`, `day_end` and the local times are in.
            Default the first address’s calendar zone.
        skip_weekends (CalendarFreeTimeSkipWeekends | Unset): Leave out Saturdays and Sundays in
            that zone.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CalendarFreeTimeResponse200]
    """

    kwargs = _get_kwargs(
        identity_ids=identity_ids,
        after=after,
        before=before,
        duration_minutes=duration_minutes,
        day_start=day_start,
        day_end=day_end,
        timezone=timezone,
        skip_weekends=skip_weekends,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    identity_ids: str,
    after: datetime.datetime | Unset = UNSET,
    before: datetime.datetime | Unset = UNSET,
    duration_minutes: int | Unset = UNSET,
    day_start: str | Unset = UNSET,
    day_end: str | Unset = UNSET,
    timezone: str | Unset = UNSET,
    skip_weekends: CalendarFreeTimeSkipWeekends | Unset = UNSET,
) -> CalendarFreeTimeResponse200:
    """When several addresses are all free

     The stretches in a window when every address in `identity_ids` is free, at least `duration_minutes`
    long. Busy is a timed event that is not cancelled and that the address has not declined; tentative
    counts as busy, all-day events do not. `day_start` and `day_end` limit it to working hours, read in
    `timezone` (the first address’s calendar zone by default), and each slot carries its wall times in
    that zone too. Needs `read` on every address. It books nothing.

    Args:
        identity_ids (str): The addresses that must all be free, comma-separated ids. Up to 10.
        after (datetime.datetime | Unset): Default now.
        before (datetime.datetime | Unset): Default a week after `after`; 31 days after it at
            most.
        duration_minutes (int | Unset): The shortest slot worth returning. Default 30.
        day_start (str | Unset): Only from this wall time each day, like `09:00`.
        day_end (str | Unset): Only until this wall time each day, like `17:30`.
        timezone (str | Unset): The zone `day_start`, `day_end` and the local times are in.
            Default the first address’s calendar zone.
        skip_weekends (CalendarFreeTimeSkipWeekends | Unset): Leave out Saturdays and Sundays in
            that zone.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CalendarFreeTimeResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            identity_ids=identity_ids,
            after=after,
            before=before,
            duration_minutes=duration_minutes,
            day_start=day_start,
            day_end=day_end,
            timezone=timezone,
            skip_weekends=skip_weekends,
        )
    ).parsed
