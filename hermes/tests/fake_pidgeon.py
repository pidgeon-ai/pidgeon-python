"""An in-memory Pidgeon API behind `Client`'s opener: the event log, messages,
threads and replies, with the envelopes and strict-after paging the real one has."""

from __future__ import annotations

import io
import json
import urllib.error
import urllib.parse
from datetime import datetime, timedelta, timezone


def iso(moment: datetime) -> str:
    return moment.astimezone(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")


def parse(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


class _Response(io.BytesIO):
    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False


class FakePidgeon:
    def __init__(self):
        self.events: list[dict] = []
        self.messages: dict[str, dict] = {}
        self.replies: list[dict] = []
        self.requests: list[tuple[str, str]] = []
        self.fail: dict[str, int] = {}  # path prefix -> HTTP status, once
        self._ids = 0
        self.access = "send"

    # ------------------------------------------------------------ fixtures

    def receive(self, at: datetime, *, sender="ana@example.com", identity="agent@pidgeon.email",
                subject="Hello", text="Hi there", thread_id=None, **fields) -> dict:
        self._ids += 1
        message = {
            "id": f"msg_{self._ids}",
            "thread_id": thread_id or f"thr_{self._ids}",
            "direction": "inbound",
            "identity": identity,
            "from": {"email": sender, "name": "Ana"},
            "to": [{"email": identity}],
            "subject": subject,
            "text": text,
            "reply_text": text,
            "is_spam": False,
            "firewall": {"verdict": "clean", "signals": []},
            "attachments": [],
            "created_at": iso(at),
            **fields,
        }
        self.messages[message["id"]] = message
        self.events.append({
            "id": f"evt_{self._ids}",
            "type": "message.received",
            "message_id": message["id"],
            "identity": identity,
            "created_at": message["created_at"],
        })
        return message

    def outbound(self, thread_id: str, at: datetime) -> dict:
        self._ids += 1
        message = {"id": f"msg_{self._ids}", "thread_id": thread_id, "direction": "outbound",
                   "created_at": iso(at)}
        self.messages[message["id"]] = message
        return message

    # ------------------------------------------------------------ transport

    def __call__(self, request):
        url = urllib.parse.urlsplit(request.full_url)
        path = url.path.removeprefix("/api/v1")
        query = dict(urllib.parse.parse_qsl(url.query))
        self.requests.append((request.get_method(), path))
        for prefix, status in list(self.fail.items()):
            if path.startswith(prefix):
                del self.fail[prefix]
                return self._error(request, status, "boom", f"Failed {path}.")
        if request.get_header("Authorization") != "Bearer pgn_test":
            return self._error(request, 401, "unauthorized", "That key is not valid.")

        if path == "/me":
            return self._ok({"data": {"kind": "key", "key": {"name": "Hermes", "access": self.access}, "reaches": 1}})
        if path == "/events":
            after = parse(query["after"])
            limit = int(query.get("limit", 100))
            rows = sorted((e for e in self.events if parse(e["created_at"]) > after), key=lambda e: e["created_at"])
            page = rows[:limit]
            more = len(rows) > limit
            return self._ok({"data": page, "has_more": more,
                             "next_cursor": page[-1]["created_at"] if more else None})
        if path == "/messages" and "thread_id" in query:
            rows = [m for m in self.messages.values() if m["thread_id"] == query["thread_id"]]
            return self._ok({"data": rows})
        if path.startswith("/messages/") and path.endswith("/reply"):
            target = urllib.parse.unquote(path.split("/")[2])
            if target not in self.messages:
                return self._error(request, 404, "not_found", "No such message.")
            key = request.get_header("Idempotency-key")
            for reply in self.replies:
                if reply["key"] == key:
                    return self._ok({"data": {"id": reply["id"], "thread_id": reply["thread_id"]}}, 202)
            body = json.loads(request.data)
            sent = self.outbound(self.messages[target]["thread_id"], parse(self.messages[target]["created_at"]) + timedelta(seconds=1))
            self.replies.append({"id": sent["id"], "to": target, "text": body["text"], "key": key,
                                 "thread_id": sent["thread_id"]})
            return self._ok({"data": {"id": sent["id"], "thread_id": sent["thread_id"]}}, 202)
        if path.startswith("/messages/"):
            message_id = urllib.parse.unquote(path.split("/")[2])
            if message_id not in self.messages:
                return self._error(request, 404, "not_found", "No such message.")
            assert query.get("body") == "clean", "the agent must read the Firewall's clean text"
            return self._ok({"data": self.messages[message_id]})
        return self._error(request, 404, "not_found", f"No route {path}.")

    @staticmethod
    def _ok(payload, status=200):
        return _Response(json.dumps(payload).encode())

    @staticmethod
    def _error(request, status, code, message):
        body = io.BytesIO(json.dumps({"error": {"code": code, "message": message}}).encode())
        raise urllib.error.HTTPError(request.full_url, status, message, {}, body)
