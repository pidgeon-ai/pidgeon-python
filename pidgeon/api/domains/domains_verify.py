from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domains_verify_response_200 import DomainsVerifyResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/domains/{id}/verify".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DomainsVerifyResponse200:
    if response.status_code >= 400:
        raise errors.PidgeonError.from_response(response)

    if response.status_code == 200:
        response_200 = DomainsVerifyResponse200.from_dict(response.json())

        return response_200

    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DomainsVerifyResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    idempotency_key: str | Unset = UNSET,
) -> Response[DomainsVerifyResponse200]:
    """Check the zone again

     Idempotent and safe to poll — calling it on a verified domain re-checks and says so rather than
    erroring. Both halves in one answer: ownership, and whether mail is configured. The floor on how
    often this is worth calling is the zone’s TTL. Better still, subscribe to `domain.verified` and do
    not poll.

    Args:
        id (str):
        idempotency_key (str | Unset):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DomainsVerifyResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    idempotency_key: str | Unset = UNSET,
) -> DomainsVerifyResponse200:
    """Check the zone again

     Idempotent and safe to poll — calling it on a verified domain re-checks and says so rather than
    erroring. Both halves in one answer: ownership, and whether mail is configured. The floor on how
    often this is worth calling is the zone’s TTL. Better still, subscribe to `domain.verified` and do
    not poll.

    Args:
        id (str):
        idempotency_key (str | Unset):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DomainsVerifyResponse200
    """

    return sync_detailed(
        id=id,
        client=client,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    idempotency_key: str | Unset = UNSET,
) -> Response[DomainsVerifyResponse200]:
    """Check the zone again

     Idempotent and safe to poll — calling it on a verified domain re-checks and says so rather than
    erroring. Both halves in one answer: ownership, and whether mail is configured. The floor on how
    often this is worth calling is the zone’s TTL. Better still, subscribe to `domain.verified` and do
    not poll.

    Args:
        id (str):
        idempotency_key (str | Unset):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DomainsVerifyResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    idempotency_key: str | Unset = UNSET,
) -> DomainsVerifyResponse200:
    """Check the zone again

     Idempotent and safe to poll — calling it on a verified domain re-checks and says so rather than
    erroring. Both halves in one answer: ownership, and whether mail is configured. The floor on how
    often this is worth calling is the zone’s TTL. Better still, subscribe to `domain.verified` and do
    not poll.

    Args:
        id (str):
        idempotency_key (str | Unset):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DomainsVerifyResponse200
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            idempotency_key=idempotency_key,
        )
    ).parsed
