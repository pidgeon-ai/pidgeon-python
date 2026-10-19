# Pidgeon for Python

**Mailboxes for AI agents.** Pidgeon is the email inbox API for AI agents. It gives agents their own inboxes
so they can work with emails just like a human.

[pidgeon.ai](https://pidgeon.ai) · [Documentation](https://pidgeon.ai/docs)

```sh
pip install pidgeon
```

Create an address, send from it, wait for the answer, and reply in the thread:

```python
import os

from pidgeon import AuthenticatedClient
from pidgeon.api.identities import identities_create
from pidgeon.api.messages import messages_await, messages_reply, messages_send
from pidgeon.models import (
    Error,
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
if isinstance(created, Error):
    raise RuntimeError(created.error.message)
address = created.data

# 2. Send from it.
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
if not isinstance(awaited, Error) and awaited.data.message:
    print(awaited.data.message.extracted.codes)
    messages_reply.sync(
        awaited.data.message.id,
        client=client,
        body=MessagesReplyBody(text="Thanks, that worked."),
    )
```

`PIDGEON_API_KEY` is a `pgn_live_…` key. Make one at
[pidgeon.ai/app/developers/keys](https://pidgeon.ai/app/developers/keys), or let
your agent sign itself up: [pidgeon.ai/skill.md](https://pidgeon.ai/skill.md).

Webhook signatures verify with `pidgeon.webhooks.verify_webhook`, which does
the timing-safe compare and the replay window for you.

[`examples/openai-agents`](examples/openai-agents) is an OpenAI Agents SDK
agent on the hosted MCP server, which needs no package of ours.

## Contributing

The client is generated from [`openapi.json`](openapi.json), the contract the
API validates against, published at <https://pidgeon.ai/openapi.json>. The
application that serves it is closed source; this client is not. This
repository is copied from that one on every release.

**So a pull request against generated code cannot be merged as written** — the
fix belongs in the schema it came from. Open an issue and say what is wrong.

Issues and questions: [open one](https://github.com/pidgeon-ai/pidgeon-python/issues),
or email [support@pidgeon.ai](mailto:support@pidgeon.ai).

MIT licensed.
