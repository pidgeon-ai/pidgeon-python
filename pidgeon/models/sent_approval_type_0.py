from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.sent_approval_type_0_reason import SentApprovalType0Reason

T = TypeVar("T", bound="SentApprovalType0")


@_attrs_define
class SentApprovalType0:
    """
    Attributes:
        reason (SentApprovalType0Reason): `first_contact`: the address asks a person before writing to someone new.
            `risky_thread`: a message in this conversation from the last 72 hours tried to give the agent instructions.
        expires_at (str): It expires unsent at this time if nobody decides.
    """

    reason: SentApprovalType0Reason
    expires_at: str

    def to_dict(self) -> dict[str, Any]:
        reason = self.reason.value

        expires_at = self.expires_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "reason": reason,
                "expires_at": expires_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        reason = SentApprovalType0Reason(d.pop("reason"))

        expires_at = d.pop("expires_at")

        sent_approval_type_0 = cls(
            reason=reason,
            expires_at=expires_at,
        )

        return sent_approval_type_0
