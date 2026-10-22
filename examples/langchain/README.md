# Pidgeon with LangChain

A command-line agent for one Pidgeon mailbox, built with LangChain's
`create_agent` and the tools from
[`langchain-pidgeon`](https://pypi.org/project/langchain-pidgeon/).

Give it the narrowest key the job needs: one address, and `read` unless it has
to send. Create one at [pidgeon.ai/app/developers/keys](https://pidgeon.ai/app/developers/keys).

```sh
pip install -r requirements.txt
PIDGEON_API_KEY=pgn_live_… ANTHROPIC_API_KEY=sk-ant-… python main.py "What came in today?"
```

`OPENAI_API_KEY` works in place of `ANTHROPIC_API_KEY`, and `MODEL` picks
any model `create_agent` takes, such as `openai:gpt-5-mini`. Anything that is
not read-only stops and asks at the prompt first.

`python main.py --check` needs no model. It makes an address that expires in
an hour, mails it a code, waits for the code, replies, and hands the
conversation to a person, then deletes the address (an `admin` key; with
`send` it is left to expire): every tool except
search.
The key needs `send` for it.

The guide is at [pidgeon.ai/docs/langchain](https://pidgeon.ai/docs/langchain).

MIT licensed.
