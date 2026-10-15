from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.me_get_response_200 import MeGetResponse200
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/me",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | MeGetResponse200 | None:
    if response.status_code == 200:
        response_200 = MeGetResponse200.from_dict(response.json())

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
) -> Response[Error | MeGetResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[Error | MeGetResponse200]:
    """What this key is, and what it may do

     The one question a credential could not ask. Everything else here answers what is *in* the account,
    so the only way to learn your own access was to try something and read the refusal — and a key that
    reaches nothing looks exactly like a key that is broken. Free: no write, no side effect, and the
    three facts that decide whether your next call works.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | MeGetResponse200]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> Error | MeGetResponse200 | None:
    """What this key is, and what it may do

     The one question a credential could not ask. Everything else here answers what is *in* the account,
    so the only way to learn your own access was to try something and read the refusal — and a key that
    reaches nothing looks exactly like a key that is broken. Free: no write, no side effect, and the
    three facts that decide whether your next call works.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | MeGetResponse200
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[Error | MeGetResponse200]:
    """What this key is, and what it may do

     The one question a credential could not ask. Everything else here answers what is *in* the account,
    so the only way to learn your own access was to try something and read the refusal — and a key that
    reaches nothing looks exactly like a key that is broken. Free: no write, no side effect, and the
    three facts that decide whether your next call works.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | MeGetResponse200]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> Error | MeGetResponse200 | None:
    """What this key is, and what it may do

     The one question a credential could not ask. Everything else here answers what is *in* the account,
    so the only way to learn your own access was to try something and read the refusal — and a key that
    reaches nothing looks exactly like a key that is broken. Free: no write, no side effect, and the
    three facts that decide whether your next call works.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | MeGetResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
