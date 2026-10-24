from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.pods_delete_delete_addresses import PodsDeleteDeleteAddresses
from ...models.pods_delete_response_200 import PodsDeleteResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    delete_addresses: PodsDeleteDeleteAddresses | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_delete_addresses: str | Unset = UNSET
    if not isinstance(delete_addresses, Unset):
        json_delete_addresses = delete_addresses.value

    params["delete_addresses"] = json_delete_addresses

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/pods/{id}".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PodsDeleteResponse200:
    if response.status_code >= 400:
        raise errors.PidgeonError.from_response(response)

    if response.status_code == 200:
        response_200 = PodsDeleteResponse200.from_dict(response.json())

        return response_200

    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PodsDeleteResponse200]:
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
    delete_addresses: PodsDeleteDeleteAddresses | Unset = UNSET,
) -> Response[PodsDeleteResponse200]:
    """Delete a pod, its addresses and their mail

     **This deletes customer data and cannot be undone.** It revokes every key of the pod, and every key
    those minted, then deletes each address in the pod with all of its mail, then the pod.

    A pod that still holds an address is refused with 409 unless you pass `delete_addresses=true`. The
    default pod and a pod holding a domain are always refused: delete the domain first. Needs a live key
    over the whole account.

    If it fails part way, call it again: it carries on from where it stopped. To keep the mail, suspend
    the addresses (`PATCH /identities/{id}`) or move them to another pod instead.

    Args:
        id (str):
        delete_addresses (PodsDeleteDeleteAddresses | Unset): `true` to delete the pod’s addresses
            and all their mail with it. Without it a pod that holds an address is refused with 409.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PodsDeleteResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        delete_addresses=delete_addresses,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    delete_addresses: PodsDeleteDeleteAddresses | Unset = UNSET,
) -> PodsDeleteResponse200:
    """Delete a pod, its addresses and their mail

     **This deletes customer data and cannot be undone.** It revokes every key of the pod, and every key
    those minted, then deletes each address in the pod with all of its mail, then the pod.

    A pod that still holds an address is refused with 409 unless you pass `delete_addresses=true`. The
    default pod and a pod holding a domain are always refused: delete the domain first. Needs a live key
    over the whole account.

    If it fails part way, call it again: it carries on from where it stopped. To keep the mail, suspend
    the addresses (`PATCH /identities/{id}`) or move them to another pod instead.

    Args:
        id (str):
        delete_addresses (PodsDeleteDeleteAddresses | Unset): `true` to delete the pod’s addresses
            and all their mail with it. Without it a pod that holds an address is refused with 409.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PodsDeleteResponse200
    """

    return sync_detailed(
        id=id,
        client=client,
        delete_addresses=delete_addresses,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    delete_addresses: PodsDeleteDeleteAddresses | Unset = UNSET,
) -> Response[PodsDeleteResponse200]:
    """Delete a pod, its addresses and their mail

     **This deletes customer data and cannot be undone.** It revokes every key of the pod, and every key
    those minted, then deletes each address in the pod with all of its mail, then the pod.

    A pod that still holds an address is refused with 409 unless you pass `delete_addresses=true`. The
    default pod and a pod holding a domain are always refused: delete the domain first. Needs a live key
    over the whole account.

    If it fails part way, call it again: it carries on from where it stopped. To keep the mail, suspend
    the addresses (`PATCH /identities/{id}`) or move them to another pod instead.

    Args:
        id (str):
        delete_addresses (PodsDeleteDeleteAddresses | Unset): `true` to delete the pod’s addresses
            and all their mail with it. Without it a pod that holds an address is refused with 409.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PodsDeleteResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        delete_addresses=delete_addresses,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    delete_addresses: PodsDeleteDeleteAddresses | Unset = UNSET,
) -> PodsDeleteResponse200:
    """Delete a pod, its addresses and their mail

     **This deletes customer data and cannot be undone.** It revokes every key of the pod, and every key
    those minted, then deletes each address in the pod with all of its mail, then the pod.

    A pod that still holds an address is refused with 409 unless you pass `delete_addresses=true`. The
    default pod and a pod holding a domain are always refused: delete the domain first. Needs a live key
    over the whole account.

    If it fails part way, call it again: it carries on from where it stopped. To keep the mail, suspend
    the addresses (`PATCH /identities/{id}`) or move them to another pod instead.

    Args:
        id (str):
        delete_addresses (PodsDeleteDeleteAddresses | Unset): `true` to delete the pod’s addresses
            and all their mail with it. Without it a pod that holds an address is refused with 409.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PodsDeleteResponse200
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            delete_addresses=delete_addresses,
        )
    ).parsed
