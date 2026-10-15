from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domains_verify_response_200 import DomainsVerifyResponse200
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/domains/{id}/verify".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DomainsVerifyResponse200 | Error | None:
    if response.status_code == 200:
        response_200 = DomainsVerifyResponse200.from_dict(response.json())

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
) -> Response[DomainsVerifyResponse200 | Error]:
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
) -> Response[DomainsVerifyResponse200 | Error]:
    """Check the zone again

     Idempotent and safe to poll — calling it on a verified domain re-checks and says so rather than
    erroring. Both halves in one answer: ownership, and whether mail is configured. The floor on how
    often this is worth calling is the zone’s TTL. Better still, subscribe to `domain.verified` and do
    not poll.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DomainsVerifyResponse200 | Error]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> DomainsVerifyResponse200 | Error | None:
    """Check the zone again

     Idempotent and safe to poll — calling it on a verified domain re-checks and says so rather than
    erroring. Both halves in one answer: ownership, and whether mail is configured. The floor on how
    often this is worth calling is the zone’s TTL. Better still, subscribe to `domain.verified` and do
    not poll.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DomainsVerifyResponse200 | Error
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DomainsVerifyResponse200 | Error]:
    """Check the zone again

     Idempotent and safe to poll — calling it on a verified domain re-checks and says so rather than
    erroring. Both halves in one answer: ownership, and whether mail is configured. The floor on how
    often this is worth calling is the zone’s TTL. Better still, subscribe to `domain.verified` and do
    not poll.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DomainsVerifyResponse200 | Error]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> DomainsVerifyResponse200 | Error | None:
    """Check the zone again

     Idempotent and safe to poll — calling it on a verified domain re-checks and says so rather than
    erroring. Both halves in one answer: ownership, and whether mail is configured. The floor on how
    often this is worth calling is the zone’s TTL. Better still, subscribe to `domain.verified` and do
    not poll.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DomainsVerifyResponse200 | Error
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
