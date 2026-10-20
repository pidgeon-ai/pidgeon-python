from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.identities_access_create_body import IdentitiesAccessCreateBody
from ...models.identities_access_create_response_200 import IdentitiesAccessCreateResponse200
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: IdentitiesAccessCreateBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/identities/{id}/access".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> IdentitiesAccessCreateResponse200:
    if response.status_code >= 400:
        raise errors.PidgeonError.from_response(response)

    if response.status_code == 200:
        response_200 = IdentitiesAccessCreateResponse200.from_dict(response.json())

        return response_200

    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[IdentitiesAccessCreateResponse200]:
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
    body: IdentitiesAccessCreateBody,
) -> Response[IdentitiesAccessCreateResponse200]:
    """Grant access

     Name exactly one of `user_id`, `api_key_id` or `everyone`. Granting **replaces** any grant that
    principal already had, so calling this twice changes the rung rather than leaving two answers
    behind. Answers 404 rather than 403 when you may not administer the address — including when you can
    read it.

    Args:
        id (str):
        body (IdentitiesAccessCreateBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IdentitiesAccessCreateResponse200]
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
    body: IdentitiesAccessCreateBody,
) -> IdentitiesAccessCreateResponse200:
    """Grant access

     Name exactly one of `user_id`, `api_key_id` or `everyone`. Granting **replaces** any grant that
    principal already had, so calling this twice changes the rung rather than leaving two answers
    behind. Answers 404 rather than 403 when you may not administer the address — including when you can
    read it.

    Args:
        id (str):
        body (IdentitiesAccessCreateBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IdentitiesAccessCreateResponse200
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
    body: IdentitiesAccessCreateBody,
) -> Response[IdentitiesAccessCreateResponse200]:
    """Grant access

     Name exactly one of `user_id`, `api_key_id` or `everyone`. Granting **replaces** any grant that
    principal already had, so calling this twice changes the rung rather than leaving two answers
    behind. Answers 404 rather than 403 when you may not administer the address — including when you can
    read it.

    Args:
        id (str):
        body (IdentitiesAccessCreateBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IdentitiesAccessCreateResponse200]
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
    body: IdentitiesAccessCreateBody,
) -> IdentitiesAccessCreateResponse200:
    """Grant access

     Name exactly one of `user_id`, `api_key_id` or `everyone`. Granting **replaces** any grant that
    principal already had, so calling this twice changes the rung rather than leaving two answers
    behind. Answers 404 rather than 403 when you may not administer the address — including when you can
    read it.

    Args:
        id (str):
        body (IdentitiesAccessCreateBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IdentitiesAccessCreateResponse200
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
