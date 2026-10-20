from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.pods_update_body import PodsUpdateBody
from ...models.pods_update_response_200 import PodsUpdateResponse200
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: PodsUpdateBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/pods/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PodsUpdateResponse200:
    if response.status_code >= 400:
        raise errors.PidgeonError.from_response(response)

    if response.status_code == 200:
        response_200 = PodsUpdateResponse200.from_dict(response.json())

        return response_200

    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PodsUpdateResponse200]:
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
    body: PodsUpdateBody,
) -> Response[PodsUpdateResponse200]:
    """Rename a pod, or change its client id

     There is no delete. A container holding mailboxes is not a thing to remove with one call, and
    nothing yet moves addresses between pods — so the verb would either refuse every non-empty pod or
    destroy mail. Suspend the addresses instead.

    Args:
        id (str):
        body (PodsUpdateBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PodsUpdateResponse200]
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
    body: PodsUpdateBody,
) -> PodsUpdateResponse200:
    """Rename a pod, or change its client id

     There is no delete. A container holding mailboxes is not a thing to remove with one call, and
    nothing yet moves addresses between pods — so the verb would either refuse every non-empty pod or
    destroy mail. Suspend the addresses instead.

    Args:
        id (str):
        body (PodsUpdateBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PodsUpdateResponse200
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
    body: PodsUpdateBody,
) -> Response[PodsUpdateResponse200]:
    """Rename a pod, or change its client id

     There is no delete. A container holding mailboxes is not a thing to remove with one call, and
    nothing yet moves addresses between pods — so the verb would either refuse every non-empty pod or
    destroy mail. Suspend the addresses instead.

    Args:
        id (str):
        body (PodsUpdateBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PodsUpdateResponse200]
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
    body: PodsUpdateBody,
) -> PodsUpdateResponse200:
    """Rename a pod, or change its client id

     There is no delete. A container holding mailboxes is not a thing to remove with one call, and
    nothing yet moves addresses between pods — so the verb would either refuse every non-empty pod or
    destroy mail. Suspend the addresses instead.

    Args:
        id (str):
        body (PodsUpdateBody):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PodsUpdateResponse200
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
