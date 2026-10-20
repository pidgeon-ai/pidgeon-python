from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.identities_receive_rules_get_response_200 import IdentitiesReceiveRulesGetResponse200
from ...types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/identities/{id}/receive-rules".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> IdentitiesReceiveRulesGetResponse200:
    if response.status_code >= 400:
        raise errors.PidgeonError.from_response(response)

    if response.status_code == 200:
        response_200 = IdentitiesReceiveRulesGetResponse200.from_dict(response.json())

        return response_200

    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[IdentitiesReceiveRulesGetResponse200]:
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
) -> Response[IdentitiesReceiveRulesGetResponse200]:
    """Who may write to this address

     The rules that decide what reaches this address. Requires `read` rather than `admin`: anybody who
    may read the mail may see why some of it did not arrive. **Workspace-wide rules are not listed
    here** — these are the address’s own, and a key that administers one address must not be able to
    silence a sender for every other address in the workspace.

    Args:
        id (str):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IdentitiesReceiveRulesGetResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> IdentitiesReceiveRulesGetResponse200:
    """Who may write to this address

     The rules that decide what reaches this address. Requires `read` rather than `admin`: anybody who
    may read the mail may see why some of it did not arrive. **Workspace-wide rules are not listed
    here** — these are the address’s own, and a key that administers one address must not be able to
    silence a sender for every other address in the workspace.

    Args:
        id (str):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IdentitiesReceiveRulesGetResponse200
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[IdentitiesReceiveRulesGetResponse200]:
    """Who may write to this address

     The rules that decide what reaches this address. Requires `read` rather than `admin`: anybody who
    may read the mail may see why some of it did not arrive. **Workspace-wide rules are not listed
    here** — these are the address’s own, and a key that administers one address must not be able to
    silence a sender for every other address in the workspace.

    Args:
        id (str):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IdentitiesReceiveRulesGetResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> IdentitiesReceiveRulesGetResponse200:
    """Who may write to this address

     The rules that decide what reaches this address. Requires `read` rather than `admin`: anybody who
    may read the mail may see why some of it did not arrive. **Workspace-wide rules are not listed
    here** — these are the address’s own, and a key that administers one address must not be able to
    silence a sender for every other address in the workspace.

    Args:
        id (str):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IdentitiesReceiveRulesGetResponse200
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
