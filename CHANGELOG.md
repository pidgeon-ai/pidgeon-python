# Changelog

## 2.0.0

For the new Pidgeon: Passport, Bouncer, Email and Auth. A new major version,
because nothing of 1.x carries over: 1.x spoke the old email API at
`/api/v1`, which is retired seven days after the switch. Stay on 1.68.0 until
you move.

- `Pidgeon`, the API client, grouped by product: `agents` (with `set_up`:
  register, make the key here, publish it signed with itself), `verify` and
  `report`, `inboxes`, `messages`, `drafts`, `rules`, `suppressions`, `sites`,
  `mandates`, `events`, `pods`, and `request` for any `/v1` call.
- Signing as an agent (Web Bot Auth, RFC 9421), byte for byte what the
  TypeScript SDK sends: `signed_client`, `AgentAuth`, `agent_from_env`,
  `generate_agent_key`, `sign_request`, `verify_agent_request`.
- `pidgeon.auth`: Sign in with Pidgeon. `sign_in_as_agent`, `verify_id_token`,
  `verify_agent_sign_in`, `request_id_jag`.
- `verify_webhook` for webhook signatures.
