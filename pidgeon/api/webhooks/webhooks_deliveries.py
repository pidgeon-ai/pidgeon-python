from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.webhooks_deliveries_response_200 import WebhooksDeliveriesResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    webhook_id: UUID,
    limit: int | Unset = 25,
    cursor: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_webhook_id = str(webhook_id)
    params["webhook_id"] = json_webhook_id

    params["limit"] = limit

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/deliveries",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> WebhooksDeliveriesResponse200:
    if response.status_code >= 400:
        raise errors.PidgeonError.from_response(response)

    if response.status_code == 200:
        response_200 = WebhooksDeliveriesResponse200.from_dict(response.json())

        return response_200

    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[WebhooksDeliveriesResponse200]:
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
    cursor: str | Unset = UNSET,
) -> Response[WebhooksDeliveriesResponse200]:
    """What happened to each event we tried to hand you

     `webhook_id` is required — the question is always about one endpoint. The ids here are what the
    replay below takes.

    Args:
        webhook_id (UUID):
        limit (int | Unset):  Default: 25.
        cursor (str | Unset): From a previous page’s `next_cursor`. Opaque — do not parse it.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebhooksDeliveriesResponse200]
    """

    kwargs = _get_kwargs(
        webhook_id=webhook_id,
        limit=limit,
        cursor=cursor,
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
    cursor: str | Unset = UNSET,
) -> WebhooksDeliveriesResponse200:
    """What happened to each event we tried to hand you

     `webhook_id` is required — the question is always about one endpoint. The ids here are what the
    replay below takes.

    Args:
        webhook_id (UUID):
        limit (int | Unset):  Default: 25.
        cursor (str | Unset): From a previous page’s `next_cursor`. Opaque — do not parse it.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebhooksDeliveriesResponse200
    """

    return sync_detailed(
        client=client,
        webhook_id=webhook_id,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    webhook_id: UUID,
    limit: int | Unset = 25,
    cursor: str | Unset = UNSET,
) -> Response[WebhooksDeliveriesResponse200]:
    """What happened to each event we tried to hand you

     `webhook_id` is required — the question is always about one endpoint. The ids here are what the
    replay below takes.

    Args:
        webhook_id (UUID):
        limit (int | Unset):  Default: 25.
        cursor (str | Unset): From a previous page’s `next_cursor`. Opaque — do not parse it.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebhooksDeliveriesResponse200]
    """

    kwargs = _get_kwargs(
        webhook_id=webhook_id,
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    webhook_id: UUID,
    limit: int | Unset = 25,
    cursor: str | Unset = UNSET,
) -> WebhooksDeliveriesResponse200:
    """What happened to each event we tried to hand you

     `webhook_id` is required — the question is always about one endpoint. The ids here are what the
    replay below takes.

    Args:
        webhook_id (UUID):
        limit (int | Unset):  Default: 25.
        cursor (str | Unset): From a previous page’s `next_cursor`. Opaque — do not parse it.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebhooksDeliveriesResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            webhook_id=webhook_id,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
