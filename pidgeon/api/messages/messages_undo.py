from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.messages_undo_body import MessagesUndoBody
from ...models.messages_undo_response_200 import MessagesUndoResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: MessagesUndoBody,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/messages/undo",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MessagesUndoResponse200:
    if response.status_code >= 400:
        raise errors.PidgeonError.from_response(response)

    if response.status_code == 200:
        response_200 = MessagesUndoResponse200.from_dict(response.json())

        return response_200

    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[MessagesUndoResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: MessagesUndoBody,
    idempotency_key: str | Unset = UNSET,
) -> Response[MessagesUndoResponse200]:
    """Put an action back

     Hand back the `undo` from a `PATCH` or a batch. Unusual for an API to have, and the argument is that
    software makes mistakes at a speed a person does not.

    Args:
        idempotency_key (str | Unset):
        body (MessagesUndoBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessagesUndoResponse200]
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
    body: MessagesUndoBody,
    idempotency_key: str | Unset = UNSET,
) -> MessagesUndoResponse200:
    """Put an action back

     Hand back the `undo` from a `PATCH` or a batch. Unusual for an API to have, and the argument is that
    software makes mistakes at a speed a person does not.

    Args:
        idempotency_key (str | Unset):
        body (MessagesUndoBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessagesUndoResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: MessagesUndoBody,
    idempotency_key: str | Unset = UNSET,
) -> Response[MessagesUndoResponse200]:
    """Put an action back

     Hand back the `undo` from a `PATCH` or a batch. Unusual for an API to have, and the argument is that
    software makes mistakes at a speed a person does not.

    Args:
        idempotency_key (str | Unset):
        body (MessagesUndoBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessagesUndoResponse200]
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
    body: MessagesUndoBody,
    idempotency_key: str | Unset = UNSET,
) -> MessagesUndoResponse200:
    """Put an action back

     Hand back the `undo` from a `PATCH` or a batch. Unusual for an API to have, and the argument is that
    software makes mistakes at a speed a person does not.

    Args:
        idempotency_key (str | Unset):
        body (MessagesUndoBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessagesUndoResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
