from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.sent_status import SentStatus

if TYPE_CHECKING:
    from ..models.sent_approval_type_0 import SentApprovalType0
    from ..models.sent_rejected_item import SentRejectedItem


T = TypeVar("T", bound="Sent")


@_attrs_define
class Sent:
    """
    Attributes:
        status (SentStatus): `sent`: handed to the network. `pending_approval`: **nothing was sent** — the message is a
            draft waiting for a person to approve it (`approval` says why and until when). Poll `GET
            /drafts/{draft_id}/approval`, or subscribe to `draft.approved`, `draft.rejected` and `draft.expired`.
        id (str): The message. On `pending_approval` it is the draft’s id, which the message keeps if it is approved.
        draft_id (None | str): The held draft on `pending_approval`; null on `sent`.
        thread_id (str):
        rejected (list[SentRejectedItem]):
        test (bool): True when this was a test-mode send: nothing was handed to the mail provider, and only this
            account’s own addresses received it.
        approval (None | SentApprovalType0): Why the send is waiting, on `pending_approval`. Null on `sent`.
    """

    status: SentStatus
    id: str
    draft_id: None | str
    thread_id: str
    rejected: list[SentRejectedItem]
    test: bool
    approval: None | SentApprovalType0

    def to_dict(self) -> dict[str, Any]:
        from ..models.sent_approval_type_0 import SentApprovalType0  # noqa: PLC0415

        status = self.status.value

        id = self.id

        draft_id: None | str
        draft_id = self.draft_id

        thread_id = self.thread_id

        rejected = []
        for rejected_item_data in self.rejected:
            rejected_item = rejected_item_data.to_dict()
            rejected.append(rejected_item)

        test = self.test

        approval: dict[str, Any] | None
        if isinstance(self.approval, SentApprovalType0):
            approval = self.approval.to_dict()
        else:
            approval = self.approval

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "status": status,
                "id": id,
                "draft_id": draft_id,
                "thread_id": thread_id,
                "rejected": rejected,
                "test": test,
                "approval": approval,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sent_approval_type_0 import SentApprovalType0  # noqa: PLC0415
        from ..models.sent_rejected_item import SentRejectedItem  # noqa: PLC0415

        d = dict(src_dict)
        status = SentStatus(d.pop("status"))

        id = d.pop("id")

        def _parse_draft_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        draft_id = _parse_draft_id(d.pop("draft_id"))

        thread_id = d.pop("thread_id")

        rejected = []
        _rejected = d.pop("rejected")
        for rejected_item_data in _rejected:
            rejected_item = SentRejectedItem.from_dict(rejected_item_data)

            rejected.append(rejected_item)

        test = d.pop("test")

        def _parse_approval(data: object) -> None | SentApprovalType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                approval_type_0 = SentApprovalType0.from_dict(data)

                return approval_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SentApprovalType0, data)

        approval = _parse_approval(d.pop("approval"))

        sent = cls(
            status=status,
            id=id,
            draft_id=draft_id,
            thread_id=thread_id,
            rejected=rejected,
            test=test,
            approval=approval,
        )

        return sent
