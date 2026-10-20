from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.identities_suspend_tenant_response_200 import IdentitiesSuspendTenantResponse200
from ...types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/tenants/{id}/suspend".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> IdentitiesSuspendTenantResponse200:
    if response.status_code >= 400:
        raise errors.PidgeonError.from_response(response)

    if response.status_code == 200:
        response_200 = IdentitiesSuspendTenantResponse200.from_dict(response.json())

        return response_200

    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[IdentitiesSuspendTenantResponse200]:
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
) -> Response[IdentitiesSuspendTenantResponse200]:
    """Offboard one of your customers

     Suspends every address carrying that `tenant_id`. **Suspends, never deletes** — the mail, the
    threads and the grants all stay, and each address emits `identity.suspended`. Deleting them is still
    one call each. Idempotent: it changes what is active and reports how many, so a retry is safe. It
    reaches only addresses you could have suspended one at a time.

    Args:
        id (str):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IdentitiesSuspendTenantResponse200]
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
) -> IdentitiesSuspendTenantResponse200:
    """Offboard one of your customers

     Suspends every address carrying that `tenant_id`. **Suspends, never deletes** — the mail, the
    threads and the grants all stay, and each address emits `identity.suspended`. Deleting them is still
    one call each. Idempotent: it changes what is active and reports how many, so a retry is safe. It
    reaches only addresses you could have suspended one at a time.

    Args:
        id (str):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IdentitiesSuspendTenantResponse200
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[IdentitiesSuspendTenantResponse200]:
    """Offboard one of your customers

     Suspends every address carrying that `tenant_id`. **Suspends, never deletes** — the mail, the
    threads and the grants all stay, and each address emits `identity.suspended`. Deleting them is still
    one call each. Idempotent: it changes what is active and reports how many, so a retry is safe. It
    reaches only addresses you could have suspended one at a time.

    Args:
        id (str):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IdentitiesSuspendTenantResponse200]
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
) -> IdentitiesSuspendTenantResponse200:
    """Offboard one of your customers

     Suspends every address carrying that `tenant_id`. **Suspends, never deletes** — the mail, the
    threads and the grants all stay, and each address emits `identity.suspended`. Deleting them is still
    one call each. Idempotent: it changes what is active and reports how many, so a retry is safe. It
    reaches only addresses you could have suspended one at a time.

    Args:
        id (str):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IdentitiesSuspendTenantResponse200
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
