from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.pods_list_response_200 import PodsListResponse200
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/pods",
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PodsListResponse200:
    if response.status_code >= 400:
        raise errors.PidgeonError.from_response(response)

    if response.status_code == 200:
        response_200 = PodsListResponse200.from_dict(response.json())

        return response_200

    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PodsListResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[PodsListResponse200]:
    """List pods

     The containers in this account, the default first. A pod holds addresses and domains — a customer of
    yours, a client, or just test apart from production.

    **Each pod has its own sending reputation**, so bounces from one customer cannot degrade delivery
    for another — mail sends under the pod its address is in, whichever domain it is on. A pod key
    (`pod_id` on `POST /api-keys`) reaches one pod and nothing else.

    Not paged: this is a menu somebody switches with, and a product where that menu needs a cursor is
    one where the menu was the wrong shape.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PodsListResponse200]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> PodsListResponse200:
    """List pods

     The containers in this account, the default first. A pod holds addresses and domains — a customer of
    yours, a client, or just test apart from production.

    **Each pod has its own sending reputation**, so bounces from one customer cannot degrade delivery
    for another — mail sends under the pod its address is in, whichever domain it is on. A pod key
    (`pod_id` on `POST /api-keys`) reaches one pod and nothing else.

    Not paged: this is a menu somebody switches with, and a product where that menu needs a cursor is
    one where the menu was the wrong shape.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PodsListResponse200
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[PodsListResponse200]:
    """List pods

     The containers in this account, the default first. A pod holds addresses and domains — a customer of
    yours, a client, or just test apart from production.

    **Each pod has its own sending reputation**, so bounces from one customer cannot degrade delivery
    for another — mail sends under the pod its address is in, whichever domain it is on. A pod key
    (`pod_id` on `POST /api-keys`) reaches one pod and nothing else.

    Not paged: this is a menu somebody switches with, and a product where that menu needs a cursor is
    one where the menu was the wrong shape.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PodsListResponse200]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> PodsListResponse200:
    """List pods

     The containers in this account, the default first. A pod holds addresses and domains — a customer of
    yours, a client, or just test apart from production.

    **Each pod has its own sending reputation**, so bounces from one customer cannot degrade delivery
    for another — mail sends under the pod its address is in, whichever domain it is on. A pod key
    (`pod_id` on `POST /api-keys`) reaches one pod and nothing else.

    Not paged: this is a menu somebody switches with, and a product where that menu needs a cursor is
    one where the menu was the wrong shape.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PodsListResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
