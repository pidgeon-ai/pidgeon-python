from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.verify_sender_body import VerifySenderBody
from ...models.verify_sender_response_200 import VerifySenderResponse200
from ...types import Response


def _get_kwargs(
    *,
    body: VerifySenderBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/verify",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> VerifySenderResponse200:
    if response.status_code >= 400:
        raise errors.PidgeonError.from_response(response)

    if response.status_code == 200:
        response_200 = VerifySenderResponse200.from_dict(response.json())

        return response_200

    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[VerifySenderResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: VerifySenderBody,
) -> Response[VerifySenderResponse200]:
    """Check who sent a message

     Public, with no key. Send a raw message, or its headers alone; the answer says whether an AI agent
    sent it, on whose behalf, and whether its signatures hold — the signed agent declaration (`Agent-of`
    under an aligned DKIM signature) and the `Post-Envelope` — for Pidgeon’s mail and any other signer
    using the same formats. Act on `verdict`. Pass `recipient`, the address it reached you at, to catch
    a signed message replayed to you. Or send `request` instead of `message`: an HTTP request an agent
    signed with HTTP Message Signatures (RFC 9421) in Web Bot Auth’s profile, which is also how an MCP
    call over HTTP is signed; the key is found by its `keyid` among domains proved with `pidgeon id`, or
    in the directory its `Signature-Agent` names. Nothing sent is stored. Limited per IP; a key may be
    sent and is not required.

    Args:
        body (VerifySenderBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[VerifySenderResponse200]
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
    body: VerifySenderBody,
) -> VerifySenderResponse200:
    """Check who sent a message

     Public, with no key. Send a raw message, or its headers alone; the answer says whether an AI agent
    sent it, on whose behalf, and whether its signatures hold — the signed agent declaration (`Agent-of`
    under an aligned DKIM signature) and the `Post-Envelope` — for Pidgeon’s mail and any other signer
    using the same formats. Act on `verdict`. Pass `recipient`, the address it reached you at, to catch
    a signed message replayed to you. Or send `request` instead of `message`: an HTTP request an agent
    signed with HTTP Message Signatures (RFC 9421) in Web Bot Auth’s profile, which is also how an MCP
    call over HTTP is signed; the key is found by its `keyid` among domains proved with `pidgeon id`, or
    in the directory its `Signature-Agent` names. Nothing sent is stored. Limited per IP; a key may be
    sent and is not required.

    Args:
        body (VerifySenderBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        VerifySenderResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: VerifySenderBody,
) -> Response[VerifySenderResponse200]:
    """Check who sent a message

     Public, with no key. Send a raw message, or its headers alone; the answer says whether an AI agent
    sent it, on whose behalf, and whether its signatures hold — the signed agent declaration (`Agent-of`
    under an aligned DKIM signature) and the `Post-Envelope` — for Pidgeon’s mail and any other signer
    using the same formats. Act on `verdict`. Pass `recipient`, the address it reached you at, to catch
    a signed message replayed to you. Or send `request` instead of `message`: an HTTP request an agent
    signed with HTTP Message Signatures (RFC 9421) in Web Bot Auth’s profile, which is also how an MCP
    call over HTTP is signed; the key is found by its `keyid` among domains proved with `pidgeon id`, or
    in the directory its `Signature-Agent` names. Nothing sent is stored. Limited per IP; a key may be
    sent and is not required.

    Args:
        body (VerifySenderBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[VerifySenderResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: VerifySenderBody,
) -> VerifySenderResponse200:
    """Check who sent a message

     Public, with no key. Send a raw message, or its headers alone; the answer says whether an AI agent
    sent it, on whose behalf, and whether its signatures hold — the signed agent declaration (`Agent-of`
    under an aligned DKIM signature) and the `Post-Envelope` — for Pidgeon’s mail and any other signer
    using the same formats. Act on `verdict`. Pass `recipient`, the address it reached you at, to catch
    a signed message replayed to you. Or send `request` instead of `message`: an HTTP request an agent
    signed with HTTP Message Signatures (RFC 9421) in Web Bot Auth’s profile, which is also how an MCP
    call over HTTP is signed; the key is found by its `keyid` among domains proved with `pidgeon id`, or
    in the directory its `Signature-Agent` names. Nothing sent is stored. Limited per IP; a key may be
    sent and is not required.

    Args:
        body (VerifySenderBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        VerifySenderResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
