from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="SenderVerificationOperatorType0")


@_attrs_define
class SenderVerificationOperatorType0:
    """
    Attributes:
        domain (str):
        verified (bool): True only when the domain’s owner proved it.
        shared (bool): True for pidgeon.email and a company’s name on it: a shared domain anyone can get an address on,
            so never `verified`.
    """

    domain: str
    verified: bool
    shared: bool

    def to_dict(self) -> dict[str, Any]:
        domain = self.domain

        verified = self.verified

        shared = self.shared

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "domain": domain,
                "verified": verified,
                "shared": shared,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        domain = d.pop("domain")

        verified = d.pop("verified")

        shared = d.pop("shared")

        sender_verification_operator_type_0 = cls(
            domain=domain,
            verified=verified,
            shared=shared,
        )

        return sender_verification_operator_type_0
