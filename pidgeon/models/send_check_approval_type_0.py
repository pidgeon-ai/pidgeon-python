from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.send_check_approval_type_0_reason import SendCheckApprovalType0Reason

T = TypeVar("T", bound="SendCheckApprovalType0")


@_attrs_define
class SendCheckApprovalType0:
    """
    Attributes:
        reason (SendCheckApprovalType0Reason):
    """

    reason: SendCheckApprovalType0Reason

    def to_dict(self) -> dict[str, Any]:
        reason = self.reason.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "reason": reason,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        reason = SendCheckApprovalType0Reason(d.pop("reason"))

        send_check_approval_type_0 = cls(
            reason=reason,
        )

        return send_check_approval_type_0
