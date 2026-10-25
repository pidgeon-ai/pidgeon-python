# langchain-pidgeon

Pidgeon is the email inbox API for AI agents. It gives agents their own inboxes
so they can work with emails just like a human. This package is its tools for
LangChain and LangGraph agents.

```sh
pip install langchain-pidgeon
```

## Give an agent an inbox

```python
from langchain.agents import create_agent

from langchain_pidgeon import PidgeonToolkit

# Reads PIDGEON_API_KEY.
tools = PidgeonToolkit().get_tools()

agent = create_agent("anthropic:claude-sonnet-5-5", tools=tools)
result = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "Make an address on pidgeon.email, then wait for the code "
                "I am about to send it and tell me what it is.",
            }
        ]
    }
)
print(result["messages"][-1].content)
```

`PIDGEON_API_KEY` is a `pgn_live_…` key. Make one at
[pidgeon.ai/app/developers/keys](https://pidgeon.ai/signup?utm_source=pypi&utm_medium=readme&utm_campaign=langchain&next=/app/developers/keys), or
let your agent sign itself up: [pidgeon.ai/skill.md](https://pidgeon.ai/skill.md)
is two calls, and the only thing it needs from a person is a six-digit code.

## The tools

The same tools as Pidgeon's hosted MCP server, by name, each one call of the
[`pidgeon`](https://pypi.org/project/pidgeon/) SDK.

| Tool               | What it does                                                              | Kind        |
| ------------------ | ------------------------------------------------------------------------- | ----------- |
| `list_addresses`   | The addresses the key can reach, with the ids the other tools take        | Read-only   |
| `create_address`   | A new address for the agent; anybody can then write to it                 | Open world  |
| `list_messages`    | One conversation, oldest first                                            | Read-only   |
| `search_messages`  | Full-text search across every address the key reaches                     | Read-only   |
| `get_message`      | One message, cleaned by Pidgeon Firewall unless you ask for the original  | Read-only   |
| `await_message`    | Waits up to 280 seconds for the next message and returns its codes, links | Read-only   |
| `send_message`     | A new message to anybody                                                  | Destructive |
| `reply_to_message` | An answer in the same conversation; recipients come off the original      | Destructive |
| `update_thread`    | Hands a conversation to a person, or takes it back                        | Reversible  |

Each tool's `metadata` carries the server's four hints: `readOnlyHint`,
`destructiveHint`, `idempotentHint` and `openWorldHint`. Use them to choose
which calls wait for a person:

```python
from langchain.agents import create_agent
from langchain.agents.middleware import HumanInTheLoopMiddleware
from langgraph.checkpoint.memory import InMemorySaver

from langchain_pidgeon import PidgeonToolkit

tools = PidgeonToolkit().get_tools()
asks_first = {tool.name: True for tool in tools if not tool.metadata["readOnlyHint"]}

agent = create_agent(
    "anthropic:claude-sonnet-5-5",
    tools=tools,
    middleware=[HumanInTheLoopMiddleware(interrupt_on=asks_first)],
    checkpointer=InMemorySaver(),
)
```

Bodies arrive cleaned: hidden text removed and fake chat turns marked. Every
message carries `firewall`, and `suspicious` means it tries to steer the
model. A refusal reaches the model as the API's own sentence, so it can tell a
person why instead of retrying.

## The key is the whole of the access control

Nothing in this package decides what the agent may reach. The key does, on the
server, whatever the prompt says. Give it the narrowest one the job needs:

- **One address.** A key lists the addresses it reaches, so an agent holding a
  key for `support@yourdomain.com` cannot read `payroll@`. A key that creates
  an address can reach the address it created.
- **The lowest level that does the job.** An agent that triages needs `read`,
  and a `read` key cannot send. One that answers needs `send`.

`PidgeonToolkit(api_key=...)` takes a key directly, and `client=` takes a
`pidgeon.AuthenticatedClient` you have built yourself.

Documentation: [pidgeon.ai/docs/langchain](https://pidgeon.ai/docs/langchain) ·
[a runnable example](https://github.com/pidgeon-ai/pidgeon-python/tree/main/examples/langchain).

MIT licensed.
