from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.messages_forward_body import MessagesForwardBody
from ...models.messages_forward_response_202 import MessagesForwardResponse202
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    body: MessagesForwardBody,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/messages/{id}/forward".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MessagesForwardResponse202:
    if response.status_code >= 400:
        raise errors.PidgeonError.from_response(response)

    if response.status_code == 202:
        response_202 = MessagesForwardResponse202.from_dict(response.json())

        return response_202

    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[MessagesForwardResponse202]:
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
    body: MessagesForwardBody,
    idempotency_key: str | Unset = UNSET,
) -> Response[MessagesForwardResponse202]:
    """Forward one message

     `to` is required: a forward exists to reach somebody the original did not.

    Args:
        id (str):
        idempotency_key (str | Unset):
        body (MessagesForwardBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessagesForwardResponse202]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: MessagesForwardBody,
    idempotency_key: str | Unset = UNSET,
) -> MessagesForwardResponse202:
    """Forward one message

     `to` is required: a forward exists to reach somebody the original did not.

    Args:
        id (str):
        idempotency_key (str | Unset):
        body (MessagesForwardBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessagesForwardResponse202
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: MessagesForwardBody,
    idempotency_key: str | Unset = UNSET,
) -> Response[MessagesForwardResponse202]:
    """Forward one message

     `to` is required: a forward exists to reach somebody the original did not.

    Args:
        id (str):
        idempotency_key (str | Unset):
        body (MessagesForwardBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessagesForwardResponse202]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: MessagesForwardBody,
    idempotency_key: str | Unset = UNSET,
) -> MessagesForwardResponse202:
    """Forward one message

     `to` is required: a forward exists to reach somebody the original did not.

    Args:
        id (str):
        idempotency_key (str | Unset):
        body (MessagesForwardBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessagesForwardResponse202
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
