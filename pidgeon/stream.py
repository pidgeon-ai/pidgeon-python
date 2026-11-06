"""Holding the event log open.

The Python twin of ``streamEvents`` (``packages/sdk/src/stream.ts``), and
hand-written for the same reason as ``webhooks.py``: ``GET /events/stream``
answers ``text/event-stream``, and a generated client resolves once with a
body. There is nowhere in it to put a connection that stays open, so the
endpoint the documentation recommends for a caller that cannot host a webhook
endpoint (a script on a laptop, a notebook, an agent runtime with no public
address) was one every customer would otherwise hand-roll.

**Hand-written, and it stays through regeneration**: ``openapi-python-client``
rewrites ``api/``, ``models/`` and ``client.py`` and leaves this alone.

The API key goes in the ``Authorization`` header, never the query string. The
same options as the TypeScript, the same wire parsing, the same reconnection;
``tests/unit/python-stream.test.ts`` runs both against one server and expects
the same events and the same requests.
"""

from __future__ import annotations

import codecs
import json
import threading
from collections.abc import Iterator
from typing import Any

import httpx

__all__ = ["StreamRefused", "stream_events"]

DEFAULT_BASE_URL = "https://pidgeon.ai/api/v1"


class StreamRefused(Exception):
    """Pidgeon refused the stream (401, 403 or 404): it will answer the same way for ever, so it is not retried."""

    def __init__(self, status: int, message: str) -> None:
        super().__init__(message)
        self.status = status


def stream_events(
    *,
    api_key: str,
    base_url: str | None = None,
    identity_id: str | None = None,
    type: str | None = None,
    after: str | None = None,
    signal: threading.Event | None = None,
) -> Iterator[dict[str, Any]]:
    """Every event, as it happens, until you stop asking.

    ::

        for event in stream_events(api_key=KEY):
            if event["type"] == "message.received" and not event["data"].get("from_self"):
                answer(event["data"]["message_id"])

    ``identity_id`` narrows it to one mailbox; ``type`` is a comma-separated
    list, exactly as ``GET /events`` takes it. ``after`` is where to start, as
    an ISO timestamp: ``1970-01-01T00:00:00Z`` reads the whole log from the
    beginning; omitted, the stream starts from now.

    **Reconnection is this function's job and it is lossless.** The server
    closes the connection itself after about 280 seconds so that the last
    thing you receive is a cursor rather than a socket error; this reconnects
    with ``Last-Event-ID``, which the server prefers over ``after``, so there
    is no gap and no repeat. A network failure is retried the same way with a
    short backoff, doubling to thirty seconds.

    It ends when you stop iterating (``break`` closes the connection at once)
    or when ``signal`` is set, which is the TypeScript's ``AbortSignal``: it
    cuts a backoff short, and is checked between reads.
    """
    base = (base_url or DEFAULT_BASE_URL).rstrip("/")
    last_event_id: str | None = None
    backoff = 1.0

    def aborted() -> bool:
        return signal is not None and signal.is_set()

    def wait(seconds: float) -> None:
        if signal is not None:
            signal.wait(seconds)
        else:
            threading.Event().wait(seconds)

    # No read timeout: the server sends a comment while it is quiet, and closes the connection itself.
    with httpx.Client(timeout=httpx.Timeout(10.0, read=None)) as client:
        while not aborted():
            params: dict[str, str] = {}
            if identity_id:
                params["identity_id"] = identity_id
            if type:
                params["type"] = type
            if after and not last_event_id:
                params["after"] = after
            headers = {"authorization": f"Bearer {api_key}", "accept": "text/event-stream"}
            if last_event_id:
                headers["last-event-id"] = last_event_id

            try:
                with client.stream("GET", f"{base}/events/stream", params=params, headers=headers) as response:
                    # A refusal is not a blip: a revoked key or an unreachable mailbox answers the same way
                    # for ever, so retrying would be a loop that never ends and never says why. 429 and the
                    # 5xx family are temporary and are retried.
                    if response.status_code in (401, 403, 404):
                        try:
                            text = response.read().decode("utf-8", errors="replace")
                        except httpx.HTTPError:
                            text = ""
                        raise StreamRefused(
                            response.status_code,
                            f"Pidgeon refused the stream: {response.status_code} {text}".strip(),
                        )

                    if not response.is_success:
                        wait(backoff)
                        backoff = min(backoff * 2, 30.0)
                        continue

                    # Connected. Anything after this is an ordinary close, not a failure.
                    backoff = 1.0

                    for frame in _frames(response, aborted):
                        # The frame's `id:` is a cursor, not the event's id: the event's `created_at`,
                        # because `Last-Event-ID` is handed back in place of `after`, which takes a
                        # timestamp. The event's own id is inside `data`.
                        if frame.get("id"):
                            last_event_id = frame["id"]
                        if not frame.get("data"):
                            continue
                        # The server sends one of these before it gives up, and then closes. It is not
                        # an event; the loop reconnects from the cursor, which is what it says to do.
                        if frame.get("event") == "error":
                            continue
                        try:
                            parsed = json.loads(frame["data"])
                        except ValueError:
                            # A frame we cannot read is one event lost, not a reason to drop the
                            # connection and re-read from a cursor we have already passed.
                            continue
                        yield parsed
            except httpx.TransportError:
                if aborted():
                    return
                wait(backoff)
                backoff = min(backoff * 2, 30.0)
                continue


def _frames(response: httpx.Response, aborted: Any) -> Iterator[dict[str, str]]:
    """The wire format: a frame ends at a blank line; a line starting ``:`` is a comment;
    ``data:`` may repeat, and the pieces join with a newline."""
    decoder = codecs.getincrementaldecoder("utf-8")(errors="replace")
    buffer = ""
    for chunk in response.iter_bytes():
        if aborted():
            return
        buffer += decoder.decode(chunk)
        boundary = buffer.find("\n\n")
        while boundary != -1:
            block = buffer[:boundary]
            buffer = buffer[boundary + 2 :]
            boundary = buffer.find("\n\n")

            frame: dict[str, str] = {}
            data: list[str] = []
            for line in block.split("\n"):
                if line.startswith(":"):
                    continue
                colon = line.find(":")
                if colon == -1:
                    continue
                name = line[:colon]
                # One optional space after the colon, per the spec.
                value = line[colon + 1 :]
                if value.startswith(" "):
                    value = value[1:]
                if name == "id":
                    frame["id"] = value
                elif name == "event":
                    frame["event"] = value
                elif name == "data":
                    data.append(value)
            if data:
                frame["data"] = "\n".join(data)
            if frame.get("id") or frame.get("data"):
                yield frame
