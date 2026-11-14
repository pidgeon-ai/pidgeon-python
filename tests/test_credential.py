import base64

import pytest
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey

import pidgeon
from pidgeon import (
    generate_agent_key,
    is_public_jwk,
    key_id_of,
    sign_request,
    verify_agent_request,
)

DIRECTORY = "https://acme.agents.pidgeon.ai"
NOW = 1_700_000_000

# A key the TypeScript SDK made (generateAgentKey), with what it signed for it:
# signAgentRequest(new Request("https://Shop.example:8443/a b/c?x=1", {method: "post"}),
#   {privateJwk, directory: DIRECTORY, now: new Date(1700000000500)}).
TS_PRIVATE_JWK = {
    "key_ops": ["sign"],
    "ext": True,
    "kty": "OKP",
    "crv": "Ed25519",
    "x": "LzVMC5dHvf0an1i_5AH-eIrZoE9wdMwj1ZoocgBAb8I",
    "d": "6lgW_k0NzhnUKzzqaDO8rhFU7J_SC-tq6SCYkdStyc4",
}
TS_KID = "DxAKKZ5ZL9dtgumxvPjP61jT_DWFQyaL-e8_KpVGc3k"
TS_SIGNATURE_INPUT = (
    'sig1=("@authority" "signature-agent" "@method" "@path");created=1700000000;'
    f'keyid="{TS_KID}";alg="ed25519";expires=1700000060;tag="web-bot-auth"'
)
TS_SIGNATURE = (
    "sig1=:ypvRAqX/Y4Tns5C46UVSbQPhGzLyv4DDsZ24+DkvpkqWHXUyg8F+CQAsjLUPO5A1z8k4oFb2hsKtLviOC6VHDg==:"
)


def public(jwk):
    return {k: jwk[k] for k in ("kty", "crv", "x")}


def publishing(*keys):
    table = {key.kid: key.public_jwk for key in keys}
    return lambda kid: table.get(kid)


def signed(url="https://shop.example/signup", method="POST", now=None, key=None):
    key = key or generate_agent_key()
    headers = sign_request(method, url, None, key.private_jwk, DIRECTORY, now=now)
    return key, headers


class TestKeys:
    def test_rfc7638_example(self):
        # RFC 8037 appendix A.3: the thumbprint of its Ed25519 example key.
        jwk = {"kty": "OKP", "crv": "Ed25519", "x": "11qYAYKxCrfVS_7TyWQHOg7hcvPapiMlrwIaaPcHURo"}
        assert key_id_of(jwk) == "kPrK_qmxVWaYVA9wwBF6Iuo3vVzz7TxHCTwXBygrS4k"

    def test_thumbprint_ignores_other_members(self):
        assert key_id_of(TS_PRIVATE_JWK) == TS_KID
        assert key_id_of(public(TS_PRIVATE_JWK)) == TS_KID

    def test_generated_keys_are_ed25519_and_named_by_their_thumbprint(self):
        key = generate_agent_key()
        assert is_public_jwk(key.public_jwk)
        assert key.kid == key_id_of(key.public_jwk)
        assert len(key.kid) == 43
        assert "alg" not in key.private_jwk
        assert set(key.private_jwk) == {"kty", "crv", "x", "d"}

    def test_never_mistakes_a_private_key_for_a_public_one(self):
        assert not is_public_jwk(generate_agent_key().private_jwk)

    def test_refuses_a_key_whose_halves_do_not_match(self):
        other = generate_agent_key()
        bad = {**TS_PRIVATE_JWK, "x": other.public_jwk["x"]}
        with pytest.raises(ValueError):
            sign_request("GET", "https://shop.example/", None, bad, DIRECTORY)

    def test_refuses_a_key_with_another_alg(self):
        with pytest.raises(ValueError):
            sign_request("GET", "https://shop.example/", None,
                         {**TS_PRIVATE_JWK, "alg": "Ed25519"}, DIRECTORY)


