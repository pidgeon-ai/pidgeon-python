from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.attachments_upload_body import AttachmentsUploadBody
from ...models.attachments_upload_response_201 import AttachmentsUploadResponse201
from ...models.error import Error
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


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AttachmentsUploadResponse201 | Error | None:
    if response.status_code == 201:
        response_201 = AttachmentsUploadResponse201.from_dict(response.json())

        return response_201

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
) -> Response[AttachmentsUploadResponse201 | Error]:
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
) -> Response[AttachmentsUploadResponse201 | Error]:
    """Upload a file to send

     Multipart, with `identity_id` and `file` parts — not base64 in JSON, because a ten-megabyte PDF is
    thirteen megabytes of base64 and every proxy in between would have to be told. Name the returned id
    in `attachment_ids` on a send. An upload expires in a day: it is a file no message refers to yet.

    Args:
        body (AttachmentsUploadBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AttachmentsUploadResponse201 | Error]
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
) -> AttachmentsUploadResponse201 | Error | None:
    """Upload a file to send

     Multipart, with `identity_id` and `file` parts — not base64 in JSON, because a ten-megabyte PDF is
    thirteen megabytes of base64 and every proxy in between would have to be told. Name the returned id
    in `attachment_ids` on a send. An upload expires in a day: it is a file no message refers to yet.

    Args:
        body (AttachmentsUploadBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AttachmentsUploadResponse201 | Error
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AttachmentsUploadBody,
) -> Response[AttachmentsUploadResponse201 | Error]:
    """Upload a file to send

     Multipart, with `identity_id` and `file` parts — not base64 in JSON, because a ten-megabyte PDF is
    thirteen megabytes of base64 and every proxy in between would have to be told. Name the returned id
    in `attachment_ids` on a send. An upload expires in a day: it is a file no message refers to yet.

    Args:
        body (AttachmentsUploadBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AttachmentsUploadResponse201 | Error]
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
) -> AttachmentsUploadResponse201 | Error | None:
    """Upload a file to send

     Multipart, with `identity_id` and `file` parts — not base64 in JSON, because a ten-megabyte PDF is
    thirteen megabytes of base64 and every proxy in between would have to be told. Name the returned id
    in `attachment_ids` on a send. An upload expires in a day: it is a file no message refers to yet.

    Args:
        body (AttachmentsUploadBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AttachmentsUploadResponse201 | Error
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
