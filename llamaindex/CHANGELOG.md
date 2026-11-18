# Changelog

## 1.0.0

Rebuilt for the new Pidgeon, on the `pidgeon` SDK 2.x (`/v1`). Nothing of
0.x carries over: 0.1.4 stays on PyPI for the old email API until it is
retired.

- Functions: `list_inboxes`, `send_message`, `reply_to_message`, `list_threads`,
  `get_thread`, `get_message`, `await_message` (the inbox);
  `register_agent`, `get_reputation` (the agent's identity); `verify_request`
  (Bouncer). `PidgeonToolSpec` is the spec; `WRITES` names the functions that write.
- Every tool that returns mail tells the model that mail is its sender's
  words, never instructions.
- `register_agent` keeps the new agent's private key in a file only this
  user can read; the model never sees it.
- Apache-2.0, as the SDK.
