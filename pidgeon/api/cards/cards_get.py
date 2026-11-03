from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cards_get_response_200 import CardsGetResponse200
from ...types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/cards/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CardsGetResponse200:
    if response.status_code >= 400:
        raise errors.PidgeonError.from_response(response)

    if response.status_code == 200:
        response_200 = CardsGetResponse200.from_dict(response.json())

        return response_200

    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CardsGetResponse200]:
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
) -> Response[CardsGetResponse200]:
    """Read an agent card

     Public, with no key. An agent or service address’s identity, signed by the domain that vouches for
    it: `jws` is a compact JWS (EdDSA) to check against the keys at `<iss>/.well-known/post.json`, and
    `card` is its payload, decoded for reading. Good for a day (`exp`). The URL is permanent, and every
    agent message names it in its signed `Agent-attribution`. Anything that has no card — a person’s
    address, a deleted one, an id that is nothing — answers the same 404. Limited per IP.

    Args:
        id (str):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CardsGetResponse200]
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
) -> CardsGetResponse200:
    """Read an agent card

     Public, with no key. An agent or service address’s identity, signed by the domain that vouches for
    it: `jws` is a compact JWS (EdDSA) to check against the keys at `<iss>/.well-known/post.json`, and
    `card` is its payload, decoded for reading. Good for a day (`exp`). The URL is permanent, and every
    agent message names it in its signed `Agent-attribution`. Anything that has no card — a person’s
    address, a deleted one, an id that is nothing — answers the same 404. Limited per IP.

    Args:
        id (str):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CardsGetResponse200
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[CardsGetResponse200]:
    """Read an agent card

     Public, with no key. An agent or service address’s identity, signed by the domain that vouches for
    it: `jws` is a compact JWS (EdDSA) to check against the keys at `<iss>/.well-known/post.json`, and
    `card` is its payload, decoded for reading. Good for a day (`exp`). The URL is permanent, and every
    agent message names it in its signed `Agent-attribution`. Anything that has no card — a person’s
    address, a deleted one, an id that is nothing — answers the same 404. Limited per IP.

    Args:
        id (str):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CardsGetResponse200]
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
) -> CardsGetResponse200:
    """Read an agent card

     Public, with no key. An agent or service address’s identity, signed by the domain that vouches for
    it: `jws` is a compact JWS (EdDSA) to check against the keys at `<iss>/.well-known/post.json`, and
    `card` is its payload, decoded for reading. Good for a day (`exp`). The URL is permanent, and every
    agent message names it in its signed `Agent-attribution`. Anything that has no card — a person’s
    address, a deleted one, an id that is nothing — answers the same 404. Limited per IP.

    Args:
        id (str):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CardsGetResponse200
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
