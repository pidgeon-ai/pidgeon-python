from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.agent_verify_body import AgentVerifyBody
from ...models.agent_verify_response_200 import AgentVerifyResponse200
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    *,
    body: AgentVerifyBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/agent/verify",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AgentVerifyResponse200 | Error | None:
    if response.status_code == 200:
        response_200 = AgentVerifyResponse200.from_dict(response.json())

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
) -> Response[AgentVerifyResponse200 | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AgentVerifyBody,
) -> Response[AgentVerifyResponse200 | Error]:
    """Verify an agent with the human’s code

     Creates the account, the address and a workspace-scoped API key. Ten wrong codes spend the signup,
    whatever comes next. The key is returned once and never again — store it before doing anything else.
    It is minted here rather than at signup because this is the call a human has vouched for.

    Args:
        body (AgentVerifyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentVerifyResponse200 | Error]
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
    body: AgentVerifyBody,
) -> AgentVerifyResponse200 | Error | None:
    """Verify an agent with the human’s code

     Creates the account, the address and a workspace-scoped API key. Ten wrong codes spend the signup,
    whatever comes next. The key is returned once and never again — store it before doing anything else.
    It is minted here rather than at signup because this is the call a human has vouched for.

    Args:
        body (AgentVerifyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentVerifyResponse200 | Error
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AgentVerifyBody,
) -> Response[AgentVerifyResponse200 | Error]:
    """Verify an agent with the human’s code

     Creates the account, the address and a workspace-scoped API key. Ten wrong codes spend the signup,
    whatever comes next. The key is returned once and never again — store it before doing anything else.
    It is minted here rather than at signup because this is the call a human has vouched for.

    Args:
        body (AgentVerifyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentVerifyResponse200 | Error]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: AgentVerifyBody,
) -> AgentVerifyResponse200 | Error | None:
    """Verify an agent with the human’s code

     Creates the account, the address and a workspace-scoped API key. Ten wrong codes spend the signup,
    whatever comes next. The key is returned once and never again — store it before doing anything else.
    It is minted here rather than at signup because this is the call a human has vouched for.

    Args:
        body (AgentVerifyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentVerifyResponse200 | Error
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
