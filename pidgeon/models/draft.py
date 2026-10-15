from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.draft_attachments_item import DraftAttachmentsItem


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
        thread_id (None | str):
        send_at (None | str):
        failed_reason (None | str):
        saved_at (None | str):
        created_at (str):
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
    thread_id: None | str
    send_at: None | str
    failed_reason: None | str
    saved_at: None | str
    created_at: str
    attachments: list[DraftAttachmentsItem]

    def to_dict(self) -> dict[str, Any]:
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

        thread_id: None | str
        thread_id = self.thread_id

        send_at: None | str
        send_at = self.send_at

        failed_reason: None | str
        failed_reason = self.failed_reason

        saved_at: None | str
        saved_at = self.saved_at

        created_at = self.created_at

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
                "thread_id": thread_id,
                "send_at": send_at,
                "failed_reason": failed_reason,
                "saved_at": saved_at,
                "created_at": created_at,
                "attachments": attachments,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.draft_attachments_item import DraftAttachmentsItem  # noqa: PLC0415

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
            thread_id=thread_id,
            send_at=send_at,
            failed_reason=failed_reason,
            saved_at=saved_at,
            created_at=created_at,
            attachments=attachments,
        )

        return draft
