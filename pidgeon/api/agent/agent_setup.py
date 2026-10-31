from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.agent_setup_response_200 import AgentSetupResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    identity_id: UUID | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_identity_id: str | Unset = UNSET
    if not isinstance(identity_id, Unset):
        json_identity_id = str(identity_id)
    params["identity_id"] = json_identity_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/agent/setup",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AgentSetupResponse200:
    if response.status_code >= 400:
        raise errors.PidgeonError.from_response(response)

    if response.status_code == 200:
        response_200 = AgentSetupResponse200.from_dict(response.json())

        return response_200

    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AgentSetupResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    identity_id: UUID | Unset = UNSET,
) -> Response[AgentSetupResponse200]:
    """What stands between this key and sending

     **Call this first.** It asks every check a send would, without sending, and answers in order:
    `steps[]`, each with `done`, who acts (`owner`: `agent` or `person`), `what` and `how`, and `next`,
    the first not done. A person returns the signup code, publishes DNS (the records are listed) or
    gives you a key that can send; you create an address or wait out a limit (`resets_at`).
    `ready_to_send` is true when nothing is left. Without `identity_id` it answers for the address
    nearest to sending and lists the rest. It sees only the addresses this key reaches.

    Args:
        identity_id (UUID | Unset):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentSetupResponse200]
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
    identity_id: UUID | Unset = UNSET,
) -> AgentSetupResponse200:
    """What stands between this key and sending

     **Call this first.** It asks every check a send would, without sending, and answers in order:
    `steps[]`, each with `done`, who acts (`owner`: `agent` or `person`), `what` and `how`, and `next`,
    the first not done. A person returns the signup code, publishes DNS (the records are listed) or
    gives you a key that can send; you create an address or wait out a limit (`resets_at`).
    `ready_to_send` is true when nothing is left. Without `identity_id` it answers for the address
    nearest to sending and lists the rest. It sees only the addresses this key reaches.

    Args:
        identity_id (UUID | Unset):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentSetupResponse200
    """

    return sync_detailed(
        client=client,
        identity_id=identity_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    identity_id: UUID | Unset = UNSET,
) -> Response[AgentSetupResponse200]:
    """What stands between this key and sending

     **Call this first.** It asks every check a send would, without sending, and answers in order:
    `steps[]`, each with `done`, who acts (`owner`: `agent` or `person`), `what` and `how`, and `next`,
    the first not done. A person returns the signup code, publishes DNS (the records are listed) or
    gives you a key that can send; you create an address or wait out a limit (`resets_at`).
    `ready_to_send` is true when nothing is left. Without `identity_id` it answers for the address
    nearest to sending and lists the rest. It sees only the addresses this key reaches.

    Args:
        identity_id (UUID | Unset):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentSetupResponse200]
    """

    kwargs = _get_kwargs(
        identity_id=identity_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    identity_id: UUID | Unset = UNSET,
) -> AgentSetupResponse200:
    """What stands between this key and sending

     **Call this first.** It asks every check a send would, without sending, and answers in order:
    `steps[]`, each with `done`, who acts (`owner`: `agent` or `person`), `what` and `how`, and `next`,
    the first not done. A person returns the signup code, publishes DNS (the records are listed) or
    gives you a key that can send; you create an address or wait out a limit (`resets_at`).
    `ready_to_send` is true when nothing is left. Without `identity_id` it answers for the address
    nearest to sending and lists the rest. It sees only the addresses this key reaches.

    Args:
        identity_id (UUID | Unset):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentSetupResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            identity_id=identity_id,
        )
    ).parsed
