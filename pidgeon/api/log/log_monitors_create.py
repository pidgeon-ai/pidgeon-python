from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.log_monitors_create_body import LogMonitorsCreateBody
from ...models.log_monitors_create_response_201 import LogMonitorsCreateResponse201
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: LogMonitorsCreateBody,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/log/monitors",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> LogMonitorsCreateResponse201:
    if response.status_code >= 400:
        raise errors.PidgeonError.from_response(response)

    if response.status_code == 201:
        response_201 = LogMonitorsCreateResponse201.from_dict(response.json())

        return response_201

    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[LogMonitorsCreateResponse201]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: LogMonitorsCreateBody,
    idempotency_key: str | Unset = UNSET,
) -> Response[LogMonitorsCreateResponse201]:
    """Watch the card log for a name

     Every new card log entry whose address, `on_behalf_of` or operator domain claims `term` — look-
    alikes included, such as a Greek Μ in “Meta” — emits a `card_log.matched` event to the account’s
    webhooks and, unless `email` is false, emails its owners. It watches from now on. An owner, or an
    admin key over every address; 50 at most.

    Args:
        idempotency_key (str | Unset):
        body (LogMonitorsCreateBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LogMonitorsCreateResponse201]
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
    body: LogMonitorsCreateBody,
    idempotency_key: str | Unset = UNSET,
) -> LogMonitorsCreateResponse201:
    """Watch the card log for a name

     Every new card log entry whose address, `on_behalf_of` or operator domain claims `term` — look-
    alikes included, such as a Greek Μ in “Meta” — emits a `card_log.matched` event to the account’s
    webhooks and, unless `email` is false, emails its owners. It watches from now on. An owner, or an
    admin key over every address; 50 at most.

    Args:
        idempotency_key (str | Unset):
        body (LogMonitorsCreateBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LogMonitorsCreateResponse201
    """

    return sync_detailed(
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: LogMonitorsCreateBody,
    idempotency_key: str | Unset = UNSET,
) -> Response[LogMonitorsCreateResponse201]:
    """Watch the card log for a name

     Every new card log entry whose address, `on_behalf_of` or operator domain claims `term` — look-
    alikes included, such as a Greek Μ in “Meta” — emits a `card_log.matched` event to the account’s
    webhooks and, unless `email` is false, emails its owners. It watches from now on. An owner, or an
    admin key over every address; 50 at most.

    Args:
        idempotency_key (str | Unset):
        body (LogMonitorsCreateBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LogMonitorsCreateResponse201]
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
    body: LogMonitorsCreateBody,
    idempotency_key: str | Unset = UNSET,
) -> LogMonitorsCreateResponse201:
    """Watch the card log for a name

     Every new card log entry whose address, `on_behalf_of` or operator domain claims `term` — look-
    alikes included, such as a Greek Μ in “Meta” — emits a `card_log.matched` event to the account’s
    webhooks and, unless `email` is false, emails its owners. It watches from now on. An owner, or an
    admin key over every address; 50 at most.

    Args:
        idempotency_key (str | Unset):
        body (LogMonitorsCreateBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LogMonitorsCreateResponse201
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
