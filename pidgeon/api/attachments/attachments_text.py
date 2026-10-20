from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.attachments_text_body import AttachmentsTextBody
from ...models.attachments_text_response_200 import AttachmentsTextResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    body: AttachmentsTextBody | Unset = AttachmentsTextBody.ORIGINAL,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_body: str | Unset = UNSET
    if not isinstance(body, Unset):
        json_body = body.value

    params["body"] = json_body

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/attachments/{id}/text".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AttachmentsTextResponse200:
    if response.status_code >= 400:
        raise errors.PidgeonError.from_response(response)

    if response.status_code == 200:
        response_200 = AttachmentsTextResponse200.from_dict(response.json())

        return response_200

    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AttachmentsTextResponse200]:
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
    body: AttachmentsTextBody | Unset = AttachmentsTextBody.ORIGINAL,
) -> Response[AttachmentsTextResponse200]:
    """Read a text attachment

     A CSV, a log, JSON or another text format, as text — up to 5 MB, and the first 200,000 characters of
    it. Screened by Pidgeon Firewall with the sender of the message it came with, because a file in an
    email is mail a model reads: `firewall` says whether it tries to steer you, and `body=clean` returns
    it with hidden characters removed and lines posing as a chat turn marked. HTML, PDF, Office files
    and images are refused; `GET /attachments/{id}` gives a link to those.

    Args:
        id (str):
        body (AttachmentsTextBody | Unset):  Default: AttachmentsTextBody.ORIGINAL.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AttachmentsTextResponse200]
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
    body: AttachmentsTextBody | Unset = AttachmentsTextBody.ORIGINAL,
) -> AttachmentsTextResponse200:
    """Read a text attachment

     A CSV, a log, JSON or another text format, as text — up to 5 MB, and the first 200,000 characters of
    it. Screened by Pidgeon Firewall with the sender of the message it came with, because a file in an
    email is mail a model reads: `firewall` says whether it tries to steer you, and `body=clean` returns
    it with hidden characters removed and lines posing as a chat turn marked. HTML, PDF, Office files
    and images are refused; `GET /attachments/{id}` gives a link to those.

    Args:
        id (str):
        body (AttachmentsTextBody | Unset):  Default: AttachmentsTextBody.ORIGINAL.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AttachmentsTextResponse200
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
    body: AttachmentsTextBody | Unset = AttachmentsTextBody.ORIGINAL,
) -> Response[AttachmentsTextResponse200]:
    """Read a text attachment

     A CSV, a log, JSON or another text format, as text — up to 5 MB, and the first 200,000 characters of
    it. Screened by Pidgeon Firewall with the sender of the message it came with, because a file in an
    email is mail a model reads: `firewall` says whether it tries to steer you, and `body=clean` returns
    it with hidden characters removed and lines posing as a chat turn marked. HTML, PDF, Office files
    and images are refused; `GET /attachments/{id}` gives a link to those.

    Args:
        id (str):
        body (AttachmentsTextBody | Unset):  Default: AttachmentsTextBody.ORIGINAL.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AttachmentsTextResponse200]
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
    body: AttachmentsTextBody | Unset = AttachmentsTextBody.ORIGINAL,
) -> AttachmentsTextResponse200:
    """Read a text attachment

     A CSV, a log, JSON or another text format, as text — up to 5 MB, and the first 200,000 characters of
    it. Screened by Pidgeon Firewall with the sender of the message it came with, because a file in an
    email is mail a model reads: `firewall` says whether it tries to steer you, and `body=clean` returns
    it with hidden characters removed and lines posing as a chat turn marked. HTML, PDF, Office files
    and images are refused; `GET /attachments/{id}` gives a link to those.

    Args:
        id (str):
        body (AttachmentsTextBody | Unset):  Default: AttachmentsTextBody.ORIGINAL.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AttachmentsTextResponse200
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
