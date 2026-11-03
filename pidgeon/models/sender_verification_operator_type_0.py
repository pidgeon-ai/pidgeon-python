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
        verified (bool):
    """

    domain: str
    verified: bool

    def to_dict(self) -> dict[str, Any]:
        domain = self.domain

        verified = self.verified

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "domain": domain,
                "verified": verified,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        domain = d.pop("domain")

        verified = d.pop("verified")

        sender_verification_operator_type_0 = cls(
            domain=domain,
            verified=verified,
        )

        return sender_verification_operator_type_0
