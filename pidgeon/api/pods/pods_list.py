from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.pods_list_response_200 import PodsListResponse200
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/pods",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | PodsListResponse200 | None:
    if response.status_code == 200:
        response_200 = PodsListResponse200.from_dict(response.json())

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
) -> Response[Error | PodsListResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[Error | PodsListResponse200]:
    """List pods

     The containers in this account, the default first. A pod holds addresses and domains — a customer of
    yours, a client, or just test apart from production.

    **Each pod has its own sending reputation**, so bounces from one customer cannot degrade delivery
    for another — mail sends under the pod its address is in, whichever domain it is on. A key is still
    a list of address ids rather than something scoped to a pod.

    Not paged: this is a menu somebody switches with, and a product where that menu needs a cursor is
    one where the menu was the wrong shape.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PodsListResponse200]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> Error | PodsListResponse200 | None:
    """List pods

     The containers in this account, the default first. A pod holds addresses and domains — a customer of
    yours, a client, or just test apart from production.

    **Each pod has its own sending reputation**, so bounces from one customer cannot degrade delivery
    for another — mail sends under the pod its address is in, whichever domain it is on. A key is still
    a list of address ids rather than something scoped to a pod.

    Not paged: this is a menu somebody switches with, and a product where that menu needs a cursor is
    one where the menu was the wrong shape.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PodsListResponse200
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[Error | PodsListResponse200]:
    """List pods

     The containers in this account, the default first. A pod holds addresses and domains — a customer of
    yours, a client, or just test apart from production.

    **Each pod has its own sending reputation**, so bounces from one customer cannot degrade delivery
    for another — mail sends under the pod its address is in, whichever domain it is on. A key is still
    a list of address ids rather than something scoped to a pod.

    Not paged: this is a menu somebody switches with, and a product where that menu needs a cursor is
    one where the menu was the wrong shape.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PodsListResponse200]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> Error | PodsListResponse200 | None:
    """List pods

     The containers in this account, the default first. A pod holds addresses and domains — a customer of
    yours, a client, or just test apart from production.

    **Each pod has its own sending reputation**, so bounces from one customer cannot degrade delivery
    for another — mail sends under the pod its address is in, whichever domain it is on. A key is still
    a list of address ids rather than something scoped to a pod.

    Not paged: this is a menu somebody switches with, and a product where that menu needs a cursor is
    one where the menu was the wrong shape.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PodsListResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
