from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.agent_connect_body import AgentConnectBody
from ...models.agent_connect_response_200 import AgentConnectResponse200
from ...types import Response


def _get_kwargs(
    *,
    body: AgentConnectBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/agent/connect",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AgentConnectResponse200:
    if response.status_code >= 400:
        raise errors.PidgeonError.from_response(response)

    if response.status_code == 200:
        response_200 = AgentConnectResponse200.from_dict(response.json())

        return response_200

    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AgentConnectResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AgentConnectBody,
) -> Response[AgentConnectResponse200]:
    """Connect an agent with a setup code

     For an inbox a person already has. They press "Get a setup code" on the dashboard and give the agent
    the code; this returns an API key with `send` on that one address. No account is created and no code
    is emailed. A code works once, for 10 minutes; every way one fails gets the same `400`. The key is
    returned once and never again, shows under the person’s API keys, and is held for approval like any
    other key.

    Args:
        body (AgentConnectBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentConnectResponse200]
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
    body: AgentConnectBody,
) -> AgentConnectResponse200:
    """Connect an agent with a setup code

     For an inbox a person already has. They press "Get a setup code" on the dashboard and give the agent
    the code; this returns an API key with `send` on that one address. No account is created and no code
    is emailed. A code works once, for 10 minutes; every way one fails gets the same `400`. The key is
    returned once and never again, shows under the person’s API keys, and is held for approval like any
    other key.

    Args:
        body (AgentConnectBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentConnectResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AgentConnectBody,
) -> Response[AgentConnectResponse200]:
    """Connect an agent with a setup code

     For an inbox a person already has. They press "Get a setup code" on the dashboard and give the agent
    the code; this returns an API key with `send` on that one address. No account is created and no code
    is emailed. A code works once, for 10 minutes; every way one fails gets the same `400`. The key is
    returned once and never again, shows under the person’s API keys, and is held for approval like any
    other key.

    Args:
        body (AgentConnectBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentConnectResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: AgentConnectBody,
) -> AgentConnectResponse200:
    """Connect an agent with a setup code

     For an inbox a person already has. They press "Get a setup code" on the dashboard and give the agent
    the code; this returns an API key with `send` on that one address. No account is created and no code
    is emailed. A code works once, for 10 minutes; every way one fails gets the same `400`. The key is
    returned once and never again, shows under the person’s API keys, and is held for approval like any
    other key.

    Args:
        body (AgentConnectBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentConnectResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
