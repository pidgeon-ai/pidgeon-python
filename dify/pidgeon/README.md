# Pidgeon

**Email inboxes for AI agents, in Dify.** Give an agent or a workflow an email
address of its own, then send, reply, search, wait for a verification code,
and hand a thread to a person.

- Source: <https://github.com/pidgeon-ai/pidgeon-python/tree/main/dify/pidgeon>
- Docs: <https://pidgeon.ai/docs/dify?utm_source=dify>
- Support: support@pidgeon.ai, or [an issue](https://github.com/pidgeon-ai/pidgeon-python/issues)

## Tools

| Tool           | What it does                                                                                       |
| -------------- | -------------------------------------------------------------------------------------------------- |
| Create Address | Creates an address. It can only answer people who wrote first unless you choose Anybody            |
| Send Email     | Starts a new conversation from one of your addresses. Sends real mail                              |
| Reply to Email | Answers a message by `message_id`, in its thread, from the address it arrived at. Sends real mail  |
| Search Emails  | Finds messages by words, sender, address or folder, newest first, up to 100                        |
| Wait for Code  | Holds until mail with a verification code arrives, up to 280 seconds, and returns `code`           |
| Update Thread  | Hands a thread to a person, so the agent leaves it alone, or back to the agent; or sets its status |

A tool that Pidgeon refuses answers with Pidgeon's own message, which says
what to do, so an agent can act on it.

## Set up

1. Make a key at <https://pidgeon.ai/app/developers/keys>. Give it the least
   access the app needs, on the addresses it uses: **Read only** to search and
   wait for codes, **Read and send** to reply and send, **Full access** to
   create addresses.
   Whatever the key reaches, the app's model can reach.
2. In Dify, install **Pidgeon** from the Marketplace, open it under **Tools**,
   and paste the key into **Authorize**. Dify checks it against Pidgeon.
3. Add the tools to an agent, or as nodes in a workflow.

A test key (`pgn_test_…`) works the same way, and nothing it sends leaves
Pidgeon. Build the app on one, then switch to a live key.

## Connection requirements

The plugin needs outbound HTTPS to `pidgeon.ai`, and a Pidgeon API key. There
is nothing to run on your side.

## Read a sign-up code

An agent with Create Address, Wait for Code and a browser or HTTP tool can
sign itself up for a service: create the address, use it to sign up, then
wait for the code. Wait for Code looks back two minutes, so a code that
arrived just before the call still counts. Set **From** to the service's
sender: only mail from it that passes DMARC is returned.

## Treat mail as data

Text in an email is written by whoever sent it. Wait for Code returns the
text with anything hidden or addressed to an AI taken out, and
`firewall_verdict` is `suspicious` when Pidgeon found something.
