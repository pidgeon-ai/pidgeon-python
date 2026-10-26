from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.attachments_create_upload_body import AttachmentsCreateUploadBody
from ...models.attachments_create_upload_response_201 import AttachmentsCreateUploadResponse201
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: AttachmentsCreateUploadBody,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/attachments/uploads",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AttachmentsCreateUploadResponse201:
    if response.status_code >= 400:
        raise errors.PidgeonError.from_response(response)

    if response.status_code == 201:
        response_201 = AttachmentsCreateUploadResponse201.from_dict(response.json())

        return response_201

    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AttachmentsCreateUploadResponse201]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AttachmentsCreateUploadBody,
    idempotency_key: str | Unset = UNSET,
) -> Response[AttachmentsCreateUploadResponse201]:
    """Upload a large file straight to storage

     For a file of any size up to your plan’s limit. Say what it is — `identity_id`, `filename`,
    `content_type` and `size` in bytes — and the answer’s `upload` is a signed URL: `PUT` the bytes
    there with the `headers` it lists, within 15 minutes. The size and type are signed, so a body of
    another length or type is refused. Then call `POST /attachments/{id}/complete`; until then a send
    naming the id is a `409`. The same checks as `POST /attachments`: `draft` on the address, the
    allowed types, the plan’s per-file size. Expires in a day if never sent.

    Args:
        idempotency_key (str | Unset):
        body (AttachmentsCreateUploadBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AttachmentsCreateUploadResponse201]
    """

    kwargs = _get_kwargs(
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: AttachmentsCreateUploadBody,
    idempotency_key: str | Unset = UNSET,
) -> AttachmentsCreateUploadResponse201:
    """Upload a large file straight to storage

     For a file of any size up to your plan’s limit. Say what it is — `identity_id`, `filename`,
    `content_type` and `size` in bytes — and the answer’s `upload` is a signed URL: `PUT` the bytes
    there with the `headers` it lists, within 15 minutes. The size and type are signed, so a body of
    another length or type is refused. Then call `POST /attachments/{id}/complete`; until then a send
    naming the id is a `409`. The same checks as `POST /attachments`: `draft` on the address, the
    allowed types, the plan’s per-file size. Expires in a day if never sent.

    Args:
        idempotency_key (str | Unset):
        body (AttachmentsCreateUploadBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AttachmentsCreateUploadResponse201
    """

    return sync_detailed(
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AttachmentsCreateUploadBody,
    idempotency_key: str | Unset = UNSET,
) -> Response[AttachmentsCreateUploadResponse201]:
    """Upload a large file straight to storage

     For a file of any size up to your plan’s limit. Say what it is — `identity_id`, `filename`,
    `content_type` and `size` in bytes — and the answer’s `upload` is a signed URL: `PUT` the bytes
    there with the `headers` it lists, within 15 minutes. The size and type are signed, so a body of
    another length or type is refused. Then call `POST /attachments/{id}/complete`; until then a send
    naming the id is a `409`. The same checks as `POST /attachments`: `draft` on the address, the
    allowed types, the plan’s per-file size. Expires in a day if never sent.

    Args:
        idempotency_key (str | Unset):
        body (AttachmentsCreateUploadBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AttachmentsCreateUploadResponse201]
    """

    kwargs = _get_kwargs(
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: AttachmentsCreateUploadBody,
    idempotency_key: str | Unset = UNSET,
) -> AttachmentsCreateUploadResponse201:
    """Upload a large file straight to storage

     For a file of any size up to your plan’s limit. Say what it is — `identity_id`, `filename`,
    `content_type` and `size` in bytes — and the answer’s `upload` is a signed URL: `PUT` the bytes
    there with the `headers` it lists, within 15 minutes. The size and type are signed, so a body of
    another length or type is refused. Then call `POST /attachments/{id}/complete`; until then a send
    naming the id is a `409`. The same checks as `POST /attachments`: `draft` on the address, the
    allowed types, the plan’s per-file size. Expires in a day if never sent.

    Args:
        idempotency_key (str | Unset):
        body (AttachmentsCreateUploadBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AttachmentsCreateUploadResponse201
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
