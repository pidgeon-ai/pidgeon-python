from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.drafts_create_body import DraftsCreateBody
from ...models.drafts_create_response_201 import DraftsCreateResponse201
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    *,
    body: DraftsCreateBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/drafts",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DraftsCreateResponse201 | Error | None:
    if response.status_code == 201:
        response_201 = DraftsCreateResponse201.from_dict(response.json())

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
) -> Response[DraftsCreateResponse201 | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DraftsCreateBody,
) -> Response[DraftsCreateResponse201 | Error]:
    """Write one without sending it

     An agent that drafts a reply, waits for a human to approve it and sends it an hour later is ordinary
    supervised automation, and this is where the half-written message lives in the meantime. Idempotent
    with `Idempotency-Key`.

    Args:
        body (DraftsCreateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DraftsCreateResponse201 | Error]
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
    body: DraftsCreateBody,
) -> DraftsCreateResponse201 | Error | None:
    """Write one without sending it

     An agent that drafts a reply, waits for a human to approve it and sends it an hour later is ordinary
    supervised automation, and this is where the half-written message lives in the meantime. Idempotent
    with `Idempotency-Key`.

    Args:
        body (DraftsCreateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DraftsCreateResponse201 | Error
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DraftsCreateBody,
) -> Response[DraftsCreateResponse201 | Error]:
    """Write one without sending it

     An agent that drafts a reply, waits for a human to approve it and sends it an hour later is ordinary
    supervised automation, and this is where the half-written message lives in the meantime. Idempotent
    with `Idempotency-Key`.

    Args:
        body (DraftsCreateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DraftsCreateResponse201 | Error]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: DraftsCreateBody,
) -> DraftsCreateResponse201 | Error | None:
    """Write one without sending it

     An agent that drafts a reply, waits for a human to approve it and sends it an hour later is ordinary
    supervised automation, and this is where the half-written message lives in the meantime. Idempotent
    with `Idempotency-Key`.

    Args:
        body (DraftsCreateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DraftsCreateResponse201 | Error
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
