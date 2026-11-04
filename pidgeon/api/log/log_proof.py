from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.log_proof_response_200 import LogProofResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    sub: UUID | Unset = UNSET,
    index: int | Unset = UNSET,
    tree_size: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_sub: str | Unset = UNSET
    if not isinstance(sub, Unset):
        json_sub = str(sub)
    params["sub"] = json_sub

    params["index"] = index

    params["tree_size"] = tree_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/log/proof",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> LogProofResponse200:
    if response.status_code >= 400:
        raise errors.PidgeonError.from_response(response)

    if response.status_code == 200:
        response_200 = LogProofResponse200.from_dict(response.json())

        return response_200

    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[LogProofResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    sub: UUID | Unset = UNSET,
    index: int | Unset = UNSET,
    tree_size: int | Unset = UNSET,
) -> Response[LogProofResponse200]:
    """Prove a card is in the card log

     Public, with no key. The inclusion proof (RFC 9162 §2.1.3) for a card’s latest entry, by its `sub`,
    against the current head; or for an entry `index` against the head at `tree_size`. 404 when it is
    not in the log: a card appears within five minutes.

    Args:
        sub (UUID | Unset): A card’s `sub`: its latest entry is proved.
        index (int | Unset): An entry’s index, instead of `sub`.
        tree_size (int | Unset): Prove against the checkpoint at this size, instead of the current
            one.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LogProofResponse200]
    """

    kwargs = _get_kwargs(
        sub=sub,
        index=index,
        tree_size=tree_size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    sub: UUID | Unset = UNSET,
    index: int | Unset = UNSET,
    tree_size: int | Unset = UNSET,
) -> LogProofResponse200:
    """Prove a card is in the card log

     Public, with no key. The inclusion proof (RFC 9162 §2.1.3) for a card’s latest entry, by its `sub`,
    against the current head; or for an entry `index` against the head at `tree_size`. 404 when it is
    not in the log: a card appears within five minutes.

    Args:
        sub (UUID | Unset): A card’s `sub`: its latest entry is proved.
        index (int | Unset): An entry’s index, instead of `sub`.
        tree_size (int | Unset): Prove against the checkpoint at this size, instead of the current
            one.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LogProofResponse200
    """

    return sync_detailed(
        client=client,
        sub=sub,
        index=index,
        tree_size=tree_size,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    sub: UUID | Unset = UNSET,
    index: int | Unset = UNSET,
    tree_size: int | Unset = UNSET,
) -> Response[LogProofResponse200]:
    """Prove a card is in the card log

     Public, with no key. The inclusion proof (RFC 9162 §2.1.3) for a card’s latest entry, by its `sub`,
    against the current head; or for an entry `index` against the head at `tree_size`. 404 when it is
    not in the log: a card appears within five minutes.

    Args:
        sub (UUID | Unset): A card’s `sub`: its latest entry is proved.
        index (int | Unset): An entry’s index, instead of `sub`.
        tree_size (int | Unset): Prove against the checkpoint at this size, instead of the current
            one.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LogProofResponse200]
    """

    kwargs = _get_kwargs(
        sub=sub,
        index=index,
        tree_size=tree_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    sub: UUID | Unset = UNSET,
    index: int | Unset = UNSET,
    tree_size: int | Unset = UNSET,
) -> LogProofResponse200:
    """Prove a card is in the card log

     Public, with no key. The inclusion proof (RFC 9162 §2.1.3) for a card’s latest entry, by its `sub`,
    against the current head; or for an entry `index` against the head at `tree_size`. 404 when it is
    not in the log: a card appears within five minutes.

    Args:
        sub (UUID | Unset): A card’s `sub`: its latest entry is proved.
        index (int | Unset): An entry’s index, instead of `sub`.
        tree_size (int | Unset): Prove against the checkpoint at this size, instead of the current
            one.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LogProofResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            sub=sub,
            index=index,
            tree_size=tree_size,
        )
    ).parsed
