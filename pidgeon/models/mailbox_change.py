from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="MailboxChange")


@_attrs_define
class MailboxChange:
    """
    Attributes:
        id (str):
        changed_at (str): ISO-8601, UTC.
        deleted (bool):
        identity_id (None | str | Unset):
        thread_id (str | Unset):
        direction (str | Unset):
        from_ (str | Unset): The address that sent it.
        from_name (None | str | Unset): The sender’s display name, when it had one.
        to (list[str] | Unset): Every address it was sent to.
        counterparty (str | Unset): Who the row is about: the sender on a received message, the recipient on a sent one.
            What a mail client prints in the list.
        counterparty_name (str | Unset): The same party, as a name to show.
        subject (None | str | Unset):
        preview (None | str | Unset):
        is_read (bool | Unset):
        is_starred (bool | Unset):
        is_draft (bool | Unset):
        is_spam (bool | Unset):
        is_held (bool | Unset): Held by Pidgeon Firewall for a person. To a key, `subject`, `preview` and `from_name`
            are null until a person releases it.
        has_attachments (bool | Unset):
        attachment_count (int | Unset):
        message_count (int | Unset):
        assignee_id (None | str | Unset):
        timestamp (str | Unset): ISO-8601, UTC.
        folder (None | str | Unset):
    """

    id: str
    changed_at: str
    deleted: bool
    identity_id: None | str | Unset = UNSET
    thread_id: str | Unset = UNSET
    direction: str | Unset = UNSET
    from_: str | Unset = UNSET
    from_name: None | str | Unset = UNSET
    to: list[str] | Unset = UNSET
    counterparty: str | Unset = UNSET
    counterparty_name: str | Unset = UNSET
    subject: None | str | Unset = UNSET
    preview: None | str | Unset = UNSET
    is_read: bool | Unset = UNSET
    is_starred: bool | Unset = UNSET
    is_draft: bool | Unset = UNSET
    is_spam: bool | Unset = UNSET
    is_held: bool | Unset = UNSET
    has_attachments: bool | Unset = UNSET
    attachment_count: int | Unset = UNSET
    message_count: int | Unset = UNSET
    assignee_id: None | str | Unset = UNSET
    timestamp: str | Unset = UNSET
    folder: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        changed_at = self.changed_at

        deleted = self.deleted

        identity_id: None | str | Unset
        if isinstance(self.identity_id, Unset):
            identity_id = UNSET
        else:
            identity_id = self.identity_id

        thread_id = self.thread_id

        direction = self.direction

        from_ = self.from_

        from_name: None | str | Unset
        if isinstance(self.from_name, Unset):
            from_name = UNSET
        else:
            from_name = self.from_name

        to: list[str] | Unset = UNSET
        if not isinstance(self.to, Unset):
            to = self.to

        counterparty = self.counterparty

        counterparty_name = self.counterparty_name

        subject: None | str | Unset
        if isinstance(self.subject, Unset):
            subject = UNSET
        else:
            subject = self.subject

        preview: None | str | Unset
        if isinstance(self.preview, Unset):
            preview = UNSET
        else:
            preview = self.preview

        is_read = self.is_read

        is_starred = self.is_starred

        is_draft = self.is_draft

        is_spam = self.is_spam

        is_held = self.is_held

        has_attachments = self.has_attachments

        attachment_count = self.attachment_count

        message_count = self.message_count

        assignee_id: None | str | Unset
        if isinstance(self.assignee_id, Unset):
            assignee_id = UNSET
        else:
            assignee_id = self.assignee_id

        timestamp = self.timestamp

        folder: None | str | Unset
        if isinstance(self.folder, Unset):
            folder = UNSET
        else:
            folder = self.folder

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "changed_at": changed_at,
                "deleted": deleted,
            }
        )
        if identity_id is not UNSET:
            field_dict["identity_id"] = identity_id
        if thread_id is not UNSET:
            field_dict["thread_id"] = thread_id
        if direction is not UNSET:
            field_dict["direction"] = direction
        if from_ is not UNSET:
            field_dict["from"] = from_
        if from_name is not UNSET:
            field_dict["from_name"] = from_name
        if to is not UNSET:
            field_dict["to"] = to
        if counterparty is not UNSET:
            field_dict["counterparty"] = counterparty
        if counterparty_name is not UNSET:
            field_dict["counterparty_name"] = counterparty_name
        if subject is not UNSET:
            field_dict["subject"] = subject
        if preview is not UNSET:
            field_dict["preview"] = preview
        if is_read is not UNSET:
            field_dict["is_read"] = is_read
        if is_starred is not UNSET:
            field_dict["is_starred"] = is_starred
        if is_draft is not UNSET:
            field_dict["is_draft"] = is_draft
        if is_spam is not UNSET:
            field_dict["is_spam"] = is_spam
        if is_held is not UNSET:
            field_dict["is_held"] = is_held
        if has_attachments is not UNSET:
            field_dict["has_attachments"] = has_attachments
        if attachment_count is not UNSET:
            field_dict["attachment_count"] = attachment_count
        if message_count is not UNSET:
            field_dict["message_count"] = message_count
        if assignee_id is not UNSET:
            field_dict["assignee_id"] = assignee_id
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if folder is not UNSET:
            field_dict["folder"] = folder

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        changed_at = d.pop("changed_at")

        deleted = d.pop("deleted")

        def _parse_identity_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        identity_id = _parse_identity_id(d.pop("identity_id", UNSET))

        thread_id = d.pop("thread_id", UNSET)

        direction = d.pop("direction", UNSET)

        from_ = d.pop("from", UNSET)

        def _parse_from_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        from_name = _parse_from_name(d.pop("from_name", UNSET))

        to = cast(list[str], d.pop("to", UNSET))

        counterparty = d.pop("counterparty", UNSET)

        counterparty_name = d.pop("counterparty_name", UNSET)

        def _parse_subject(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subject = _parse_subject(d.pop("subject", UNSET))

        def _parse_preview(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        preview = _parse_preview(d.pop("preview", UNSET))

        is_read = d.pop("is_read", UNSET)

        is_starred = d.pop("is_starred", UNSET)

        is_draft = d.pop("is_draft", UNSET)

        is_spam = d.pop("is_spam", UNSET)

        is_held = d.pop("is_held", UNSET)

        has_attachments = d.pop("has_attachments", UNSET)

        attachment_count = d.pop("attachment_count", UNSET)

        message_count = d.pop("message_count", UNSET)

        def _parse_assignee_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        assignee_id = _parse_assignee_id(d.pop("assignee_id", UNSET))

        timestamp = d.pop("timestamp", UNSET)

        def _parse_folder(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        folder = _parse_folder(d.pop("folder", UNSET))

        mailbox_change = cls(
            id=id,
            changed_at=changed_at,
            deleted=deleted,
            identity_id=identity_id,
            thread_id=thread_id,
            direction=direction,
            from_=from_,
            from_name=from_name,
            to=to,
            counterparty=counterparty,
            counterparty_name=counterparty_name,
            subject=subject,
            preview=preview,
            is_read=is_read,
            is_starred=is_starred,
            is_draft=is_draft,
            is_spam=is_spam,
            is_held=is_held,
            has_attachments=has_attachments,
            attachment_count=attachment_count,
            message_count=message_count,
            assignee_id=assignee_id,
            timestamp=timestamp,
            folder=folder,
        )

        return mailbox_change
