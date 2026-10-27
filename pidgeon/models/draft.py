from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.draft_approval_type_0 import DraftApprovalType0
    from ..models.draft_attachments_item import DraftAttachmentsItem
    from ..models.draft_data_type_0 import DraftDataType0


T = TypeVar("T", bound="Draft")


@_attrs_define
class Draft:
    """
    Attributes:
        id (str):
        identity (None | str):
        identity_id (str):
        from_ (str):
        to (list[str]):
        cc (list[str]):
        bcc (list[str]):
        subject (None | str):
        text (None | str):
        data (DraftDataType0 | None): Typed data, sent with the draft when it goes. Null when there is none.
        thread_id (None | str):
        send_at (None | str):
        failed_reason (None | str):
        saved_at (None | str):
        created_at (str):
        approval (DraftApprovalType0 | None): Set when a send of this draft was held for a person to approve. Null on a
            draft nobody tried to send.
        attachments (list[DraftAttachmentsItem]):
    """

    id: str
    identity: None | str
    identity_id: str
    from_: str
    to: list[str]
    cc: list[str]
    bcc: list[str]
    subject: None | str
    text: None | str
    data: DraftDataType0 | None
    thread_id: None | str
    send_at: None | str
    failed_reason: None | str
    saved_at: None | str
    created_at: str
    approval: DraftApprovalType0 | None
    attachments: list[DraftAttachmentsItem]

    def to_dict(self) -> dict[str, Any]:
        from ..models.draft_approval_type_0 import DraftApprovalType0  # noqa: PLC0415
        from ..models.draft_data_type_0 import DraftDataType0  # noqa: PLC0415

        id = self.id

        identity: None | str
        identity = self.identity

        identity_id = self.identity_id

        from_ = self.from_

        to = self.to

        cc = self.cc

        bcc = self.bcc

        subject: None | str
        subject = self.subject

        text: None | str
        text = self.text

        data: dict[str, Any] | None
        if isinstance(self.data, DraftDataType0):
            data = self.data.to_dict()
        else:
            data = self.data

        thread_id: None | str
        thread_id = self.thread_id

        send_at: None | str
        send_at = self.send_at

        failed_reason: None | str
        failed_reason = self.failed_reason

        saved_at: None | str
        saved_at = self.saved_at

        created_at = self.created_at

        approval: dict[str, Any] | None
        if isinstance(self.approval, DraftApprovalType0):
            approval = self.approval.to_dict()
        else:
            approval = self.approval

        attachments = []
        for attachments_item_data in self.attachments:
            attachments_item = attachments_item_data.to_dict()
            attachments.append(attachments_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "identity": identity,
                "identity_id": identity_id,
                "from": from_,
                "to": to,
                "cc": cc,
                "bcc": bcc,
                "subject": subject,
                "text": text,
                "data": data,
                "thread_id": thread_id,
                "send_at": send_at,
                "failed_reason": failed_reason,
                "saved_at": saved_at,
                "created_at": created_at,
                "approval": approval,
                "attachments": attachments,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.draft_approval_type_0 import DraftApprovalType0  # noqa: PLC0415
        from ..models.draft_attachments_item import DraftAttachmentsItem  # noqa: PLC0415
        from ..models.draft_data_type_0 import DraftDataType0  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id")

        def _parse_identity(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        identity = _parse_identity(d.pop("identity"))

        identity_id = d.pop("identity_id")

        from_ = d.pop("from")

        to = cast(list[str], d.pop("to"))

        cc = cast(list[str], d.pop("cc"))

        bcc = cast(list[str], d.pop("bcc"))

        def _parse_subject(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        subject = _parse_subject(d.pop("subject"))

        def _parse_text(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        text = _parse_text(d.pop("text"))

        def _parse_data(data: object) -> DraftDataType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = DraftDataType0.from_dict(data)

                return data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DraftDataType0 | None, data)

        data = _parse_data(d.pop("data"))

        def _parse_thread_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        thread_id = _parse_thread_id(d.pop("thread_id"))

        def _parse_send_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        send_at = _parse_send_at(d.pop("send_at"))

        def _parse_failed_reason(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        failed_reason = _parse_failed_reason(d.pop("failed_reason"))

        def _parse_saved_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        saved_at = _parse_saved_at(d.pop("saved_at"))

        created_at = d.pop("created_at")

        def _parse_approval(data: object) -> DraftApprovalType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                approval_type_0 = DraftApprovalType0.from_dict(data)

                return approval_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DraftApprovalType0 | None, data)

        approval = _parse_approval(d.pop("approval"))

        attachments = []
        _attachments = d.pop("attachments")
        for attachments_item_data in _attachments:
            attachments_item = DraftAttachmentsItem.from_dict(attachments_item_data)

            attachments.append(attachments_item)

        draft = cls(
            id=id,
            identity=identity,
            identity_id=identity_id,
            from_=from_,
            to=to,
            cc=cc,
            bcc=bcc,
            subject=subject,
            text=text,
            data=data,
            thread_id=thread_id,
            send_at=send_at,
            failed_reason=failed_reason,
            saved_at=saved_at,
            created_at=created_at,
            approval=approval,
            attachments=attachments,
        )

        return draft
