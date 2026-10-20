from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.identities_receive_rules_delete_response_200 import IdentitiesReceiveRulesDeleteResponse200
from ...types import UNSET, Response


def _get_kwargs(
    id: str,
    *,
    rule_id: UUID,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_rule_id = str(rule_id)
    params["rule_id"] = json_rule_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/identities/{id}/receive-rules".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> IdentitiesReceiveRulesDeleteResponse200:
    if response.status_code >= 400:
        raise errors.PidgeonError.from_response(response)

    if response.status_code == 200:
        response_200 = IdentitiesReceiveRulesDeleteResponse200.from_dict(response.json())

        return response_200

    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[IdentitiesReceiveRulesDeleteResponse200]:
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
    rule_id: UUID,
) -> Response[IdentitiesReceiveRulesDeleteResponse200]:
    """Remove a rule

     By the rule’s own id, which `GET` returned as `id`.

    Args:
        id (str):
        rule_id (UUID):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IdentitiesReceiveRulesDeleteResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        rule_id=rule_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    rule_id: UUID,
) -> IdentitiesReceiveRulesDeleteResponse200:
    """Remove a rule

     By the rule’s own id, which `GET` returned as `id`.

    Args:
        id (str):
        rule_id (UUID):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IdentitiesReceiveRulesDeleteResponse200
    """

    return sync_detailed(
        id=id,
        client=client,
        rule_id=rule_id,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    rule_id: UUID,
) -> Response[IdentitiesReceiveRulesDeleteResponse200]:
    """Remove a rule

     By the rule’s own id, which `GET` returned as `id`.

    Args:
        id (str):
        rule_id (UUID):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IdentitiesReceiveRulesDeleteResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        rule_id=rule_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    rule_id: UUID,
) -> IdentitiesReceiveRulesDeleteResponse200:
    """Remove a rule

     By the rule’s own id, which `GET` returned as `id`.

    Args:
        id (str):
        rule_id (UUID):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IdentitiesReceiveRulesDeleteResponse200
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            rule_id=rule_id,
        )
    ).parsed
