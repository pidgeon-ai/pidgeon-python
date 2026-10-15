from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="SentRejectedItem")


@_attrs_define
class SentRejectedItem:
    """
    Attributes:
        address (str):
        reason (str):
    """

    address: str
    reason: str

    def to_dict(self) -> dict[str, Any]:
        address = self.address

        reason = self.reason

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "address": address,
                "reason": reason,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        address = d.pop("address")

        reason = d.pop("reason")

        sent_rejected_item = cls(
            address=address,
            reason=reason,
        )

        return sent_rejected_item
