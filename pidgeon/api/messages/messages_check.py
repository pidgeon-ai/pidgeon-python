from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.messages_check_body import MessagesCheckBody
from ...models.messages_check_response_200 import MessagesCheckResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: MessagesCheckBody,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/messages/check",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MessagesCheckResponse200:
    if response.status_code >= 400:
        raise errors.PidgeonError.from_response(response)

    if response.status_code == 200:
        response_200 = MessagesCheckResponse200.from_dict(response.json())

        return response_200

    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[MessagesCheckResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: MessagesCheckBody,
    idempotency_key: str | Unset = UNSET,
) -> Response[MessagesCheckResponse200]:
    """Check a send without sending

     Would this send? The body `POST /messages` takes, plus `forward`, through every check a send makes:
    the address, the plan’s sending limits, suppression, the send policy and rules, the per-recipient
    cooldown, the daily cap, canary tokens, hand-over and approval. Answers `200` with `would_send` and
    the envelope, or the exact refusal the send would give — the same status, `error.code`, message,
    field and `Retry-After`. Nothing is sent or written, and nothing counts against a limit. A reply is
    checked with `in_reply_to`; a forward with `in_reply_to` and `forward: true`. The answer is for now:
    a send a moment later can meet a limit this did not.

    Args:
        idempotency_key (str | Unset):
        body (MessagesCheckBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessagesCheckResponse200]
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
    body: MessagesCheckBody,
    idempotency_key: str | Unset = UNSET,
) -> MessagesCheckResponse200:
    """Check a send without sending

     Would this send? The body `POST /messages` takes, plus `forward`, through every check a send makes:
    the address, the plan’s sending limits, suppression, the send policy and rules, the per-recipient
    cooldown, the daily cap, canary tokens, hand-over and approval. Answers `200` with `would_send` and
    the envelope, or the exact refusal the send would give — the same status, `error.code`, message,
    field and `Retry-After`. Nothing is sent or written, and nothing counts against a limit. A reply is
    checked with `in_reply_to`; a forward with `in_reply_to` and `forward: true`. The answer is for now:
    a send a moment later can meet a limit this did not.

    Args:
        idempotency_key (str | Unset):
        body (MessagesCheckBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessagesCheckResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: MessagesCheckBody,
    idempotency_key: str | Unset = UNSET,
) -> Response[MessagesCheckResponse200]:
    """Check a send without sending

     Would this send? The body `POST /messages` takes, plus `forward`, through every check a send makes:
    the address, the plan’s sending limits, suppression, the send policy and rules, the per-recipient
    cooldown, the daily cap, canary tokens, hand-over and approval. Answers `200` with `would_send` and
    the envelope, or the exact refusal the send would give — the same status, `error.code`, message,
    field and `Retry-After`. Nothing is sent or written, and nothing counts against a limit. A reply is
    checked with `in_reply_to`; a forward with `in_reply_to` and `forward: true`. The answer is for now:
    a send a moment later can meet a limit this did not.

    Args:
        idempotency_key (str | Unset):
        body (MessagesCheckBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessagesCheckResponse200]
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
    body: MessagesCheckBody,
    idempotency_key: str | Unset = UNSET,
) -> MessagesCheckResponse200:
    """Check a send without sending

     Would this send? The body `POST /messages` takes, plus `forward`, through every check a send makes:
    the address, the plan’s sending limits, suppression, the send policy and rules, the per-recipient
    cooldown, the daily cap, canary tokens, hand-over and approval. Answers `200` with `would_send` and
    the envelope, or the exact refusal the send would give — the same status, `error.code`, message,
    field and `Retry-After`. Nothing is sent or written, and nothing counts against a limit. A reply is
    checked with `in_reply_to`; a forward with `in_reply_to` and `forward: true`. The answer is for now:
    a send a moment later can meet a limit this did not.

    Args:
        idempotency_key (str | Unset):
        body (MessagesCheckBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessagesCheckResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
