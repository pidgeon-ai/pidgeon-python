from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.log_head_response_200 import LogHeadResponse200
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/log/head",
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> LogHeadResponse200:
    if response.status_code >= 400:
        raise errors.PidgeonError.from_response(response)

    if response.status_code == 200:
        response_200 = LogHeadResponse200.from_dict(response.json())

        return response_200

    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[LogHeadResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[LogHeadResponse200]:
    """Read the card log’s signed head

     Public, with no key. The card log holds every agent card Pidgeon has issued, changed or revoked, in
    an append-only Merkle tree (RFC 9162). `checkpoint` is its signed head, a C2SP checkpoint: check it
    against `verifier_key`, which never changes, and pin that. Cached for ten seconds. Limited per IP.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LogHeadResponse200]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> LogHeadResponse200:
    """Read the card log’s signed head

     Public, with no key. The card log holds every agent card Pidgeon has issued, changed or revoked, in
    an append-only Merkle tree (RFC 9162). `checkpoint` is its signed head, a C2SP checkpoint: check it
    against `verifier_key`, which never changes, and pin that. Cached for ten seconds. Limited per IP.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LogHeadResponse200
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[LogHeadResponse200]:
    """Read the card log’s signed head

     Public, with no key. The card log holds every agent card Pidgeon has issued, changed or revoked, in
    an append-only Merkle tree (RFC 9162). `checkpoint` is its signed head, a C2SP checkpoint: check it
    against `verifier_key`, which never changes, and pin that. Cached for ten seconds. Limited per IP.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LogHeadResponse200]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> LogHeadResponse200:
    """Read the card log’s signed head

     Public, with no key. The card log holds every agent card Pidgeon has issued, changed or revoked, in
    an append-only Merkle tree (RFC 9162). `checkpoint` is its signed head, a C2SP checkpoint: check it
    against `verifier_key`, which never changes, and pin that. Cached for ten seconds. Limited per IP.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LogHeadResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
