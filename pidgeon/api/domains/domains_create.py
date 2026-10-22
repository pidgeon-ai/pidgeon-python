from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domains_create_body import DomainsCreateBody
from ...models.domains_create_response_201 import DomainsCreateResponse201
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: DomainsCreateBody,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/domains",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DomainsCreateResponse201:
    if response.status_code >= 400:
        raise errors.PidgeonError.from_response(response)

    if response.status_code == 201:
        response_201 = DomainsCreateResponse201.from_dict(response.json())

        return response_201

    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DomainsCreateResponse201]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DomainsCreateBody,
    idempotency_key: str | Unset = UNSET,
) -> Response[DomainsCreateResponse201]:
    """Connect a domain

     Returns the domain **and the records to publish**, because showing them to your own customer is the
    one thing every caller does next. DNS is the step this API cannot perform — we cannot write in
    somebody else’s zone — so the job is to make the human step delegable. Watch `dns_complete`: it is
    false while the DKIM records do not exist yet, and a list published in that state verifies and
    cannot sign mail.

    Args:
        idempotency_key (str | Unset):
        body (DomainsCreateBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DomainsCreateResponse201]
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
    body: DomainsCreateBody,
    idempotency_key: str | Unset = UNSET,
) -> DomainsCreateResponse201:
    """Connect a domain

     Returns the domain **and the records to publish**, because showing them to your own customer is the
    one thing every caller does next. DNS is the step this API cannot perform — we cannot write in
    somebody else’s zone — so the job is to make the human step delegable. Watch `dns_complete`: it is
    false while the DKIM records do not exist yet, and a list published in that state verifies and
    cannot sign mail.

    Args:
        idempotency_key (str | Unset):
        body (DomainsCreateBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DomainsCreateResponse201
    """

    return sync_detailed(
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DomainsCreateBody,
    idempotency_key: str | Unset = UNSET,
) -> Response[DomainsCreateResponse201]:
    """Connect a domain

     Returns the domain **and the records to publish**, because showing them to your own customer is the
    one thing every caller does next. DNS is the step this API cannot perform — we cannot write in
    somebody else’s zone — so the job is to make the human step delegable. Watch `dns_complete`: it is
    false while the DKIM records do not exist yet, and a list published in that state verifies and
    cannot sign mail.

    Args:
        idempotency_key (str | Unset):
        body (DomainsCreateBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DomainsCreateResponse201]
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
    body: DomainsCreateBody,
    idempotency_key: str | Unset = UNSET,
) -> DomainsCreateResponse201:
    """Connect a domain

     Returns the domain **and the records to publish**, because showing them to your own customer is the
    one thing every caller does next. DNS is the step this API cannot perform — we cannot write in
    somebody else’s zone — so the job is to make the human step delegable. Watch `dns_complete`: it is
    false while the DKIM records do not exist yet, and a list published in that state verifies and
    cannot sign mail.

    Args:
        idempotency_key (str | Unset):
        body (DomainsCreateBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DomainsCreateResponse201
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
