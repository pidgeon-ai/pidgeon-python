"""
The part of Structured Field Values (RFC 8941) that HTTP Message Signatures
use: dictionaries of items and inner lists, with parameters, over integers,
decimals, strings, tokens, byte sequences and booleans.

Parsed values keep their kind, so a value serializes back exactly: a token
is a `Token`, a byte sequence is `bytes`, a string is `str`.
"""

from __future__ import annotations

import base64
import re
from dataclasses import dataclass, field
from typing import Union


class Token(str):
    """An sf-token, which serializes without quotes."""


BareItem = Union[int, float, str, Token, bytes, bool]
Parameters = dict[str, BareItem]


@dataclass
class Item:
    value: BareItem
    params: Parameters = field(default_factory=dict)


@dataclass
class InnerList:
    items: list[Item]
    params: Parameters = field(default_factory=dict)


Member = Union[Item, InnerList]

_KEY = re.compile(r"[a-z*][a-z0-9_.*-]*")
_TOKEN = re.compile(r"[A-Za-z*][!#$%&'*+\-.^_`|~0-9A-Za-z:/]*")
_NUMBER = re.compile(r"-?[0-9]+(\.[0-9]+)?")
_BYTES = re.compile(r"[A-Za-z0-9+/=]*")


class ParseError(ValueError):
    pass


class _Parser:
    def __init__(self, text: str) -> None:
        self.text = text
        self.pos = 0

    def peek(self) -> str:
        return self.text[self.pos] if self.pos < len(self.text) else ""

    def skip_sp(self) -> None:
        while self.peek() == " ":
            self.pos += 1

    def skip_ows(self) -> None:
        while self.peek() in (" ", "\t") and self.peek():
            self.pos += 1

    def expect(self, char: str) -> None:
        if self.peek() != char:
            raise ParseError(f"expected {char!r} at {self.pos}")
        self.pos += 1

    def key(self) -> str:
        match = _KEY.match(self.text, self.pos)
        if not match:
            raise ParseError(f"expected a key at {self.pos}")
        self.pos = match.end()
        return match.group()

    def bare_item(self) -> BareItem:
        char = self.peek()
        if char == '"':
            return self.string()
        if char == ":":
            return self.byte_sequence()
        if char == "?":
            self.pos += 1
            value = self.peek()
            if value not in ("0", "1"):
                raise ParseError(f"expected a boolean at {self.pos}")
            self.pos += 1
            return value == "1"
        if char == "-" or char.isdigit():
            match = _NUMBER.match(self.text, self.pos)
            if not match:
                raise ParseError(f"expected a number at {self.pos}")
            self.pos = match.end()
            text = match.group()
            return float(text) if match.group(1) else int(text)
        match = _TOKEN.match(self.text, self.pos)
        if match:
            self.pos = match.end()
            return Token(match.group())
        raise ParseError(f"unexpected {char!r} at {self.pos}")

    def string(self) -> str:
        self.expect('"')
        out: list[str] = []
        while True:
            char = self.peek()
            if not char:
                raise ParseError("unterminated string")
            self.pos += 1
            if char == "\\":
                escaped = self.peek()
                if escaped not in ('"', "\\"):
                    raise ParseError(f"bad escape at {self.pos}")
                out.append(escaped)
                self.pos += 1
            elif char == '"':
                return "".join(out)
            elif not (0x20 <= ord(char) <= 0x7E):
                raise ParseError(f"non-ASCII in string at {self.pos}")
            else:
                out.append(char)

    def byte_sequence(self) -> bytes:
        self.expect(":")
        match = _BYTES.match(self.text, self.pos)
        assert match is not None
        self.pos = match.end()
        self.expect(":")
        try:
            return base64.b64decode(match.group(), validate=True)
        except ValueError as error:
            raise ParseError("bad byte sequence") from error

    def parameters(self) -> Parameters:
        params: Parameters = {}
        while self.peek() == ";":
            self.pos += 1
            self.skip_sp()
            name = self.key()
            value: BareItem = True
            if self.peek() == "=":
                self.pos += 1
                value = self.bare_item()
            params[name] = value
        return params

    def item(self) -> Item:
        value = self.bare_item()
        return Item(value, self.parameters())

    def inner_list(self) -> InnerList:
        self.expect("(")
        items: list[Item] = []
        while True:
            self.skip_sp()
            if self.peek() == ")":
                self.pos += 1
                return InnerList(items, self.parameters())
            items.append(self.item())
            if self.peek() not in (" ", ")"):
                raise ParseError(f"expected ' ' or ')' at {self.pos}")

    def member(self) -> Member:
        return self.inner_list() if self.peek() == "(" else self.item()

    def done(self) -> None:
        self.skip_sp()
        if self.pos != len(self.text):
            raise ParseError(f"trailing characters at {self.pos}")


def parse_dictionary(text: str) -> dict[str, Member]:
    parser = _Parser(text)
    parser.skip_sp()
    out: dict[str, Member] = {}
    if parser.pos == len(text):
        return out
    while True:
        name = parser.key()
        if parser.peek() == "=":
            parser.pos += 1
            member = parser.member()
        else:
            member = Item(True, parser.parameters())
        if name in out:
            raise ParseError(f"duplicate key {name}")
        out[name] = member
        parser.skip_ows()
        if parser.pos == len(text):
            return out
        parser.expect(",")
        parser.skip_ows()
        if parser.pos == len(text):
            raise ParseError("trailing comma")


def parse_item(text: str) -> Item:
    parser = _Parser(text)
    parser.skip_sp()
    item = parser.item()
    parser.done()
    return item


def serialize_bare_item(value: BareItem) -> str:
    if isinstance(value, bool):
        return "?1" if value else "?0"
    if isinstance(value, Token):
        return str(value)
    if isinstance(value, str):
        if any(not (0x20 <= ord(char) <= 0x7E) for char in value):
            raise ValueError("strings must be printable ASCII")
        return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'
    if isinstance(value, bytes):
        return ":" + base64.b64encode(value).decode("ascii") + ":"
    if isinstance(value, int):
        return str(value)
    if isinstance(value, float):
        return f"{value:.3f}".rstrip("0").rstrip(".") if value != int(value) else f"{int(value)}.0"
    raise TypeError(f"cannot serialize {value!r}")


def serialize_parameters(params: Parameters) -> str:
    out = ""
    for name, value in params.items():
        out += ";" + name
        if value is not True:
            out += "=" + serialize_bare_item(value)
    return out


def serialize_item(item: Item) -> str:
    return serialize_bare_item(item.value) + serialize_parameters(item.params)


def serialize_inner_list(inner: InnerList) -> str:
    return (
        "(" + " ".join(serialize_item(item) for item in inner.items) + ")"
        + serialize_parameters(inner.params)
    )


def serialize_member(member: Member) -> str:
    return serialize_inner_list(member) if isinstance(member, InnerList) else serialize_item(member)


def serialize_dictionary(members: dict[str, Member]) -> str:
    parts = []
    for name, member in members.items():
        if isinstance(member, Item) and member.value is True:
            parts.append(name + serialize_parameters(member.params))
        else:
            parts.append(f"{name}={serialize_member(member)}")
    return ", ".join(parts)
