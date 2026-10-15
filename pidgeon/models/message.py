from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.message_attachments_item import MessageAttachmentsItem
    from ..models.message_authentication import MessageAuthentication
    from ..models.message_cc_item import MessageCcItem
    from ..models.message_from import MessageFrom
    from ..models.message_headers import MessageHeaders
    from ..models.message_invitation_type_0 import MessageInvitationType0
    from ..models.message_to_item import MessageToItem


T = TypeVar("T", bound="Message")


@_attrs_define
class Message:
    """
    Attributes:
        id (str):
        thread_id (str):
        identity_id (None | str): The mailbox this message is in, as an id. What `POST /attachments` and the other
            endpoints that take a mailbox expect — `identity` below is the same address as text.
        identity (None | str):
        direction (str):
        from_ (MessageFrom): A mailbox, with the display name when one was given.
        to (list[MessageToItem]):
        cc (list[MessageCcItem]):
        subject (None | str):
        delivered_to (None | str): The envelope recipient, which is not always in `to`.
        text (None | str):
        html (str): Sanitised server-side: our policy travels with the content.
        reply_html (str): `html` with the quoted history taken off: what the sender wrote this time.
        quoted_html (None | str): The history the reply quoted, or null when there was nothing to fold.
        reply_text (str): The reply as plain text. `text` is the message’s own text part, quote and all.
        is_read (bool):
        is_spam (bool):
        headers (MessageHeaders): The headers we keep, lowercased: `message-id`, `in-reply-to`, `references`, `date`,
            `reply-to`, `return-path`, `list-id`, `list-unsubscribe`, `precedence`, `auto-submitted`, `x-auto-response-
            suppress`, `x-mailer` and `x-priority`. Not the whole envelope — that is `GET /messages/{id}/raw`. Empty when
            none were present.
        authentication (MessageAuthentication): What the receiving transport said about the sending domain. Null means
            it did not report, not that the check failed — normal on outbound, and on inbound it is the difference between
            unknown and forged.
        attachments (list[MessageAttachmentsItem]):
        invitation (MessageInvitationType0 | None): The calendar part this message carried, or null — the invitation,
            who was asked, and what they answered.
        calendar_event_id (None | str): The event the calendar made of that invitation, or null. A different fact from
            `invitation`: that is what the mail said, this is what the calendar now holds — a meeting later moved still
            reports the time this message invited you to.
        created_at (str): ISO-8601, UTC.
    """

    id: str
    thread_id: str
    identity_id: None | str
    identity: None | str
    direction: str
    from_: MessageFrom
    to: list[MessageToItem]
    cc: list[MessageCcItem]
    subject: None | str
    delivered_to: None | str
    text: None | str
    html: str
    reply_html: str
    quoted_html: None | str
    reply_text: str
    is_read: bool
    is_spam: bool
    headers: MessageHeaders
    authentication: MessageAuthentication
    attachments: list[MessageAttachmentsItem]
    invitation: MessageInvitationType0 | None
    calendar_event_id: None | str
    created_at: str

    def to_dict(self) -> dict[str, Any]:
        from ..models.message_invitation_type_0 import MessageInvitationType0  # noqa: PLC0415

        id = self.id

        thread_id = self.thread_id

        identity_id: None | str
        identity_id = self.identity_id

        identity: None | str
        identity = self.identity

        direction = self.direction

        from_ = self.from_.to_dict()

        to = []
        for to_item_data in self.to:
            to_item = to_item_data.to_dict()
            to.append(to_item)

        cc = []
        for cc_item_data in self.cc:
            cc_item = cc_item_data.to_dict()
            cc.append(cc_item)

        subject: None | str
        subject = self.subject

        delivered_to: None | str
        delivered_to = self.delivered_to

        text: None | str
        text = self.text

        html = self.html

        reply_html = self.reply_html

        quoted_html: None | str
        quoted_html = self.quoted_html

        reply_text = self.reply_text

        is_read = self.is_read

        is_spam = self.is_spam

        headers = self.headers.to_dict()

        authentication = self.authentication.to_dict()

        attachments = []
        for attachments_item_data in self.attachments:
            attachments_item = attachments_item_data.to_dict()
            attachments.append(attachments_item)

        invitation: dict[str, Any] | None
        if isinstance(self.invitation, MessageInvitationType0):
            invitation = self.invitation.to_dict()
        else:
            invitation = self.invitation

        calendar_event_id: None | str
        calendar_event_id = self.calendar_event_id

        created_at = self.created_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "thread_id": thread_id,
                "identity_id": identity_id,
                "identity": identity,
                "direction": direction,
                "from": from_,
                "to": to,
                "cc": cc,
                "subject": subject,
                "delivered_to": delivered_to,
                "text": text,
                "html": html,
                "reply_html": reply_html,
                "quoted_html": quoted_html,
                "reply_text": reply_text,
                "is_read": is_read,
                "is_spam": is_spam,
                "headers": headers,
                "authentication": authentication,
                "attachments": attachments,
                "invitation": invitation,
                "calendar_event_id": calendar_event_id,
                "created_at": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.message_attachments_item import MessageAttachmentsItem  # noqa: PLC0415
        from ..models.message_authentication import MessageAuthentication  # noqa: PLC0415
        from ..models.message_cc_item import MessageCcItem  # noqa: PLC0415
        from ..models.message_from import MessageFrom  # noqa: PLC0415
        from ..models.message_headers import MessageHeaders  # noqa: PLC0415
        from ..models.message_invitation_type_0 import MessageInvitationType0  # noqa: PLC0415
        from ..models.message_to_item import MessageToItem  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id")

        thread_id = d.pop("thread_id")

        def _parse_identity_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        identity_id = _parse_identity_id(d.pop("identity_id"))

        def _parse_identity(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        identity = _parse_identity(d.pop("identity"))

        direction = d.pop("direction")

        from_ = MessageFrom.from_dict(d.pop("from"))

        to = []
        _to = d.pop("to")
        for to_item_data in _to:
            to_item = MessageToItem.from_dict(to_item_data)

            to.append(to_item)

        cc = []
        _cc = d.pop("cc")
        for cc_item_data in _cc:
            cc_item = MessageCcItem.from_dict(cc_item_data)

            cc.append(cc_item)

        def _parse_subject(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        subject = _parse_subject(d.pop("subject"))

        def _parse_delivered_to(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        delivered_to = _parse_delivered_to(d.pop("delivered_to"))

        def _parse_text(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        text = _parse_text(d.pop("text"))

        html = d.pop("html")

        reply_html = d.pop("reply_html")

        def _parse_quoted_html(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        quoted_html = _parse_quoted_html(d.pop("quoted_html"))

        reply_text = d.pop("reply_text")

        is_read = d.pop("is_read")

        is_spam = d.pop("is_spam")

        headers = MessageHeaders.from_dict(d.pop("headers"))

        authentication = MessageAuthentication.from_dict(d.pop("authentication"))

        attachments = []
        _attachments = d.pop("attachments")
        for attachments_item_data in _attachments:
            attachments_item = MessageAttachmentsItem.from_dict(attachments_item_data)

            attachments.append(attachments_item)

        def _parse_invitation(data: object) -> MessageInvitationType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invitation_type_0 = MessageInvitationType0.from_dict(data)

                return invitation_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MessageInvitationType0 | None, data)

        invitation = _parse_invitation(d.pop("invitation"))

        def _parse_calendar_event_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        calendar_event_id = _parse_calendar_event_id(d.pop("calendar_event_id"))

        created_at = d.pop("created_at")

        message = cls(
            id=id,
            thread_id=thread_id,
            identity_id=identity_id,
            identity=identity,
            direction=direction,
            from_=from_,
            to=to,
            cc=cc,
            subject=subject,
            delivered_to=delivered_to,
            text=text,
            html=html,
            reply_html=reply_html,
            quoted_html=quoted_html,
            reply_text=reply_text,
            is_read=is_read,
            is_spam=is_spam,
            headers=headers,
            authentication=authentication,
            attachments=attachments,
            invitation=invitation,
            calendar_event_id=calendar_event_id,
            created_at=created_at,
        )

        return message
