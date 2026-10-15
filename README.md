# Pidgeon for Python

**Mailboxes for AI agents.** Give your agents a proper mailbox, on a domain
you own, so they can run email like you would — [pidgeon.ai](https://pidgeon.ai).

```sh
pip install pidgeon
```

```python
import os
from pidgeon import AuthenticatedClient
from pidgeon.api.identities import identities_list

client = AuthenticatedClient(
    base_url="https://pidgeon.ai/api/v1",
    token=os.environ["PIDGEON_API_KEY"],
)

print(identities_list.sync(client=client))
```

Webhook signatures verify with `pidgeon.webhooks.verify_webhook`, which does
the timing-safe compare and the replay window for you.

## This repository is generated

The client is generated from [`openapi.json`](openapi.json), the contract the
API validates against, published at <https://pidgeon.ai/openapi.json>. The
application that serves it is closed source; this client is not.

**So a pull request against generated code cannot be merged as written** — the
fix belongs in the schema it came from. Open an issue and say what is wrong.

Issues and questions: [open one](https://github.com/pidgeon-ai/pidgeon-python/issues),
or email [support@pidgeon.ai](mailto:support@pidgeon.ai). Documentation lives
at [pidgeon.ai/docs](https://pidgeon.ai/docs).

MIT licensed.
