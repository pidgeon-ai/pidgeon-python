from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.drafts_list_response_200 import DraftsListResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    identity_id: UUID,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_identity_id = str(identity_id)
    params["identity_id"] = json_identity_id

    params["limit"] = limit

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/drafts",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DraftsListResponse200:
    if response.status_code >= 400:
        raise errors.PidgeonError.from_response(response)

    if response.status_code == 200:
        response_200 = DraftsListResponse200.from_dict(response.json())

        return response_200

    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DraftsListResponse200]:
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
    cursor: str | Unset = UNSET,
) -> Response[DraftsListResponse200]:
    """Every draft in one mailbox

     Newest first, and including scheduled ones — a scheduled message is a draft with `send_at` set. `GET
    /mailboxes/drafts` lists the same rows as a mail client draws them: sender, subject, preview. This
    gives the recipients and the body, because a caller here is coming back to finish writing.

    Args:
        identity_id (UUID):
        limit (int | Unset):
        cursor (str | Unset): From a previous page’s `next_cursor`. Opaque — do not parse it.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DraftsListResponse200]
    """

    kwargs = _get_kwargs(
        identity_id=identity_id,
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
    identity_id: UUID,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> DraftsListResponse200:
    """Every draft in one mailbox

     Newest first, and including scheduled ones — a scheduled message is a draft with `send_at` set. `GET
    /mailboxes/drafts` lists the same rows as a mail client draws them: sender, subject, preview. This
    gives the recipients and the body, because a caller here is coming back to finish writing.

    Args:
        identity_id (UUID):
        limit (int | Unset):
        cursor (str | Unset): From a previous page’s `next_cursor`. Opaque — do not parse it.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DraftsListResponse200
    """

    return sync_detailed(
        client=client,
        identity_id=identity_id,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    identity_id: UUID,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> Response[DraftsListResponse200]:
    """Every draft in one mailbox

     Newest first, and including scheduled ones — a scheduled message is a draft with `send_at` set. `GET
    /mailboxes/drafts` lists the same rows as a mail client draws them: sender, subject, preview. This
    gives the recipients and the body, because a caller here is coming back to finish writing.

    Args:
        identity_id (UUID):
        limit (int | Unset):
        cursor (str | Unset): From a previous page’s `next_cursor`. Opaque — do not parse it.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DraftsListResponse200]
    """

    kwargs = _get_kwargs(
        identity_id=identity_id,
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    identity_id: UUID,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> DraftsListResponse200:
    """Every draft in one mailbox

     Newest first, and including scheduled ones — a scheduled message is a draft with `send_at` set. `GET
    /mailboxes/drafts` lists the same rows as a mail client draws them: sender, subject, preview. This
    gives the recipients and the body, because a caller here is coming back to finish writing.

    Args:
        identity_id (UUID):
        limit (int | Unset):
        cursor (str | Unset): From a previous page’s `next_cursor`. Opaque — do not parse it.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DraftsListResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            identity_id=identity_id,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
