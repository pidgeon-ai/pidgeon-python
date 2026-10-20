from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.attachments_upload_body import AttachmentsUploadBody
from ...models.attachments_upload_response_201 import AttachmentsUploadResponse201
from ...types import Response


def _get_kwargs(
    *,
    body: AttachmentsUploadBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/attachments",
    }

    _kwargs["files"] = body.to_multipart()

    headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AttachmentsUploadResponse201:
    if response.status_code >= 400:
        raise errors.PidgeonError.from_response(response)

    if response.status_code == 201:
        response_201 = AttachmentsUploadResponse201.from_dict(response.json())

        return response_201

    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AttachmentsUploadResponse201]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AttachmentsUploadBody,
) -> Response[AttachmentsUploadResponse201]:
    """Upload a file to send

     Multipart, with `identity_id` and `file` parts — not base64 in JSON, because a ten-megabyte PDF is
    thirteen megabytes of base64 and every proxy in between would have to be told. Name the returned id
    in `attachment_ids` on a send. An upload expires in a day: it is a file no message refers to yet.

    Args:
        body (AttachmentsUploadBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AttachmentsUploadResponse201]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: AttachmentsUploadBody,
) -> AttachmentsUploadResponse201:
    """Upload a file to send

     Multipart, with `identity_id` and `file` parts — not base64 in JSON, because a ten-megabyte PDF is
    thirteen megabytes of base64 and every proxy in between would have to be told. Name the returned id
    in `attachment_ids` on a send. An upload expires in a day: it is a file no message refers to yet.

    Args:
        body (AttachmentsUploadBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AttachmentsUploadResponse201
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AttachmentsUploadBody,
) -> Response[AttachmentsUploadResponse201]:
    """Upload a file to send

     Multipart, with `identity_id` and `file` parts — not base64 in JSON, because a ten-megabyte PDF is
    thirteen megabytes of base64 and every proxy in between would have to be told. Name the returned id
    in `attachment_ids` on a send. An upload expires in a day: it is a file no message refers to yet.

    Args:
        body (AttachmentsUploadBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AttachmentsUploadResponse201]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: AttachmentsUploadBody,
) -> AttachmentsUploadResponse201:
    """Upload a file to send

     Multipart, with `identity_id` and `file` parts — not base64 in JSON, because a ten-megabyte PDF is
    thirteen megabytes of base64 and every proxy in between would have to be told. Name the returned id
    in `attachment_ids` on a send. An upload expires in a day: it is a file no message refers to yet.

    Args:
        body (AttachmentsUploadBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AttachmentsUploadResponse201
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
