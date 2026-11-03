from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.contacts_list_response_200 import ContactsListResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    identity_id: UUID | Unset = UNSET,
    search: str | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_identity_id: str | Unset = UNSET
    if not isinstance(identity_id, Unset):
        json_identity_id = str(identity_id)
    params["identity_id"] = json_identity_id

    params["search"] = search

    params["limit"] = limit

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/contacts",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ContactsListResponse200:
    if response.status_code >= 400:
        raise errors.PidgeonError.from_response(response)

    if response.status_code == 200:
        response_200 = ContactsListResponse200.from_dict(response.json())

        return response_200

    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ContactsListResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    identity_id: UUID | Unset = UNSET,
    search: str | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> Response[ContactsListResponse200]:
    """Find contacts

     The people and agents your addresses correspond with, most recent first: noted from the mail as it
    comes and goes, and editable. A contact belongs to one address, so the same person on two addresses
    is two contacts. `search` matches part of a name or an address. Only the addresses this key reads
    are listed; naming one it cannot read lists nothing. Pages through `next_cursor`.

    Args:
        identity_id (UUID | Unset): Only the contacts of this address.
        search (str | Unset): Part of a name or an address: `priya`, `@acme.com`.
        limit (int | Unset):  Default: 50.
        cursor (str | Unset): From a previous page’s `next_cursor`. Opaque — do not parse it.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContactsListResponse200]
    """

    kwargs = _get_kwargs(
        identity_id=identity_id,
        search=search,
        limit=limit,
        cursor=cursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    identity_id: UUID | Unset = UNSET,
    search: str | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> ContactsListResponse200:
    """Find contacts

     The people and agents your addresses correspond with, most recent first: noted from the mail as it
    comes and goes, and editable. A contact belongs to one address, so the same person on two addresses
    is two contacts. `search` matches part of a name or an address. Only the addresses this key reads
    are listed; naming one it cannot read lists nothing. Pages through `next_cursor`.

    Args:
        identity_id (UUID | Unset): Only the contacts of this address.
        search (str | Unset): Part of a name or an address: `priya`, `@acme.com`.
        limit (int | Unset):  Default: 50.
        cursor (str | Unset): From a previous page’s `next_cursor`. Opaque — do not parse it.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContactsListResponse200
    """

    return sync_detailed(
        client=client,
        identity_id=identity_id,
        search=search,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    identity_id: UUID | Unset = UNSET,
    search: str | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> Response[ContactsListResponse200]:
    """Find contacts

     The people and agents your addresses correspond with, most recent first: noted from the mail as it
    comes and goes, and editable. A contact belongs to one address, so the same person on two addresses
    is two contacts. `search` matches part of a name or an address. Only the addresses this key reads
    are listed; naming one it cannot read lists nothing. Pages through `next_cursor`.

    Args:
        identity_id (UUID | Unset): Only the contacts of this address.
        search (str | Unset): Part of a name or an address: `priya`, `@acme.com`.
        limit (int | Unset):  Default: 50.
        cursor (str | Unset): From a previous page’s `next_cursor`. Opaque — do not parse it.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContactsListResponse200]
    """

    kwargs = _get_kwargs(
        identity_id=identity_id,
        search=search,
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    identity_id: UUID | Unset = UNSET,
    search: str | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> ContactsListResponse200:
    """Find contacts

     The people and agents your addresses correspond with, most recent first: noted from the mail as it
    comes and goes, and editable. A contact belongs to one address, so the same person on two addresses
    is two contacts. `search` matches part of a name or an address. Only the addresses this key reads
    are listed; naming one it cannot read lists nothing. Pages through `next_cursor`.

    Args:
        identity_id (UUID | Unset): Only the contacts of this address.
        search (str | Unset): Part of a name or an address: `priya`, `@acme.com`.
        limit (int | Unset):  Default: 50.
        cursor (str | Unset): From a previous page’s `next_cursor`. Opaque — do not parse it.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContactsListResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            identity_id=identity_id,
            search=search,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
