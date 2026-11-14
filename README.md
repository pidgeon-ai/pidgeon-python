# pidgeon

Pidgeon's Python SDK for its four products: Passport (your agents' keys and
reputation), Bouncer (verify agents at your site), Email (inboxes for agents)
and Auth (Sign in with Pidgeon).

Version 2 is for the new Pidgeon. Code written for 1.x (the old email API at
`/api/v1`) keeps working on 1.68.0 until that API is retired.

An agent signs each request with its own Ed25519 key under
[Web Bot Auth](https://datatracker.ietf.org/wg/webbotauth/about/) (HTTP Message
Signatures, RFC 9421). The signature names the operator's directory on
Pidgeon, so a website can tell who stands behind the agent and how they stand.
The output is byte for byte what the TypeScript SDK (`@pidgeon-ai/sdk`) sends.

```sh
pip install pidgeon
```

Python 3.10 or later. Depends on `cryptography` and `httpx`.

## For an agent

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
a client you already have, sync or async. A signature lasts a minute.

## For a website

Forward the request as you received it; Pidgeon checks the signature and
answers with the agent, its operator and their reputation.

```python
from pidgeon import Pidgeon, PidgeonError

pidgeon = Pidgeon(api_key="pk_…")

answer = pidgeon.verify(request.method, request.url, request.headers)
if answer["valid"] and answer["reputation"]["band"] in ("new", "good"):
    ...

pidgeon.report(answer["verification_id"], "fake_signups", "Forty signups in a minute.")
```

Errors raise `PidgeonError` with `status`, `code` and `message`.

Checking only the signature is free and offline: `verify_agent_request(method,
url, headers, find_key)` takes a function from key id to public JWK.

## Sign in with Pidgeon

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

## For an operator's tooling

Set an agent up in one call: it is registered, its key is made here, and only
the public half is published, in a request signed with the key itself (which
is how Pidgeon knows you hold it).

```python
from pidgeon import Pidgeon

pidgeon = Pidgeon(api_key="pgn_…")
made = pidgeon.agents.set_up("Booking agent", "Books tables.")
made.key.private_jwk    # keep it where the agent runs; Pidgeon never sees it
pidgeon.agents.get(made.agent["id"])["reputation"]["band"]
```

Or by hand: `generate_agent_key()` (`key.kid`, `key.public_jwk`,
`key.private_jwk`), then `pidgeon.publish_key(agent_id, key, directory)`.

## Email

```python
inbox = pidgeon.inboxes.create("bookings", agent_id=made.agent["id"])
pidgeon.messages.send(inbox["id"], to=["ana@example.com"], subject="Table for two", text="Friday at 8?")

# A person looks first:
draft = pidgeon.drafts.create(inbox["id"], to=["ana@example.com"], subject="…", text="…")
pidgeon.drafts.request_approval(draft["id"])
```

Also `pidgeon.rules`, `pidgeon.suppressions`, `pidgeon.sites` and
`pidgeon.mandates` (Auth), `pidgeon.events`, `pidgeon.pods`, and
`pidgeon.request(method, path, body)` for any `/v1` call.

The key id is the key's RFC 7638 JWK thumbprint.

## License

Apache-2.0
