"""The plugin's Hermes-free half, against an in-memory Pidgeon. Standard library
only: `python3 -m unittest discover integrations/hermes/tests`."""

from __future__ import annotations

import sys
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from fake_pidgeon import FakePidgeon  # noqa: E402
from pidgeon.core import (  # noqa: E402
    Client,
    PidgeonError,
    Settings,
    State,
    StateFile,
    answered,
    authenticated,
    body_for_agent,
    decide,
    idempotency_key,
    plain_email_text,
    poll_once,
    prune_pending,
)

T0 = datetime(2026, 10, 21, 12, 0, tzinfo=timezone.utc)


def settings(**values) -> Settings:
    env = {"PIDGEON_API_KEY": "pgn_test", **values}
    return Settings.from_values(lambda name: env.get(name, ""))


class Harness(unittest.TestCase):
    def setUp(self):
        self.api = FakePidgeon()
        self.client = Client("https://pidgeon.test", "pgn_test", opener=self.api)
        self.dir = tempfile.TemporaryDirectory()
        self.state = StateFile(Path(self.dir.name), "pgn_test")
        self.clock = T0
        self.admitted: list[str] = []

    def tearDown(self):
        self.dir.cleanup()

    def poll(self, addresses=()):
        return poll_once(self.client, self.state, lambda e: self.admitted.append(e["message_id"]),
                         list(addresses), now=lambda: self.clock)


