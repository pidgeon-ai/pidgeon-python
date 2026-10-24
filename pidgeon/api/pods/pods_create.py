from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.pods_create_body import PodsCreateBody
from ...models.pods_create_response_201 import PodsCreateResponse201
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PodsCreateBody,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/pods",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PodsCreateResponse201:
    if response.status_code >= 400:
        raise errors.PidgeonError.from_response(response)

    if response.status_code == 201:
        response_201 = PodsCreateResponse201.from_dict(response.json())

        return response_201

    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PodsCreateResponse201]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PodsCreateBody,
    idempotency_key: str | Unset = UNSET,
) -> Response[PodsCreateResponse201]:
    """Create a pod

     Name it after whatever it holds — a customer, an environment. `client_id` is your own id for it,
    carried and never parsed, and has to be unique within the account so that looking one up by it has
    an answer.

    **Provisioning in one call.** Pass `address` to create an address in the new pod (the same fields as
    `POST /identities`) and `key` to mint a pod key: a key that reaches the pod’s addresses, now and
    later, and nothing else. All of it is made or none of it is. Needs a live key over the whole
    account; a test key gets 403, and `key.test` mints a test key for the pod instead.

    **The token is shown once.** Send an `Idempotency-Key`: a retry with it returns the same pod,
    address and key, with `token: null`, because the secret is never stored. If the first answer was
    lost, rotate the key (`POST /api-keys/{id}/rotate`) for a new secret.

    Args:
        idempotency_key (str | Unset):
        body (PodsCreateBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PodsCreateResponse201]
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
    body: PodsCreateBody,
    idempotency_key: str | Unset = UNSET,
) -> PodsCreateResponse201:
    """Create a pod

     Name it after whatever it holds — a customer, an environment. `client_id` is your own id for it,
    carried and never parsed, and has to be unique within the account so that looking one up by it has
    an answer.

    **Provisioning in one call.** Pass `address` to create an address in the new pod (the same fields as
    `POST /identities`) and `key` to mint a pod key: a key that reaches the pod’s addresses, now and
    later, and nothing else. All of it is made or none of it is. Needs a live key over the whole
    account; a test key gets 403, and `key.test` mints a test key for the pod instead.

    **The token is shown once.** Send an `Idempotency-Key`: a retry with it returns the same pod,
    address and key, with `token: null`, because the secret is never stored. If the first answer was
    lost, rotate the key (`POST /api-keys/{id}/rotate`) for a new secret.

    Args:
        idempotency_key (str | Unset):
        body (PodsCreateBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PodsCreateResponse201
    """

    return sync_detailed(
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PodsCreateBody,
    idempotency_key: str | Unset = UNSET,
) -> Response[PodsCreateResponse201]:
    """Create a pod

     Name it after whatever it holds — a customer, an environment. `client_id` is your own id for it,
    carried and never parsed, and has to be unique within the account so that looking one up by it has
    an answer.

    **Provisioning in one call.** Pass `address` to create an address in the new pod (the same fields as
    `POST /identities`) and `key` to mint a pod key: a key that reaches the pod’s addresses, now and
    later, and nothing else. All of it is made or none of it is. Needs a live key over the whole
    account; a test key gets 403, and `key.test` mints a test key for the pod instead.

    **The token is shown once.** Send an `Idempotency-Key`: a retry with it returns the same pod,
    address and key, with `token: null`, because the secret is never stored. If the first answer was
    lost, rotate the key (`POST /api-keys/{id}/rotate`) for a new secret.

    Args:
        idempotency_key (str | Unset):
        body (PodsCreateBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PodsCreateResponse201]
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
    body: PodsCreateBody,
    idempotency_key: str | Unset = UNSET,
) -> PodsCreateResponse201:
    """Create a pod

     Name it after whatever it holds — a customer, an environment. `client_id` is your own id for it,
    carried and never parsed, and has to be unique within the account so that looking one up by it has
    an answer.

    **Provisioning in one call.** Pass `address` to create an address in the new pod (the same fields as
    `POST /identities`) and `key` to mint a pod key: a key that reaches the pod’s addresses, now and
    later, and nothing else. All of it is made or none of it is. Needs a live key over the whole
    account; a test key gets 403, and `key.test` mints a test key for the pod instead.

    **The token is shown once.** Send an `Idempotency-Key`: a retry with it returns the same pod,
    address and key, with `token: null`, because the secret is never stored. If the first answer was
    lost, rotate the key (`POST /api-keys/{id}/rotate`) for a new secret.

    Args:
        idempotency_key (str | Unset):
        body (PodsCreateBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PodsCreateResponse201
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
