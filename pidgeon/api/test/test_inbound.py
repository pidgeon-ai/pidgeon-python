from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.test_inbound_body import TestInboundBody
from ...models.test_inbound_response_201 import TestInboundResponse201
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: TestInboundBody,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/test/inbound",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> TestInboundResponse201:
    if response.status_code >= 400:
        raise errors.PidgeonError.from_response(response)

    if response.status_code == 201:
        response_201 = TestInboundResponse201.from_dict(response.json())

        return response_201

    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[TestInboundResponse201]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TestInboundBody,
    idempotency_key: str | Unset = UNSET,
) -> Response[TestInboundResponse201]:
    """Simulate an inbound message (test keys only)

     Delivers a message to one of this **test key**’s addresses as though it had arrived from outside,
    through the real inbound pipeline — routing, sender rules, spam, the Firewall, threading,
    `message.received` and its webhooks — marked `test`. Pass `in_reply_to` with a message id to have it
    arrive as a reply in that thread, which is how a test plays the customer answering your agent.

    A live key gets `403`. The address must be one the key reaches at `send`. Nothing is sent to `from`,
    and the message counts against nothing on your plan.

    Args:
        idempotency_key (str | Unset):
        body (TestInboundBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TestInboundResponse201]
    """

    kwargs = _get_kwargs(
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: TestInboundBody,
    idempotency_key: str | Unset = UNSET,
) -> TestInboundResponse201:
    """Simulate an inbound message (test keys only)

     Delivers a message to one of this **test key**’s addresses as though it had arrived from outside,
    through the real inbound pipeline — routing, sender rules, spam, the Firewall, threading,
    `message.received` and its webhooks — marked `test`. Pass `in_reply_to` with a message id to have it
    arrive as a reply in that thread, which is how a test plays the customer answering your agent.

    A live key gets `403`. The address must be one the key reaches at `send`. Nothing is sent to `from`,
    and the message counts against nothing on your plan.

    Args:
        idempotency_key (str | Unset):
        body (TestInboundBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TestInboundResponse201
    """

    return sync_detailed(
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TestInboundBody,
    idempotency_key: str | Unset = UNSET,
) -> Response[TestInboundResponse201]:
    """Simulate an inbound message (test keys only)

     Delivers a message to one of this **test key**’s addresses as though it had arrived from outside,
    through the real inbound pipeline — routing, sender rules, spam, the Firewall, threading,
    `message.received` and its webhooks — marked `test`. Pass `in_reply_to` with a message id to have it
    arrive as a reply in that thread, which is how a test plays the customer answering your agent.

    A live key gets `403`. The address must be one the key reaches at `send`. Nothing is sent to `from`,
    and the message counts against nothing on your plan.

    Args:
        idempotency_key (str | Unset):
        body (TestInboundBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TestInboundResponse201]
    """

    kwargs = _get_kwargs(
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: TestInboundBody,
    idempotency_key: str | Unset = UNSET,
) -> TestInboundResponse201:
    """Simulate an inbound message (test keys only)

     Delivers a message to one of this **test key**’s addresses as though it had arrived from outside,
    through the real inbound pipeline — routing, sender rules, spam, the Firewall, threading,
    `message.received` and its webhooks — marked `test`. Pass `in_reply_to` with a message id to have it
    arrive as a reply in that thread, which is how a test plays the customer answering your agent.

    A live key gets `403`. The address must be one the key reaches at `send`. Nothing is sent to `from`,
    and the message counts against nothing on your plan.

    Args:
        idempotency_key (str | Unset):
        body (TestInboundBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TestInboundResponse201
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
