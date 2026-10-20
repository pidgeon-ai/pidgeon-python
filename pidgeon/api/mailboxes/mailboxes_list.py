from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.mailboxes_list_response_200 import MailboxesListResponse200
from ...types import UNSET, Response


def _get_kwargs(
    *,
    identity_id: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["identity_id"] = identity_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/mailboxes",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MailboxesListResponse200:
    if response.status_code >= 400:
        raise errors.PidgeonError.from_response(response)

    if response.status_code == 200:
        response_200 = MailboxesListResponse200.from_dict(response.json())

        return response_200

    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[MailboxesListResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    identity_id: str,
) -> Response[MailboxesListResponse200]:
    """List the folders of one mailbox

     The shape of a sidebar. `identity_id` is required — there is no cross-mailbox view, because merging
    the folders of several addresses would invent a mailbox nobody has.

    Args:
        identity_id (str):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MailboxesListResponse200]
    """

    kwargs = _get_kwargs(
        identity_id=identity_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    identity_id: str,
) -> MailboxesListResponse200:
    """List the folders of one mailbox

     The shape of a sidebar. `identity_id` is required — there is no cross-mailbox view, because merging
    the folders of several addresses would invent a mailbox nobody has.

    Args:
        identity_id (str):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MailboxesListResponse200
    """

    return sync_detailed(
        client=client,
        identity_id=identity_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    identity_id: str,
) -> Response[MailboxesListResponse200]:
    """List the folders of one mailbox

     The shape of a sidebar. `identity_id` is required — there is no cross-mailbox view, because merging
    the folders of several addresses would invent a mailbox nobody has.

    Args:
        identity_id (str):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MailboxesListResponse200]
    """

    kwargs = _get_kwargs(
        identity_id=identity_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    identity_id: str,
) -> MailboxesListResponse200:
    """List the folders of one mailbox

     The shape of a sidebar. `identity_id` is required — there is no cross-mailbox view, because merging
    the folders of several addresses would invent a mailbox nobody has.

    Args:
        identity_id (str):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MailboxesListResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            identity_id=identity_id,
        )
    ).parsed
