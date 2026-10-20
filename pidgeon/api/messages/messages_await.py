import datetime
from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.messages_await_body import MessagesAwaitBody
from ...models.messages_await_has_code import MessagesAwaitHasCode
from ...models.messages_await_include_spam import MessagesAwaitIncludeSpam
from ...models.messages_await_response_200 import MessagesAwaitResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    identity_id: UUID,
    body: MessagesAwaitBody | Unset = MessagesAwaitBody.ORIGINAL,
    from_: str | Unset = UNSET,
    subject_contains: str | Unset = UNSET,
    has_code: MessagesAwaitHasCode | Unset = UNSET,
    include_spam: MessagesAwaitIncludeSpam | Unset = UNSET,
    after: datetime.datetime | Unset = UNSET,
    timeout: int | Unset = 60,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_identity_id = str(identity_id)
    params["identity_id"] = json_identity_id

    json_body: str | Unset = UNSET
    if not isinstance(body, Unset):
        json_body = body.value

    params["body"] = json_body

    params["from"] = from_

    params["subject_contains"] = subject_contains

    json_has_code: str | Unset = UNSET
    if not isinstance(has_code, Unset):
        json_has_code = has_code.value

    params["has_code"] = json_has_code

    json_include_spam: str | Unset = UNSET
    if not isinstance(include_spam, Unset):
        json_include_spam = include_spam.value

    params["include_spam"] = json_include_spam

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


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MessagesAwaitResponse200:
    if response.status_code >= 400:
        raise errors.PidgeonError.from_response(response)

    if response.status_code == 200:
        response_200 = MessagesAwaitResponse200.from_dict(response.json())

        return response_200

    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[MessagesAwaitResponse200]:
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
    body: MessagesAwaitBody | Unset = MessagesAwaitBody.ORIGINAL,
    from_: str | Unset = UNSET,
    subject_contains: str | Unset = UNSET,
    has_code: MessagesAwaitHasCode | Unset = UNSET,
    include_spam: MessagesAwaitIncludeSpam | Unset = UNSET,
    after: datetime.datetime | Unset = UNSET,
    timeout: int | Unset = 60,
) -> Response[MessagesAwaitResponse200]:
    """Wait for the next message

     Holds the request open until a message matching the filters arrives at the address, or `timeout`
    seconds pass — one call where you would otherwise poll. The message carries `extracted`:
    verification codes and links, most likely first. Pass the returned `cursor` as `after` on the next
    call so nothing arriving between calls is missed. Answers 200 with `message: null` and `timed_out:
    true` when nothing came. A matching message filed as spam is not returned unless you pass
    `include_spam=true`; it is counted in `held_back`, with its id, so a timeout never hides mail that
    arrived.

    Args:
        identity_id (UUID):
        body (MessagesAwaitBody | Unset):  Default: MessagesAwaitBody.ORIGINAL.
        from_ (str | Unset):
        subject_contains (str | Unset):
        has_code (MessagesAwaitHasCode | Unset):
        include_spam (MessagesAwaitIncludeSpam | Unset): Also return a matching message filed as
            spam. Without it, one is counted in `held_back` instead, with its id.
        after (datetime.datetime | Unset):
        timeout (int | Unset):  Default: 60.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessagesAwaitResponse200]
    """

    kwargs = _get_kwargs(
        identity_id=identity_id,
        body=body,
        from_=from_,
        subject_contains=subject_contains,
        has_code=has_code,
        include_spam=include_spam,
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
    body: MessagesAwaitBody | Unset = MessagesAwaitBody.ORIGINAL,
    from_: str | Unset = UNSET,
    subject_contains: str | Unset = UNSET,
    has_code: MessagesAwaitHasCode | Unset = UNSET,
    include_spam: MessagesAwaitIncludeSpam | Unset = UNSET,
    after: datetime.datetime | Unset = UNSET,
    timeout: int | Unset = 60,
) -> MessagesAwaitResponse200:
    """Wait for the next message

     Holds the request open until a message matching the filters arrives at the address, or `timeout`
    seconds pass — one call where you would otherwise poll. The message carries `extracted`:
    verification codes and links, most likely first. Pass the returned `cursor` as `after` on the next
    call so nothing arriving between calls is missed. Answers 200 with `message: null` and `timed_out:
    true` when nothing came. A matching message filed as spam is not returned unless you pass
    `include_spam=true`; it is counted in `held_back`, with its id, so a timeout never hides mail that
    arrived.

    Args:
        identity_id (UUID):
        body (MessagesAwaitBody | Unset):  Default: MessagesAwaitBody.ORIGINAL.
        from_ (str | Unset):
        subject_contains (str | Unset):
        has_code (MessagesAwaitHasCode | Unset):
        include_spam (MessagesAwaitIncludeSpam | Unset): Also return a matching message filed as
            spam. Without it, one is counted in `held_back` instead, with its id.
        after (datetime.datetime | Unset):
        timeout (int | Unset):  Default: 60.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessagesAwaitResponse200
    """

    return sync_detailed(
        client=client,
        identity_id=identity_id,
        body=body,
        from_=from_,
        subject_contains=subject_contains,
        has_code=has_code,
        include_spam=include_spam,
        after=after,
        timeout=timeout,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    identity_id: UUID,
    body: MessagesAwaitBody | Unset = MessagesAwaitBody.ORIGINAL,
    from_: str | Unset = UNSET,
    subject_contains: str | Unset = UNSET,
    has_code: MessagesAwaitHasCode | Unset = UNSET,
    include_spam: MessagesAwaitIncludeSpam | Unset = UNSET,
    after: datetime.datetime | Unset = UNSET,
    timeout: int | Unset = 60,
) -> Response[MessagesAwaitResponse200]:
    """Wait for the next message

     Holds the request open until a message matching the filters arrives at the address, or `timeout`
    seconds pass — one call where you would otherwise poll. The message carries `extracted`:
    verification codes and links, most likely first. Pass the returned `cursor` as `after` on the next
    call so nothing arriving between calls is missed. Answers 200 with `message: null` and `timed_out:
    true` when nothing came. A matching message filed as spam is not returned unless you pass
    `include_spam=true`; it is counted in `held_back`, with its id, so a timeout never hides mail that
    arrived.

    Args:
        identity_id (UUID):
        body (MessagesAwaitBody | Unset):  Default: MessagesAwaitBody.ORIGINAL.
        from_ (str | Unset):
        subject_contains (str | Unset):
        has_code (MessagesAwaitHasCode | Unset):
        include_spam (MessagesAwaitIncludeSpam | Unset): Also return a matching message filed as
            spam. Without it, one is counted in `held_back` instead, with its id.
        after (datetime.datetime | Unset):
        timeout (int | Unset):  Default: 60.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessagesAwaitResponse200]
    """

    kwargs = _get_kwargs(
        identity_id=identity_id,
        body=body,
        from_=from_,
        subject_contains=subject_contains,
        has_code=has_code,
        include_spam=include_spam,
        after=after,
        timeout=timeout,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    identity_id: UUID,
    body: MessagesAwaitBody | Unset = MessagesAwaitBody.ORIGINAL,
    from_: str | Unset = UNSET,
    subject_contains: str | Unset = UNSET,
    has_code: MessagesAwaitHasCode | Unset = UNSET,
    include_spam: MessagesAwaitIncludeSpam | Unset = UNSET,
    after: datetime.datetime | Unset = UNSET,
    timeout: int | Unset = 60,
) -> MessagesAwaitResponse200:
    """Wait for the next message

     Holds the request open until a message matching the filters arrives at the address, or `timeout`
    seconds pass — one call where you would otherwise poll. The message carries `extracted`:
    verification codes and links, most likely first. Pass the returned `cursor` as `after` on the next
    call so nothing arriving between calls is missed. Answers 200 with `message: null` and `timed_out:
    true` when nothing came. A matching message filed as spam is not returned unless you pass
    `include_spam=true`; it is counted in `held_back`, with its id, so a timeout never hides mail that
    arrived.

    Args:
        identity_id (UUID):
        body (MessagesAwaitBody | Unset):  Default: MessagesAwaitBody.ORIGINAL.
        from_ (str | Unset):
        subject_contains (str | Unset):
        has_code (MessagesAwaitHasCode | Unset):
        include_spam (MessagesAwaitIncludeSpam | Unset): Also return a matching message filed as
            spam. Without it, one is counted in `held_back` instead, with its id.
        after (datetime.datetime | Unset):
        timeout (int | Unset):  Default: 60.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessagesAwaitResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            identity_id=identity_id,
            body=body,
            from_=from_,
            subject_contains=subject_contains,
            has_code=has_code,
            include_spam=include_spam,
            after=after,
            timeout=timeout,
        )
    ).parsed
