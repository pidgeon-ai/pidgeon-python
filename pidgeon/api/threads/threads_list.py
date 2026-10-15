from http import HTTPStatus
from typing import Any, Literal
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.threads_list_owner_type import ThreadsListOwnerType
from ...models.threads_list_response_200 import ThreadsListResponse200
from ...models.threads_list_status import ThreadsListStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    identity_id: UUID | Unset = UNSET,
    status: ThreadsListStatus | Unset = UNSET,
    owner_type: ThreadsListOwnerType | Unset = UNSET,
    assignee_id: Literal["unassigned"] | Unset | UUID = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["cursor"] = cursor

    json_identity_id: str | Unset = UNSET
    if not isinstance(identity_id, Unset):
        json_identity_id = str(identity_id)
    params["identity_id"] = json_identity_id

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    json_owner_type: str | Unset = UNSET
    if not isinstance(owner_type, Unset):
        json_owner_type = owner_type.value

    params["owner_type"] = json_owner_type

    json_assignee_id: Literal["unassigned"] | str | Unset
    if isinstance(assignee_id, Unset):
        json_assignee_id = UNSET
    elif isinstance(assignee_id, UUID):
        json_assignee_id = str(assignee_id)
    else:
        json_assignee_id = assignee_id
    params["assignee_id"] = json_assignee_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/threads",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | ThreadsListResponse200 | None:
    if response.status_code == 200:
        response_200 = ThreadsListResponse200.from_dict(response.json())

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
) -> Response[Error | ThreadsListResponse200]:
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
    identity_id: UUID | Unset = UNSET,
    status: ThreadsListStatus | Unset = UNSET,
    owner_type: ThreadsListOwnerType | Unset = UNSET,
    assignee_id: Literal["unassigned"] | Unset | UUID = UNSET,
) -> Response[Error | ThreadsListResponse200]:
    """List threads

     Filter with `identity_id`, `status`, `owner_type` and `assignee_id`. `assignee_id` takes a person’s
    id, or the literal `unassigned` for the queue nobody has picked up — it says which *human* is
    answering, where `owner_type` says which kind of thing is.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset): From a previous page’s `next_cursor`. Opaque — do not parse it.
        identity_id (UUID | Unset):
        status (ThreadsListStatus | Unset):
        owner_type (ThreadsListOwnerType | Unset):
        assignee_id (Literal['unassigned'] | Unset | UUID): A person’s id, or `unassigned` for the
            queue nobody has taken.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ThreadsListResponse200]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
        identity_id=identity_id,
        status=status,
        owner_type=owner_type,
        assignee_id=assignee_id,
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
    identity_id: UUID | Unset = UNSET,
    status: ThreadsListStatus | Unset = UNSET,
    owner_type: ThreadsListOwnerType | Unset = UNSET,
    assignee_id: Literal["unassigned"] | Unset | UUID = UNSET,
) -> Error | ThreadsListResponse200 | None:
    """List threads

     Filter with `identity_id`, `status`, `owner_type` and `assignee_id`. `assignee_id` takes a person’s
    id, or the literal `unassigned` for the queue nobody has picked up — it says which *human* is
    answering, where `owner_type` says which kind of thing is.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset): From a previous page’s `next_cursor`. Opaque — do not parse it.
        identity_id (UUID | Unset):
        status (ThreadsListStatus | Unset):
        owner_type (ThreadsListOwnerType | Unset):
        assignee_id (Literal['unassigned'] | Unset | UUID): A person’s id, or `unassigned` for the
            queue nobody has taken.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ThreadsListResponse200
    """

    return sync_detailed(
        client=client,
        limit=limit,
        cursor=cursor,
        identity_id=identity_id,
        status=status,
        owner_type=owner_type,
        assignee_id=assignee_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    identity_id: UUID | Unset = UNSET,
    status: ThreadsListStatus | Unset = UNSET,
    owner_type: ThreadsListOwnerType | Unset = UNSET,
    assignee_id: Literal["unassigned"] | Unset | UUID = UNSET,
) -> Response[Error | ThreadsListResponse200]:
    """List threads

     Filter with `identity_id`, `status`, `owner_type` and `assignee_id`. `assignee_id` takes a person’s
    id, or the literal `unassigned` for the queue nobody has picked up — it says which *human* is
    answering, where `owner_type` says which kind of thing is.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset): From a previous page’s `next_cursor`. Opaque — do not parse it.
        identity_id (UUID | Unset):
        status (ThreadsListStatus | Unset):
        owner_type (ThreadsListOwnerType | Unset):
        assignee_id (Literal['unassigned'] | Unset | UUID): A person’s id, or `unassigned` for the
            queue nobody has taken.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ThreadsListResponse200]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
        identity_id=identity_id,
        status=status,
        owner_type=owner_type,
        assignee_id=assignee_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    identity_id: UUID | Unset = UNSET,
    status: ThreadsListStatus | Unset = UNSET,
    owner_type: ThreadsListOwnerType | Unset = UNSET,
    assignee_id: Literal["unassigned"] | Unset | UUID = UNSET,
) -> Error | ThreadsListResponse200 | None:
    """List threads

     Filter with `identity_id`, `status`, `owner_type` and `assignee_id`. `assignee_id` takes a person’s
    id, or the literal `unassigned` for the queue nobody has picked up — it says which *human* is
    answering, where `owner_type` says which kind of thing is.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset): From a previous page’s `next_cursor`. Opaque — do not parse it.
        identity_id (UUID | Unset):
        status (ThreadsListStatus | Unset):
        owner_type (ThreadsListOwnerType | Unset):
        assignee_id (Literal['unassigned'] | Unset | UUID): A person’s id, or `unassigned` for the
            queue nobody has taken.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ThreadsListResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            cursor=cursor,
            identity_id=identity_id,
            status=status,
            owner_type=owner_type,
            assignee_id=assignee_id,
        )
    ).parsed
