from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.webhooks_deliveries_response_200 import WebhooksDeliveriesResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    webhook_id: UUID,
    limit: int | Unset = 25,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_webhook_id = str(webhook_id)
    params["webhook_id"] = json_webhook_id

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/deliveries",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | WebhooksDeliveriesResponse200 | None:
    if response.status_code == 200:
        response_200 = WebhooksDeliveriesResponse200.from_dict(response.json())

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
) -> Response[Error | WebhooksDeliveriesResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    webhook_id: UUID,
    limit: int | Unset = 25,
) -> Response[Error | WebhooksDeliveriesResponse200]:
    """What happened to each event we tried to hand you

     `webhook_id` is required — the question is always about one endpoint. The ids here are what the
    replay below takes.

    Args:
        webhook_id (UUID):
        limit (int | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | WebhooksDeliveriesResponse200]
    """

    kwargs = _get_kwargs(
        webhook_id=webhook_id,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    webhook_id: UUID,
    limit: int | Unset = 25,
) -> Error | WebhooksDeliveriesResponse200 | None:
    """What happened to each event we tried to hand you

     `webhook_id` is required — the question is always about one endpoint. The ids here are what the
    replay below takes.

    Args:
        webhook_id (UUID):
        limit (int | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | WebhooksDeliveriesResponse200
    """

    return sync_detailed(
        client=client,
        webhook_id=webhook_id,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    webhook_id: UUID,
    limit: int | Unset = 25,
) -> Response[Error | WebhooksDeliveriesResponse200]:
    """What happened to each event we tried to hand you

     `webhook_id` is required — the question is always about one endpoint. The ids here are what the
    replay below takes.

    Args:
        webhook_id (UUID):
        limit (int | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | WebhooksDeliveriesResponse200]
    """

    kwargs = _get_kwargs(
        webhook_id=webhook_id,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    webhook_id: UUID,
    limit: int | Unset = 25,
) -> Error | WebhooksDeliveriesResponse200 | None:
    """What happened to each event we tried to hand you

     `webhook_id` is required — the question is always about one endpoint. The ids here are what the
    replay below takes.

    Args:
        webhook_id (UUID):
        limit (int | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | WebhooksDeliveriesResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            webhook_id=webhook_id,
            limit=limit,
        )
    ).parsed
