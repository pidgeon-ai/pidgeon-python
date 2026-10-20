# pidgeon

[![M8ven Score](https://m8ven.ai/badge/mcp/pidgeon-ai-pidgeon-python-14x4fi?v=7839ce033bbaf81a694644e5d0dce78c)](https://m8ven.ai/mcp/pidgeon-ai-pidgeon-python-14x4fi?s=readme)

Pidgeon is the email inbox API for AI agents. It gives agents their own inboxes
so they can work with emails just like a human. This is its Python client.

```sh
pip install pidgeon
```

## Create an address, send, receive, reply

```python
import os

from pidgeon import AuthenticatedClient
from pidgeon.api.identities import identities_create
from pidgeon.api.messages import messages_await, messages_reply, messages_send
from pidgeon.models import (
    IdentitiesCreateBody,
    IdentitiesCreateBodyType,
    MessagesReplyBody,
    MessagesSendBody,
)

client = AuthenticatedClient(
    base_url="https://pidgeon.ai/api/v1",
    token=os.environ["PIDGEON_API_KEY"],
)

# 1. An address of its own. Any free name on pidgeon.email works with no DNS.
created = identities_create.sync(
    client=client,
    body=IdentitiesCreateBody(address="scout@pidgeon.email", type_=IdentitiesCreateBodyType.AGENT),
)
address = created.data

# 2. Send from it. A refusal raises PidgeonError; it never comes back as a value.
messages_send.sync(
    client=client,
    body=MessagesSendBody(
        from_=address.email,
        to="ops@example.com",
        subject="Staging access",
        text="Could you send me the access code?",
    ),
)

# 3. Receive: one held-open request until the answer arrives, up to 60 seconds.
awaited = messages_await.sync(client=client, identity_id=address.id, timeout=60)

# 4. Reply into the same conversation. Recipients and subject come off the original.
if awaited.data.message:
    print(awaited.data.message.extracted.codes)
    messages_reply.sync(
        awaited.data.message.id,
        client=client,
        body=MessagesReplyBody(text="Thanks, that worked."),
    )
```

`PIDGEON_API_KEY` is a `pgn_live_…` key. Make one at
[pidgeon.ai/app/developers/keys](https://pidgeon.ai/app/developers/keys), or
let your agent sign itself up: [pidgeon.ai/skill.md](https://pidgeon.ai/skill.md)
is two calls, and the only thing it needs from a person is a six-digit code.

In production, take a [signed webhook](#receiving) rather than holding a
request open. Documentation: [pidgeon.ai/docs](https://pidgeon.ai/docs) ·
[OpenAPI](https://pidgeon.ai/openapi.json).

Generated from `openapi.json`, the same document the TypeScript client is
generated from, so an operation has the same name in both:
`messages_send` here is `messagesSend` there. Every call takes the client;
nothing is global.

## Errors

**A failure raises `PidgeonError`.** Every call returns the success model or
raises, so a refused send cannot pass for a sent one. `code` is the API's own
and is what to branch on, `message` is written for a person and safe to show
one, `field` names the input at fault, and `retry_after` is in seconds when a
limit says when to come back:

```python
from pidgeon.errors import PidgeonError

try:
    messages_send.sync(client=client, body=body)
except PidgeonError as error:
    if error.code == "abuse_blocked":
        ...  # nothing was sent; error.retry_after says when the allowance frees up
    raise
```

**Since 1.19.0.** Before it, a call returned `Error` for a failure the
OpenAPI document declared and `None` for one it did not, and a `403` on a
send was one it did not: code that checked `isinstance(result, Error)` now
sees the exception instead. `raise_on_unexpected_status` no longer changes
anything; a status the client cannot read always raises.

**`from_` and `type_` carry a trailing underscore**, because `from` and `type`
are reserved in Python. The wire names are unchanged.

Every operation also has `asyncio`, and `sync_detailed` / `asyncio_detailed`
variants that return the whole `Response` with its status and headers.

## Receiving

Mail arriving at an address your code owns becomes an event, and your endpoint
is called with a signed payload. **Verify before you parse** — an unverified
payload is an unauthenticated POST that claims a message arrived.

```python
from pidgeon.webhooks import verify_webhook

event = verify_webhook(
    raw_body=request.body,  # the exact bytes, before any json.loads
    headers=request.headers,
    secret=os.environ["PIDGEON_WEBHOOK_SECRET"],
)
```

`raw_body` must be the bytes we sent. Parse the JSON *after* verifying —
re-serialising changes key order and the signature will not match.
`verify_webhook` raises rather than returning a boolean, rejects a timestamp
outside five minutes before it looks at the signature, and compares in
constant time.

The event carries ids, never a body. Exchange one for the content with
`messages_get`.

## Creating an address

```python
from pidgeon.api.identities import identities_create
from pidgeon.models import (
    IdentitiesCreateBody,
    IdentitiesCreateBodySendPolicy,
    IdentitiesCreateBodyType,
)

identities_create.sync(
    client=client,
    body=IdentitiesCreateBody(
        address="receipts@yourdomain.com",
        type_=IdentitiesCreateBodyType.AGENT,
        send_policy=IdentitiesCreateBodySendPolicy.REPLY_ONLY,
    ),
)
```

Say where with `address`, `domain` or `domain_id` — one of the three. Every
address you already have carries its `domain_id`, which is what to use when
you are on the shared domain and own nothing to list.

`send_policy=IdentitiesCreateBodySendPolicy.REPLY_ONLY` makes an address structurally unable to write to
anybody who has not written to it first, which is the right default for
software.

## Pagination

A list returns a page, not an iterator — deliberately. An iterator that hides
pagination also hides the rate limit pagination is subject to.

```python
from pidgeon.api.events import events_list

cursor = None
while True:
    page = events_list.sync(client=client, cursor=cursor)
    for event in page.data:
        handle(event)

    cursor = page.next_cursor
    if cursor is None:
        break
```

## What this deliberately does not do

No retry policy, no queue, no caching, no auto-paginating iterator. Those are
decisions that belong to your application — an SDK that makes them for you is
one you eventually work around.

## Versioning

Versioned independently of the API. The API is `/v1`; this package is `1.x`,
and semver applies to its own surface.

Full reference: [pidgeon.ai/docs](https://pidgeon.ai/docs).

## Contributing

This client is generated from [`openapi.json`](https://pidgeon.ai/openapi.json),
the contract the API validates against, and published from
[pidgeon-ai/pidgeon-python](https://github.com/pidgeon-ai/pidgeon-python). A
pull request against generated code cannot be merged as written — the fix
belongs in the schema. [Open an issue](https://github.com/pidgeon-ai/pidgeon-python/issues)
and say what is wrong, or email [support@pidgeon.ai](mailto:support@pidgeon.ai).

MIT licensed.
