from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.messages_search_in import MessagesSearchIn
from ...models.messages_search_response_200 import MessagesSearchResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    identity_id: UUID | Unset = UNSET,
    q: str | Unset = UNSET,
    in_: MessagesSearchIn | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    has_attachment: str | Unset = UNSET,
    is_unread: str | Unset = UNSET,
    is_starred: str | Unset = UNSET,
    label_id: UUID | Unset = UNSET,
    limit: int | Unset = 50,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_identity_id: str | Unset = UNSET
    if not isinstance(identity_id, Unset):
        json_identity_id = str(identity_id)
    params["identity_id"] = json_identity_id

    params["q"] = q

    json_in_: str | Unset = UNSET
    if not isinstance(in_, Unset):
        json_in_ = in_.value

    params["in"] = json_in_

    params["from"] = from_

    params["to"] = to

    params["has_attachment"] = has_attachment

    params["is_unread"] = is_unread

    params["is_starred"] = is_starred

    json_label_id: str | Unset = UNSET
    if not isinstance(label_id, Unset):
        json_label_id = str(label_id)
    params["label_id"] = json_label_id

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/messages/search",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | MessagesSearchResponse200 | None:
    if response.status_code == 200:
        response_200 = MessagesSearchResponse200.from_dict(response.json())

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
) -> Response[Error | MessagesSearchResponse200]:
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
    q: str | Unset = UNSET,
    in_: MessagesSearchIn | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    has_attachment: str | Unset = UNSET,
    is_unread: str | Unset = UNSET,
    is_starred: str | Unset = UNSET,
    label_id: UUID | Unset = UNSET,
    limit: int | Unset = 50,
) -> Response[Error | MessagesSearchResponse200]:
    """Search one mailbox

     Full-text, ranked by relevance, one mailbox at a time. Results carry the folder they were found in.
    Not paged: page two of a relevance ranking is a place nobody goes, so narrow the query instead.

    Args:
        identity_id (UUID | Unset):
        q (str | Unset):
        in_ (MessagesSearchIn | Unset):
        from_ (str | Unset):
        to (str | Unset):
        has_attachment (str | Unset):
        is_unread (str | Unset):
        is_starred (str | Unset):
        label_id (UUID | Unset):
        limit (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | MessagesSearchResponse200]
    """

    kwargs = _get_kwargs(
        identity_id=identity_id,
        q=q,
        in_=in_,
        from_=from_,
        to=to,
        has_attachment=has_attachment,
        is_unread=is_unread,
        is_starred=is_starred,
        label_id=label_id,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    identity_id: UUID | Unset = UNSET,
    q: str | Unset = UNSET,
    in_: MessagesSearchIn | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    has_attachment: str | Unset = UNSET,
    is_unread: str | Unset = UNSET,
    is_starred: str | Unset = UNSET,
    label_id: UUID | Unset = UNSET,
    limit: int | Unset = 50,
) -> Error | MessagesSearchResponse200 | None:
    """Search one mailbox

     Full-text, ranked by relevance, one mailbox at a time. Results carry the folder they were found in.
    Not paged: page two of a relevance ranking is a place nobody goes, so narrow the query instead.

    Args:
        identity_id (UUID | Unset):
        q (str | Unset):
        in_ (MessagesSearchIn | Unset):
        from_ (str | Unset):
        to (str | Unset):
        has_attachment (str | Unset):
        is_unread (str | Unset):
        is_starred (str | Unset):
        label_id (UUID | Unset):
        limit (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | MessagesSearchResponse200
    """

    return sync_detailed(
        client=client,
        identity_id=identity_id,
        q=q,
        in_=in_,
        from_=from_,
        to=to,
        has_attachment=has_attachment,
        is_unread=is_unread,
        is_starred=is_starred,
        label_id=label_id,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    identity_id: UUID | Unset = UNSET,
    q: str | Unset = UNSET,
    in_: MessagesSearchIn | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    has_attachment: str | Unset = UNSET,
    is_unread: str | Unset = UNSET,
    is_starred: str | Unset = UNSET,
    label_id: UUID | Unset = UNSET,
    limit: int | Unset = 50,
) -> Response[Error | MessagesSearchResponse200]:
    """Search one mailbox

     Full-text, ranked by relevance, one mailbox at a time. Results carry the folder they were found in.
    Not paged: page two of a relevance ranking is a place nobody goes, so narrow the query instead.

    Args:
        identity_id (UUID | Unset):
        q (str | Unset):
        in_ (MessagesSearchIn | Unset):
        from_ (str | Unset):
        to (str | Unset):
        has_attachment (str | Unset):
        is_unread (str | Unset):
        is_starred (str | Unset):
        label_id (UUID | Unset):
        limit (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | MessagesSearchResponse200]
    """

    kwargs = _get_kwargs(
        identity_id=identity_id,
        q=q,
        in_=in_,
        from_=from_,
        to=to,
        has_attachment=has_attachment,
        is_unread=is_unread,
        is_starred=is_starred,
        label_id=label_id,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    identity_id: UUID | Unset = UNSET,
    q: str | Unset = UNSET,
    in_: MessagesSearchIn | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    has_attachment: str | Unset = UNSET,
    is_unread: str | Unset = UNSET,
    is_starred: str | Unset = UNSET,
    label_id: UUID | Unset = UNSET,
    limit: int | Unset = 50,
) -> Error | MessagesSearchResponse200 | None:
    """Search one mailbox

     Full-text, ranked by relevance, one mailbox at a time. Results carry the folder they were found in.
    Not paged: page two of a relevance ranking is a place nobody goes, so narrow the query instead.

    Args:
        identity_id (UUID | Unset):
        q (str | Unset):
        in_ (MessagesSearchIn | Unset):
        from_ (str | Unset):
        to (str | Unset):
        has_attachment (str | Unset):
        is_unread (str | Unset):
        is_starred (str | Unset):
        label_id (UUID | Unset):
        limit (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | MessagesSearchResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            identity_id=identity_id,
            q=q,
            in_=in_,
            from_=from_,
            to=to,
            has_attachment=has_attachment,
            is_unread=is_unread,
            is_starred=is_starred,
            label_id=label_id,
            limit=limit,
        )
    ).parsed
