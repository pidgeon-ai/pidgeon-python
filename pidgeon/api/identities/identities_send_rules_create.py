from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.identities_send_rules_create_body import IdentitiesSendRulesCreateBody
from ...models.identities_send_rules_create_response_200 import IdentitiesSendRulesCreateResponse200
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: IdentitiesSendRulesCreateBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/identities/{id}/send-rules".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | IdentitiesSendRulesCreateResponse200 | None:
    if response.status_code == 200:
        response_200 = IdentitiesSendRulesCreateResponse200.from_dict(response.json())

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
) -> Response[Error | IdentitiesSendRulesCreateResponse200]:
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
    body: IdentitiesSendRulesCreateBody,
) -> Response[Error | IdentitiesSendRulesCreateResponse200]:
    """Allow or block a recipient

     `value` is an address or a domain and the string says which: `billing@acme.com` matches one person,
    `acme.com` matches everybody there. **The more specific rule wins**, so blocking a domain and
    allowing one person at it does what it looks like. Adding **replaces** any rule already there for
    that value, so `allow` where `block` sat is a change of mind rather than a conflict. A `block`
    refuses under every policy, including `open`.

    Args:
        id (str):
        body (IdentitiesSendRulesCreateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | IdentitiesSendRulesCreateResponse200]
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
    body: IdentitiesSendRulesCreateBody,
) -> Error | IdentitiesSendRulesCreateResponse200 | None:
    """Allow or block a recipient

     `value` is an address or a domain and the string says which: `billing@acme.com` matches one person,
    `acme.com` matches everybody there. **The more specific rule wins**, so blocking a domain and
    allowing one person at it does what it looks like. Adding **replaces** any rule already there for
    that value, so `allow` where `block` sat is a change of mind rather than a conflict. A `block`
    refuses under every policy, including `open`.

    Args:
        id (str):
        body (IdentitiesSendRulesCreateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | IdentitiesSendRulesCreateResponse200
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
    body: IdentitiesSendRulesCreateBody,
) -> Response[Error | IdentitiesSendRulesCreateResponse200]:
    """Allow or block a recipient

     `value` is an address or a domain and the string says which: `billing@acme.com` matches one person,
    `acme.com` matches everybody there. **The more specific rule wins**, so blocking a domain and
    allowing one person at it does what it looks like. Adding **replaces** any rule already there for
    that value, so `allow` where `block` sat is a change of mind rather than a conflict. A `block`
    refuses under every policy, including `open`.

    Args:
        id (str):
        body (IdentitiesSendRulesCreateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | IdentitiesSendRulesCreateResponse200]
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
    body: IdentitiesSendRulesCreateBody,
) -> Error | IdentitiesSendRulesCreateResponse200 | None:
    """Allow or block a recipient

     `value` is an address or a domain and the string says which: `billing@acme.com` matches one person,
    `acme.com` matches everybody there. **The more specific rule wins**, so blocking a domain and
    allowing one person at it does what it looks like. Adding **replaces** any rule already there for
    that value, so `allow` where `block` sat is a change of mind rather than a conflict. A `block`
    refuses under every policy, including `open`.

    Args:
        id (str):
        body (IdentitiesSendRulesCreateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | IdentitiesSendRulesCreateResponse200
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
