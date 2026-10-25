from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.identities_create_body import IdentitiesCreateBody
from ...models.identities_create_response_201 import IdentitiesCreateResponse201
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: IdentitiesCreateBody,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/identities",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> IdentitiesCreateResponse201:
    if response.status_code >= 400:
        raise errors.PidgeonError.from_response(response)

    if response.status_code == 201:
        response_201 = IdentitiesCreateResponse201.from_dict(response.json())

        return response_201

    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[IdentitiesCreateResponse201]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: IdentitiesCreateBody,
    idempotency_key: str | Unset = UNSET,
) -> Response[IdentitiesCreateResponse201]:
    """Create an address

     Idempotent with an `Idempotency-Key` header: the same key returns the first result rather than
    creating a second address.

    Needs a key with admin over the account, or over its pod. A **test key** creates a test address
    (`test: true`): outside your plan’s counts, at most 100 at once, taking only test mail, and deleted
    a day after it was made.

    Args:
        idempotency_key (str | Unset):
        body (IdentitiesCreateBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IdentitiesCreateResponse201]
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
    body: IdentitiesCreateBody,
    idempotency_key: str | Unset = UNSET,
) -> IdentitiesCreateResponse201:
    """Create an address

     Idempotent with an `Idempotency-Key` header: the same key returns the first result rather than
    creating a second address.

    Needs a key with admin over the account, or over its pod. A **test key** creates a test address
    (`test: true`): outside your plan’s counts, at most 100 at once, taking only test mail, and deleted
    a day after it was made.

    Args:
        idempotency_key (str | Unset):
        body (IdentitiesCreateBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IdentitiesCreateResponse201
    """

    return sync_detailed(
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: IdentitiesCreateBody,
    idempotency_key: str | Unset = UNSET,
) -> Response[IdentitiesCreateResponse201]:
    """Create an address

     Idempotent with an `Idempotency-Key` header: the same key returns the first result rather than
    creating a second address.

    Needs a key with admin over the account, or over its pod. A **test key** creates a test address
    (`test: true`): outside your plan’s counts, at most 100 at once, taking only test mail, and deleted
    a day after it was made.

    Args:
        idempotency_key (str | Unset):
        body (IdentitiesCreateBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IdentitiesCreateResponse201]
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
    body: IdentitiesCreateBody,
    idempotency_key: str | Unset = UNSET,
) -> IdentitiesCreateResponse201:
    """Create an address

     Idempotent with an `Idempotency-Key` header: the same key returns the first result rather than
    creating a second address.

    Needs a key with admin over the account, or over its pod. A **test key** creates a test address
    (`test: true`): outside your plan’s counts, at most 100 at once, taking only test mail, and deleted
    a day after it was made.

    Args:
        idempotency_key (str | Unset):
        body (IdentitiesCreateBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IdentitiesCreateResponse201
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
