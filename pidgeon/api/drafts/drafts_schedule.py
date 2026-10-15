from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.drafts_schedule_body import DraftsScheduleBody
from ...models.drafts_schedule_response_200 import DraftsScheduleResponse200
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: DraftsScheduleBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/drafts/{id}/schedule".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DraftsScheduleResponse200 | Error | None:
    if response.status_code == 200:
        response_200 = DraftsScheduleResponse200.from_dict(response.json())

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
) -> Response[DraftsScheduleResponse200 | Error]:
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
    body: DraftsScheduleBody,
) -> Response[DraftsScheduleResponse200 | Error]:
    """Send it later

     A minute from now at the earliest, thirty days at the latest. A refused send unschedules rather than
    retrying forever, so a draft can come back on its own with `failed_reason` set — read that before
    scheduling the same message again.

    Args:
        id (str):
        body (DraftsScheduleBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DraftsScheduleResponse200 | Error]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DraftsScheduleBody,
) -> DraftsScheduleResponse200 | Error | None:
    """Send it later

     A minute from now at the earliest, thirty days at the latest. A refused send unschedules rather than
    retrying forever, so a draft can come back on its own with `failed_reason` set — read that before
    scheduling the same message again.

    Args:
        id (str):
        body (DraftsScheduleBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DraftsScheduleResponse200 | Error
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DraftsScheduleBody,
) -> Response[DraftsScheduleResponse200 | Error]:
    """Send it later

     A minute from now at the earliest, thirty days at the latest. A refused send unschedules rather than
    retrying forever, so a draft can come back on its own with `failed_reason` set — read that before
    scheduling the same message again.

    Args:
        id (str):
        body (DraftsScheduleBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DraftsScheduleResponse200 | Error]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DraftsScheduleBody,
) -> DraftsScheduleResponse200 | Error | None:
    """Send it later

     A minute from now at the earliest, thirty days at the latest. A refused send unschedules rather than
    retrying forever, so a draft can come back on its own with `failed_reason` set — read that before
    scheduling the same message again.

    Args:
        id (str):
        body (DraftsScheduleBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DraftsScheduleResponse200 | Error
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