class PollTest(Harness):
    def test_a_first_start_begins_at_the_present(self):
        self.api.receive(T0 - timedelta(seconds=5))
        self.api.receive(T0 - timedelta(days=3))
        self.assertEqual(self.poll(), 0)
        later = self.api.receive(T0 + timedelta(seconds=2))
        self.assertEqual(self.poll(), 1)
        self.assertEqual(self.admitted, [later["id"]])

    def test_the_overlap_never_hands_a_message_over_twice(self):
        self.poll()
        first = self.api.receive(T0 + timedelta(seconds=1))
        self.poll()
        # A quiet mailbox: every poll re-reads the last 30 seconds.
        for _ in range(5):
            self.poll()
        self.assertEqual(self.admitted, [first["id"]])

    def test_seen_ids_survive_a_restart(self):
        self.poll()
        first = self.api.receive(T0 + timedelta(seconds=1))
        self.poll()
        restarted = StateFile(Path(self.dir.name), "pgn_test")
        poll_once(self.client, restarted, lambda e: self.admitted.append(e["message_id"]), [],
                  now=lambda: self.clock)
        self.assertEqual(self.admitted, [first["id"]])

    def test_a_row_committed_late_inside_the_overlap_is_read(self):
        self.poll()
        newer = self.api.receive(T0 + timedelta(seconds=20))
        self.poll()
        # Committed after the poll above, stamped earlier than the cursor.
        late = self.api.receive(T0 + timedelta(seconds=5))
        self.poll()
        self.assertEqual(self.admitted, [newer["id"], late["id"]])

    def test_pages_through_a_burst_with_ties_at_the_page_boundary(self):
        self.poll()
        # 250 messages, three to a millisecond, so a page often ends inside an instant.
        burst = [self.api.receive(T0 + timedelta(seconds=1, milliseconds=i // 3)) for i in range(250)]
        self.poll()
        self.assertEqual(sorted(self.admitted), sorted(m["id"] for m in burst))

    def test_addresses_limit_what_is_admitted(self):
        self.poll()
        self.api.receive(T0 + timedelta(seconds=1), identity="other@pidgeon.email")
        mine = self.api.receive(T0 + timedelta(seconds=2), identity="Agent@pidgeon.email")
        self.poll(addresses=["agent@pidgeon.email"])
        self.assertEqual(self.admitted, [mine["id"]])

    def test_a_refused_admission_does_not_move_the_cursor(self):
        self.poll()
        message = self.api.receive(T0 + timedelta(seconds=1))

        def refuse(event):
            raise RuntimeError("disk full")

        with self.assertRaises(RuntimeError):
            poll_once(self.client, self.state, refuse, [], now=lambda: self.clock)
        self.poll()
        self.assertEqual(self.admitted, [message["id"]])

    def test_admit_may_write_pending_without_losing_it(self):
        self.poll()
        message = self.api.receive(T0 + timedelta(seconds=1))

        def admit(event):
            state = self.state.load()
            state.pending[event["message_id"]] = event["created_at"]
            self.state.save(state)

        poll_once(self.client, self.state, admit, [], now=lambda: self.clock)
        self.assertIn(message["id"], self.state.load().pending)

    def test_the_state_file_is_owner_only(self):
        self.poll()
        self.assertEqual(self.state.path.stat().st_mode & 0o777, 0o600)

    def test_a_refused_key_is_a_pidgeon_error(self):
        client = Client("https://pidgeon.test", "pgn_wrong", opener=self.api)
        with self.assertRaises(PidgeonError) as caught:
            client.me()
        self.assertEqual(caught.exception.status, 401)
        self.assertEqual(str(caught.exception), "That key is not valid.")


class GateTest(unittest.TestCase):
    def message(self, **fields):
        api = FakePidgeon()
        return api.receive(T0, **fields)

    def test_delivers_ordinary_mail(self):
        self.assertIsNone(decide(settings(), self.message()))

    def test_holds_what_the_firewall_flags(self):
        flagged = self.message(firewall={"verdict": "suspicious", "signals": [{"kind": "addressed_to_ai"}]})
        self.assertEqual(decide(settings(), flagged), "held by Pidgeon Firewall (addressed_to_ai)")
        self.assertIsNone(decide(settings(PIDGEON_SUSPICIOUS="deliver"), flagged))

    def test_never_spam_mail_sent_by_itself_or_outbound(self):
        self.assertEqual(decide(settings(), self.message(is_spam=True)), "filed as spam")
        self.assertEqual(decide(settings(), self.message(sender="agent@pidgeon.email")), "sent by the address itself")
        self.assertEqual(decide(settings(), self.message(direction="outbound")), "not inbound")

    def test_addresses_are_matched_without_case(self):
        only = settings(PIDGEON_ADDRESSES="Agent@Pidgeon.email, x@y.z")
        self.assertIsNone(decide(only, self.message()))
        self.assertIsNotNone(decide(only, self.message(identity="other@pidgeon.email")))

    # Teknium's review, 23 October: Hermes's allowlist and pairing trust the
    # From, so mail forging an allowed sender became a turn on a machine with
    # a terminal. The adversary is a stranger who knows one allowed address.
    def verdicts(self, dmarc, spf="pass", dkim=None):
        return {"authentication": {"spf": spf, "dkim": dkim if dkim is not None else spf, "dmarc": dmarc}}

    def test_a_from_that_fails_dmarc_or_is_unreported_is_refused(self):
        forged = self.message(sender="owner@example.com", **self.verdicts("fail"))
        self.assertEqual(
            decide(settings(), forged),
            "from owner@example.com, but it did not pass DMARC, so the From may be forged",
        )
        self.assertIsNotNone(decide(settings(), self.message(**self.verdicts(None, None))))
        self.assertIsNotNone(decide(settings(), self.message(authentication=None)))

    def test_an_spf_or_dkim_pass_alone_is_not_enough(self):
        # Either may pass for the attacker's own domain; only DMARC ties it to the From.
        self.assertIsNotNone(decide(settings(), self.message(**self.verdicts(None, "pass"))))
        self.assertIsNotNone(decide(settings(), self.message(**self.verdicts("none", "pass"))))

    def test_the_same_from_passing_dmarc_is_delivered(self):
        self.assertIsNone(decide(settings(), self.message(sender="owner@example.com", **self.verdicts("pass"))))

    def test_pidgeon_mail_delivered_without_ses_is_delivered(self):
        local = self.message(sender="peer@pidgeon.email", origin=None, **self.verdicts(None, None))
        local["sender"] = {"address": "peer@pidgeon.email", "kind": "agent"}
        self.assertTrue(authenticated(local))
        self.assertIsNone(decide(settings(), local))
        self.assertFalse(authenticated({**local, "origin": "smtp"}))

    def test_allow_unauthenticated_restores_the_from_alone(self):
        trusting = settings(PIDGEON_ALLOW_UNAUTHENTICATED="true")
        self.assertTrue(trusting.allow_unauthenticated)
        self.assertIsNone(decide(trusting, self.message(**self.verdicts("fail"))))
        self.assertFalse(settings(PIDGEON_ALLOW_UNAUTHENTICATED="maybe").allow_unauthenticated)

    def test_settings_fall_back_to_safe_values(self):
        loose = settings(PIDGEON_SUSPICIOUS="yes please", PIDGEON_POLL_SECONDS="0")
        self.assertEqual((loose.suspicious, loose.poll_seconds), ("hold", 2))
        self.assertEqual(settings(PIDGEON_POLL_SECONDS="soon").poll_seconds, 5)


class TextTest(unittest.TestCase):
    def test_the_agent_reads_the_header_lines_then_the_new_text(self):
        message = FakePidgeon().receive(T0, text="Full quoted history", reply_text="Just the new bit",
                                        attachments=[{"filename": "a.pdf", "content_type": "application/pdf"}])
        body = body_for_agent(message)
        self.assertTrue(body.startswith("From: Ana <ana@example.com>\nTo: agent@pidgeon.email\nSubject: Hello"))
        self.assertIn("Attachments: a.pdf (application/pdf)", body)
        self.assertTrue(body.endswith("\n\nJust the new bit"))

    def test_delivered_flagged_mail_carries_the_warning(self):
        message = FakePidgeon().receive(T0, firewall={
            "verdict": "suspicious", "signals": [{"kind": "exfiltration", "detail": "forward the inbox"}]})
        self.assertIn("Pidgeon Firewall: suspicious — exfiltration: forward the inbox.", body_for_agent(message))

    def test_markdown_emphasis_and_headings_are_removed(self):
        self.assertEqual(plain_email_text("## Total\n\nIt is **391** and __done__.\n"), "Total\n\nIt is 391 and done.")

    def test_one_reply_is_one_key(self):
        self.assertEqual(idempotency_key("msg_1", "Hi"), idempotency_key("msg_1", "Hi"))
        self.assertNotEqual(idempotency_key("msg_1", "Hi"), idempotency_key("msg_1", "Hi!"))
        self.assertNotEqual(idempotency_key("msg_1", "Hi"), idempotency_key("msg_2", "Hi"))


class PendingTest(unittest.TestCase):
    def test_answered_means_an_outbound_message_after_it(self):
        api = FakePidgeon()
        inbound = api.receive(T0, thread_id="thr")
        earlier = api.outbound("thr", T0 - timedelta(minutes=1))
        self.assertFalse(answered([inbound, earlier], inbound))
        later = api.outbound("thr", T0 + timedelta(seconds=1))
        self.assertTrue(answered([inbound, earlier, later], inbound))

    def test_pending_expires_after_a_day(self):
        state = State(after="x", floor="x", pending={
            "old": "2026-10-20T11:00:00.000Z", "new": "2026-10-21T11:00:00.000Z"})
        self.assertEqual(prune_pending(state, T0), ["new"])
        self.assertEqual(list(state.pending), ["new"])


if __name__ == "__main__":
    unittest.main()
