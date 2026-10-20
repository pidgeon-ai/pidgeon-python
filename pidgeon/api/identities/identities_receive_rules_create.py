from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.identities_receive_rules_create_body import IdentitiesReceiveRulesCreateBody
from ...models.identities_receive_rules_create_response_200 import IdentitiesReceiveRulesCreateResponse200
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: IdentitiesReceiveRulesCreateBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/identities/{id}/receive-rules".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> IdentitiesReceiveRulesCreateResponse200:
    if response.status_code >= 400:
        raise errors.PidgeonError.from_response(response)

    if response.status_code == 200:
        response_200 = IdentitiesReceiveRulesCreateResponse200.from_dict(response.json())

        return response_200

    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[IdentitiesReceiveRulesCreateResponse200]:
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
    body: IdentitiesReceiveRulesCreateBody,
) -> Response[IdentitiesReceiveRulesCreateResponse200]:
    """Decide what happens to a sender

     `value` is an address or a domain and the string says which: `billing@acme.com` matches one person,
    `acme.com` matches everybody there. **The more specific rule wins**, and an address’s own rule wins
    over a workspace-wide one. Adding **replaces** any rule already there for that value.

    `action` is `reject`, `spam`, `trash`, `archive` or `inbox`. **`reject` refuses before the message
    is stored** — no row, no thread, no storage charged and no webhook — which is what an address nobody
    will ever open wants. The other four file it, and `inbox` means *never classify this sender as
    spam*.

    **It is not a security control.** The `From:` header is written by the sender, and anybody blocked
    can change it for the price of a new address. What this buys is not paying for mail from senders who
    have not bothered.

    Args:
        id (str):
        body (IdentitiesReceiveRulesCreateBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IdentitiesReceiveRulesCreateResponse200]
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
    body: IdentitiesReceiveRulesCreateBody,
) -> IdentitiesReceiveRulesCreateResponse200:
    """Decide what happens to a sender

     `value` is an address or a domain and the string says which: `billing@acme.com` matches one person,
    `acme.com` matches everybody there. **The more specific rule wins**, and an address’s own rule wins
    over a workspace-wide one. Adding **replaces** any rule already there for that value.

    `action` is `reject`, `spam`, `trash`, `archive` or `inbox`. **`reject` refuses before the message
    is stored** — no row, no thread, no storage charged and no webhook — which is what an address nobody
    will ever open wants. The other four file it, and `inbox` means *never classify this sender as
    spam*.

    **It is not a security control.** The `From:` header is written by the sender, and anybody blocked
    can change it for the price of a new address. What this buys is not paying for mail from senders who
    have not bothered.

    Args:
        id (str):
        body (IdentitiesReceiveRulesCreateBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IdentitiesReceiveRulesCreateResponse200
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
    body: IdentitiesReceiveRulesCreateBody,
) -> Response[IdentitiesReceiveRulesCreateResponse200]:
    """Decide what happens to a sender

     `value` is an address or a domain and the string says which: `billing@acme.com` matches one person,
    `acme.com` matches everybody there. **The more specific rule wins**, and an address’s own rule wins
    over a workspace-wide one. Adding **replaces** any rule already there for that value.

    `action` is `reject`, `spam`, `trash`, `archive` or `inbox`. **`reject` refuses before the message
    is stored** — no row, no thread, no storage charged and no webhook — which is what an address nobody
    will ever open wants. The other four file it, and `inbox` means *never classify this sender as
    spam*.

    **It is not a security control.** The `From:` header is written by the sender, and anybody blocked
    can change it for the price of a new address. What this buys is not paying for mail from senders who
    have not bothered.

    Args:
        id (str):
        body (IdentitiesReceiveRulesCreateBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IdentitiesReceiveRulesCreateResponse200]
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
    body: IdentitiesReceiveRulesCreateBody,
) -> IdentitiesReceiveRulesCreateResponse200:
    """Decide what happens to a sender

     `value` is an address or a domain and the string says which: `billing@acme.com` matches one person,
    `acme.com` matches everybody there. **The more specific rule wins**, and an address’s own rule wins
    over a workspace-wide one. Adding **replaces** any rule already there for that value.

    `action` is `reject`, `spam`, `trash`, `archive` or `inbox`. **`reject` refuses before the message
    is stored** — no row, no thread, no storage charged and no webhook — which is what an address nobody
    will ever open wants. The other four file it, and `inbox` means *never classify this sender as
    spam*.

    **It is not a security control.** The `From:` header is written by the sender, and anybody blocked
    can change it for the price of a new address. What this buys is not paying for mail from senders who
    have not bothered.

    Args:
        id (str):
        body (IdentitiesReceiveRulesCreateBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IdentitiesReceiveRulesCreateResponse200
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
