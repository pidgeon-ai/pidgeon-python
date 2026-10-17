import datetime
from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.messages_await_has_code import MessagesAwaitHasCode
from ...models.messages_await_response_200 import MessagesAwaitResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    identity_id: UUID,
    from_: str | Unset = UNSET,
    subject_contains: str | Unset = UNSET,
    has_code: MessagesAwaitHasCode | Unset = UNSET,
    after: datetime.datetime | Unset = UNSET,
    timeout: int | Unset = 60,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_identity_id = str(identity_id)
    params["identity_id"] = json_identity_id

    params["from"] = from_

    params["subject_contains"] = subject_contains

    json_has_code: str | Unset = UNSET
    if not isinstance(has_code, Unset):
        json_has_code = has_code.value

    params["has_code"] = json_has_code

    json_after: str | Unset = UNSET
    if not isinstance(after, Unset):
        json_after = after.isoformat()
    params["after"] = json_after

    params["timeout"] = timeout

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/messages/await",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | MessagesAwaitResponse200 | None:
    if response.status_code == 200:
        response_200 = MessagesAwaitResponse200.from_dict(response.json())

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
) -> Response[Error | MessagesAwaitResponse200]:
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
    from_: str | Unset = UNSET,
    subject_contains: str | Unset = UNSET,
    has_code: MessagesAwaitHasCode | Unset = UNSET,
    after: datetime.datetime | Unset = UNSET,
    timeout: int | Unset = 60,
) -> Response[Error | MessagesAwaitResponse200]:
    """Wait for the next message

     Holds the request open until a message matching the filters arrives at the address, or `timeout`
    seconds pass — one call where you would otherwise poll. The message carries `extracted`:
    verification codes and links, most likely first. Pass the returned `cursor` as `after` on the next
    call so nothing arriving between calls is missed. Answers 200 with `message: null` and `timed_out:
    true` when nothing came.

    Args:
        identity_id (UUID):
        from_ (str | Unset):
        subject_contains (str | Unset):
        has_code (MessagesAwaitHasCode | Unset):
        after (datetime.datetime | Unset):
        timeout (int | Unset):  Default: 60.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | MessagesAwaitResponse200]
    """

    kwargs = _get_kwargs(
        identity_id=identity_id,
        from_=from_,
        subject_contains=subject_contains,
        has_code=has_code,
        after=after,
        timeout=timeout,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    identity_id: UUID,
    from_: str | Unset = UNSET,
    subject_contains: str | Unset = UNSET,
    has_code: MessagesAwaitHasCode | Unset = UNSET,
    after: datetime.datetime | Unset = UNSET,
    timeout: int | Unset = 60,
) -> Error | MessagesAwaitResponse200 | None:
    """Wait for the next message

     Holds the request open until a message matching the filters arrives at the address, or `timeout`
    seconds pass — one call where you would otherwise poll. The message carries `extracted`:
    verification codes and links, most likely first. Pass the returned `cursor` as `after` on the next
    call so nothing arriving between calls is missed. Answers 200 with `message: null` and `timed_out:
    true` when nothing came.

    Args:
        identity_id (UUID):
        from_ (str | Unset):
        subject_contains (str | Unset):
        has_code (MessagesAwaitHasCode | Unset):
        after (datetime.datetime | Unset):
        timeout (int | Unset):  Default: 60.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | MessagesAwaitResponse200
    """

    return sync_detailed(
        client=client,
        identity_id=identity_id,
        from_=from_,
        subject_contains=subject_contains,
        has_code=has_code,
        after=after,
        timeout=timeout,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    identity_id: UUID,
    from_: str | Unset = UNSET,
    subject_contains: str | Unset = UNSET,
    has_code: MessagesAwaitHasCode | Unset = UNSET,
    after: datetime.datetime | Unset = UNSET,
    timeout: int | Unset = 60,
) -> Response[Error | MessagesAwaitResponse200]:
    """Wait for the next message

     Holds the request open until a message matching the filters arrives at the address, or `timeout`
    seconds pass — one call where you would otherwise poll. The message carries `extracted`:
    verification codes and links, most likely first. Pass the returned `cursor` as `after` on the next
    call so nothing arriving between calls is missed. Answers 200 with `message: null` and `timed_out:
    true` when nothing came.

    Args:
        identity_id (UUID):
        from_ (str | Unset):
        subject_contains (str | Unset):
        has_code (MessagesAwaitHasCode | Unset):
        after (datetime.datetime | Unset):
        timeout (int | Unset):  Default: 60.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | MessagesAwaitResponse200]
    """

    kwargs = _get_kwargs(
        identity_id=identity_id,
        from_=from_,
        subject_contains=subject_contains,
        has_code=has_code,
        after=after,
        timeout=timeout,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    identity_id: UUID,
    from_: str | Unset = UNSET,
    subject_contains: str | Unset = UNSET,
    has_code: MessagesAwaitHasCode | Unset = UNSET,
    after: datetime.datetime | Unset = UNSET,
    timeout: int | Unset = 60,
) -> Error | MessagesAwaitResponse200 | None:
    """Wait for the next message

     Holds the request open until a message matching the filters arrives at the address, or `timeout`
    seconds pass — one call where you would otherwise poll. The message carries `extracted`:
    verification codes and links, most likely first. Pass the returned `cursor` as `after` on the next
    call so nothing arriving between calls is missed. Answers 200 with `message: null` and `timed_out:
    true` when nothing came.

    Args:
        identity_id (UUID):
        from_ (str | Unset):
        subject_contains (str | Unset):
        has_code (MessagesAwaitHasCode | Unset):
        after (datetime.datetime | Unset):
        timeout (int | Unset):  Default: 60.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | MessagesAwaitResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            identity_id=identity_id,
            from_=from_,
            subject_contains=subject_contains,
            has_code=has_code,
            after=after,
            timeout=timeout,
        )
    ).parsed
