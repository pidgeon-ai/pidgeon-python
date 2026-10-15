from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.threads_labels_delete_response_200 import ThreadsLabelsDeleteResponse200
from ...types import UNSET, Response


def _get_kwargs(
    id: str,
    *,
    label_id: UUID,
) -> dict[str, Any]:

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

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | ThreadsLabelsDeleteResponse200 | None:
    if response.status_code == 200:
        response_200 = ThreadsLabelsDeleteResponse200.from_dict(response.json())

        return response_200

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
) -> Response[Error | ThreadsLabelsDeleteResponse200]:
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
) -> Response[Error | ThreadsLabelsDeleteResponse200]:
    """Remove a label

     `label_id` in the query, because a label hangs off the conversation.

    Args:
        id (str):
        label_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ThreadsLabelsDeleteResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        label_id=label_id,
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
) -> Error | ThreadsLabelsDeleteResponse200 | None:
    """Remove a label

     `label_id` in the query, because a label hangs off the conversation.

    Args:
        id (str):
        label_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ThreadsLabelsDeleteResponse200
    """

    return sync_detailed(
        id=id,
        client=client,
        label_id=label_id,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    label_id: UUID,
) -> Response[Error | ThreadsLabelsDeleteResponse200]:
    """Remove a label

     `label_id` in the query, because a label hangs off the conversation.

    Args:
        id (str):
        label_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ThreadsLabelsDeleteResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        label_id=label_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    label_id: UUID,
) -> Error | ThreadsLabelsDeleteResponse200 | None:
    """Remove a label

     `label_id` in the query, because a label hangs off the conversation.

    Args:
        id (str):
        label_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ThreadsLabelsDeleteResponse200
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            label_id=label_id,
        )
    ).parsed
