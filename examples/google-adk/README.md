# Pidgeon with the Google ADK

An ADK agent for one Pidgeon inbox, connected to the hosted MCP server at
`https://pidgeon.ai/api/mcp`. There is no Pidgeon package to install: ADK's
`McpToolset` takes the server as it is.

Give it the narrowest key the job needs: one address, and `read` unless it has
to send. Create one at [pidgeon.ai/app/developers/keys](https://pidgeon.ai/app/developers/keys).

```sh
pip install -r requirements.txt
export PIDGEON_API_KEY=pgn_live_… GOOGLE_API_KEY=…
adk web
```

`adk run pidgeon_agent` runs it in the terminal instead. Anything that changes
the inbox waits for you to confirm it.

The guide is at [pidgeon.ai/docs/google-adk](https://pidgeon.ai/docs/google-adk).

MIT licensed.
