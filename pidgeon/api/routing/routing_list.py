from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.routing_list_response_200 import RoutingListResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    domain_id: UUID | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_domain_id: str | Unset = UNSET
    if not isinstance(domain_id, Unset):
        json_domain_id = str(domain_id)
    params["domain_id"] = json_domain_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/routing-rules",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> RoutingListResponse200:
    if response.status_code >= 400:
        raise errors.PidgeonError.from_response(response)

    if response.status_code == 200:
        response_200 = RoutingListResponse200.from_dict(response.json())

        return response_200

    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RoutingListResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    domain_id: UUID | Unset = UNSET,
) -> Response[RoutingListResponse200]:
    """List routing rules

     Every rule in the workspace, newest domain-first. `domain_id` narrows it to one domain.

    Args:
        domain_id (UUID | Unset):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RoutingListResponse200]
    """

    kwargs = _get_kwargs(
        domain_id=domain_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    domain_id: UUID | Unset = UNSET,
) -> RoutingListResponse200:
    """List routing rules

     Every rule in the workspace, newest domain-first. `domain_id` narrows it to one domain.

    Args:
        domain_id (UUID | Unset):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RoutingListResponse200
    """

    return sync_detailed(
        client=client,
        domain_id=domain_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    domain_id: UUID | Unset = UNSET,
) -> Response[RoutingListResponse200]:
    """List routing rules

     Every rule in the workspace, newest domain-first. `domain_id` narrows it to one domain.

    Args:
        domain_id (UUID | Unset):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RoutingListResponse200]
    """

    kwargs = _get_kwargs(
        domain_id=domain_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    domain_id: UUID | Unset = UNSET,
) -> RoutingListResponse200:
    """List routing rules

     Every rule in the workspace, newest domain-first. `domain_id` narrows it to one domain.

    Args:
        domain_id (UUID | Unset):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RoutingListResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            domain_id=domain_id,
        )
    ).parsed
