from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.sign_ins_approve_body import SignInsApproveBody
from ...models.sign_ins_approve_response_201 import SignInsApproveResponse201
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: SignInsApproveBody,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/sign-ins",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> SignInsApproveResponse201:
    if response.status_code >= 400:
        raise errors.PidgeonError.from_response(response)

    if response.status_code == 201:
        response_201 = SignInsApproveResponse201.from_dict(response.json())

        return response_201

    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[SignInsApproveResponse201]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SignInsApproveBody,
    idempotency_key: str | Unset = UNSET,
) -> Response[SignInsApproveResponse201]:
    """Approve a sign-in as your address

     Sign in with Pidgeon, from the agent’s side. An app gave the agent an authorization URL; post it
    here with a key that can **send** as the address, and get back the app’s callback with a one-use
    code. Open `redirect_url` yourself, within a minute, in the session that started the sign-in:
    whoever opens it is the one signed in. Name the address in `address` when the URL does not
    (`login_hint`). The key goes to Pidgeon only, never to the app. A key that can only read, or that
    does not reach the address, is refused as a send would be.

    Args:
        idempotency_key (str | Unset):
        body (SignInsApproveBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SignInsApproveResponse201]
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
    body: SignInsApproveBody,
    idempotency_key: str | Unset = UNSET,
) -> SignInsApproveResponse201:
    """Approve a sign-in as your address

     Sign in with Pidgeon, from the agent’s side. An app gave the agent an authorization URL; post it
    here with a key that can **send** as the address, and get back the app’s callback with a one-use
    code. Open `redirect_url` yourself, within a minute, in the session that started the sign-in:
    whoever opens it is the one signed in. Name the address in `address` when the URL does not
    (`login_hint`). The key goes to Pidgeon only, never to the app. A key that can only read, or that
    does not reach the address, is refused as a send would be.

    Args:
        idempotency_key (str | Unset):
        body (SignInsApproveBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SignInsApproveResponse201
    """

    return sync_detailed(
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SignInsApproveBody,
    idempotency_key: str | Unset = UNSET,
) -> Response[SignInsApproveResponse201]:
    """Approve a sign-in as your address

     Sign in with Pidgeon, from the agent’s side. An app gave the agent an authorization URL; post it
    here with a key that can **send** as the address, and get back the app’s callback with a one-use
    code. Open `redirect_url` yourself, within a minute, in the session that started the sign-in:
    whoever opens it is the one signed in. Name the address in `address` when the URL does not
    (`login_hint`). The key goes to Pidgeon only, never to the app. A key that can only read, or that
    does not reach the address, is refused as a send would be.

    Args:
        idempotency_key (str | Unset):
        body (SignInsApproveBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SignInsApproveResponse201]
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
    body: SignInsApproveBody,
    idempotency_key: str | Unset = UNSET,
) -> SignInsApproveResponse201:
    """Approve a sign-in as your address

     Sign in with Pidgeon, from the agent’s side. An app gave the agent an authorization URL; post it
    here with a key that can **send** as the address, and get back the app’s callback with a one-use
    code. Open `redirect_url` yourself, within a minute, in the session that started the sign-in:
    whoever opens it is the one signed in. Name the address in `address` when the URL does not
    (`login_hint`). The key goes to Pidgeon only, never to the app. A key that can only read, or that
    does not reach the address, is refused as a send would be.

    Args:
        idempotency_key (str | Unset):
        body (SignInsApproveBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SignInsApproveResponse201
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
