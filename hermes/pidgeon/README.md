# Pidgeon for Hermes Agent

Email for [Hermes Agent](https://github.com/NousResearch/hermes-agent). Mail
to your agent's [Pidgeon](https://pidgeon.ai) address starts a Hermes
conversation, one per email thread, and the agent's answer goes back as a
reply in that thread.

```sh
hermes plugins install pidgeon-ai/pidgeon-python/hermes/pidgeon --enable
```

Then, in `~/.hermes/.env`:

```sh
PIDGEON_API_KEY=pgn_live_…                    # a key that reads and sends
PIDGEON_ALLOWED_USERS=you@example.com         # who may write to the agent
PIDGEON_ADDRESSES=agent@pidgeon.email         # optional: which addresses to answer
```

and `hermes gateway run`. `[Pidgeon] Connected with key "…"; answering …` is
the gateway reading mail.

## What reaches the agent

The sender, the address, the subject and the attachment names, then
[Pidgeon Firewall's clean text](https://pidgeon.ai/docs/firewall) of the new
message: never the raw HTML. Mail filed as spam never becomes a turn, and mail
the Firewall marks `suspicious` is held unless `PIDGEON_SUSPICIOUS=deliver`.
A sender not in `PIDGEON_ALLOWED_USERS` is ignored, not sent a pairing code.

Mail whose From did not pass DMARC never reaches Hermes, because Hermes's
allowlist and pairing trust the sender's address and anyone can forge one.
Mail between two Pidgeon addresses passes. `PIDGEON_ALLOW_UNAUTHENTICATED=true`
trusts the From alone; with it, anyone who knows an allowed address can
instruct your agent.

The agent can only reply in the thread. Hermes's setup notices and mid-turn
status messages go to the gateway log, never to the person who wrote.

## How it stays up

It reads Pidgeon's event log every five seconds (`PIDGEON_POLL_SECONDS`) from
a cursor in `~/.hermes/pidgeon/`, so a dropped connection is one failed
request. A message is pending from the moment it is read until a reply to it
is sent; after a restart, a pending message whose thread has no later reply
goes to the agent again, for up to a day. A first start begins at the present.
One gateway per key on a machine: a second is refused.

## What it does on your machine

- Network: HTTPS to `pidgeon.ai` only (or `PIDGEON_BASE_URL`), every five
  seconds while the gateway runs, plus one request per message and per reply.
- Files: one state file per key under `~/.hermes/pidgeon/`, readable by you
  only, holding the cursor and message ids; no mail content.
- Credentials: reads `PIDGEON_API_KEY` from Hermes's environment and never
  writes it anywhere.
- No telemetry, no shell commands, no self-update.

Standard library only. The tests are beside this directory:
`python3 -m unittest discover -s hermes/tests -t hermes/tests` runs the half
that does not need Hermes; under Hermes's interpreter, the adapter tests run
too.

[Setup guide](https://pidgeon.ai/docs/hermes) · MIT licensed.
