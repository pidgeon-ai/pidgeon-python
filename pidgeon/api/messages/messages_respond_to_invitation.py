from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.messages_respond_to_invitation_body import MessagesRespondToInvitationBody
from ...models.messages_respond_to_invitation_response_200 import MessagesRespondToInvitationResponse200
from ...models.messages_respond_to_invitation_response_202 import MessagesRespondToInvitationResponse202
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: MessagesRespondToInvitationBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/messages/{id}/invitation/respond".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | MessagesRespondToInvitationResponse200 | MessagesRespondToInvitationResponse202 | None:
    if response.status_code == 200:
        response_200 = MessagesRespondToInvitationResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = MessagesRespondToInvitationResponse202.from_dict(response.json())

        return response_202

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
) -> Response[Error | MessagesRespondToInvitationResponse200 | MessagesRespondToInvitationResponse202]:
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
    body: MessagesRespondToInvitationBody,
) -> Response[Error | MessagesRespondToInvitationResponse200 | MessagesRespondToInvitationResponse202]:
    """Accept, decline or tentatively accept a meeting

     The one call here that changes something in somebody else's calendar: an iCalendar `REPLY` goes to
    the organiser, which is how Google, Outlook and Calendly learn about an acceptance. The message must
    be carrying an `invitation`, and one of this mailbox's own addresses must be on it — including an
    address routed to it, which is the half you cannot work out from the message. Idempotent on the
    answer: the same answer to the same `sequence` sends once and returns `already_sent`.

    Args:
        id (str):
        body (MessagesRespondToInvitationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | MessagesRespondToInvitationResponse200 | MessagesRespondToInvitationResponse202]
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
    body: MessagesRespondToInvitationBody,
) -> Error | MessagesRespondToInvitationResponse200 | MessagesRespondToInvitationResponse202 | None:
    """Accept, decline or tentatively accept a meeting

     The one call here that changes something in somebody else's calendar: an iCalendar `REPLY` goes to
    the organiser, which is how Google, Outlook and Calendly learn about an acceptance. The message must
    be carrying an `invitation`, and one of this mailbox's own addresses must be on it — including an
    address routed to it, which is the half you cannot work out from the message. Idempotent on the
    answer: the same answer to the same `sequence` sends once and returns `already_sent`.

    Args:
        id (str):
        body (MessagesRespondToInvitationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | MessagesRespondToInvitationResponse200 | MessagesRespondToInvitationResponse202
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
    body: MessagesRespondToInvitationBody,
) -> Response[Error | MessagesRespondToInvitationResponse200 | MessagesRespondToInvitationResponse202]:
    """Accept, decline or tentatively accept a meeting

     The one call here that changes something in somebody else's calendar: an iCalendar `REPLY` goes to
    the organiser, which is how Google, Outlook and Calendly learn about an acceptance. The message must
    be carrying an `invitation`, and one of this mailbox's own addresses must be on it — including an
    address routed to it, which is the half you cannot work out from the message. Idempotent on the
    answer: the same answer to the same `sequence` sends once and returns `already_sent`.

    Args:
        id (str):
        body (MessagesRespondToInvitationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | MessagesRespondToInvitationResponse200 | MessagesRespondToInvitationResponse202]
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
    body: MessagesRespondToInvitationBody,
) -> Error | MessagesRespondToInvitationResponse200 | MessagesRespondToInvitationResponse202 | None:
    """Accept, decline or tentatively accept a meeting

     The one call here that changes something in somebody else's calendar: an iCalendar `REPLY` goes to
    the organiser, which is how Google, Outlook and Calendly learn about an acceptance. The message must
    be carrying an `invitation`, and one of this mailbox's own addresses must be on it — including an
    address routed to it, which is the half you cannot work out from the message. Idempotent on the
    answer: the same answer to the same `sequence` sends once and returns `already_sent`.

    Args:
        id (str):
        body (MessagesRespondToInvitationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | MessagesRespondToInvitationResponse200 | MessagesRespondToInvitationResponse202
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
