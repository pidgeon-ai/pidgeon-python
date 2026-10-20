from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.messages_reply_all_body import MessagesReplyAllBody
from ...models.messages_reply_all_response_202 import MessagesReplyAllResponse202
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: MessagesReplyAllBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/messages/{id}/reply-all".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MessagesReplyAllResponse202:
    if response.status_code >= 400:
        raise errors.PidgeonError.from_response(response)

    if response.status_code == 202:
        response_202 = MessagesReplyAllResponse202.from_dict(response.json())

        return response_202

    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[MessagesReplyAllResponse202]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: MessagesReplyAllBody,
) -> Response[MessagesReplyAllResponse202]:
    """Reply to everybody on one message

     Every address on the message except the ones that reach this mailbox — which a caller cannot work
    out, because it needs the routing table.

    Args:
        id (str):
        body (MessagesReplyAllBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessagesReplyAllResponse202]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: MessagesReplyAllBody,
) -> MessagesReplyAllResponse202:
    """Reply to everybody on one message

     Every address on the message except the ones that reach this mailbox — which a caller cannot work
    out, because it needs the routing table.

    Args:
        id (str):
        body (MessagesReplyAllBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessagesReplyAllResponse202
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: MessagesReplyAllBody,
) -> Response[MessagesReplyAllResponse202]:
    """Reply to everybody on one message

     Every address on the message except the ones that reach this mailbox — which a caller cannot work
    out, because it needs the routing table.

    Args:
        id (str):
        body (MessagesReplyAllBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessagesReplyAllResponse202]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: MessagesReplyAllBody,
) -> MessagesReplyAllResponse202:
    """Reply to everybody on one message

     Every address on the message except the ones that reach this mailbox — which a caller cannot work
    out, because it needs the routing table.

    Args:
        id (str):
        body (MessagesReplyAllBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessagesReplyAllResponse202
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
