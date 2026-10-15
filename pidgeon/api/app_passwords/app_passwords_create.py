from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_passwords_create_body import AppPasswordsCreateBody
from ...models.app_passwords_create_response_201 import AppPasswordsCreateResponse201
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    *,
    body: AppPasswordsCreateBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/app-passwords",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppPasswordsCreateResponse201 | Error | None:
    if response.status_code == 201:
        response_201 = AppPasswordsCreateResponse201.from_dict(response.json())

        return response_201

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
) -> Response[AppPasswordsCreateResponse201 | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AppPasswordsCreateBody,
) -> Response[AppPasswordsCreateResponse201 | Error]:
    """Issue IMAP and SMTP credentials for one address

     What lets you hand a customer a mailbox they can open in a mail client. Only for an address this key
    can already **send** from — the credential reads the inbox and sends as the address, so issuing one
    is handing over exactly that. `username` and `password` are returned together and are useless apart.

    Args:
        body (AppPasswordsCreateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppPasswordsCreateResponse201 | Error]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: AppPasswordsCreateBody,
) -> AppPasswordsCreateResponse201 | Error | None:
    """Issue IMAP and SMTP credentials for one address

     What lets you hand a customer a mailbox they can open in a mail client. Only for an address this key
    can already **send** from — the credential reads the inbox and sends as the address, so issuing one
    is handing over exactly that. `username` and `password` are returned together and are useless apart.

    Args:
        body (AppPasswordsCreateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppPasswordsCreateResponse201 | Error
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AppPasswordsCreateBody,
) -> Response[AppPasswordsCreateResponse201 | Error]:
    """Issue IMAP and SMTP credentials for one address

     What lets you hand a customer a mailbox they can open in a mail client. Only for an address this key
    can already **send** from — the credential reads the inbox and sends as the address, so issuing one
    is handing over exactly that. `username` and `password` are returned together and are useless apart.

    Args:
        body (AppPasswordsCreateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppPasswordsCreateResponse201 | Error]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: AppPasswordsCreateBody,
) -> AppPasswordsCreateResponse201 | Error | None:
    """Issue IMAP and SMTP credentials for one address

     What lets you hand a customer a mailbox they can open in a mail client. Only for an address this key
    can already **send** from — the credential reads the inbox and sends as the address, so issuing one
    is handing over exactly that. `username` and `password` are returned together and are useless apart.

    Args:
        body (AppPasswordsCreateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppPasswordsCreateResponse201 | Error
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
