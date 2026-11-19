import json

import httpx
import pytest

from pidgeon import (
    Pidgeon,
    PidgeonError,
    agent_from_env,
    generate_agent_key,
    signed_client,
    verify_agent_request,
)

DIRECTORY = "https://acme.agents.pidgeon.ai"


def recording(answer=None, status=200):
    seen: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return httpx.Response(status, json=answer if answer is not None else {})

    return seen, httpx.Client(transport=httpx.MockTransport(handler))


def test_verify_forwards_the_request():
    seen, http = recording({"valid": False, "verification_id": "ver_1", "reason": "unsigned"})
    answer = Pidgeon("pk_test", client=http).verify(
        "POST", "https://shop.example/signup", {"Signature": "x", "Accept": ["a", "b"]}
    )
    assert answer["verification_id"] == "ver_1"
    (request,) = seen
    assert str(request.url) == "https://pidgeon.ai/v1/verify"
    assert request.headers["authorization"] == "Bearer pk_test"
    assert json.loads(request.content) == {
        "request": {"method": "POST", "url": "https://shop.example/signup",
                    "headers": {"signature": "x", "accept": "a, b"}}
    }


def test_report():
    seen, http = recording({"id": "rep_1"})
    client = Pidgeon("pk_test", "https://pidgeon.test/", client=http)
    assert client.report("ver_1", "spam", "Forty signups.") == {"id": "rep_1"}
    assert str(seen[0].url) == "https://pidgeon.test/v1/reports"
    assert json.loads(seen[0].content) == {
        "verification_id": "ver_1", "category": "spam", "evidence": "Forty signups."
    }


def test_publish_key_is_signed_with_the_key_itself():
    key = generate_agent_key()
    seen, http = recording({"kid": key.kid})
    assert Pidgeon("pk_test", client=http).publish_key("agt 1", key, DIRECTORY) == {"kid": key.kid}
    (request,) = seen
    assert request.url.raw_path == b"/v1/agents/agt%201/keys"
    assert request.headers["authorization"] == "Bearer pk_test"
    assert json.loads(request.content) == {"public_jwk": key.public_jwk}
    result = verify_agent_request(request.method, request.url, request.headers,
                                  lambda kid: key.public_jwk if kid == key.kid else None)
    assert result.ok and result.directory == DIRECTORY


def test_errors_carry_the_api_code():
    _, http = recording({"error": {"code": "forbidden", "message": "Not your agent."}}, status=403)
    with pytest.raises(PidgeonError) as caught:
        Pidgeon("pk_test", client=http).report("ver_1", "spam", "x")
    assert (caught.value.status, caught.value.code, str(caught.value)) == (
        403, "forbidden", "Not your agent."
    )


def test_errors_without_a_body():
    http = httpx.Client(transport=httpx.MockTransport(lambda r: httpx.Response(502, text="bad")))
    with pytest.raises(PidgeonError) as caught:
        Pidgeon("pk_test", client=http).report("ver_1", "spam", "x")
    assert (caught.value.code, caught.value.message) == ("error", "Pidgeon answered 502.")


def test_needs_an_api_key():
    with pytest.raises(ValueError):
        Pidgeon("")


def test_signed_client_signs_every_request():
    key = generate_agent_key()
    seen: list[httpx.Request] = []
    transport = httpx.MockTransport(lambda r: (seen.append(r), httpx.Response(204))[1])
    with signed_client(key.private_jwk, DIRECTORY, transport=transport) as http:
        http.get("https://shop.example/a")
        http.post("https://shop.example/b?q=1", json={"x": 1})
    for request in seen:
        result = verify_agent_request(request.method, request.url, request.headers,
                                      lambda kid: key.public_jwk)
        assert result.ok, result.detail


def test_agent_from_env():
    key = generate_agent_key()
    agent = agent_from_env({"PIDGEON_AGENT_KEY": json.dumps(key.private_jwk),
                            "PIDGEON_DIRECTORY": DIRECTORY})
    headers = agent.sign("GET", "https://shop.example/")
    assert verify_agent_request("GET", "https://shop.example/", headers,
                                lambda kid: key.public_jwk).ok
    with pytest.raises(RuntimeError, match="PIDGEON_AGENT_KEY"):
        agent_from_env({})


# The Email API and webhooks: each method's HTTP method, path, query and body.

