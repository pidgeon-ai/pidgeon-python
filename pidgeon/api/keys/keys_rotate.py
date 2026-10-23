from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.keys_rotate_body import KeysRotateBody
from ...models.keys_rotate_response_200 import KeysRotateResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    body: KeysRotateBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api-keys/{id}/rotate".format(
            id=quote(str(id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> KeysRotateResponse200:
    if response.status_code >= 400:
        raise errors.PidgeonError.from_response(response)

    if response.status_code == 200:
        response_200 = KeysRotateResponse200.from_dict(response.json())

        return response_200

    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[KeysRotateResponse200]:
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
    body: KeysRotateBody | Unset = UNSET,
) -> Response[KeysRotateResponse200]:
    """Give a key a new secret

     A new secret for the same key id. Everything that hangs off the id is unchanged — its scope, its
    ceiling, its expiry, and **every key it minted**, which keep working — so rotating an admin key does
    not take its children down. Revoking is still how a key and its children end together.

    The old secret stops now, or after `grace_period_seconds` (at most 86400, a day), so the servers
    that hold it can move over. One previous secret at a time: rotating again inside the window ends the
    older one immediately.

    A key may rotate itself and keys it minted; a person must own the workspace. The `token` is in this
    response and nowhere else, ever.

    Args:
        id (str):
        body (KeysRotateBody | Unset):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[KeysRotateResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: KeysRotateBody | Unset = UNSET,
) -> KeysRotateResponse200:
    """Give a key a new secret

     A new secret for the same key id. Everything that hangs off the id is unchanged — its scope, its
    ceiling, its expiry, and **every key it minted**, which keep working — so rotating an admin key does
    not take its children down. Revoking is still how a key and its children end together.

    The old secret stops now, or after `grace_period_seconds` (at most 86400, a day), so the servers
    that hold it can move over. One previous secret at a time: rotating again inside the window ends the
    older one immediately.

    A key may rotate itself and keys it minted; a person must own the workspace. The `token` is in this
    response and nowhere else, ever.

    Args:
        id (str):
        body (KeysRotateBody | Unset):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        KeysRotateResponse200
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: KeysRotateBody | Unset = UNSET,
) -> Response[KeysRotateResponse200]:
    """Give a key a new secret

     A new secret for the same key id. Everything that hangs off the id is unchanged — its scope, its
    ceiling, its expiry, and **every key it minted**, which keep working — so rotating an admin key does
    not take its children down. Revoking is still how a key and its children end together.

    The old secret stops now, or after `grace_period_seconds` (at most 86400, a day), so the servers
    that hold it can move over. One previous secret at a time: rotating again inside the window ends the
    older one immediately.

    A key may rotate itself and keys it minted; a person must own the workspace. The `token` is in this
    response and nowhere else, ever.

    Args:
        id (str):
        body (KeysRotateBody | Unset):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[KeysRotateResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: KeysRotateBody | Unset = UNSET,
) -> KeysRotateResponse200:
    """Give a key a new secret

     A new secret for the same key id. Everything that hangs off the id is unchanged — its scope, its
    ceiling, its expiry, and **every key it minted**, which keep working — so rotating an admin key does
    not take its children down. Revoking is still how a key and its children end together.

    The old secret stops now, or after `grace_period_seconds` (at most 86400, a day), so the servers
    that hold it can move over. One previous secret at a time: rotating again inside the window ends the
    older one immediately.

    A key may rotate itself and keys it minted; a person must own the workspace. The `token` is in this
    response and nowhere else, ever.

    Args:
        id (str):
        body (KeysRotateBody | Unset):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        KeysRotateResponse200
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
