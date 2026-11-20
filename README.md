# pidgeon

Email inboxes for AI agents. Give each agent its own address on
@pidgeon.email or your own domain, or give every user of your platform inboxes
of their own. Plus Sign in with Pidgeon. https://pidgeon.ai

Version 2 is for the new Pidgeon. Code written for 1.x (the old email API at
`/api/v1`) keeps working on 1.68.0 until that API is retired.

```sh
pip install pidgeon
```

Python 3.10 or later. Depends on `cryptography` and `httpx`.

## Give an agent an inbox

Everything Email does is under `pidgeon.email`; each call answers the API's
JSON as a `dict`. Create an inbox, send, and wait for the reply:

```python
from pidgeon import Pidgeon

pidgeon = Pidgeon(api_key="pgn_…")
inbox = pidgeon.email.inboxes.create("bookings")  # bookings@pidgeon.email

# Send, with a file:
pdf = pidgeon.email.attachments.upload(inbox["id"], "menu.pdf")
pidgeon.email.messages.send(inbox["id"], to=["ana@example.com"], subject="Table for two",
                            text="Friday at 8?", attachment_ids=[pdf["id"]])

# Wait for the answer (up to 50 seconds a call), then read it cleaned:
got = pidgeon.email.messages.wait(inbox["id"], timeout=50)
for message in got["data"]:
    pidgeon.email.messages.get(message["id"], body="clean")
    pidgeon.email.messages.update(message["id"], seen=True)

# A person looks first:
draft = pidgeon.email.drafts.create(inbox["id"], to=["ana@example.com"], subject="…", text="…")
pidgeon.email.drafts.request_approval(draft["id"])

# Hand a conversation to a person:
thread = pidgeon.email.threads.list(inbox_id=inbox["id"], status="open")["data"][0]
pidgeon.email.threads.update(thread["id"], owner_type="human", status="human_review")
```

On your own domain, pass `domain="example.com"` once mail is on for it
(`pidgeon.email.domains.enable_mail`).

Also under `pidgeon.email`: `messages.list`, `search(q)`, `threads`
(`get`, `remove`, `add_label`, `remove_label`), `labels`, `contacts`,
`attachments.upload_large` (up to 25 MB: describe, put and complete in one
call) and `attachments.get`, `storage()`, `inboxes.update(hold_suspicious=True)`,
`domains` (`enable_mail`, `disable_mail`, `check`), `app_passwords` for mail
apps, `calendar.events`, `rules`, `suppressions`, and `test_inbound` (with a
test key, deliver mail to your inbox as if someone sent it).

Errors raise `PidgeonError` with `status`, `code` and `message`. A PATCH
sends only the fields you pass; `None` clears one that can be cleared
(`contacts.update(id, notes=None)`).

`pidgeon.webhooks` (`list`, `create`, `remove`) adds endpoints for the
account's events; check their signatures with `verify_webhook`. Also
`pidgeon.sites` and `pidgeon.mandates` (Sign in with Pidgeon), `pidgeon.events`,
`pidgeon.pods`, and `pidgeon.request(method, path, body)` for any `/v1` call.

## For platforms

Give every user of your platform inboxes of their own, white-labelled on their
own domain. Each user gets a pod; a key of that pod reaches only its mail.

```python
pod = pidgeon.pods.create("Acme Ltd")
# acme.com is the user's domain, with mail on, in their pod.
inbox = pidgeon.email.inboxes.create("support", pod_id=pod["id"], domain="acme.com")
key = pidgeon.keys.create("Acme", access="send", pod_id=pod["id"])["key"]
```

## Sign in with Pidgeon

Agents sign in to websites as themselves, with a key of their own.

### Set an agent up

Set an agent up in one call: it is registered, its key is made here, and only
the public half is published, in a request signed with the key itself (which
is how Pidgeon knows you hold it).

```python
made = pidgeon.agents.set_up("Booking agent", "Books tables.")
made.key.private_jwk    # keep it where the agent runs; Pidgeon never sees it
```

Or by hand: `generate_agent_key()` (`key.kid`, `key.public_jwk`,
`key.private_jwk`), then `pidgeon.publish_key(agent_id, key, directory)`.

### Sign its requests

Your agent's page on pidgeon.ai gives you `PIDGEON_AGENT_KEY` and
`PIDGEON_DIRECTORY`. Then every request you send through the client is signed:

```python
from pidgeon import agent_from_env

with agent_from_env().client() as http:
    http.post("https://shop.example/signup", json={"email": "agent@example.com"})
```

Or with a key you hold yourself:

```python
from pidgeon import signed_client, sign_request

http = signed_client(private_jwk, "https://acme.agents.pidgeon.ai")

# Without httpx: the three headers to add to any request.
headers = sign_request("POST", "https://shop.example/signup", None,
                       private_jwk, "https://acme.agents.pidgeon.ai")
```

`AgentAuth(private_jwk, directory)` is the same signer as an `httpx.Auth`, for
a client you already have, sync or async. A signature covers the host,
method, path and query, carries a new nonce, and lasts a minute. Pidgeon
accepts a signature once, so sign again to retry; never resend old signature
headers.

An agent's key id is the key's RFC 7638 JWK thumbprint.

### Your site

Register it with `pidgeon.sites.create(name, redirect_uris)`, and ask a person
to let your agent act for them with `pidgeon.mandates.create(…)`.

People sign in to your site with any OpenID Connect library: the issuer is
`https://pidgeon.ai`, with the client id and secret you registered. Check an ID
token with `verify_id_token(id_token, client_id)`.

An agent signs in with no person present, and sends its ID token with every
request it signs:

```python
from pidgeon import signed_client
from pidgeon.auth import sign_in_as_agent

session = sign_in_as_agent("site_…", key.private_jwk, "https://acme.agents.pidgeon.ai")
shop = signed_client(key.private_jwk, "https://acme.agents.pidgeon.ai",
                     headers={"authorization": f"Bearer {session.id_token}"})
```

Your site accepts the request only when it is signed with the key the token
names, so a copied token is useless on its own:

```python
from pidgeon.auth import verify_agent_sign_in, SignInError

claims = verify_agent_sign_in(request.method, request.url, request.headers, "site_…")
claims["sub"], claims["agent"], claims["account"], claims["reputation"]
```

For an MCP server whose authorization server trusts Pidgeon, the agent asks
for an ID-JAG and presents it there as a JWT bearer grant:

```python
from pidgeon.auth import request_id_jag

id_jag = request_id_jag("https://auth.example.com", "https://agent.example.com/oauth/client.json",
                        key.private_jwk, "https://acme.agents.pidgeon.ai",
                        resource="https://mcp.example.com/mcp")
```

## License

Apache-2.0
