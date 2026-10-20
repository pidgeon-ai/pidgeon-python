from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.identities_list_response_200 import IdentitiesListResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    tenant_id: str | Unset = UNSET,
    pod_id: UUID | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["cursor"] = cursor

    params["tenant_id"] = tenant_id

    json_pod_id: str | Unset = UNSET
    if not isinstance(pod_id, Unset):
        json_pod_id = str(pod_id)
    params["pod_id"] = json_pod_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/identities",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> IdentitiesListResponse200:
    if response.status_code >= 400:
        raise errors.PidgeonError.from_response(response)

    if response.status_code == 200:
        response_200 = IdentitiesListResponse200.from_dict(response.json())

        return response_200

    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[IdentitiesListResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    tenant_id: str | Unset = UNSET,
    pod_id: UUID | Unset = UNSET,
) -> Response[IdentitiesListResponse200]:
    """List addresses

     Alphabetical by address. `cursor` is the last address on the page before it, not a timestamp — this
    is the one list that is not ordered by time, because it is read by somebody looking for a particular
    address.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset): From a previous page’s `next_cursor`. Opaque — do not parse it.
        tenant_id (str | Unset):
        pod_id (UUID | Unset):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IdentitiesListResponse200]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
        tenant_id=tenant_id,
        pod_id=pod_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    tenant_id: str | Unset = UNSET,
    pod_id: UUID | Unset = UNSET,
) -> IdentitiesListResponse200:
    """List addresses

     Alphabetical by address. `cursor` is the last address on the page before it, not a timestamp — this
    is the one list that is not ordered by time, because it is read by somebody looking for a particular
    address.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset): From a previous page’s `next_cursor`. Opaque — do not parse it.
        tenant_id (str | Unset):
        pod_id (UUID | Unset):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IdentitiesListResponse200
    """

    return sync_detailed(
        client=client,
        limit=limit,
        cursor=cursor,
        tenant_id=tenant_id,
        pod_id=pod_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    tenant_id: str | Unset = UNSET,
    pod_id: UUID | Unset = UNSET,
) -> Response[IdentitiesListResponse200]:
    """List addresses

     Alphabetical by address. `cursor` is the last address on the page before it, not a timestamp — this
    is the one list that is not ordered by time, because it is read by somebody looking for a particular
    address.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset): From a previous page’s `next_cursor`. Opaque — do not parse it.
        tenant_id (str | Unset):
        pod_id (UUID | Unset):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IdentitiesListResponse200]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
        tenant_id=tenant_id,
        pod_id=pod_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    tenant_id: str | Unset = UNSET,
    pod_id: UUID | Unset = UNSET,
) -> IdentitiesListResponse200:
    """List addresses

     Alphabetical by address. `cursor` is the last address on the page before it, not a timestamp — this
    is the one list that is not ordered by time, because it is read by somebody looking for a particular
    address.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset): From a previous page’s `next_cursor`. Opaque — do not parse it.
        tenant_id (str | Unset):
        pod_id (UUID | Unset):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IdentitiesListResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            cursor=cursor,
            tenant_id=tenant_id,
            pod_id=pod_id,
        )
    ).parsed
