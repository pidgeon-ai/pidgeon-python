# Changelog

## 2.5.0

- `sites.update(client_id, name=, redirect_uris=)` and
  `sites.rotate_secret(client_id)`: edit a site, and give it a new secret
  (answered once; the old one stops working at once).
- `verify_agent_sign_in` requires the request's `Signature-Agent` to be the
  agent's own directory (the token's `agent.directory`), as Pidgeon's token
  exchange now does: `wrong_directory` otherwise.
- `SignInError.reason` says which: `wrong_request` (signed for another
  method, path or host) and `expired` (the signature is too old or dated
  ahead) are no longer reported as `wrong_key`.
- `verify_agent_sign_in` takes `client_secret`: a token issued under a
  mandate is checked with Pidgeon's `/oauth/introspect`, and one whose
  mandate was stopped is refused at once (`mandate_ended`).
- `same_directory(named, directory)`.

## 2.4.0

- Every signature carries a fresh 64-byte nonce and covers `@query` (`?`
  when the URL has none), so neither the query nor the signature can be
  reused: sign again to retry. `new_nonce()`; `sign_request` takes `nonce`
  for tests. `verify_agent_request` answers the signature's `nonce` and
  refuses a malformed one.
- `agents.update`, `agents.revoke`, `agents.revoke_key` and `pods.remove`.

## 2.3.0

- `email.search` takes `body="clean"`, as reading does.
- `InboxKind` is `"agent"` or `"events"`, the kinds the API makes.
- `inboxes.update(hold_suspicious=True)`: `True` is the only value a key
  may send, so it is the default and the only one typed.
- `subject` is optional when sending or drafting, as in the API.
- `drafts.update` no longer takes `reply_to`: a draft keeps its conversation.

## 2.2.0

- `webhooks.create` takes `inbox_ids`: the endpoint hears only those
  inboxes' events. A listed webhook has `inbox_ids`, `None` for one of the
  whole account.

## 2.1.1

- `email.calendar.events`: `create` and `update` take `attendees` and
  `send_invites`, and `remove` takes `send_invites`: the attendees get an
  invitation, an update or a cancellation from the inbox.

## 2.1.0

The whole Email API, and webhooks. Additive: 2.0 code runs unchanged, and
`inboxes`, `messages`, `drafts`, `rules` and `suppressions` stay on the client
as well as under `email`.

- `client.email`: `inboxes` (now `update` for `hold_suspicious`, and `create`
  takes `domain`), `messages` (`list`, `wait` for `…/messages/await`, `get`,
  `update` for `seen`; `send` takes `attachment_ids`), `drafts` (take
  `attachment_ids`), `threads` (`list`, `get`, `update`, `remove`,
  `add_label`, `remove_label`), `labels`, `contacts`, `attachments` (`upload`
  of bytes or a path; `upload_large` describes, puts and completes a file of
  up to 25 MB in one call; `get`), `domains` (`enable_mail`, `disable_mail`,
  `check`), `app_passwords`, `calendar.events`, `search`, `storage` and
  `test_inbound`.
- `client.webhooks`: `list`, `create`, `remove`.
- `request` takes `files` (multipart) and a per-call `timeout`.
- `UNSET`: what a PATCH method's field defaults to, so that `None` can clear
  it (a contact's `notes`, an event's `location`, a thread's `assignee_id`).

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
