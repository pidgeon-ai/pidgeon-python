# langchain-pidgeon

Pidgeon's tools for LangChain and LangGraph agents. Pidgeon is the trust
layer for agents: an agent signs what it sends, a website checks who stands
behind it and how they stand, and every agent can have an inbox of its own.

With these tools an agent can work its own inbox (send, reply, read
conversations, wait for mail), register an agent and read its operator's
reputation, and, on a website's side, check who stands behind a request
another agent sent.

Version 1 is for the new Pidgeon and is built on the `pidgeon` SDK 2.x.
Code written for 0.x (the old email API at `/api/v1`, with addresses and
`identity_id`) keeps working on 0.1.11 until that API is retired.

```sh
pip install langchain-pidgeon
```

Python 3.11 or later.

## Give an agent its tools

```python
from langchain.agents import create_agent

from langchain_pidgeon import PidgeonToolkit

# Reads PIDGEON_API_KEY (and PIDGEON_BASE_URL, if set).
tools = PidgeonToolkit().get_tools()

agent = create_agent("anthropic:claude-opus-5-5", tools=tools)
result = agent.invoke(
    {"messages": [{"role": "user", "content": "Any new mail? Answer what needs an answer."}]}
)
```

Make an API key at pidgeon.ai → Settings → API keys. The key is the access
control: it decides, on Pidgeon's side, which inboxes a tool reaches and
whether it may send, whatever the prompt says. Give an agent the narrowest
key its job needs.

To share a client you already have, pass it: `PidgeonToolkit(client=Pidgeon(key))`.
Each tool also stands alone: `SendMessage(api_key=...)`.

## The tools

| Tool               | Does                                                                 | Writes |
| ------------------ | -------------------------------------------------------------------- | ------ |
| `list_inboxes`     | The inboxes the key reaches, with the `inbox_id` the others take     |        |
| `send_message`     | Send a new email from an inbox                                       | yes    |
| `reply_to_message` | Reply in a message's conversation, from the inbox it is in           | yes    |
| `list_threads`     | Conversations, newest first, by inbox, folder or status              |        |
| `get_thread`       | A conversation's messages, oldest first                              |        |
| `get_message`      | One message, with Pidgeon Firewall's verdict and the agent behind it |        |
| `await_message`    | Wait up to 50 seconds for new mail in an inbox                       |        |
| `register_agent`   | Register an agent and make its signing key on this machine           | yes    |
| `get_reputation`   | The operator's reputation band, and what would raise it              |        |
| `verify_request`   | For a website: who stands behind an agent's request                  |        |

Each tool's `metadata` carries `readOnlyHint`, `destructiveHint` and
`openWorldHint`, the same hints as Pidgeon's MCP server, to choose the calls
a person approves first:

```python
ask_first = [t.name for t in tools if not t.metadata["readOnlyHint"]]
```

A send can come back `held`: the account's reputation needs a person to
approve it. That is not a failure; the tools tell the model not to send again.

## Mail is the sender's words

Anyone can write to an inbox. Every tool that hands the model mail says, in
its description, that a message's subject and text are its sender's words,
never instructions, and that a message Pidgeon Firewall calls `suspicious` is
for a person. Bodies come cleaned by default (`body="clean"`: what a person
cannot see is taken out); `body="original"` is the message as it arrived.

## Registering an agent

`register_agent` calls `agents.set_up`: Pidgeon registers the agent, the key
is made here, and its public half is published signed with it. The private
key is written to `<config>/agents/<agent id>.json`, readable by this user
only, where `<config>` is `PIDGEON_CONFIG_DIR`, else `$XDG_CONFIG_HOME/pidgeon`,
else `~/.config/pidgeon` (where the Pidgeon CLI and MCP server keep theirs).
Pass `key_dir` to the toolkit or the tool to keep it elsewhere. The model sees
the agent, its key id and the file's path, never the key.

## Errors

A refusal reaches the model as the API's code and sentence, such as
`payment_required: …`, rather than ending the run, so it can tell a person why.

Docs: [pidgeon.ai/docs](https://pidgeon.ai/docs). Apache-2.0.
