from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.drafts_remove_attachment_response_200 import DraftsRemoveAttachmentResponse200
from ...types import Response


def _get_kwargs(
    id: str,
    attachment_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/drafts/{id}/attachments/{attachment_id}".format(
            id=quote(str(id), safe=""),
            attachment_id=quote(str(attachment_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DraftsRemoveAttachmentResponse200:
    if response.status_code >= 400:
        raise errors.PidgeonError.from_response(response)

    if response.status_code == 200:
        response_200 = DraftsRemoveAttachmentResponse200.from_dict(response.json())

        return response_200

    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DraftsRemoveAttachmentResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    attachment_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DraftsRemoveAttachmentResponse200]:
    """Take a file off a draft

     The object goes with the row. An attachment belongs to its draft rather than being shared, so
    leaving the bytes behind would be storage nobody can reach and everybody is billed for. `POST
    /attachments` is how one gets on.

    Args:
        id (str):
        attachment_id (str):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DraftsRemoveAttachmentResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        attachment_id=attachment_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    attachment_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> DraftsRemoveAttachmentResponse200:
    """Take a file off a draft

     The object goes with the row. An attachment belongs to its draft rather than being shared, so
    leaving the bytes behind would be storage nobody can reach and everybody is billed for. `POST
    /attachments` is how one gets on.

    Args:
        id (str):
        attachment_id (str):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DraftsRemoveAttachmentResponse200
    """

    return sync_detailed(
        id=id,
        attachment_id=attachment_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    attachment_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DraftsRemoveAttachmentResponse200]:
    """Take a file off a draft

     The object goes with the row. An attachment belongs to its draft rather than being shared, so
    leaving the bytes behind would be storage nobody can reach and everybody is billed for. `POST
    /attachments` is how one gets on.

    Args:
        id (str):
        attachment_id (str):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DraftsRemoveAttachmentResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        attachment_id=attachment_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    attachment_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> DraftsRemoveAttachmentResponse200:
    """Take a file off a draft

     The object goes with the row. An attachment belongs to its draft rather than being shared, so
    leaving the bytes behind would be storage nobody can reach and everybody is billed for. `POST
    /attachments` is how one gets on.

    Args:
        id (str):
        attachment_id (str):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DraftsRemoveAttachmentResponse200
    """

    return (
        await asyncio_detailed(
            id=id,
            attachment_id=attachment_id,
            client=client,
        )
    ).parsed
