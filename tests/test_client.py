import json

import httpx
import pytest

from pidgeon import (
    Pidgeon,
    PidgeonError,
    agent_from_env,
    generate_agent_key,
    signed_client,
    verify_agent_request,
)

DIRECTORY = "https://acme.agents.pidgeon.ai"


def recording(answer=None, status=200):
    seen: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return httpx.Response(status, json=answer if answer is not None else {})

    return seen, httpx.Client(transport=httpx.MockTransport(handler))


def test_verify_forwards_the_request():
    seen, http = recording({"valid": False, "verification_id": "ver_1", "reason": "unsigned"})
    answer = Pidgeon("pk_test", client=http).verify(
        "POST", "https://shop.example/signup", {"Signature": "x", "Accept": ["a", "b"]}
    )
    assert answer["verification_id"] == "ver_1"
    (request,) = seen
    assert str(request.url) == "https://pidgeon.ai/v1/verify"
    assert request.headers["authorization"] == "Bearer pk_test"
    assert json.loads(request.content) == {
        "request": {"method": "POST", "url": "https://shop.example/signup",
                    "headers": {"signature": "x", "accept": "a, b"}}
    }


def test_report():
    seen, http = recording({"id": "rep_1"})
    client = Pidgeon("pk_test", "https://pidgeon.test/", client=http)
    assert client.report("ver_1", "spam", "Forty signups.") == {"id": "rep_1"}
    assert str(seen[0].url) == "https://pidgeon.test/v1/reports"
    assert json.loads(seen[0].content) == {
        "verification_id": "ver_1", "category": "spam", "evidence": "Forty signups."
    }


def test_publish_key_is_signed_with_the_key_itself():
    key = generate_agent_key()
    seen, http = recording({"kid": key.kid})
    assert Pidgeon("pk_test", client=http).publish_key("agt 1", key, DIRECTORY) == {"kid": key.kid}
    (request,) = seen
    assert request.url.raw_path == b"/v1/agents/agt%201/keys"
    assert request.headers["authorization"] == "Bearer pk_test"
    assert json.loads(request.content) == {"public_jwk": key.public_jwk}
    result = verify_agent_request(request.method, request.url, request.headers,
                                  lambda kid: key.public_jwk if kid == key.kid else None)
    assert result.ok and result.directory == DIRECTORY


def test_errors_carry_the_api_code():
    _, http = recording({"error": {"code": "forbidden", "message": "Not your agent."}}, status=403)
    with pytest.raises(PidgeonError) as caught:
        Pidgeon("pk_test", client=http).report("ver_1", "spam", "x")
    assert (caught.value.status, caught.value.code, str(caught.value)) == (
        403, "forbidden", "Not your agent."
    )


def test_errors_without_a_body():
    http = httpx.Client(transport=httpx.MockTransport(lambda r: httpx.Response(502, text="bad")))
    with pytest.raises(PidgeonError) as caught:
        Pidgeon("pk_test", client=http).report("ver_1", "spam", "x")
    assert (caught.value.code, caught.value.message) == ("error", "Pidgeon answered 502.")


def test_needs_an_api_key():
    with pytest.raises(ValueError):
        Pidgeon("")


def test_signed_client_signs_every_request():
    key = generate_agent_key()
    seen: list[httpx.Request] = []
    transport = httpx.MockTransport(lambda r: (seen.append(r), httpx.Response(204))[1])
    with signed_client(key.private_jwk, DIRECTORY, transport=transport) as http:
        http.get("https://shop.example/a")
        http.post("https://shop.example/b?q=1", json={"x": 1})
    for request in seen:
        result = verify_agent_request(request.method, request.url, request.headers,
                                      lambda kid: key.public_jwk)
        assert result.ok, result.detail


def test_agent_from_env():
    key = generate_agent_key()
    agent = agent_from_env({"PIDGEON_AGENT_KEY": json.dumps(key.private_jwk),
                            "PIDGEON_DIRECTORY": DIRECTORY})
    headers = agent.sign("GET", "https://shop.example/")
    assert verify_agent_request("GET", "https://shop.example/", headers,
                                lambda kid: key.public_jwk).ok
    with pytest.raises(RuntimeError, match="PIDGEON_AGENT_KEY"):
        agent_from_env({})
