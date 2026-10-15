from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.search_hit_folder import SearchHitFolder

T = TypeVar("T", bound="SearchHit")


@_attrs_define
class SearchHit:
    """
    Attributes:
        id (str):
        identity_id (None | str):
        thread_id (str):
        direction (str):
        from_ (str): The address that sent it.
        from_name (None | str): The sender’s display name, when it had one.
        to (list[str]): Every address it was sent to.
        counterparty (str): Who the row is about: the sender on a received message, the recipient on a sent one. What a
            mail client prints in the list.
        counterparty_name (str): The same party, as a name to show.
        subject (None | str):
        preview (None | str):
        is_read (bool):
        is_starred (bool):
        is_draft (bool):
        is_spam (bool):
        has_attachments (bool):
        attachment_count (int):
        message_count (int):
        assignee_id (None | str):
        timestamp (str): ISO-8601, UTC.
        folder (SearchHitFolder): The folder the hit was found in.
        identity (None | str): The mailbox it was found in, as the address. `identity_id` is the same row.
    """

    id: str
    identity_id: None | str
    thread_id: str
    direction: str
    from_: str
    from_name: None | str
    to: list[str]
    counterparty: str
    counterparty_name: str
    subject: None | str
    preview: None | str
    is_read: bool
    is_starred: bool
    is_draft: bool
    is_spam: bool
    has_attachments: bool
    attachment_count: int
    message_count: int
    assignee_id: None | str
    timestamp: str
    folder: SearchHitFolder
    identity: None | str

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        identity_id: None | str
        identity_id = self.identity_id

        thread_id = self.thread_id

        direction = self.direction

        from_ = self.from_

        from_name: None | str
        from_name = self.from_name

        to = self.to

        counterparty = self.counterparty

        counterparty_name = self.counterparty_name

        subject: None | str
        subject = self.subject

        preview: None | str
        preview = self.preview

        is_read = self.is_read

        is_starred = self.is_starred

        is_draft = self.is_draft

        is_spam = self.is_spam

        has_attachments = self.has_attachments

        attachment_count = self.attachment_count

        message_count = self.message_count

        assignee_id: None | str
        assignee_id = self.assignee_id

        timestamp = self.timestamp

        folder = self.folder.value

        identity: None | str
        identity = self.identity

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "identity_id": identity_id,
                "thread_id": thread_id,
                "direction": direction,
                "from": from_,
                "from_name": from_name,
                "to": to,
                "counterparty": counterparty,
                "counterparty_name": counterparty_name,
                "subject": subject,
                "preview": preview,
                "is_read": is_read,
                "is_starred": is_starred,
                "is_draft": is_draft,
                "is_spam": is_spam,
                "has_attachments": has_attachments,
                "attachment_count": attachment_count,
                "message_count": message_count,
                "assignee_id": assignee_id,
                "timestamp": timestamp,
                "folder": folder,
                "identity": identity,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_identity_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        identity_id = _parse_identity_id(d.pop("identity_id"))

        thread_id = d.pop("thread_id")

        direction = d.pop("direction")

        from_ = d.pop("from")

        def _parse_from_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        from_name = _parse_from_name(d.pop("from_name"))

        to = cast(list[str], d.pop("to"))

        counterparty = d.pop("counterparty")

        counterparty_name = d.pop("counterparty_name")

        def _parse_subject(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        subject = _parse_subject(d.pop("subject"))

        def _parse_preview(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        preview = _parse_preview(d.pop("preview"))

        is_read = d.pop("is_read")

        is_starred = d.pop("is_starred")

        is_draft = d.pop("is_draft")

        is_spam = d.pop("is_spam")

        has_attachments = d.pop("has_attachments")

        attachment_count = d.pop("attachment_count")

        message_count = d.pop("message_count")

        def _parse_assignee_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        assignee_id = _parse_assignee_id(d.pop("assignee_id"))

        timestamp = d.pop("timestamp")

        folder = SearchHitFolder(d.pop("folder"))

        def _parse_identity(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        identity = _parse_identity(d.pop("identity"))

        search_hit = cls(
            id=id,
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
            has_attachments=has_attachments,
            attachment_count=attachment_count,
            message_count=message_count,
            assignee_id=assignee_id,
            timestamp=timestamp,
            folder=folder,
            identity=identity,
        )

        return search_hit
