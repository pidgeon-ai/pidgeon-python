from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.agent_sign_up_body import AgentSignUpBody
from ...models.agent_sign_up_response_201 import AgentSignUpResponse201
from ...types import Response


def _get_kwargs(
    *,
    body: AgentSignUpBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/agent/signup",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AgentSignUpResponse201:
    if response.status_code >= 400:
        raise errors.PidgeonError.from_response(response)

    if response.status_code == 201:
        response_201 = AgentSignUpResponse201.from_dict(response.json())

        return response_201

    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AgentSignUpResponse201]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AgentSignUpBody,
) -> Response[AgentSignUpResponse201]:
    """Sign an agent up

     The one call in this API that needs no key. An agent names a username and, optionally, the human who
    will own the mailbox; a six-digit code goes to that human and **nothing is created until it comes
    back**. Without a `human_email` the name is reserved and dormant — attach one with `POST
    /agent/human`.

    Args:
        body (AgentSignUpBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentSignUpResponse201]
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
    body: AgentSignUpBody,
) -> AgentSignUpResponse201:
    """Sign an agent up

     The one call in this API that needs no key. An agent names a username and, optionally, the human who
    will own the mailbox; a six-digit code goes to that human and **nothing is created until it comes
    back**. Without a `human_email` the name is reserved and dormant — attach one with `POST
    /agent/human`.

    Args:
        body (AgentSignUpBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentSignUpResponse201
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AgentSignUpBody,
) -> Response[AgentSignUpResponse201]:
    """Sign an agent up

     The one call in this API that needs no key. An agent names a username and, optionally, the human who
    will own the mailbox; a six-digit code goes to that human and **nothing is created until it comes
    back**. Without a `human_email` the name is reserved and dormant — attach one with `POST
    /agent/human`.

    Args:
        body (AgentSignUpBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentSignUpResponse201]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: AgentSignUpBody,
) -> AgentSignUpResponse201:
    """Sign an agent up

     The one call in this API that needs no key. An agent names a username and, optionally, the human who
    will own the mailbox; a six-digit code goes to that human and **nothing is created until it comes
    back**. Without a `human_email` the name is reserved and dormant — attach one with `POST
    /agent/human`.

    Args:
        body (AgentSignUpBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentSignUpResponse201
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