class TestSigning:
    def test_matches_the_typescript_sdk_byte_for_byte(self):
        headers = sign_request("post", "https://Shop.example:8443/a b/c?x=1", None,
                               TS_PRIVATE_JWK, DIRECTORY, now=NOW + 0.5)
        assert headers == {
            "signature-agent": f'"{DIRECTORY}"',
            "signature-input": TS_SIGNATURE_INPUT,
            "signature": TS_SIGNATURE,
        }

    def test_shape(self):
        key, headers = signed(now=NOW)
        assert headers["signature-agent"] == f'"{DIRECTORY}"'
        assert headers["signature-input"] == (
            'sig1=("@authority" "signature-agent" "@method" "@path");'
            f'created={NOW};keyid="{key.kid}";alg="ed25519";expires={NOW + 60};tag="web-bot-auth"'
        )
        assert headers["signature"].startswith("sig1=:") and headers["signature"].endswith(":")
        assert len(base64.b64decode(headers["signature"][6:-1])) == 64

    def test_signs_the_rfc9421_base(self):
        key, headers = signed("https://shop.example/signup?ref=1", now=NOW)
        base = "\n".join([
            '"@authority": shop.example',
            f'"signature-agent": "{DIRECTORY}"',
            '"@method": POST',
            '"@path": /signup',
            '"@signature-params": ' + headers["signature-input"][len("sig1="):],
        ]).encode()
        raw = base64.b64decode(headers["signature"][6:-1])
        x = base64.urlsafe_b64decode(key.public_jwk["x"] + "=")
        Ed25519PublicKey.from_public_bytes(x).verify(raw, base)  # raises if wrong

    def test_lifetime_is_capped_at_five_minutes(self):
        # The cap was a day; it is five minutes since a copied request was
        # replayable at the same site for as long as the verifier accepted it.
        headers = sign_request("GET", "https://shop.example/", None,
                               TS_PRIVATE_JWK, DIRECTORY, lifetime_seconds=10**9, now=NOW)
        assert f"expires={NOW + 300}" in headers["signature-input"]

    def test_authority_drops_the_default_port_and_path_defaults_to_slash(self):
        key, a = signed("https://Shop.Example:443", method="GET", now=NOW)
        _, b = signed("https://shop.example/", method="GET", now=NOW, key=key)
        assert a == b


class TestVerifying:
    def test_round_trip(self):
        key, headers = signed()
        result = verify_agent_request("POST", "https://shop.example/signup", headers, publishing(key))
        assert result.ok and result.kid == key.kid and result.directory == DIRECTORY

    def test_accepts_the_typescript_signature(self):
        headers = {"signature-agent": f'"{DIRECTORY}"', "signature-input": TS_SIGNATURE_INPUT,
                   "signature": TS_SIGNATURE}
        result = verify_agent_request("POST", "https://shop.example:8443/a%20b/c?x=1", headers,
                                      lambda kid: public(TS_PRIVATE_JWK), now=NOW + 10)
        assert result.ok

    def test_refuses_an_unsigned_request(self):
        result = verify_agent_request("GET", "https://shop.example/", {}, publishing())
        assert result.reason == "unsigned"

    def test_refuses_a_key_never_published(self):
        key, headers = signed()
        result = verify_agent_request("POST", "https://shop.example/signup", headers, publishing())
        assert (result.ok, result.reason, result.kid) == (False, "unknown_key", key.kid)

    def test_refuses_a_signature_moved_to_another_site(self):
        key, headers = signed()
        result = verify_agent_request("POST", "https://bank.example/signup", headers, publishing(key))
        assert result.reason == "invalid"

    @pytest.mark.parametrize("method,url", [("POST", "https://shop.example/admin"),
                                            ("DELETE", "https://shop.example/signup")])
    def test_refuses_a_changed_method_or_path(self, method, url):
        key, headers = signed()
        assert not verify_agent_request(method, url, headers, publishing(key)).ok

    def test_refuses_a_swapped_signature_agent(self):
        key, headers = signed()
        swapped = {**headers, "signature-agent": '"https://evil.agents.pidgeon.ai"'}
        assert not verify_agent_request("POST", "https://shop.example/signup", swapped,
                                        publishing(key)).ok

    def test_refuses_one_key_standing_in_for_another(self):
        _, headers = signed()
        other = generate_agent_key()
        result = verify_agent_request("POST", "https://shop.example/signup", headers,
                                      lambda kid: other.public_jwk)
        assert not result.ok

    def test_refuses_an_expired_signature_and_says_so(self):
        import time
        key, headers = signed(now=time.time() - 600)
        result = verify_agent_request("POST", "https://shop.example/signup", headers, publishing(key))
        assert result.reason == "expired"

    def test_accepts_the_dictionary_form_of_signature_agent(self):
        # The working group's form: Signature-Agent: sig1="https://…", covered by key.
        from pidgeon import _sf
        from pidgeon.credential import _signature_base, _target

        key = generate_agent_key()
        inner = _sf.InnerList(
            [_sf.Item("@authority"), _sf.Item("signature-agent", {"key": "sig1"})],
            {"created": NOW, "keyid": key.kid, "alg": "ed25519", "expires": NOW + 60,
             "tag": "web-bot-auth"},
        )
        headers = {"signature-agent": f'sig1="{DIRECTORY}"'}
        base = _signature_base(_target("GET", "https://shop.example/"), headers, inner)
        from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
        d = base64.urlsafe_b64decode(key.private_jwk["d"] + "=")
        raw = Ed25519PrivateKey.from_private_bytes(d).sign(base)
        headers["signature-input"] = _sf.serialize_dictionary({"sig1": inner})
        headers["signature"] = _sf.serialize_dictionary({"sig1": _sf.Item(raw)})
        result = verify_agent_request("GET", "https://shop.example/", headers, publishing(key),
                                      now=NOW + 1)
        assert result.ok and result.directory == DIRECTORY


def test_version():
    assert pidgeon.__version__ == "2.1.1"
