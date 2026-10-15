from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.workspace_get_response_200 import WorkspaceGetResponse200
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/workspace",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | WorkspaceGetResponse200 | None:
    if response.status_code == 200:
        response_200 = WorkspaceGetResponse200.from_dict(response.json())

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
) -> Response[Error | WorkspaceGetResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[Error | WorkspaceGetResponse200]:
    """Which account this key is for

     Read-only. Renaming is a settings field and deleting takes the calling credential with it; neither
    belongs to a bearer token. `plan` is here so a caller can say "your plan allows N" rather than
    discovering it from a 402.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | WorkspaceGetResponse200]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> Error | WorkspaceGetResponse200 | None:
    """Which account this key is for

     Read-only. Renaming is a settings field and deleting takes the calling credential with it; neither
    belongs to a bearer token. `plan` is here so a caller can say "your plan allows N" rather than
    discovering it from a 402.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | WorkspaceGetResponse200
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[Error | WorkspaceGetResponse200]:
    """Which account this key is for

     Read-only. Renaming is a settings field and deleting takes the calling credential with it; neither
    belongs to a bearer token. `plan` is here so a caller can say "your plan allows N" rather than
    discovering it from a 402.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | WorkspaceGetResponse200]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> Error | WorkspaceGetResponse200 | None:
    """Which account this key is for

     Read-only. Renaming is a settings field and deleting takes the calling credential with it; neither
    belongs to a bearer token. `plan` is here so a caller can say "your plan allows N" rather than
    discovering it from a 402.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | WorkspaceGetResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
