from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.metrics_query_response_200 import MetricsQueryResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    days: int | Unset = UNSET,
    identity_id: UUID | Unset = UNSET,
    pod_id: UUID | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["days"] = days

    json_identity_id: str | Unset = UNSET
    if not isinstance(identity_id, Unset):
        json_identity_id = str(identity_id)
    params["identity_id"] = json_identity_id

    json_pod_id: str | Unset = UNSET
    if not isinstance(pod_id, Unset):
        json_pod_id = str(pod_id)
    params["pod_id"] = json_pod_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/metrics",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MetricsQueryResponse200:
    if response.status_code >= 400:
        raise errors.PidgeonError.from_response(response)

    if response.status_code == 200:
        response_200 = MetricsQueryResponse200.from_dict(response.json())

        return response_200

    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[MetricsQueryResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    days: int | Unset = UNSET,
    identity_id: UUID | Unset = UNSET,
    pod_id: UUID | Unset = UNSET,
) -> Response[MetricsQueryResponse200]:
    """What happened to the mail

     Counted from the event log rather than from the messages: a message row says what was sent, and
    whether it bounced is something the provider told us afterwards. `identity_id` narrows it to one
    mailbox, which is the question worth asking when you run several — reputation belongs to the address
    that sent the mail. `pod_id` narrows it to one pod, which is the question a platform asks: sending
    reputation is isolated per pod, so this is the scope that isolation is claimed at, and the response
    carries `reputation.sending` — `paused` is the provider having suspended that pod and nobody else.
    `delivery_rate` is null rather than zero when nothing was sent. An unknown parameter is refused
    rather than ignored.

    Args:
        days (int | Unset):
        identity_id (UUID | Unset):
        pod_id (UUID | Unset):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MetricsQueryResponse200]
    """

    kwargs = _get_kwargs(
        days=days,
        identity_id=identity_id,
        pod_id=pod_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    days: int | Unset = UNSET,
    identity_id: UUID | Unset = UNSET,
    pod_id: UUID | Unset = UNSET,
) -> MetricsQueryResponse200:
    """What happened to the mail

     Counted from the event log rather than from the messages: a message row says what was sent, and
    whether it bounced is something the provider told us afterwards. `identity_id` narrows it to one
    mailbox, which is the question worth asking when you run several — reputation belongs to the address
    that sent the mail. `pod_id` narrows it to one pod, which is the question a platform asks: sending
    reputation is isolated per pod, so this is the scope that isolation is claimed at, and the response
    carries `reputation.sending` — `paused` is the provider having suspended that pod and nobody else.
    `delivery_rate` is null rather than zero when nothing was sent. An unknown parameter is refused
    rather than ignored.

    Args:
        days (int | Unset):
        identity_id (UUID | Unset):
        pod_id (UUID | Unset):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MetricsQueryResponse200
    """

    return sync_detailed(
        client=client,
        days=days,
        identity_id=identity_id,
        pod_id=pod_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    days: int | Unset = UNSET,
    identity_id: UUID | Unset = UNSET,
    pod_id: UUID | Unset = UNSET,
) -> Response[MetricsQueryResponse200]:
    """What happened to the mail

     Counted from the event log rather than from the messages: a message row says what was sent, and
    whether it bounced is something the provider told us afterwards. `identity_id` narrows it to one
    mailbox, which is the question worth asking when you run several — reputation belongs to the address
    that sent the mail. `pod_id` narrows it to one pod, which is the question a platform asks: sending
    reputation is isolated per pod, so this is the scope that isolation is claimed at, and the response
    carries `reputation.sending` — `paused` is the provider having suspended that pod and nobody else.
    `delivery_rate` is null rather than zero when nothing was sent. An unknown parameter is refused
    rather than ignored.

    Args:
        days (int | Unset):
        identity_id (UUID | Unset):
        pod_id (UUID | Unset):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MetricsQueryResponse200]
    """

    kwargs = _get_kwargs(
        days=days,
        identity_id=identity_id,
        pod_id=pod_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    days: int | Unset = UNSET,
    identity_id: UUID | Unset = UNSET,
    pod_id: UUID | Unset = UNSET,
) -> MetricsQueryResponse200:
    """What happened to the mail

     Counted from the event log rather than from the messages: a message row says what was sent, and
    whether it bounced is something the provider told us afterwards. `identity_id` narrows it to one
    mailbox, which is the question worth asking when you run several — reputation belongs to the address
    that sent the mail. `pod_id` narrows it to one pod, which is the question a platform asks: sending
    reputation is isolated per pod, so this is the scope that isolation is claimed at, and the response
    carries `reputation.sending` — `paused` is the provider having suspended that pod and nobody else.
    `delivery_rate` is null rather than zero when nothing was sent. An unknown parameter is refused
    rather than ignored.

    Args:
        days (int | Unset):
        identity_id (UUID | Unset):
        pod_id (UUID | Unset):

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MetricsQueryResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            days=days,
            identity_id=identity_id,
            pod_id=pod_id,
        )
    ).parsed
