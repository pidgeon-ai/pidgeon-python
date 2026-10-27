from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.draft_approval_type_0_reason import DraftApprovalType0Reason
from ..models.draft_approval_type_0_status import DraftApprovalType0Status

T = TypeVar("T", bound="DraftApprovalType0")


@_attrs_define
class DraftApprovalType0:
    """
    Attributes:
        status (DraftApprovalType0Status): `pending` until a person decides. `expired` after 24 hours with no decision;
            the draft stays, unsent.
        reason (DraftApprovalType0Reason): `first_contact`: a first message to someone the address has never written to
            or heard from. `risky_thread`: a reply or forward on a conversation where a message from the last 72 hours tried
            to give the agent instructions.
        expires_at (str): When a pending send expires unsent.
    """

    status: DraftApprovalType0Status
    reason: DraftApprovalType0Reason
    expires_at: str

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        reason = self.reason.value

        expires_at = self.expires_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "status": status,
                "reason": reason,
                "expires_at": expires_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = DraftApprovalType0Status(d.pop("status"))

        reason = DraftApprovalType0Reason(d.pop("reason"))

        expires_at = d.pop("expires_at")

        draft_approval_type_0 = cls(
            status=status,
            reason=reason,
            expires_at=expires_at,
        )

        return draft_approval_type_0
