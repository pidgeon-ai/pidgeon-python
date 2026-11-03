from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.identities_card_response_200 import IdentitiesCardResponse200
from ...types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/identities/{id}/card".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> IdentitiesCardResponse200:
    if response.status_code >= 400:
        raise errors.PidgeonError.from_response(response)

    if response.status_code == 200:
        response_200 = IdentitiesCardResponse200.from_dict(response.json())

        return response_200

    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[IdentitiesCardResponse200]:
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
) -> Response[IdentitiesCardResponse200]:
    """This address’s agent card

     The signed card for an address an agent or a service sends from: who it is, for whom, which keys
    sign its mail, and a coarse standing. The same document anyone can read without a key at `GET
    /cards/{id}`. A person’s or a team’s address has one once software has sent from it as an agent;
    until then it answers 404.

    Args:
        id (str):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IdentitiesCardResponse200]
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
) -> IdentitiesCardResponse200:
    """This address’s agent card

     The signed card for an address an agent or a service sends from: who it is, for whom, which keys
    sign its mail, and a coarse standing. The same document anyone can read without a key at `GET
    /cards/{id}`. A person’s or a team’s address has one once software has sent from it as an agent;
    until then it answers 404.

    Args:
        id (str):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IdentitiesCardResponse200
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[IdentitiesCardResponse200]:
    """This address’s agent card

     The signed card for an address an agent or a service sends from: who it is, for whom, which keys
    sign its mail, and a coarse standing. The same document anyone can read without a key at `GET
    /cards/{id}`. A person’s or a team’s address has one once software has sent from it as an agent;
    until then it answers 404.

    Args:
        id (str):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IdentitiesCardResponse200]
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
) -> IdentitiesCardResponse200:
    """This address’s agent card

     The signed card for an address an agent or a service sends from: who it is, for whom, which keys
    sign its mail, and a coarse standing. The same document anyone can read without a key at `GET
    /cards/{id}`. A person’s or a team’s address has one once software has sent from it as an agent;
    until then it answers 404.

    Args:
        id (str):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IdentitiesCardResponse200
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
