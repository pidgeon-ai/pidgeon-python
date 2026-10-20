from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.workspace_members_response_200 import WorkspaceMembersResponse200
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/workspace/members",
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> WorkspaceMembersResponse200:
    if response.status_code >= 400:
        raise errors.PidgeonError.from_response(response)

    if response.status_code == 200:
        response_200 = WorkspaceMembersResponse200.from_dict(response.json())

        return response_200

    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[WorkspaceMembersResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[WorkspaceMembersResponse200]:
    """List the people in this workspace

     Read-only, and workspace-level: a key with no mailbox grants can still read it, for the same reason
    it can list domains. Assigning a conversation needs an id from here. Inviting and removing people
    stay in the dashboard — an invitation is mail to a person, and removing somebody hands on their
    mailboxes.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WorkspaceMembersResponse200]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> WorkspaceMembersResponse200:
    """List the people in this workspace

     Read-only, and workspace-level: a key with no mailbox grants can still read it, for the same reason
    it can list domains. Assigning a conversation needs an id from here. Inviting and removing people
    stay in the dashboard — an invitation is mail to a person, and removing somebody hands on their
    mailboxes.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WorkspaceMembersResponse200
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[WorkspaceMembersResponse200]:
    """List the people in this workspace

     Read-only, and workspace-level: a key with no mailbox grants can still read it, for the same reason
    it can list domains. Assigning a conversation needs an id from here. Inviting and removing people
    stay in the dashboard — an invitation is mail to a person, and removing somebody hands on their
    mailboxes.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WorkspaceMembersResponse200]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> WorkspaceMembersResponse200:
    """List the people in this workspace

     Read-only, and workspace-level: a key with no mailbox grants can still read it, for the same reason
    it can list domains. Assigning a conversation needs an id from here. Inviting and removing people
    stay in the dashboard — an invitation is mail to a person, and removing somebody hands on their
    mailboxes.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WorkspaceMembersResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
