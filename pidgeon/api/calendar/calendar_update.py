from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.calendar_update_body import CalendarUpdateBody
from ...models.calendar_update_response_200 import CalendarUpdateResponse200
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    body: CalendarUpdateBody,
    if_match: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(if_match, Unset):
        headers["If-Match"] = if_match

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/identities/{id}/calendar".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CalendarUpdateResponse200 | Error | None:
    if response.status_code == 200:
        response_200 = CalendarUpdateResponse200.from_dict(response.json())

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
) -> Response[CalendarUpdateResponse200 | Error]:
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
    body: CalendarUpdateBody,
    if_match: str | Unset = UNSET,
) -> Response[CalendarUpdateResponse200 | Error]:
    """Set the default time zone

     The zone an event created without one gets. **Changing it does not move existing events**: an event
    stores the wall time it was given, so "every Tuesday at 09:00" is still 09:00 afterwards.

    Args:
        id (str):
        if_match (str | Unset):
        body (CalendarUpdateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CalendarUpdateResponse200 | Error]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        if_match=if_match,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CalendarUpdateBody,
    if_match: str | Unset = UNSET,
) -> CalendarUpdateResponse200 | Error | None:
    """Set the default time zone

     The zone an event created without one gets. **Changing it does not move existing events**: an event
    stores the wall time it was given, so "every Tuesday at 09:00" is still 09:00 afterwards.

    Args:
        id (str):
        if_match (str | Unset):
        body (CalendarUpdateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CalendarUpdateResponse200 | Error
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
        if_match=if_match,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CalendarUpdateBody,
    if_match: str | Unset = UNSET,
) -> Response[CalendarUpdateResponse200 | Error]:
    """Set the default time zone

     The zone an event created without one gets. **Changing it does not move existing events**: an event
    stores the wall time it was given, so "every Tuesday at 09:00" is still 09:00 afterwards.

    Args:
        id (str):
        if_match (str | Unset):
        body (CalendarUpdateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CalendarUpdateResponse200 | Error]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        if_match=if_match,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CalendarUpdateBody,
    if_match: str | Unset = UNSET,
) -> CalendarUpdateResponse200 | Error | None:
    """Set the default time zone

     The zone an event created without one gets. **Changing it does not move existing events**: an event
    stores the wall time it was given, so "every Tuesday at 09:00" is still 09:00 afterwards.

    Args:
        id (str):
        if_match (str | Unset):
        body (CalendarUpdateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CalendarUpdateResponse200 | Error
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            if_match=if_match,
        )
    ).parsed