INBOX = "11111111-1111-1111-1111-111111111111"
OTHER = "22222222-2222-2222-2222-222222222222"


def call(fn, answer=None, status=200):
    """Run ``fn(client)`` against a recording transport; answer the one request seen."""
    seen, http = recording(answer, status)
    result = fn(Pidgeon("pk_test", client=http))
    (request,) = seen
    body = json.loads(request.content) if request.content else None
    return request.method, request.url.path, dict(request.url.params), body, result


def test_email_groups_share_the_top_level_ones():
    client = Pidgeon("pk_test")
    assert client.email.inboxes is client.inboxes
    assert client.email.messages is client.messages
    assert client.email.drafts is client.drafts


def test_agents_update_revoke_and_revoke_key():
    assert call(lambda c: c.agents.update(INBOX, name="Booking agent"))[:4] == (
        "PATCH", f"/v1/agents/{INBOX}", {}, {"name": "Booking agent"}
    )
    assert call(lambda c: c.agents.revoke(INBOX), status=204)[:2] == (
        "DELETE", f"/v1/agents/{INBOX}"
    )
    assert call(lambda c: c.agents.revoke_key(INBOX, "kid_1"), status=204)[:2] == (
        "DELETE", f"/v1/agents/{INBOX}/keys/kid_1"
    )


def test_pods_rename():
    assert call(lambda c: c.pods.rename(OTHER, "Acme Ltd"))[:4] == (
        "PATCH", f"/v1/pods/{OTHER}", {}, {"name": "Acme Ltd"}
    )


def test_pods_move():
    assert call(lambda c: c.pods.move(OTHER, "agent", INBOX))[:4] == (
        "POST", f"/v1/pods/{OTHER}/move", {}, {"type": "agent", "id": INBOX}
    )


def test_pods_remove():
    assert call(lambda c: c.pods.remove(OTHER), status=204)[:2] == ("DELETE", f"/v1/pods/{OTHER}")


def test_inboxes_create_with_domain():
    assert call(lambda c: c.email.inboxes.create("bookings", domain="acme.com"))[:4] == (
        "POST", "/v1/email/inboxes", {}, {"name": "bookings", "kind": "agent", "domain": "acme.com"}
    )


def test_inboxes_update():
    assert call(lambda c: c.email.inboxes.update(INBOX, hold_suspicious=True))[:4] == (
        "PATCH", f"/v1/email/inboxes/{INBOX}", {}, {"hold_suspicious": True}
    )


def test_messages_list():
    seen = call(lambda c: c.email.messages.list(INBOX, limit=10, cursor="c1", body="clean"))
    assert seen[:4] == (
        "GET", f"/v1/email/inboxes/{INBOX}/messages",
        {"limit": "10", "cursor": "c1", "body": "clean"}, None,
    )


def test_messages_wait_outlasts_the_server():
    seen, http = recording({"data": [], "next_since": "t"})
    Pidgeon("pk_test", client=http).email.messages.wait(INBOX, since="msg_1", timeout=40)
    (request,) = seen
    assert request.method == "GET"
    assert request.url.path == f"/v1/email/inboxes/{INBOX}/messages/await"
    assert dict(request.url.params) == {"since": "msg_1", "timeout": "40"}
    assert request.extensions["timeout"]["read"] == 50
    seen.clear()
    Pidgeon("pk_test", client=http).email.messages.wait(INBOX)
    assert dict(seen[0].url.params) == {}
    assert seen[0].extensions["timeout"]["read"] == 35


def test_messages_get():
    assert call(lambda c: c.email.messages.get(OTHER, body="clean"))[:4] == (
        "GET", f"/v1/email/messages/{OTHER}", {"body": "clean"}, None
    )


def test_messages_update():
    assert call(lambda c: c.email.messages.update(OTHER, seen=False))[:4] == (
        "PATCH", f"/v1/email/messages/{OTHER}", {}, {"seen": False}
    )


def test_messages_send_with_attachments():
    assert call(lambda c: c.email.messages.send(
        INBOX, to=["ana@example.com"], subject="Hi", text="Hello", attachment_ids=[OTHER]
    ))[:4] == (
        "POST", f"/v1/email/inboxes/{INBOX}/messages", {},
        {"to": ["ana@example.com"], "subject": "Hi", "text": "Hello", "attachment_ids": [OTHER]},
    )


