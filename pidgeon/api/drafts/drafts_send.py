from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.drafts_send_response_202 import DraftsSendResponse202
from ...types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/drafts/{id}/send".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DraftsSendResponse202:
    if response.status_code >= 400:
        raise errors.PidgeonError.from_response(response)

    if response.status_code == 202:
        response_202 = DraftsSendResponse202.from_dict(response.json())

        return response_202

    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DraftsSendResponse202]:
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
) -> Response[DraftsSendResponse202]:
    """Send what is stored

     No body: the row is the message. The browser passes the composer contents and the draft id together,
    because the composer *is* the draft; a caller here saved it an hour ago and may be a different
    process. `PATCH` first to change anything. The id that comes back is the draft's, because a send
    converts the row.

    Args:
        id (str):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DraftsSendResponse202]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> DraftsSendResponse202:
    """Send what is stored

     No body: the row is the message. The browser passes the composer contents and the draft id together,
    because the composer *is* the draft; a caller here saved it an hour ago and may be a different
    process. `PATCH` first to change anything. The id that comes back is the draft's, because a send
    converts the row.

    Args:
        id (str):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DraftsSendResponse202
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DraftsSendResponse202]:
    """Send what is stored

     No body: the row is the message. The browser passes the composer contents and the draft id together,
    because the composer *is* the draft; a caller here saved it an hour ago and may be a different
    process. `PATCH` first to change anything. The id that comes back is the draft's, because a send
    converts the row.

    Args:
        id (str):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DraftsSendResponse202]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> DraftsSendResponse202:
    """Send what is stored

     No body: the row is the message. The browser passes the composer contents and the draft id together,
    because the composer *is* the draft; a caller here saved it an hour ago and may be a different
    process. `PATCH` first to change anything. The id that comes back is the draft's, because a send
    converts the row.

    Args:
        id (str):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DraftsSendResponse202
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
