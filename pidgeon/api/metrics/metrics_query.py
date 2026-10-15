from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.metrics_query_response_200 import MetricsQueryResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    days: int | Unset = UNSET,
    identity_id: UUID | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["days"] = days

    json_identity_id: str | Unset = UNSET
    if not isinstance(identity_id, Unset):
        json_identity_id = str(identity_id)
    params["identity_id"] = json_identity_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/metrics",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | MetricsQueryResponse200 | None:
    if response.status_code == 200:
        response_200 = MetricsQueryResponse200.from_dict(response.json())

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
) -> Response[Error | MetricsQueryResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    days: int | Unset = UNSET,
    identity_id: UUID | Unset = UNSET,
) -> Response[Error | MetricsQueryResponse200]:
    """What happened to the mail

     Counted from the event log rather than from the messages: a message row says what was sent, and
    whether it bounced is something the provider told us afterwards. `identity_id` narrows it to one
    mailbox, which is the question worth asking when you run several — reputation belongs to the address
    that sent the mail. `delivery_rate` is null rather than zero when nothing was sent.

    Args:
        days (int | Unset):
        identity_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | MetricsQueryResponse200]
    """

    kwargs = _get_kwargs(
        days=days,
        identity_id=identity_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    days: int | Unset = UNSET,
    identity_id: UUID | Unset = UNSET,
) -> Error | MetricsQueryResponse200 | None:
    """What happened to the mail

     Counted from the event log rather than from the messages: a message row says what was sent, and
    whether it bounced is something the provider told us afterwards. `identity_id` narrows it to one
    mailbox, which is the question worth asking when you run several — reputation belongs to the address
    that sent the mail. `delivery_rate` is null rather than zero when nothing was sent.

    Args:
        days (int | Unset):
        identity_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | MetricsQueryResponse200
    """

    return sync_detailed(
        client=client,
        days=days,
        identity_id=identity_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    days: int | Unset = UNSET,
    identity_id: UUID | Unset = UNSET,
) -> Response[Error | MetricsQueryResponse200]:
    """What happened to the mail

     Counted from the event log rather than from the messages: a message row says what was sent, and
    whether it bounced is something the provider told us afterwards. `identity_id` narrows it to one
    mailbox, which is the question worth asking when you run several — reputation belongs to the address
    that sent the mail. `delivery_rate` is null rather than zero when nothing was sent.

    Args:
        days (int | Unset):
        identity_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | MetricsQueryResponse200]
    """

    kwargs = _get_kwargs(
        days=days,
        identity_id=identity_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    days: int | Unset = UNSET,
    identity_id: UUID | Unset = UNSET,
) -> Error | MetricsQueryResponse200 | None:
    """What happened to the mail

     Counted from the event log rather than from the messages: a message row says what was sent, and
    whether it bounced is something the provider told us afterwards. `identity_id` narrows it to one
    mailbox, which is the question worth asking when you run several — reputation belongs to the address
    that sent the mail. `delivery_rate` is null rather than zero when nothing was sent.

    Args:
        days (int | Unset):
        identity_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | MetricsQueryResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            days=days,
            identity_id=identity_id,
        )
    ).parsed
