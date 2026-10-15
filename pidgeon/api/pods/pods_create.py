from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.pods_create_body import PodsCreateBody
from ...models.pods_create_response_201 import PodsCreateResponse201
from ...types import Response


def _get_kwargs(
    *,
    body: PodsCreateBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/pods",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | PodsCreateResponse201 | None:
    if response.status_code == 201:
        response_201 = PodsCreateResponse201.from_dict(response.json())

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
) -> Response[Error | PodsCreateResponse201]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PodsCreateBody,
) -> Response[Error | PodsCreateResponse201]:
    """Create a pod

     Name it after whatever it holds — a customer, an environment. `client_id` is your own id for it,
    carried and never parsed, and has to be unique within the account so that looking one up by it has
    an answer.

    Args:
        body (PodsCreateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PodsCreateResponse201]
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
    body: PodsCreateBody,
) -> Error | PodsCreateResponse201 | None:
    """Create a pod

     Name it after whatever it holds — a customer, an environment. `client_id` is your own id for it,
    carried and never parsed, and has to be unique within the account so that looking one up by it has
    an answer.

    Args:
        body (PodsCreateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PodsCreateResponse201
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PodsCreateBody,
) -> Response[Error | PodsCreateResponse201]:
    """Create a pod

     Name it after whatever it holds — a customer, an environment. `client_id` is your own id for it,
    carried and never parsed, and has to be unique within the account so that looking one up by it has
    an answer.

    Args:
        body (PodsCreateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PodsCreateResponse201]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PodsCreateBody,
) -> Error | PodsCreateResponse201 | None:
    """Create a pod

     Name it after whatever it holds — a customer, an environment. `client_id` is your own id for it,
    carried and never parsed, and has to be unique within the account so that looking one up by it has
    an answer.

    Args:
        body (PodsCreateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PodsCreateResponse201
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
