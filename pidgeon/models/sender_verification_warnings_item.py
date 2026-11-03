from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.sender_verification_warnings_item_code import SenderVerificationWarningsItemCode

T = TypeVar("T", bound="SenderVerificationWarningsItem")


@_attrs_define
class SenderVerificationWarningsItem:
    """
    Attributes:
        code (SenderVerificationWarningsItemCode):
        message (str):
    """

    code: SenderVerificationWarningsItemCode
    message: str

    def to_dict(self) -> dict[str, Any]:
        code = self.code.value

        message = self.message

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "code": code,
                "message": message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = SenderVerificationWarningsItemCode(d.pop("code"))

        message = d.pop("message")

        sender_verification_warnings_item = cls(
            code=code,
            message=message,
        )

        return sender_verification_warnings_item
