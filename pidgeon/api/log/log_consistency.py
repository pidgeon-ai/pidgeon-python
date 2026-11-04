from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.log_consistency_response_200 import LogConsistencyResponse200
from ...types import UNSET, Response


def _get_kwargs(
    *,
    first: int,
    second: int,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["first"] = first

    params["second"] = second

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/log/consistency",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> LogConsistencyResponse200:
    if response.status_code >= 400:
        raise errors.PidgeonError.from_response(response)

    if response.status_code == 200:
        response_200 = LogConsistencyResponse200.from_dict(response.json())

        return response_200

    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[LogConsistencyResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    first: int,
    second: int,
) -> Response[LogConsistencyResponse200]:
    """Prove the card log only grew

     Public, with no key. The consistency proof (RFC 9162 §2.1.4) that the tree of `first` entries is a
    prefix of the tree of `second`: what a monitor asks each time the head moves, so nothing it saw was
    rewritten.

    Args:
        first (int): The smaller tree size.
        second (int): The larger tree size.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LogConsistencyResponse200]
    """

    kwargs = _get_kwargs(
        first=first,
        second=second,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    first: int,
    second: int,
) -> LogConsistencyResponse200:
    """Prove the card log only grew

     Public, with no key. The consistency proof (RFC 9162 §2.1.4) that the tree of `first` entries is a
    prefix of the tree of `second`: what a monitor asks each time the head moves, so nothing it saw was
    rewritten.

    Args:
        first (int): The smaller tree size.
        second (int): The larger tree size.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LogConsistencyResponse200
    """

    return sync_detailed(
        client=client,
        first=first,
        second=second,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    first: int,
    second: int,
) -> Response[LogConsistencyResponse200]:
    """Prove the card log only grew

     Public, with no key. The consistency proof (RFC 9162 §2.1.4) that the tree of `first` entries is a
    prefix of the tree of `second`: what a monitor asks each time the head moves, so nothing it saw was
    rewritten.

    Args:
        first (int): The smaller tree size.
        second (int): The larger tree size.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LogConsistencyResponse200]
    """

    kwargs = _get_kwargs(
        first=first,
        second=second,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    first: int,
    second: int,
) -> LogConsistencyResponse200:
    """Prove the card log only grew

     Public, with no key. The consistency proof (RFC 9162 §2.1.4) that the tree of `first` entries is a
    prefix of the tree of `second`: what a monitor asks each time the head moves, so nothing it saw was
    rewritten.

    Args:
        first (int): The smaller tree size.
        second (int): The larger tree size.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LogConsistencyResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            first=first,
            second=second,
        )
    ).parsed
