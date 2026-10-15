from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.drafts_list_response_200 import DraftsListResponse200
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    identity_id: UUID,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_identity_id = str(identity_id)
    params["identity_id"] = json_identity_id

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/drafts",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DraftsListResponse200 | Error | None:
    if response.status_code == 200:
        response_200 = DraftsListResponse200.from_dict(response.json())

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
) -> Response[DraftsListResponse200 | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    identity_id: UUID,
    limit: int | Unset = UNSET,
) -> Response[DraftsListResponse200 | Error]:
    """Every draft in one mailbox

     Newest first, and including scheduled ones — a scheduled message is a draft with `send_at` set. `GET
    /mailboxes/drafts` lists the same rows as a mail client draws them: sender, subject, preview. This
    gives the recipients and the body, because a caller here is coming back to finish writing.

    Args:
        identity_id (UUID):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DraftsListResponse200 | Error]
    """

    kwargs = _get_kwargs(
        identity_id=identity_id,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    identity_id: UUID,
    limit: int | Unset = UNSET,
) -> DraftsListResponse200 | Error | None:
    """Every draft in one mailbox

     Newest first, and including scheduled ones — a scheduled message is a draft with `send_at` set. `GET
    /mailboxes/drafts` lists the same rows as a mail client draws them: sender, subject, preview. This
    gives the recipients and the body, because a caller here is coming back to finish writing.

    Args:
        identity_id (UUID):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DraftsListResponse200 | Error
    """

    return sync_detailed(
        client=client,
        identity_id=identity_id,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    identity_id: UUID,
    limit: int | Unset = UNSET,
) -> Response[DraftsListResponse200 | Error]:
    """Every draft in one mailbox

     Newest first, and including scheduled ones — a scheduled message is a draft with `send_at` set. `GET
    /mailboxes/drafts` lists the same rows as a mail client draws them: sender, subject, preview. This
    gives the recipients and the body, because a caller here is coming back to finish writing.

    Args:
        identity_id (UUID):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DraftsListResponse200 | Error]
    """

    kwargs = _get_kwargs(
        identity_id=identity_id,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    identity_id: UUID,
    limit: int | Unset = UNSET,
) -> DraftsListResponse200 | Error | None:
    """Every draft in one mailbox

     Newest first, and including scheduled ones — a scheduled message is a draft with `send_at` set. `GET
    /mailboxes/drafts` lists the same rows as a mail client draws them: sender, subject, preview. This
    gives the recipients and the body, because a caller here is coming back to finish writing.

    Args:
        identity_id (UUID):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DraftsListResponse200 | Error
    """

    return (
        await asyncio_detailed(
            client=client,
            identity_id=identity_id,
            limit=limit,
        )
    ).parsed
