from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.webhooks_update_headers_body import WebhooksUpdateHeadersBody
from ...models.webhooks_update_headers_response_200 import WebhooksUpdateHeadersResponse200
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: WebhooksUpdateHeadersBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/webhooks/{id}/headers".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> WebhooksUpdateHeadersResponse200:
    if response.status_code >= 400:
        raise errors.PidgeonError.from_response(response)

    if response.status_code == 200:
        response_200 = WebhooksUpdateHeadersResponse200.from_dict(response.json())

        return response_200

    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[WebhooksUpdateHeadersResponse200]:
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
    body: WebhooksUpdateHeadersBody,
) -> Response[WebhooksUpdateHeadersResponse200]:
    """Replace the headers this endpoint carries

     We sign every delivery, and a signature answers *is this from Pidgeon*. It does not answer the
    question a gateway asks, which is *does this request carry the token we issued*. PUT, not PATCH:
    what you send is what the endpoint has afterwards, and `{}` clears them — a merge could not remove
    one, and removing one is what rotating a token is. The headers we set ourselves are refused by name.

    Args:
        id (str):
        body (WebhooksUpdateHeadersBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebhooksUpdateHeadersResponse200]
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
    body: WebhooksUpdateHeadersBody,
) -> WebhooksUpdateHeadersResponse200:
    """Replace the headers this endpoint carries

     We sign every delivery, and a signature answers *is this from Pidgeon*. It does not answer the
    question a gateway asks, which is *does this request carry the token we issued*. PUT, not PATCH:
    what you send is what the endpoint has afterwards, and `{}` clears them — a merge could not remove
    one, and removing one is what rotating a token is. The headers we set ourselves are refused by name.

    Args:
        id (str):
        body (WebhooksUpdateHeadersBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebhooksUpdateHeadersResponse200
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
    body: WebhooksUpdateHeadersBody,
) -> Response[WebhooksUpdateHeadersResponse200]:
    """Replace the headers this endpoint carries

     We sign every delivery, and a signature answers *is this from Pidgeon*. It does not answer the
    question a gateway asks, which is *does this request carry the token we issued*. PUT, not PATCH:
    what you send is what the endpoint has afterwards, and `{}` clears them — a merge could not remove
    one, and removing one is what rotating a token is. The headers we set ourselves are refused by name.

    Args:
        id (str):
        body (WebhooksUpdateHeadersBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebhooksUpdateHeadersResponse200]
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
    body: WebhooksUpdateHeadersBody,
) -> WebhooksUpdateHeadersResponse200:
    """Replace the headers this endpoint carries

     We sign every delivery, and a signature answers *is this from Pidgeon*. It does not answer the
    question a gateway asks, which is *does this request carry the token we issued*. PUT, not PATCH:
    what you send is what the endpoint has afterwards, and `{}` clears them — a merge could not remove
    one, and removing one is what rotating a token is. The headers we set ourselves are refused by name.

    Args:
        id (str):
        body (WebhooksUpdateHeadersBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebhooksUpdateHeadersResponse200
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
