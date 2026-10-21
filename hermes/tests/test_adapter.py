"""The Hermes half, on Hermes's real `BasePlatformAdapter`. Skipped unless
Hermes is importable; run with Hermes's interpreter and its checkout on the
path (`integrations/hermes/README.md`)."""

from __future__ import annotations

import asyncio
import os
import subprocess
import sys
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from fake_pidgeon import FakePidgeon  # noqa: E402

try:
    from gateway.config import PlatformConfig
    from gateway.platform_registry import PlatformEntry, platform_registry
except ImportError:  # no Hermes here
    PlatformConfig = None

from pidgeon.core import Client, idempotency_key, poll_once  # noqa: E402


@unittest.skipIf(PlatformConfig is None, "Hermes is not importable")
class AdapterTest(unittest.TestCase):
    def setUp(self):
        self.home = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        os.environ["HERMES_HOME"] = self.home.name
        # The plugin reads its settings from the environment, so a developer's
        # own PIDGEON_ADDRESSES would filter out every test message.
        for name in [n for n in os.environ if n.startswith("PIDGEON_")]:
            self.addCleanup(os.environ.__setitem__, name, os.environ.pop(name))
        os.environ["PIDGEON_API_KEY"] = "pgn_test"
        # Hermes's key locks are per OS user; keep these out of the real ones.
        os.environ["HERMES_GATEWAY_LOCK_DIR"] = os.path.join(self.home.name, "locks")
        from pidgeon import adapter

        self.module = adapter
        entry = {}

        class Ctx:
            def register_platform(self, **kwargs):
                entry.update(kwargs)

        adapter.register(Ctx())
        platform_registry.register(PlatformEntry(source="plugin", **entry))
        self.entry = entry
        self.api = FakePidgeon()
        self.now = datetime.now(timezone.utc)
        self.adapter = self.fresh()

    def tearDown(self):
        os.environ.pop("PIDGEON_API_KEY", None)
        self.home.cleanup()

    def fresh(self):
        """An adapter as a (re)started gateway builds it, on the same state file."""
        built = self.entry["adapter_factory"](PlatformConfig(enabled=True, extra={}))
        built._client = Client("https://pidgeon.test", "pgn_test", opener=self.api)
        built.handed_over = []

        async def capture(event):
            built.handed_over.append(event)

        built.handle_message = capture
        return built

    def tick(self, adapter=None):
        adapter = adapter or self.adapter
        poll_once(adapter._client, adapter._state, adapter._admit, adapter._settings.addresses,
                  now=lambda: self.now)
        asyncio.run(adapter._drain_pending())

    def receive(self, seconds=1, **fields):
        return self.api.receive(self.now + timedelta(seconds=seconds), **fields)

    def test_registration_reads_like_a_platform(self):
        self.assertEqual(self.entry["required_env"], ["PIDGEON_API_KEY"])
        self.assertEqual(self.entry["allowed_users_env"], "PIDGEON_ALLOWED_USERS")
        self.assertFalse(self.entry["allow_update_command"])
        seed = self.entry["env_enablement_fn"]()
        self.assertNotIn("api_key", seed, "the key stays in the environment")

    def test_mail_becomes_one_conversation_per_thread(self):
        self.tick()
        message = self.receive(thread_id="thr_a", subject="Quote")
        self.tick()
        self.tick()
        [event] = self.adapter.handed_over
        self.assertEqual(event.source.chat_id, "thr_a")
        self.assertEqual(event.source.user_id, "ana@example.com")
        self.assertEqual(event.source.chat_name, "Quote")
        self.assertEqual(event.message_id, message["id"])
        self.assertFalse(event.allow_gateway_control)
        self.assertTrue(event.text.endswith("Hi there"))

    def test_a_slash_command_in_an_email_stays_text(self):
        self.tick()
        self.receive(text="/reset", reply_text="/reset")
        self.tick()
        [event] = self.adapter.handed_over
        self.assertFalse(event.is_command())
        # Even were the header lines gone, the event refuses gateway control.
        event.text = "/reset"
        self.assertFalse(event.is_command())

    def test_held_mail_never_reaches_the_agent_and_is_settled(self):
        self.tick()
        self.receive(firewall={"verdict": "suspicious", "signals": [{"kind": "exfiltration"}]})
        self.receive(seconds=2, is_spam=True)
        self.tick()
        self.assertEqual(self.adapter.handed_over, [])
        self.assertEqual(self.adapter._state.load().pending, {})

    def test_the_answer_is_a_reply_and_settles_the_message(self):
        self.tick()
        message = self.receive(thread_id="thr_a")
        self.tick()
        result = asyncio.run(self.adapter.send("thr_a", "It is **391**.", reply_to=message["id"]))
        self.assertTrue(result.success)
        [reply] = self.api.replies
        self.assertEqual((reply["to"], reply["text"]), (message["id"], "It is 391."))
        self.assertEqual(reply["key"], idempotency_key(message["id"], "It is 391."))
        self.assertEqual(self.adapter._state.load().pending, {})

    def test_a_send_without_reply_to_answers_the_newest_inbound(self):
        self.tick()
        self.receive(thread_id="thr_a")
        newer = self.receive(seconds=2, thread_id="thr_a")
        self.tick()
        asyncio.run(self.adapter.send("thr_a", "Both answered."))
        self.assertEqual(self.api.replies[0]["to"], newer["id"])

    def test_a_retried_send_is_one_email(self):
        self.tick()
        message = self.receive(thread_id="thr_a")
        self.tick()
        for _ in range(2):
            asyncio.run(self.adapter.send("thr_a", "Once.", reply_to=message["id"]))
        self.assertEqual(len(self.api.replies), 1)

    def test_a_restart_replays_unanswered_mail_only(self):
        self.tick()
        answered = self.receive(thread_id="thr_a")
        unanswered = self.receive(seconds=2, thread_id="thr_b")
        self.tick()
        asyncio.run(self.adapter.send("thr_a", "Done.", reply_to=answered["id"]))
        # The reply landed but the process died before settling: simulate by re-adding.
        state = self.adapter._state.load()
        state.pending[answered["id"]] = answered["created_at"]
        self.adapter._state.save(state)

        restarted = self.fresh()
        self.tick(restarted)
        self.assertEqual([e.message_id for e in restarted.handed_over], [unanswered["id"]])
        self.assertNotIn(answered["id"], restarted._state.load().pending)

    def test_a_failed_fetch_is_retried_on_the_next_pass(self):
        self.tick()
        message = self.receive()
        self.api.fail[f"/messages/{message['id']}"] = 503
        self.tick()
        self.assertEqual(self.adapter.handed_over, [])
        self.tick()
        self.assertEqual([e.message_id for e in self.adapter.handed_over], [message["id"]])

    def test_a_stranger_is_ignored_not_sent_a_pairing_code(self):
        from gateway.config import GatewayConfig
        from gateway.platforms.base import Platform

        seed = self.entry["env_enablement_fn"]()
        config = GatewayConfig(platforms={Platform("pidgeon"): PlatformConfig(enabled=True, extra=seed)})
        self.assertEqual(config.get_unauthorized_dm_behavior(Platform("pidgeon")), "ignore")
        self.assertEqual(self.adapter.config.extra["unauthorized_dm_behavior"], "ignore")

    def test_hermes_notices_are_never_emailed(self):
        self.assertEqual(self.adapter.config.extra["notice_delivery"], "private")
        result = asyncio.run(self.adapter.send_private_notice("thr_a", "ana@example.com", "No home channel is set."))
        self.assertTrue(result.success)
        self.assertEqual(self.api.replies, [])

    def test_mid_turn_status_is_never_emailed(self):
        self.tick()
        message = self.receive(thread_id="thr_a")
        self.tick()
        asyncio.run(self.adapter.send("thr_a", "Hermes is shutting down", metadata={"_interim_send": True}))
        self.assertEqual(self.api.replies, [])
        self.assertIn(message["id"], self.adapter._state.load().pending)

    def test_a_second_gateway_on_the_same_key_is_refused(self):
        # Another process holds the key, as a second `hermes gateway run` would.
        # Hermes treats a lock as live only while its holder looks like `hermes
        # gateway run`, so the holder's command line says that.
        script = Path(self.home.name) / "hermes"
        script.write_text(
            "import os, sys\n"
            "sys.path[:0] = os.environ['TEST_PATH'].split(os.pathsep)\n"
            "import hermes_bootstrap\n"
            "from gateway.status import acquire_scoped_lock\n"
            "print(acquire_scoped_lock('pidgeon-key', 'pgn_test')[0], flush=True)\n"
            "sys.stdin.read()\n"
        )
        holder = subprocess.Popen(
            [sys.executable, str(script), "gateway", "run"],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True,
            env={**os.environ, "TEST_PATH": os.pathsep.join(p for p in sys.path if p)},
        )
        try:
            self.assertEqual(holder.stdout.readline().strip(), "True")
            self.assertFalse(asyncio.run(self.adapter.connect()))
        finally:
            holder.stdin.close()
            holder.wait()
        self.assertTrue(asyncio.run(self.adapter.connect()))
        asyncio.run(self.adapter.disconnect())

    def test_a_read_only_key_is_refused_at_connect(self):
        self.api.access = "read"
        self.assertFalse(asyncio.run(self.adapter.connect()))
        self.api.access = "send"
        self.assertTrue(asyncio.run(self.adapter.connect()))
        asyncio.run(self.adapter.disconnect())

    def test_a_quiet_mailbox_hands_nothing_over_again(self):
        self.tick()
        self.receive()
        for _ in range(4):
            self.tick()
        self.assertEqual(len(self.adapter.handed_over), 1)


if __name__ == "__main__":
    unittest.main()
