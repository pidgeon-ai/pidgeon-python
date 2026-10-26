# Privacy

## What the plugin sends, and where

The plugin talks to one host, `pidgeon.ai`, over HTTPS, with the Pidgeon API
key you connect. Each tool sends Pidgeon what it needs for that call: the
addresses, subject and text of mail you send or reply with; the words, sender
and folder of a search; the address and sender a wait is for; and a thread's
new owner, status and reason.

## What comes back

Pidgeon answers with the mail the key can reach: senders, recipients,
subjects, text, verification codes and links. The plugin passes it to your
Dify app as the tool's output and keeps none of it.

## What the plugin keeps

Nothing. It has no storage and no logging of its own, and it sends nothing
to any other service. Dify keeps the API key as a credential, and keeps tool
outputs under its own policy.

## Pidgeon

Pidgeon stores the mail of the addresses you create, under its privacy
policy: <https://pidgeon.ai/legal/privacy>. A test key (`pgn_test_…`) sends
nothing outside Pidgeon.

## Contact

support@pidgeon.ai
