"""What JavaScript would have written, byte for byte.

Every signature in this package is over bytes the TypeScript twin produces
with ``JSON.stringify``, ``Buffer.toString('base64url')`` and the WHATWG
``URL``. Python's ``json.dumps`` is not ``JSON.stringify``: it writes ``1.0``
where JavaScript writes ``1``, ``1e+16`` where it writes
``10000000000000000``, escapes differently by default, and keeps the
insertion order of keys that JavaScript moves to the front because they look
like array indices. A signature over the wrong spelling of the same value
fails at the receiver, so the spelling lives here, once, and
``tests/unit/python-identity.test.ts`` holds it to Node's.
"""

from __future__ import annotations

import base64
import math
from decimal import Decimal
from typing import Any

import httpx

__all__ = [
    "b64",
    "b64url",
    "from_b64",
    "from_b64url",
    "js_number",
    "js_string",
    "js_stringify",
    "url_parts",
]


def b64url(data: bytes) -> str:
    """``Buffer.toString('base64url')``: URL-safe, unpadded."""
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode("ascii")


def from_b64url(text: str) -> bytes:
    """``Buffer.from(text, 'base64url')``, which takes either alphabet and no padding."""
    return from_b64(text)


def b64(data: bytes) -> str:
    """``Buffer.toString('base64')``: standard alphabet, padded."""
    return base64.b64encode(data).decode("ascii")


def from_b64(text: str) -> bytes:
    """``Buffer.from(text, 'base64')``: lenient, as Node is — either alphabet, padding optional."""
    cleaned = "".join(
        ch for ch in text.replace("-", "+").replace("_", "/") if (ch.isascii() and ch.isalnum()) or ch in "+/"
    )
    return base64.b64decode(cleaned + "=" * (-len(cleaned) % 4))


def js_number(value: int | float) -> str:
    """ECMAScript ``Number::toString``, which is what ``JSON.stringify`` and RFC 8785 write."""
    # Beyond 2^53 an integer is the double JavaScript would have parsed it as.
    if isinstance(value, int) and abs(value) <= 2**53:
        return str(value)
    number = float(value)
    if not math.isfinite(number):
        raise ValueError("JSON has no NaN or Infinity.")
    if number == 0:
        return "0"
    sign = "-" if number < 0 else ""
    # `repr` is the shortest string that round-trips, as ECMAScript's digits are.
    _, digits, exponent = Decimal(repr(abs(number))).as_tuple()
    text = "".join(map(str, digits)).rstrip("0")
    exponent += len(digits) - len(text)
    k = len(text)
    n = k + exponent  # The value is 0.<text> × 10^n.
    if k <= n <= 21:
        out = text + "0" * (n - k)
    elif 0 < n <= 21:
        out = f"{text[:n]}.{text[n:]}"
    elif -6 < n <= 0:
        out = f"0.{'0' * -n}{text}"
    else:
        e = n - 1
        mantissa = text if k == 1 else f"{text[0]}.{text[1:]}"
        out = f"{mantissa}e{'+' if e >= 0 else '-'}{abs(e)}"
    return sign + out


_ESCAPES = {'"': '\\"', "\\": "\\\\", "\b": "\\b", "\f": "\\f", "\n": "\\n", "\r": "\\r", "\t": "\\t"}


def js_string(value: str) -> str:
    """``JSON.stringify`` of a string: UTF-8 left alone, controls and lone surrogates escaped."""
    out = ['"']
    for ch in value:
        code = ord(ch)
        if ch in _ESCAPES:
            out.append(_ESCAPES[ch])
        elif code < 0x20 or 0xD800 <= code <= 0xDFFF:
            out.append(f"\\u{code:04x}")
        else:
            out.append(ch)
    out.append('"')
    return "".join(out)


def _is_index(key: str) -> bool:
    """An ECMAScript array index, which an object enumerates first, in numeric order."""
    return key.isdigit() and key.isascii() and str(int(key)) == key and int(key) < 2**32 - 1


def js_keys(mapping: dict[str, Any]) -> list[str]:
    """The order ``Object.keys`` gives: integer-like keys ascending, then the rest as inserted."""
    keys = [str(key) for key in mapping]
    indices = sorted((key for key in keys if _is_index(key)), key=int)
    return indices + [key for key in keys if not _is_index(key)]


def js_stringify(value: Any) -> str:
    """``JSON.stringify(value)``, compact."""
    if value is None:
        return "null"
    if value is True:
        return "true"
    if value is False:
        return "false"
    if isinstance(value, (int, float)):
        return js_number(value) if math.isfinite(value) else "null"
    if isinstance(value, str):
        return js_string(value)
    if isinstance(value, (list, tuple)):
        return "[" + ",".join(js_stringify(item) for item in value) + "]"
    if isinstance(value, dict):
        by_key = {str(key): member for key, member in value.items()}
        return "{" + ",".join(f"{js_string(key)}:{js_stringify(by_key[key])}" for key in js_keys(by_key)) + "}"
    raise TypeError(f"{type(value).__name__} is not JSON.")


class UrlParts:
    """The parts of a URL that HTTP Message Signatures and DPoP read, as the WHATWG ``URL`` gives them."""

    def __init__(self, url: str | httpx.URL) -> None:
        parsed = url if isinstance(url, httpx.URL) else httpx.URL(url)
        host = parsed.raw_host.decode("ascii").lower()
        if ":" in host and not host.startswith("["):
            host = f"[{host}]"
        self.scheme = parsed.scheme
        # httpx, like `URL.port`, drops the scheme's default port.
        self.port = parsed.port
        self.hostname = host
        self.host = f"{host}:{self.port}" if self.port else host
        raw = parsed.raw_path.decode("ascii")
        path, _, query = raw.partition("?")
        self.pathname = path or "/"
        self.search = f"?{query}" if query else ""
        self.origin = f"{self.scheme}://{self.host}"
        self.href = str(parsed)


def url_parts(url: str | httpx.URL) -> UrlParts:
    return UrlParts(url)