def test_drafts_carry_attachments():
    assert call(lambda c: c.email.drafts.update(
        OTHER, to=["ana@example.com"], subject="Hi", attachment_ids=[INBOX]
    ))[3] == {"to": ["ana@example.com"], "subject": "Hi", "attachment_ids": [INBOX]}


def test_search():
    seen = call(lambda c: c.email.search("invoice", inbox_id=INBOX, limit=5, cursor=OTHER))
    assert seen[:4] == (
        "GET", "/v1/email/search",
        {"q": "invoice", "inbox_id": INBOX, "limit": "5", "cursor": OTHER}, None,
    )


def test_contacts_list():
    assert call(lambda c: c.email.contacts.list(inbox_id=INBOX, search="ana", limit=3))[:4] == (
        "GET", "/v1/email/contacts", {"inbox_id": INBOX, "search": "ana", "limit": "3"}, None
    )


def test_contacts_get():
    assert call(lambda c: c.email.contacts.get(OTHER))[:4] == (
        "GET", f"/v1/email/contacts/{OTHER}", {}, None
    )


def test_contacts_update_sends_only_what_is_passed_and_none_clears():
    assert call(lambda c: c.email.contacts.update(OTHER, notes=None))[:4] == (
        "PATCH", f"/v1/email/contacts/{OTHER}", {}, {"notes": None}
    )
    assert call(lambda c: c.email.contacts.update(OTHER, name="Ana"))[3] == {"name": "Ana"}


def test_contacts_remove():
    assert call(lambda c: c.email.contacts.remove(OTHER), status=204)[:4] == (
        "DELETE", f"/v1/email/contacts/{OTHER}", {}, None
    )


def test_threads_list():
    assert call(lambda c: c.email.threads.list(
        inbox_id=INBOX, folder="inbox", label_id=OTHER, status="open", starred=True, limit=20,
        cursor="c",
    ))[:4] == (
        "GET", "/v1/email/threads",
        {"inbox_id": INBOX, "folder": "inbox", "label_id": OTHER, "status": "open",
         "starred": "true", "limit": "20", "cursor": "c"},
        None,
    )


def test_threads_get():
    assert call(lambda c: c.email.threads.get(OTHER, limit=200, body="clean"))[:4] == (
        "GET", f"/v1/email/threads/{OTHER}", {"limit": "200", "body": "clean"}, None
    )


def test_threads_update():
    assert call(lambda c: c.email.threads.update(
        OTHER, owner_type="human", status="human_review", assignee_id=None
    ))[:4] == (
        "PATCH", f"/v1/email/threads/{OTHER}", {},
        {"owner_type": "human", "status": "human_review", "assignee_id": None},
    )
    assert call(lambda c: c.email.threads.update(OTHER, starred=False))[3] == {"starred": False}


def test_threads_remove():
    assert call(lambda c: c.email.threads.remove(OTHER), status=204)[:2] == (
        "DELETE", f"/v1/email/threads/{OTHER}"
    )


def test_threads_add_label():
    assert call(lambda c: c.email.threads.add_label(OTHER, INBOX))[:4] == (
        "POST", f"/v1/email/threads/{OTHER}/labels", {}, {"label_id": INBOX}
    )


def test_threads_remove_label():
    assert call(lambda c: c.email.threads.remove_label(OTHER, INBOX))[:4] == (
        "DELETE", f"/v1/email/threads/{OTHER}/labels/{INBOX}", {}, None
    )


def test_labels_list():
    assert call(lambda c: c.email.labels.list(INBOX))[:4] == (
        "GET", f"/v1/email/inboxes/{INBOX}/labels", {}, None
    )


def test_labels_create():
    assert call(lambda c: c.email.labels.create(INBOX, "Leads", colour="green"))[:4] == (
        "POST", f"/v1/email/inboxes/{INBOX}/labels", {}, {"name": "Leads", "colour": "green"}
    )


def test_labels_update():
    assert call(lambda c: c.email.labels.update(OTHER, colour="red"))[:4] == (
        "PATCH", f"/v1/email/labels/{OTHER}", {}, {"colour": "red"}
    )


def test_labels_remove():
    assert call(lambda c: c.email.labels.remove(OTHER), status=204)[:2] == (
        "DELETE", f"/v1/email/labels/{OTHER}"
    )


