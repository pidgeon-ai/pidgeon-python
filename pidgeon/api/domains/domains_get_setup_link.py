from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domains_get_setup_link_response_200 import DomainsGetSetupLinkResponse200
from ...models.domains_get_setup_link_template import DomainsGetSetupLinkTemplate
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    template: DomainsGetSetupLinkTemplate | Unset = DomainsGetSetupLinkTemplate.MAIL,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_template: str | Unset = UNSET
    if not isinstance(template, Unset):
        json_template = template.value

    params["template"] = json_template

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/domains/{id}/setup-link".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DomainsGetSetupLinkResponse200:
    if response.status_code >= 400:
        raise errors.PidgeonError.from_response(response)

    if response.status_code == 200:
        response_200 = DomainsGetSetupLinkResponse200.from_dict(response.json())

        return response_200

    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DomainsGetSetupLinkResponse200]:
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
    template: DomainsGetSetupLinkTemplate | Unset = DomainsGetSetupLinkTemplate.MAIL,
) -> Response[DomainsGetSetupLinkResponse200]:
    """One-click DNS setup, when the provider supports it

     The **Domain Connect** standard: the URL returned is signed by and points at the domain’s own DNS
    provider, where the owner signs in, reviews the records and approves — the provider writes them.
    Nothing here is a credential of ours.

    Answers `200` either way. `supported: false` is a fact about somebody else’s DNS provider rather
    than a failure of this request, and `reason` says whose problem it is: `provider` means that zone
    cannot do it, `unconfigured` means this deployment is not registered. Either way, fall back to `GET
    /domains/{id}/zone-file` or the `records` on the domain.

    `template` is `mail` (everything: ownership, DKIM and MX) or `mx` (the MX alone, for a domain
    already sending through us that is now going to receive).

    Args:
        id (str):
        template (DomainsGetSetupLinkTemplate | Unset):  Default:
            DomainsGetSetupLinkTemplate.MAIL.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DomainsGetSetupLinkResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        template=template,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    template: DomainsGetSetupLinkTemplate | Unset = DomainsGetSetupLinkTemplate.MAIL,
) -> DomainsGetSetupLinkResponse200:
    """One-click DNS setup, when the provider supports it

     The **Domain Connect** standard: the URL returned is signed by and points at the domain’s own DNS
    provider, where the owner signs in, reviews the records and approves — the provider writes them.
    Nothing here is a credential of ours.

    Answers `200` either way. `supported: false` is a fact about somebody else’s DNS provider rather
    than a failure of this request, and `reason` says whose problem it is: `provider` means that zone
    cannot do it, `unconfigured` means this deployment is not registered. Either way, fall back to `GET
    /domains/{id}/zone-file` or the `records` on the domain.

    `template` is `mail` (everything: ownership, DKIM and MX) or `mx` (the MX alone, for a domain
    already sending through us that is now going to receive).

    Args:
        id (str):
        template (DomainsGetSetupLinkTemplate | Unset):  Default:
            DomainsGetSetupLinkTemplate.MAIL.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DomainsGetSetupLinkResponse200
    """

    return sync_detailed(
        id=id,
        client=client,
        template=template,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    template: DomainsGetSetupLinkTemplate | Unset = DomainsGetSetupLinkTemplate.MAIL,
) -> Response[DomainsGetSetupLinkResponse200]:
    """One-click DNS setup, when the provider supports it

     The **Domain Connect** standard: the URL returned is signed by and points at the domain’s own DNS
    provider, where the owner signs in, reviews the records and approves — the provider writes them.
    Nothing here is a credential of ours.

    Answers `200` either way. `supported: false` is a fact about somebody else’s DNS provider rather
    than a failure of this request, and `reason` says whose problem it is: `provider` means that zone
    cannot do it, `unconfigured` means this deployment is not registered. Either way, fall back to `GET
    /domains/{id}/zone-file` or the `records` on the domain.

    `template` is `mail` (everything: ownership, DKIM and MX) or `mx` (the MX alone, for a domain
    already sending through us that is now going to receive).

    Args:
        id (str):
        template (DomainsGetSetupLinkTemplate | Unset):  Default:
            DomainsGetSetupLinkTemplate.MAIL.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DomainsGetSetupLinkResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        template=template,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    template: DomainsGetSetupLinkTemplate | Unset = DomainsGetSetupLinkTemplate.MAIL,
) -> DomainsGetSetupLinkResponse200:
    """One-click DNS setup, when the provider supports it

     The **Domain Connect** standard: the URL returned is signed by and points at the domain’s own DNS
    provider, where the owner signs in, reviews the records and approves — the provider writes them.
    Nothing here is a credential of ours.

    Answers `200` either way. `supported: false` is a fact about somebody else’s DNS provider rather
    than a failure of this request, and `reason` says whose problem it is: `provider` means that zone
    cannot do it, `unconfigured` means this deployment is not registered. Either way, fall back to `GET
    /domains/{id}/zone-file` or the `records` on the domain.

    `template` is `mail` (everything: ownership, DKIM and MX) or `mx` (the MX alone, for a domain
    already sending through us that is now going to receive).

    Args:
        id (str):
        template (DomainsGetSetupLinkTemplate | Unset):  Default:
            DomainsGetSetupLinkTemplate.MAIL.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DomainsGetSetupLinkResponse200
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            template=template,
        )
    ).parsed
