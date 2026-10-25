from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.threads_labels_delete_response_200 import ThreadsLabelsDeleteResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    label_id: UUID,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    params: dict[str, Any] = {}

    json_label_id = str(label_id)
    params["label_id"] = json_label_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/threads/{id}/labels".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ThreadsLabelsDeleteResponse200:
    if response.status_code >= 400:
        raise errors.PidgeonError.from_response(response)

    if response.status_code == 200:
        response_200 = ThreadsLabelsDeleteResponse200.from_dict(response.json())

        return response_200

    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ThreadsLabelsDeleteResponse200]:
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
    label_id: UUID,
    idempotency_key: str | Unset = UNSET,
) -> Response[ThreadsLabelsDeleteResponse200]:
    """Remove a label

     `label_id` in the query, because a label hangs off the conversation.

    Args:
        id (str):
        label_id (UUID):
        idempotency_key (str | Unset):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ThreadsLabelsDeleteResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        label_id=label_id,
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
    label_id: UUID,
    idempotency_key: str | Unset = UNSET,
) -> ThreadsLabelsDeleteResponse200:
    """Remove a label

     `label_id` in the query, because a label hangs off the conversation.

    Args:
        id (str):
        label_id (UUID):
        idempotency_key (str | Unset):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ThreadsLabelsDeleteResponse200
    """

    return sync_detailed(
        id=id,
        client=client,
        label_id=label_id,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    label_id: UUID,
    idempotency_key: str | Unset = UNSET,
) -> Response[ThreadsLabelsDeleteResponse200]:
    """Remove a label

     `label_id` in the query, because a label hangs off the conversation.

    Args:
        id (str):
        label_id (UUID):
        idempotency_key (str | Unset):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ThreadsLabelsDeleteResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        label_id=label_id,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    label_id: UUID,
    idempotency_key: str | Unset = UNSET,
) -> ThreadsLabelsDeleteResponse200:
    """Remove a label

     `label_id` in the query, because a label hangs off the conversation.

    Args:
        id (str):
        label_id (UUID):
        idempotency_key (str | Unset):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ThreadsLabelsDeleteResponse200
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            label_id=label_id,
            idempotency_key=idempotency_key,
        )
    ).parsed
