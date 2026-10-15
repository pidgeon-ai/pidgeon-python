from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.routing_create_body_type_0 import RoutingCreateBodyType0
from ...models.routing_create_body_type_1 import RoutingCreateBodyType1
from ...models.routing_create_body_type_2 import RoutingCreateBodyType2
from ...models.routing_create_response_201 import RoutingCreateResponse201
from ...types import Response


def _get_kwargs(
    *,
    body: RoutingCreateBodyType0 | RoutingCreateBodyType1 | RoutingCreateBodyType2,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/routing-rules",
    }

    if isinstance(body, RoutingCreateBodyType0):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, RoutingCreateBodyType1):
        _kwargs["json"] = body.to_dict()
    else:
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | RoutingCreateResponse201 | None:
    if response.status_code == 201:
        response_201 = RoutingCreateResponse201.from_dict(response.json())

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
) -> Response[Error | RoutingCreateResponse201]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RoutingCreateBodyType0 | RoutingCreateBodyType1 | RoutingCreateBodyType2,
) -> Response[Error | RoutingCreateResponse201]:
    """Route an address somewhere

     An address always beats a rule, so a rule for an address that already exists is refused rather than
    silently ignored. Name exactly one destination: an address you could already send from, or a webhook
    — a webhook destination has no inbox, so the message is handed to the endpoint and then gone.

    Args:
        body (RoutingCreateBodyType0 | RoutingCreateBodyType1 | RoutingCreateBodyType2):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | RoutingCreateResponse201]
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
    body: RoutingCreateBodyType0 | RoutingCreateBodyType1 | RoutingCreateBodyType2,
) -> Error | RoutingCreateResponse201 | None:
    """Route an address somewhere

     An address always beats a rule, so a rule for an address that already exists is refused rather than
    silently ignored. Name exactly one destination: an address you could already send from, or a webhook
    — a webhook destination has no inbox, so the message is handed to the endpoint and then gone.

    Args:
        body (RoutingCreateBodyType0 | RoutingCreateBodyType1 | RoutingCreateBodyType2):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | RoutingCreateResponse201
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RoutingCreateBodyType0 | RoutingCreateBodyType1 | RoutingCreateBodyType2,
) -> Response[Error | RoutingCreateResponse201]:
    """Route an address somewhere

     An address always beats a rule, so a rule for an address that already exists is refused rather than
    silently ignored. Name exactly one destination: an address you could already send from, or a webhook
    — a webhook destination has no inbox, so the message is handed to the endpoint and then gone.

    Args:
        body (RoutingCreateBodyType0 | RoutingCreateBodyType1 | RoutingCreateBodyType2):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | RoutingCreateResponse201]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: RoutingCreateBodyType0 | RoutingCreateBodyType1 | RoutingCreateBodyType2,
) -> Error | RoutingCreateResponse201 | None:
    """Route an address somewhere

     An address always beats a rule, so a rule for an address that already exists is refused rather than
    silently ignored. Name exactly one destination: an address you could already send from, or a webhook
    — a webhook destination has no inbox, so the message is handed to the endpoint and then gone.

    Args:
        body (RoutingCreateBodyType0 | RoutingCreateBodyType1 | RoutingCreateBodyType2):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | RoutingCreateResponse201
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
