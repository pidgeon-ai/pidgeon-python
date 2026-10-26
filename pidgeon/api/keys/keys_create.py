from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.keys_create_body import KeysCreateBody
from ...models.keys_create_response_201 import KeysCreateResponse201
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: KeysCreateBody,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api-keys",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> KeysCreateResponse201:
    if response.status_code >= 400:
        raise errors.PidgeonError.from_response(response)

    if response.status_code == 201:
        response_201 = KeysCreateResponse201.from_dict(response.json())

        return response_201

    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[KeysCreateResponse201]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: KeysCreateBody,
    idempotency_key: str | Unset = UNSET,
) -> Response[KeysCreateResponse201]:
    """Mint a key

     Say what the key reaches and what it may do: one of `identity_ids` or `pod_id`, and `access`.
    `identity_ids` must be addresses the calling key administers, at no more than its own `access`: a
    key cannot delegate reach it does not have, and `reaches_all` is refused to a key.

    Until 26 November 2026 a request without `access` still works — the new key takes the calling key’s
    level — and is answered with `Deprecation`, `Sunset` and a `warnings` entry. From that date it is a
    400 with `field: "access"`.

    The `token` is in this response and nowhere else, ever.

    Args:
        idempotency_key (str | Unset):
        body (KeysCreateBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[KeysCreateResponse201]
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
    body: KeysCreateBody,
    idempotency_key: str | Unset = UNSET,
) -> KeysCreateResponse201:
    """Mint a key

     Say what the key reaches and what it may do: one of `identity_ids` or `pod_id`, and `access`.
    `identity_ids` must be addresses the calling key administers, at no more than its own `access`: a
    key cannot delegate reach it does not have, and `reaches_all` is refused to a key.

    Until 26 November 2026 a request without `access` still works — the new key takes the calling key’s
    level — and is answered with `Deprecation`, `Sunset` and a `warnings` entry. From that date it is a
    400 with `field: "access"`.

    The `token` is in this response and nowhere else, ever.

    Args:
        idempotency_key (str | Unset):
        body (KeysCreateBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        KeysCreateResponse201
    """

    return sync_detailed(
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: KeysCreateBody,
    idempotency_key: str | Unset = UNSET,
) -> Response[KeysCreateResponse201]:
    """Mint a key

     Say what the key reaches and what it may do: one of `identity_ids` or `pod_id`, and `access`.
    `identity_ids` must be addresses the calling key administers, at no more than its own `access`: a
    key cannot delegate reach it does not have, and `reaches_all` is refused to a key.

    Until 26 November 2026 a request without `access` still works — the new key takes the calling key’s
    level — and is answered with `Deprecation`, `Sunset` and a `warnings` entry. From that date it is a
    400 with `field: "access"`.

    The `token` is in this response and nowhere else, ever.

    Args:
        idempotency_key (str | Unset):
        body (KeysCreateBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[KeysCreateResponse201]
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
    body: KeysCreateBody,
    idempotency_key: str | Unset = UNSET,
) -> KeysCreateResponse201:
    """Mint a key

     Say what the key reaches and what it may do: one of `identity_ids` or `pod_id`, and `access`.
    `identity_ids` must be addresses the calling key administers, at no more than its own `access`: a
    key cannot delegate reach it does not have, and `reaches_all` is refused to a key.

    Until 26 November 2026 a request without `access` still works — the new key takes the calling key’s
    level — and is answered with `Deprecation`, `Sunset` and a `warnings` entry. From that date it is a
    400 with `field: "access"`.

    The `token` is in this response and nowhere else, ever.

    Args:
        idempotency_key (str | Unset):
        body (KeysCreateBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        KeysCreateResponse201
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
