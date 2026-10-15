from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domains_update_body import DomainsUpdateBody
from ...models.domains_update_response_200 import DomainsUpdateResponse200
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: DomainsUpdateBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/domains/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DomainsUpdateResponse200 | Error | None:
    if response.status_code == 200:
        response_200 = DomainsUpdateResponse200.from_dict(response.json())

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
) -> Response[DomainsUpdateResponse200 | Error]:
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
    body: DomainsUpdateBody,
) -> Response[DomainsUpdateResponse200 | Error]:
    """Turn the catch-all on or off

     The one thing about a domain that can change. Catch-all is two gates: this switch, and a `catch_all`
    routing rule saying where the mail goes — so turning it on without a rule does nothing, and turning
    it off later does not throw away where the mail was going.

    Args:
        id (str):
        body (DomainsUpdateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DomainsUpdateResponse200 | Error]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DomainsUpdateBody,
) -> DomainsUpdateResponse200 | Error | None:
    """Turn the catch-all on or off

     The one thing about a domain that can change. Catch-all is two gates: this switch, and a `catch_all`
    routing rule saying where the mail goes — so turning it on without a rule does nothing, and turning
    it off later does not throw away where the mail was going.

    Args:
        id (str):
        body (DomainsUpdateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DomainsUpdateResponse200 | Error
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DomainsUpdateBody,
) -> Response[DomainsUpdateResponse200 | Error]:
    """Turn the catch-all on or off

     The one thing about a domain that can change. Catch-all is two gates: this switch, and a `catch_all`
    routing rule saying where the mail goes — so turning it on without a rule does nothing, and turning
    it off later does not throw away where the mail was going.

    Args:
        id (str):
        body (DomainsUpdateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DomainsUpdateResponse200 | Error]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DomainsUpdateBody,
) -> DomainsUpdateResponse200 | Error | None:
    """Turn the catch-all on or off

     The one thing about a domain that can change. Catch-all is two gates: this switch, and a `catch_all`
    routing rule saying where the mail goes — so turning it on without a rule does nothing, and turning
    it off later does not throw away where the mail was going.

    Args:
        id (str):
        body (DomainsUpdateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DomainsUpdateResponse200 | Error
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
