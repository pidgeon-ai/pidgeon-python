from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.approval_reason import ApprovalReason
from ..models.approval_status import ApprovalStatus

T = TypeVar("T", bound="Approval")


@_attrs_define
class Approval:
    """
    Attributes:
        draft_id (str):
        identity_id (str):
        thread_id (str):
        status (ApprovalStatus): `pending` until a person decides, or 24 hours pass.
        reason (ApprovalReason): Why it was held. The person approving sees the same reason.
        requested_at (str):
        expires_at (str):
        decided_at (None | str): When it was approved, rejected or expired. Null while pending.
        message_id (None | str): The sent message, once approved — the draft’s own id, because a send converts the
            draft.
    """

    draft_id: str
    identity_id: str
    thread_id: str
    status: ApprovalStatus
    reason: ApprovalReason
    requested_at: str
    expires_at: str
    decided_at: None | str
    message_id: None | str

    def to_dict(self) -> dict[str, Any]:
        draft_id = self.draft_id

        identity_id = self.identity_id

        thread_id = self.thread_id

        status = self.status.value

        reason = self.reason.value

        requested_at = self.requested_at

        expires_at = self.expires_at

        decided_at: None | str
        decided_at = self.decided_at

        message_id: None | str
        message_id = self.message_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "draft_id": draft_id,
                "identity_id": identity_id,
                "thread_id": thread_id,
                "status": status,
                "reason": reason,
                "requested_at": requested_at,
                "expires_at": expires_at,
                "decided_at": decided_at,
                "message_id": message_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        draft_id = d.pop("draft_id")

        identity_id = d.pop("identity_id")

        thread_id = d.pop("thread_id")

        status = ApprovalStatus(d.pop("status"))

        reason = ApprovalReason(d.pop("reason"))

        requested_at = d.pop("requested_at")

        expires_at = d.pop("expires_at")

        def _parse_decided_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        decided_at = _parse_decided_at(d.pop("decided_at"))

        def _parse_message_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        message_id = _parse_message_id(d.pop("message_id"))

        approval = cls(
            draft_id=draft_id,
            identity_id=identity_id,
            thread_id=thread_id,
            status=status,
            reason=reason,
            requested_at=requested_at,
            expires_at=expires_at,
            decided_at=decided_at,
            message_id=message_id,
        )

        return approval
