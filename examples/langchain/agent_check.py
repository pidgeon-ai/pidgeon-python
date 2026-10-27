"""The agent in main.py, run with a model and checked step by step.

    PIDGEON_API_KEY=pgn_live_… OPENAI_API_KEY=sk-… python agent_check.py

`main.run` with a model, the human-in-the-loop gate and nobody at the
prompt: this file answers each pause itself. The agent makes an address,
reads a code mailed to it with `await_message`, and replies quoting it. The
gate stops it before the address is made and before the reply goes; both are
approved, and anything else it asks to do is refused and fails the check.

`PIDGEON_API_KEY` is an admin key. The agent never holds it: it gets a test
key minted from it, admin over the default pod for the hour, so the address it
makes is a test address and nothing it sends leaves Pidgeon. The code
arrives through `POST /v1/test/inbound`, as mail from outside would. At the
end the address is deleted and the test key revoked; a crash leaves the
address to be deleted after a day and the key to expire.

CI runs it after every production deploy and nightly (examples.yml).
"""

import json
import os
import secrets
import sys
import threading
import time
from datetime import UTC, datetime, timedelta

from langchain.chat_models import init_chat_model
from langchain_core.messages import ToolMessage
from pidgeon.api.identities import identities_delete
from pidgeon.api.keys import keys_create, keys_revoke
from pidgeon.api.pods import pods_list
from pidgeon.api.test import test_inbound
from pidgeon.errors import PidgeonError
from pidgeon.models import KeysCreateBody, KeysCreateBodyAccess, TestInboundBody

import main
from langchain_pidgeon import PidgeonToolkit
from langchain_pidgeon.tools import AwaitMessage

# The cheapest OpenAI model that did this reliably on 26 October, with room
# for a short reply and no more.
MODEL = os.environ.get("MODEL", "openai:gpt-5.4-nano")
main.model = lambda: init_chat_model(MODEL, max_tokens=2000)

email = f"langchain-agent-{secrets.token_hex(4)}@pidgeon.email"
expires = datetime.now(UTC) + timedelta(hours=1)
code = f"{secrets.randbelow(900000) + 100000}"

TASK = (
    f"Create the address {email} (type agent, with an inbox, expiring at "
    f"{expires.isoformat()}). A sign-in code will be emailed to it within a "
    "minute: wait for it with await_message (has_code true, timeout 90). "
    "Then reply to that message with: Thanks, the code was <the code>. "
    "Send nothing else, and finish with the code."
)


def fail(reason: str) -> None:
    sys.exit(f"FAILED: {reason}")


def results(messages: list, name: str) -> list[dict]:
    """What a tool returned, leaving out the errors the agent read and got past."""
    found = []
    for message in messages:
        if isinstance(message, ToolMessage) and message.name == name:
            try:
                found.append(json.loads(message.content)["data"])
            except (ValueError, KeyError):
                print(f"note: {name} returned an error to the agent: {message.content}")
    return found


live = PidgeonToolkit()
# A key mints only keys narrower than itself, and never one for every
# address: admin over the default pod is what creating an address needs.
pod = next(pod for pod in pods_list.sync(client=live.client).data if pod.is_default)
minted = keys_create.sync(
    client=live.client,
    body=KeysCreateBody(
        name="LangChain agent check",
        access=KeysCreateBodyAccess.ADMIN,
        pod_id=pod.id,
        test=True,
        expires_at=expires,
    ),
).data
# What main.run's toolkit reads.
os.environ["PIDGEON_API_KEY"] = minted.token
test = PidgeonToolkit()
get_message = {tool.name: tool for tool in test.get_tools()}["get_message"]


# The code is mailed once the agent is waiting, as a sign-in form's would be
# after the agent submitted it. Mailed as soon as the address existed, it raced
# a model that waits with `after: "now"`, as the tool tells it to before it
# causes the mail: arriving first, it was before the cursor and the wait timed
# out after 90 seconds (27 October, twice in three runs on gpt-5.4-nano).
waiting = threading.Event()
_await = AwaitMessage._run


def _await_and_signal(self, **args):
    waiting.set()
    return _await(self, **args)


AwaitMessage._run = _await_and_signal


def mail_the_code() -> None:
    """Delivered as mail from outside, a moment after the agent starts waiting."""
    if waiting.wait(timeout=120):
        time.sleep(3)
    for _ in range(30):
        try:
            test_inbound.sync(
                client=test.client,
                body=TestInboundBody(
                    to=email,
                    from_="sign-in@example.com",
                    subject="Your sign-in code",
                    text=f"Your sign-in code is {code}. It expires in ten minutes.",
                ),
            )
            print(f"delivered {code} to {email}")
            return
        except PidgeonError:
            time.sleep(2)
    print(f"could not deliver the code to {email}")


asked: list[str] = []


def approve(call: dict) -> bool:
    asked.append(call["name"])
    print(f"asked: {call['name']}({json.dumps(call['args'], default=str)})")
    if call["name"] == "create_address" and call["args"].get("address") == email:
        threading.Thread(target=mail_the_code, daemon=True).start()
        return True
    return call["name"] == "reply_to_message"


started = time.monotonic()
address = None
try:
    messages = main.run(TASK, approve=approve)
    made = results(messages, "create_address")
    address = made[0] if made else None

    if asked != ["create_address", "reply_to_message"]:
        fail(f"the gate should have stopped create_address, then reply_to_message: {asked}")
    print("ok: the gate stopped create_address, then reply_to_message, and both were approved")

    if len(made) != 1 or made[0]["email"] != email or not made[0]["test"]:
        fail(f"expected {email} made once, as a test address: {made}")
    print(f"ok: made {email}, a test address")

    awaited = [found for found in results(messages, "await_message") if not found["timed_out"]]
    codes = [c["value"] for found in awaited for c in found["message"]["extracted"]["codes"]]
    if code not in codes:
        fail(f"await_message never returned {code}: {codes}")
    print(f"ok: await_message read {code}")

    replies = results(messages, "reply_to_message")
    if len(replies) != 1:
        fail(f"expected one reply: {replies}")
    reply = json.loads(get_message.invoke({"id": replies[0]["id"]}))["data"]
    if reply["identity_id"] != address["id"] or code not in json.dumps(reply):
        fail(f"the reply does not quote {code}: {reply}")
    print(f"ok: the reply went from {email}, quoting {code}")

    print(f"passed in {time.monotonic() - started:.0f}s on {MODEL}")
finally:
    # Not a tool: deleting an address is a person's call, not a model's.
    if address is not None:
        identities_delete.sync(address["id"], client=test.client)
        print("deleted the address")
    keys_revoke.sync(minted.id, client=live.client)
    print("revoked the test key")
