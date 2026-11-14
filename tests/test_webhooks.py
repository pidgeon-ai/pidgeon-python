import json

import pytest

from pidgeon import PidgeonError, sign_webhook, verify_webhook

SECRET = "whsec_test"
BODY = json.dumps({"id": "evt_1", "type": "reputation.changed", "created": "x", "data": {"band": "new"}})


def test_accepts_a_signed_delivery():
    header = sign_webhook(SECRET, BODY, 1_800_000_000)
    assert verify_webhook(SECRET, BODY, header, now=1_800_000_010)["data"] == {"band": "new"}


def test_refuses_a_changed_body():
    header = sign_webhook(SECRET, BODY, 1_800_000_000)
    with pytest.raises(PidgeonError, match="does not match"):
        verify_webhook(SECRET, BODY.replace("new", "good"), header, now=1_800_000_000)


def test_refuses_an_old_delivery():
    header = sign_webhook(SECRET, BODY, 1_800_000_000)
    with pytest.raises(PidgeonError, match="too long ago"):
        verify_webhook(SECRET, BODY, header, now=1_800_001_000)


def test_matches_the_server_signature_format():
    # The same bytes the server's signWebhook produces (src/server/webhooks.ts): HMAC-SHA256 of "<t>.<body>".
    assert sign_webhook("s", "{}", 1).startswith("t=1,v1=")
