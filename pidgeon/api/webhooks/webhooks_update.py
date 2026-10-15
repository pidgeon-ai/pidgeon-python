from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.webhooks_update_body import WebhooksUpdateBody
from ...models.webhooks_update_response_200 import WebhooksUpdateResponse200
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: WebhooksUpdateBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/webhooks/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | WebhooksUpdateResponse200 | None:
    if response.status_code == 200:
        response_200 = WebhooksUpdateResponse200.from_dict(response.json())

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
) -> Response[Error | WebhooksUpdateResponse200]:
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
    body: WebhooksUpdateBody,
) -> Response[Error | WebhooksUpdateResponse200]:
    """Turn an endpoint off, or back on

     We disable one ourselves after enough consecutive failures. Without this you would have to delete
    and recreate it, which changes the signing secret every receiver is verifying against. Re-enabling
    forgives the failure count.

    Args:
        id (str):
        body (WebhooksUpdateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | WebhooksUpdateResponse200]
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
    body: WebhooksUpdateBody,
) -> Error | WebhooksUpdateResponse200 | None:
    """Turn an endpoint off, or back on

     We disable one ourselves after enough consecutive failures. Without this you would have to delete
    and recreate it, which changes the signing secret every receiver is verifying against. Re-enabling
    forgives the failure count.

    Args:
        id (str):
        body (WebhooksUpdateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | WebhooksUpdateResponse200
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
    body: WebhooksUpdateBody,
) -> Response[Error | WebhooksUpdateResponse200]:
    """Turn an endpoint off, or back on

     We disable one ourselves after enough consecutive failures. Without this you would have to delete
    and recreate it, which changes the signing secret every receiver is verifying against. Re-enabling
    forgives the failure count.

    Args:
        id (str):
        body (WebhooksUpdateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | WebhooksUpdateResponse200]
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
    body: WebhooksUpdateBody,
) -> Error | WebhooksUpdateResponse200 | None:
    """Turn an endpoint off, or back on

     We disable one ourselves after enough consecutive failures. Without this you would have to delete
    and recreate it, which changes the signing secret every receiver is verifying against. Re-enabling
    forgives the failure count.

    Args:
        id (str):
        body (WebhooksUpdateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | WebhooksUpdateResponse200
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