def test_attachments_upload_bytes_is_multipart():
    seen, http = recording({"id": OTHER})
    Pidgeon("pk_test", client=http).email.attachments.upload(INBOX, b"%PDF-1", filename="a.pdf")
    (request,) = seen
    assert (request.method, request.url.path) == ("POST", f"/v1/email/inboxes/{INBOX}/attachments")
    assert request.headers["content-type"].startswith("multipart/form-data; boundary=")
    assert request.headers["authorization"] == "Bearer pk_test"
    content = request.content
    assert b'name="file"; filename="a.pdf"' in content
    assert b"Content-Type: application/pdf" in content
    assert b"%PDF-1" in content


def test_attachments_upload_a_path(tmp_path):
    path = tmp_path / "notes.txt"
    path.write_bytes(b"hello")
    seen, http = recording({"id": OTHER})
    Pidgeon("pk_test", client=http).email.attachments.upload(INBOX, path)
    assert b'filename="notes.txt"' in seen[0].content
    assert b"Content-Type: text/plain" in seen[0].content
    with pytest.raises(ValueError):
        Pidgeon("pk_test", client=http).email.attachments.upload(INBOX, b"x")


def test_attachments_upload_large_takes_three_steps():
    seen: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        if request.url.host == "storage.test":
            return httpx.Response(200, json={"Key": "k"})
        if request.url.path.endswith("/uploads"):
            return httpx.Response(201, json={
                "id": OTHER, "upload": {"url": "https://storage.test/put?token=t", "method": "PUT",
                                        "expires_in": 7200},
            })
        return httpx.Response(200, json={"id": OTHER, "ready": True})

    http = httpx.Client(transport=httpx.MockTransport(handler))
    done = Pidgeon("pk_test", client=http).email.attachments.upload_large(
        INBOX, b"0123456789", filename="big.pdf"
    )
    assert done == {"id": OTHER, "ready": True}
    describe, put, complete = seen
    assert (describe.method, describe.url.path) == (
        "POST", f"/v1/email/inboxes/{INBOX}/attachments/uploads"
    )
    assert json.loads(describe.content) == {
        "filename": "big.pdf", "content_type": "application/pdf", "size": 10
    }
    assert (put.method, str(put.url)) == ("PUT", "https://storage.test/put?token=t")
    assert put.content == b"0123456789"
    assert put.headers["content-type"] == "application/pdf"
    assert "authorization" not in put.headers
    assert (complete.method, complete.url.path) == (
        "POST", f"/v1/email/attachments/{OTHER}/complete"
    )


def test_attachments_upload_large_raises_when_the_put_fails():
    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.host == "storage.test":
            return httpx.Response(403, text="expired")
        return httpx.Response(201, json={"id": OTHER, "upload": {"url": "https://storage.test/x"}})

    http = httpx.Client(transport=httpx.MockTransport(handler))
    with pytest.raises(PidgeonError) as caught:
        Pidgeon("pk_test", client=http).email.attachments.upload_large(INBOX, b"x", filename="a")
    assert (caught.value.status, caught.value.code) == (403, "upload_failed")


def test_attachments_get():
    assert call(lambda c: c.email.attachments.get(OTHER))[:4] == (
        "GET", f"/v1/email/attachments/{OTHER}", {}, None
    )


def test_storage():
    answer = {"used_bytes": 1, "limit_bytes": 10}
    assert call(lambda c: c.email.storage(), answer) == (
        "GET", "/v1/email/storage", {}, None, answer
    )


def test_domains_list():
    assert call(lambda c: c.email.domains.list())[:2] == ("GET", "/v1/email/domains")


def test_domains_get():
    assert call(lambda c: c.email.domains.get(OTHER))[:2] == ("GET", f"/v1/email/domains/{OTHER}")


def test_domains_enable_mail():
    assert call(lambda c: c.email.domains.enable_mail(OTHER))[:4] == (
        "POST", f"/v1/email/domains/{OTHER}/mail", {}, None
    )


def test_domains_disable_mail():
    assert call(lambda c: c.email.domains.disable_mail(OTHER), status=204)[:2] == (
        "DELETE", f"/v1/email/domains/{OTHER}/mail"
    )


def test_domains_check():
    assert call(lambda c: c.email.domains.check(OTHER))[:4] == (
        "POST", f"/v1/email/domains/{OTHER}/check", {}, None
    )


