from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.messages_raw_headers import MessagesRawHeaders
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    headers: MessagesRawHeaders | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_headers: str | Unset = UNSET
    if not isinstance(headers, Unset):
        json_headers = headers.value

    params["headers"] = json_headers

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/messages/{id}/raw".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any:
    if response.status_code >= 400:
        raise errors.PidgeonError.from_response(response)

    return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any]:
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
    headers: MessagesRawHeaders | Unset = UNSET,
) -> Response[Any]:
    """The message as MIME

     `message/rfc822`, not JSON. An API key gets the message rebuilt from the stored message, with a
    canary token in its text (/docs/firewall): the original bytes cannot carry one, so `X-Pidgeon-
    Reconstructed` is `true` and a rebuild cannot verify DKIM. The message’s `authentication` is our
    check of the original’s signatures. `headers=original` returns only the original’s header section,
    for any caller: the signed agent declaration, checkable as /verify checks it, with no body to stamp.

    Args:
        id (str):
        headers (MessagesRawHeaders | Unset): original: only the header section of the message as
            it arrived, with no body, so its DKIM signatures (the agent declaration’s among them) can
            be checked, as /verify does. 404 when the original is no longer kept.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        headers=headers,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    headers: MessagesRawHeaders | Unset = UNSET,
) -> Response[Any]:
    """The message as MIME

     `message/rfc822`, not JSON. An API key gets the message rebuilt from the stored message, with a
    canary token in its text (/docs/firewall): the original bytes cannot carry one, so `X-Pidgeon-
    Reconstructed` is `true` and a rebuild cannot verify DKIM. The message’s `authentication` is our
    check of the original’s signatures. `headers=original` returns only the original’s header section,
    for any caller: the signed agent declaration, checkable as /verify checks it, with no body to stamp.

    Args:
        id (str):
        headers (MessagesRawHeaders | Unset): original: only the header section of the message as
            it arrived, with no body, so its DKIM signatures (the agent declaration’s among them) can
            be checked, as /verify does. 404 when the original is no longer kept.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        headers=headers,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
