from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.identities_send_rules_create_body import IdentitiesSendRulesCreateBody
from ...models.identities_send_rules_create_response_200 import IdentitiesSendRulesCreateResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    body: IdentitiesSendRulesCreateBody,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

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
) -> IdentitiesSendRulesCreateResponse200:
    if response.status_code >= 400:
        raise errors.PidgeonError.from_response(response)

    if response.status_code == 200:
        response_200 = IdentitiesSendRulesCreateResponse200.from_dict(response.json())

        return response_200

    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[IdentitiesSendRulesCreateResponse200]:
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
    idempotency_key: str | Unset = UNSET,
) -> Response[IdentitiesSendRulesCreateResponse200]:
    """Allow or block a recipient

     `value` is an address or a domain and the string says which: `billing@acme.com` matches one person,
    `acme.com` matches everybody there. **The more specific rule wins**, so blocking a domain and
    allowing one person at it does what it looks like. Adding **replaces** any rule already there for
    that value, so `allow` where `block` sat is a change of mind rather than a conflict. A `block`
    refuses under every policy, including `open`.

    Args:
        id (str):
        idempotency_key (str | Unset):
        body (IdentitiesSendRulesCreateBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IdentitiesSendRulesCreateResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
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
    body: IdentitiesSendRulesCreateBody,
    idempotency_key: str | Unset = UNSET,
) -> IdentitiesSendRulesCreateResponse200:
    """Allow or block a recipient

     `value` is an address or a domain and the string says which: `billing@acme.com` matches one person,
    `acme.com` matches everybody there. **The more specific rule wins**, so blocking a domain and
    allowing one person at it does what it looks like. Adding **replaces** any rule already there for
    that value, so `allow` where `block` sat is a change of mind rather than a conflict. A `block`
    refuses under every policy, including `open`.

    Args:
        id (str):
        idempotency_key (str | Unset):
        body (IdentitiesSendRulesCreateBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IdentitiesSendRulesCreateResponse200
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: IdentitiesSendRulesCreateBody,
    idempotency_key: str | Unset = UNSET,
) -> Response[IdentitiesSendRulesCreateResponse200]:
    """Allow or block a recipient

     `value` is an address or a domain and the string says which: `billing@acme.com` matches one person,
    `acme.com` matches everybody there. **The more specific rule wins**, so blocking a domain and
    allowing one person at it does what it looks like. Adding **replaces** any rule already there for
    that value, so `allow` where `block` sat is a change of mind rather than a conflict. A `block`
    refuses under every policy, including `open`.

    Args:
        id (str):
        idempotency_key (str | Unset):
        body (IdentitiesSendRulesCreateBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IdentitiesSendRulesCreateResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: IdentitiesSendRulesCreateBody,
    idempotency_key: str | Unset = UNSET,
) -> IdentitiesSendRulesCreateResponse200:
    """Allow or block a recipient

     `value` is an address or a domain and the string says which: `billing@acme.com` matches one person,
    `acme.com` matches everybody there. **The more specific rule wins**, so blocking a domain and
    allowing one person at it does what it looks like. Adding **replaces** any rule already there for
    that value, so `allow` where `block` sat is a change of mind rather than a conflict. A `block`
    refuses under every policy, including `open`.

    Args:
        id (str):
        idempotency_key (str | Unset):
        body (IdentitiesSendRulesCreateBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IdentitiesSendRulesCreateResponse200
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