def test_app_passwords_list():
    assert call(lambda c: c.email.app_passwords.list(INBOX))[:2] == (
        "GET", f"/v1/email/inboxes/{INBOX}/app-passwords"
    )


def test_app_passwords_create():
    assert call(lambda c: c.email.app_passwords.create(INBOX, "Thunderbird"))[:4] == (
        "POST", f"/v1/email/inboxes/{INBOX}/app-passwords", {}, {"name": "Thunderbird"}
    )


def test_app_passwords_revoke():
    assert call(lambda c: c.email.app_passwords.revoke(OTHER), status=204)[:2] == (
        "DELETE", f"/v1/email/app-passwords/{OTHER}"
    )


def test_calendar_events_list():
    assert call(lambda c: c.email.calendar.events.list(
        INBOX, after="2026-11-01T00:00:00Z", before="2026-12-01T00:00:00Z", limit=50
    ))[:4] == (
        "GET", f"/v1/email/inboxes/{INBOX}/events",
        {"after": "2026-11-01T00:00:00Z", "before": "2026-12-01T00:00:00Z", "limit": "50"}, None,
    )


def test_calendar_events_create():
    assert call(lambda c: c.email.calendar.events.create(
        INBOX, title="Offsite", start="2026-11-20", all_day=True, location="Lisbon"
    ))[:4] == (
        "POST", f"/v1/email/inboxes/{INBOX}/events", {},
        {"title": "Offsite", "start": "2026-11-20", "all_day": True, "location": "Lisbon"},
    )


def test_calendar_events_get():
    assert call(lambda c: c.email.calendar.events.get(OTHER))[:2] == (
        "GET", f"/v1/email/events/{OTHER}"
    )


def test_calendar_events_update():
    seen = call(lambda c: c.email.calendar.events.update(OTHER, title="Lunch", location=None))
    assert seen[:4] == (
        "PATCH", f"/v1/email/events/{OTHER}", {}, {"title": "Lunch", "location": None}
    )


def test_calendar_events_remove():
    assert call(lambda c: c.email.calendar.events.remove(OTHER), status=204)[:2] == (
        "DELETE", f"/v1/email/events/{OTHER}"
    )


def test_test_inbound():
    assert call(lambda c: c.email.test_inbound(
        INBOX, from_="ana@example.com", from_name="Ana", subject="Hi", text="Hello",
        in_reply_to="<m1@pidgeon.ai>",
    ))[:4] == (
        "POST", "/v1/email/test/inbound", {},
        {"inbox_id": INBOX, "from": "ana@example.com", "from_name": "Ana", "subject": "Hi",
         "text": "Hello", "in_reply_to": "<m1@pidgeon.ai>"},
    )


def test_webhooks_list():
    assert call(lambda c: c.webhooks.list())[:4] == ("GET", "/v1/webhooks", {}, None)


def test_webhooks_create():
    seen = call(lambda c: c.webhooks.create("https://acme.example/hook", ["message.received"]))
    assert seen[:4] == (
        "POST", "/v1/webhooks", {},
        {"url": "https://acme.example/hook", "events": ["message.received"]},
    )


def test_webhooks_remove():
    assert call(lambda c: c.webhooks.remove(OTHER), status=204)[:2] == (
        "DELETE", f"/v1/webhooks/{OTHER}"
    )


def test_verify_sends_the_address_for_the_verdict():
    seen, http = recording({"valid": True, "verdict": "v.v.v"})
    Pidgeon("pk_test", client=http).verify(
        "POST", "https://shop.example/signup", {"Signature": "x"}, ip="203.0.113.7"
    )
    assert json.loads(seen[0].content)["ip"] == "203.0.113.7"


def test_check_verdict_posts_the_verdict():
    seen, http = recording({"valid": False, "reason": "used"})
    answer = Pidgeon("pk_test", client=http).check_verdict(
        "v.v.v", origin="https://shop.example", ip="203.0.113.7"
    )
    assert answer == {"valid": False, "reason": "used"}
    (request,) = seen
    assert str(request.url) == "https://pidgeon.ai/v1/verify/verdict"
    assert json.loads(request.content) == {
        "verdict": "v.v.v", "origin": "https://shop.example", "ip": "203.0.113.7"
    }
