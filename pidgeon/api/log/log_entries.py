from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.log_entries_response_200 import LogEntriesResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    start: int | Unset = 0,
    end: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["start"] = start

    params["end"] = end

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/log/entries",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> LogEntriesResponse200:
    if response.status_code >= 400:
        raise errors.PidgeonError.from_response(response)

    if response.status_code == 200:
        response_200 = LogEntriesResponse200.from_dict(response.json())

        return response_200

    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[LogEntriesResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    start: int | Unset = 0,
    end: int | Unset = UNSET,
) -> Response[LogEntriesResponse200]:
    """List card log entries

     Public, with no key. Entries from `start` up to `end`, at most 100. An entry is one card subject’s
    claims at the moment they changed: `issued`, `updated` or `revoked`. `data` is its exact bytes,
    canonical JSON; a leaf hash is SHA-256 of 0x00 and `data`. Entries never change.

    Args:
        start (int | Unset): The first entry’s index. Default: 0.
        end (int | Unset): One past the last entry’s index. At most 100 are returned.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LogEntriesResponse200]
    """

    kwargs = _get_kwargs(
        start=start,
        end=end,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    start: int | Unset = 0,
    end: int | Unset = UNSET,
) -> LogEntriesResponse200:
    """List card log entries

     Public, with no key. Entries from `start` up to `end`, at most 100. An entry is one card subject’s
    claims at the moment they changed: `issued`, `updated` or `revoked`. `data` is its exact bytes,
    canonical JSON; a leaf hash is SHA-256 of 0x00 and `data`. Entries never change.

    Args:
        start (int | Unset): The first entry’s index. Default: 0.
        end (int | Unset): One past the last entry’s index. At most 100 are returned.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LogEntriesResponse200
    """

    return sync_detailed(
        client=client,
        start=start,
        end=end,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    start: int | Unset = 0,
    end: int | Unset = UNSET,
) -> Response[LogEntriesResponse200]:
    """List card log entries

     Public, with no key. Entries from `start` up to `end`, at most 100. An entry is one card subject’s
    claims at the moment they changed: `issued`, `updated` or `revoked`. `data` is its exact bytes,
    canonical JSON; a leaf hash is SHA-256 of 0x00 and `data`. Entries never change.

    Args:
        start (int | Unset): The first entry’s index. Default: 0.
        end (int | Unset): One past the last entry’s index. At most 100 are returned.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LogEntriesResponse200]
    """

    kwargs = _get_kwargs(
        start=start,
        end=end,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    start: int | Unset = 0,
    end: int | Unset = UNSET,
) -> LogEntriesResponse200:
    """List card log entries

     Public, with no key. Entries from `start` up to `end`, at most 100. An entry is one card subject’s
    claims at the moment they changed: `issued`, `updated` or `revoked`. `data` is its exact bytes,
    canonical JSON; a leaf hash is SHA-256 of 0x00 and `data`. Entries never change.

    Args:
        start (int | Unset): The first entry’s index. Default: 0.
        end (int | Unset): One past the last entry’s index. At most 100 are returned.

    Raises:
        errors.PidgeonError: If the API answers with a failure, 400 or above. It carries the API's `code`, `message` and `field`.
        errors.UnexpectedStatus: If the API answers with any other status this operation does not declare.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LogEntriesResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            start=start,
            end=end,
        )
    ).parsed
