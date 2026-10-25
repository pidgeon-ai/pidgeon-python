from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.messages_send_body import MessagesSendBody
from ...models.messages_send_response_202 import MessagesSendResponse202
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: MessagesSendBody,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/messages",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MessagesSendResponse202:
    if response.status_code >= 400:
        raise errors.PidgeonError.from_response(response)

    if response.status_code == 202:
        response_202 = MessagesSendResponse202.from_dict(response.json())

        return response_202

    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[MessagesSendResponse202]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: MessagesSendBody,
    idempotency_key: str | Unset = UNSET,
) -> Response[MessagesSendResponse202]:
    """Send a message

     Idempotent with an `Idempotency-Key` header. Answers `202` with the id, the thread and anything
    **rejected** — addresses the provider would not accept at hand-off, so read it before assuming every
    recipient got it. A recipient this address is not allowed to write to is a different thing and
    refuses the whole send: `403` with `blocked` when a rule says no, `not_permitted` when the send
    policy does. Nothing is sent to anybody in that case. With a test key, `rejected@` at any domain is
    always rejected and `bounce@` bounces, and `Pidgeon-Test-Fail` causes a 429, a 503, a slow answer or
    a lost one: https://pidgeon.ai/docs/test-mode#causing-failures.

    Args:
        idempotency_key (str | Unset):
        body (MessagesSendBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessagesSendResponse202]
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
    body: MessagesSendBody,
    idempotency_key: str | Unset = UNSET,
) -> MessagesSendResponse202:
    """Send a message

     Idempotent with an `Idempotency-Key` header. Answers `202` with the id, the thread and anything
    **rejected** — addresses the provider would not accept at hand-off, so read it before assuming every
    recipient got it. A recipient this address is not allowed to write to is a different thing and
    refuses the whole send: `403` with `blocked` when a rule says no, `not_permitted` when the send
    policy does. Nothing is sent to anybody in that case. With a test key, `rejected@` at any domain is
    always rejected and `bounce@` bounces, and `Pidgeon-Test-Fail` causes a 429, a 503, a slow answer or
    a lost one: https://pidgeon.ai/docs/test-mode#causing-failures.

    Args:
        idempotency_key (str | Unset):
        body (MessagesSendBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessagesSendResponse202
    """

    return sync_detailed(
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: MessagesSendBody,
    idempotency_key: str | Unset = UNSET,
) -> Response[MessagesSendResponse202]:
    """Send a message

     Idempotent with an `Idempotency-Key` header. Answers `202` with the id, the thread and anything
    **rejected** — addresses the provider would not accept at hand-off, so read it before assuming every
    recipient got it. A recipient this address is not allowed to write to is a different thing and
    refuses the whole send: `403` with `blocked` when a rule says no, `not_permitted` when the send
    policy does. Nothing is sent to anybody in that case. With a test key, `rejected@` at any domain is
    always rejected and `bounce@` bounces, and `Pidgeon-Test-Fail` causes a 429, a 503, a slow answer or
    a lost one: https://pidgeon.ai/docs/test-mode#causing-failures.

    Args:
        idempotency_key (str | Unset):
        body (MessagesSendBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessagesSendResponse202]
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
    body: MessagesSendBody,
    idempotency_key: str | Unset = UNSET,
) -> MessagesSendResponse202:
    """Send a message

     Idempotent with an `Idempotency-Key` header. Answers `202` with the id, the thread and anything
    **rejected** — addresses the provider would not accept at hand-off, so read it before assuming every
    recipient got it. A recipient this address is not allowed to write to is a different thing and
    refuses the whole send: `403` with `blocked` when a rule says no, `not_permitted` when the send
    policy does. Nothing is sent to anybody in that case. With a test key, `rejected@` at any domain is
    always rejected and `bounce@` bounces, and `Pidgeon-Test-Fail` causes a 429, a 503, a slow answer or
    a lost one: https://pidgeon.ai/docs/test-mode#causing-failures.

    Args:
        idempotency_key (str | Unset):
        body (MessagesSendBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessagesSendResponse202
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
