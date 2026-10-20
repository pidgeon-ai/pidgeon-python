from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.messages_list_in_thread_body import MessagesListInThreadBody
from ...models.messages_list_in_thread_response_200 import MessagesListInThreadResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    thread_id: UUID,
    body: MessagesListInThreadBody | Unset = MessagesListInThreadBody.ORIGINAL,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["cursor"] = cursor

    json_thread_id = str(thread_id)
    params["thread_id"] = json_thread_id

    json_body: str | Unset = UNSET
    if not isinstance(body, Unset):
        json_body = body.value

    params["body"] = json_body

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/messages",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> MessagesListInThreadResponse200:
    if response.status_code >= 400:
        raise errors.PidgeonError.from_response(response)

    if response.status_code == 200:
        response_200 = MessagesListInThreadResponse200.from_dict(response.json())

        return response_200

    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[MessagesListInThreadResponse200]:
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
    thread_id: UUID,
    body: MessagesListInThreadBody | Unset = MessagesListInThreadBody.ORIGINAL,
) -> Response[MessagesListInThreadResponse200]:
    """List messages

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset): From a previous page’s `next_cursor`. Opaque — do not parse it.
        thread_id (UUID):
        body (MessagesListInThreadBody | Unset):  Default: MessagesListInThreadBody.ORIGINAL.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessagesListInThreadResponse200]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
        thread_id=thread_id,
        body=body,
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
    thread_id: UUID,
    body: MessagesListInThreadBody | Unset = MessagesListInThreadBody.ORIGINAL,
) -> MessagesListInThreadResponse200:
    """List messages

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset): From a previous page’s `next_cursor`. Opaque — do not parse it.
        thread_id (UUID):
        body (MessagesListInThreadBody | Unset):  Default: MessagesListInThreadBody.ORIGINAL.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessagesListInThreadResponse200
    """

    return sync_detailed(
        client=client,
        limit=limit,
        cursor=cursor,
        thread_id=thread_id,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    thread_id: UUID,
    body: MessagesListInThreadBody | Unset = MessagesListInThreadBody.ORIGINAL,
) -> Response[MessagesListInThreadResponse200]:
    """List messages

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset): From a previous page’s `next_cursor`. Opaque — do not parse it.
        thread_id (UUID):
        body (MessagesListInThreadBody | Unset):  Default: MessagesListInThreadBody.ORIGINAL.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessagesListInThreadResponse200]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
        thread_id=thread_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    thread_id: UUID,
    body: MessagesListInThreadBody | Unset = MessagesListInThreadBody.ORIGINAL,
) -> MessagesListInThreadResponse200:
    """List messages

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset): From a previous page’s `next_cursor`. Opaque — do not parse it.
        thread_id (UUID):
        body (MessagesListInThreadBody | Unset):  Default: MessagesListInThreadBody.ORIGINAL.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessagesListInThreadResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            cursor=cursor,
            thread_id=thread_id,
            body=body,
        )
    ).parsed
