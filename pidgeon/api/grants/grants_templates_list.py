from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.grants_templates_list_response_200 import GrantsTemplatesListResponse200
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/grant-templates",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GrantsTemplatesListResponse200:
    if response.status_code >= 400:
        raise errors.PidgeonError.from_response(response)

    if response.status_code == 200:
        response_200 = GrantsTemplatesListResponse200.from_dict(response.json())

        return response_200

    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GrantsTemplatesListResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[GrantsTemplatesListResponse200]:
    """List grant templates

     What this account’s agents may ask a person for: a scope (`name`, and the `label` the consent screen
    says), where (`audience`), for what (`subject_type`), a ceiling and a longest term. Any key reads
    them.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GrantsTemplatesListResponse200]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> GrantsTemplatesListResponse200:
    """List grant templates

     What this account’s agents may ask a person for: a scope (`name`, and the `label` the consent screen
    says), where (`audience`), for what (`subject_type`), a ceiling and a longest term. Any key reads
    them.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GrantsTemplatesListResponse200
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[GrantsTemplatesListResponse200]:
    """List grant templates

     What this account’s agents may ask a person for: a scope (`name`, and the `label` the consent screen
    says), where (`audience`), for what (`subject_type`), a ceiling and a longest term. Any key reads
    them.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GrantsTemplatesListResponse200]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> GrantsTemplatesListResponse200:
    """List grant templates

     What this account’s agents may ask a person for: a scope (`name`, and the `label` the consent screen
    says), where (`audience`), for what (`subject_type`), a ceiling and a longest term. Any key reads
    them.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GrantsTemplatesListResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
