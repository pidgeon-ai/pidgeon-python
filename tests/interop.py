"""
A bridge for tests/python-sdk.test.ts: reads one JSON command on stdin and
prints the answer as JSON, so the TypeScript side can check the Python SDK.

  {"op": "generate"}                                  -> {kid, public_jwk, private_jwk}
  {"op": "kid", "jwk": {...}}                         -> {kid}
  {"op": "sign", "method", "url", "private_jwk", "directory", "now"?, "nonce"?}  -> headers
  {"op": "verify", "method", "url", "headers", "public_jwk", "now"?}   -> verification
  {"op": "auth_request", "site", "private_jwk", "directory", "issuer"}  -> {url, headers, body}
  {"op": "auth_verify", "id_token", "client_id", "issuer", "jwks"}       -> claims or {error}
  {"op": "auth_verify_agent", "method", "url", "headers", "client_id", "issuer", "jwks"} -> claims or {error}
  {"op": "api_tour", "base_url", "api_key", "inbox_name"}  -> what each product's calls answered
"""

import json
import sys

import pidgeon


def api_tour(base_url: str, api_key: str, inbox_name: str) -> dict:
    """Every product's calls, against the real routes the TypeScript side serves."""
    with pidgeon.Pidgeon(api_key, base_url) as client:
        set_up = client.agents.set_up("Python agent", "Tests the SDK.")
        agent = client.agents.get(set_up.agent["id"])
        listed = [a["id"] for a in client.agents.list()["data"]]
        inbox = client.inboxes.create(inbox_name)
        sent = client.messages.send(inbox["id"], to=["ana@example.com"], subject="Hi", text="Py.")
        draft = client.drafts.create(inbox["id"], to=["ana@example.com"], subject="D", text="1")
        edited = client.drafts.update(draft["id"], to=["bo@example.com"], subject="D", text="2")
        draft_sent = client.drafts.send(draft["id"])
        site = client.sites.create("Shop", ["https://shop.example/callback"])
        client.sites.remove(site["client_id"])
        pod = client.pods.create("Customer A")
        rule = client.rules.create("receive", "block", "spam.example")
        rules = [r["id"] for r in client.rules.list()["data"]]
        client.rules.remove(rule["id"])
        client.suppressions.add("gone@example.com")
        suppressed = [s["address"] for s in client.suppressions.list()["data"]]
        client.suppressions.remove("gone@example.com")
        try:
            client.drafts.get("00000000-0000-4000-8000-000000000000")
            missing = None
        except pidgeon.PidgeonError as error:
            missing = {"status": error.status, "code": error.code}
        return {
            "agent_id": set_up.agent["id"],
            "kid": set_up.kid,
            "keys": [k["kid"] for k in agent["keys"]],
            "band": agent["reputation"]["band"],
            "listed": listed,
            "address": inbox["address"],
            "sent": sent["status"],
            "edited_to": edited["to"],
            "draft_sent": draft_sent["status"],
            "site_secret": bool(site.get("client_secret")),
            "pods": [p["id"] for p in client.pods.list()["data"]],
            "pod_id": pod["id"],
            "events": [e["type"] for e in client.events.list(limit=50)["data"]],
            "mandates": client.mandates.list()["data"],
            "missing": missing,
            "rule_listed": rule["id"] in rules,
            "rules_after": client.rules.list()["data"],
            "suppressed": suppressed,
            "suppressed_after": client.suppressions.list()["data"],
        }


def main() -> None:
    command = json.load(sys.stdin)
    op = command["op"]
    if op == "generate":
        key = pidgeon.generate_agent_key()
        out = {"kid": key.kid, "public_jwk": key.public_jwk, "private_jwk": key.private_jwk}
    elif op == "kid":
        out = {"kid": pidgeon.key_id_of(command["jwk"])}
    elif op == "sign":
        out = pidgeon.sign_request(
            command["method"],
            command["url"],
            command.get("headers"),
            command["private_jwk"],
            command["directory"],
            now=command.get("now"),
            nonce=command.get("nonce"),
        )
    elif op == "verify":
        published = command["public_jwk"]
        result = pidgeon.verify_agent_request(
            command["method"],
            command["url"],
            command["headers"],
            lambda kid: published if pidgeon.key_id_of(published) == kid else None,
            now=command.get("now"),
        )
        out = {"ok": result.ok, "reason": result.reason, "kid": result.kid,
               "directory": result.directory, "detail": result.detail}
    elif op == "auth_request":
        url, headers, body = pidgeon.auth.agent_sign_in_request(
            command["site"], command["private_jwk"], command["directory"], command["issuer"]
        )
        out = {"url": url, "headers": headers, "body": body}
    elif op == "id_jag_request":
        url, headers, body = pidgeon.auth.id_jag_request(
            command["audience"], command["client_id"], command["private_jwk"],
            command["directory"], command.get("resource"), command.get("scope"), command["issuer"],
        )
        out = {"url": url, "headers": headers, "body": body}
    elif op in ("auth_verify", "auth_verify_agent"):
        try:
            if op == "auth_verify":
                out = pidgeon.auth.verify_id_token(
                    command["id_token"], command["client_id"], command["issuer"], jwks=command["jwks"]
                )
            else:
                out = pidgeon.auth.verify_agent_sign_in(
                    command["method"], command["url"], command["headers"],
                    command["client_id"], command["issuer"], jwks=command["jwks"],
                )
        except pidgeon.auth.SignInError as error:
            out = {"error": error.reason}
    elif op == "api_tour":
        out = api_tour(command["base_url"], command["api_key"], command["inbox_name"])
    else:
        raise SystemExit(f"unknown op {op}")
    json.dump(out, sys.stdout)


if __name__ == "__main__":
    main()
