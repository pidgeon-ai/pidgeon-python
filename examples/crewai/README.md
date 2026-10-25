# Pidgeon with CrewAI

A CrewAI agent that gets an inbox of its own, sends itself a sign-in code and
waits for it to arrive, connected to the hosted MCP server at
`https://pidgeon.ai/api/mcp`. There is no Pidgeon package to install: CrewAI
takes the server as it is.

`PIDGEON_API_KEY` is an admin key. The program uses it to make an address that
expires in an hour and a key for that address alone, with send access and the
same hour. The agent gets only that key. Create the admin key at
[pidgeon.ai/app/developers/keys](https://pidgeon.ai/app/developers/keys).

```sh
pip install -r requirements.txt
PIDGEON_API_KEY=pgn_live_… OPENAI_API_KEY=sk-… python main.py
```

It uses `MODEL` when set, Claude when `ANTHROPIC_API_KEY` is, and
`gpt-5-mini` otherwise.

The guide is at [pidgeon.ai/docs/crewai](https://pidgeon.ai/docs/crewai).

MIT licensed.
