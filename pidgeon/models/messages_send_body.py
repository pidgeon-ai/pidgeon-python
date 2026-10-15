from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="MessagesSendBody")


@_attrs_define
class MessagesSendBody:
    """
    Attributes:
        from_ (str): An address on a domain you own, and one this key may send from.
        to (list[str] | str): One address or several. A string is accepted for the single case.
        cc (list[str] | str | Unset): Copied, and visible to everybody who receives the message.
        bcc (list[str] | str | Unset): Copied, and visible to nobody else.
        subject (str | Unset): Left off a reply, where the thread already has one. Default: ''.
        text (str | Unset): The plain-text body. Send this even when you send `html` — some clients only read it.
            Default: ''.
        html (str | Unset): The rich body. Sanitised on the way in; scripts and remote content are removed.
        attachment_ids (list[UUID] | Unset): Ids from `POST /attachments`, uploaded before the message that carries
            them. Up to 20.
        in_reply_to (None | Unset | UUID): The message being answered. Keeps the conversation together in the
            recipient’s client too.
        in_reply_to_message_id (None | Unset | UUID): The same field as `in_reply_to`, under the name this endpoint has
            always used. Both names work on both endpoints; reach for `in_reply_to`.
    """

    from_: str
    to: list[str] | str
    cc: list[str] | str | Unset = UNSET
    bcc: list[str] | str | Unset = UNSET
    subject: str | Unset = ""
    text: str | Unset = ""
    html: str | Unset = UNSET
    attachment_ids: list[UUID] | Unset = UNSET
    in_reply_to: None | Unset | UUID = UNSET
    in_reply_to_message_id: None | Unset | UUID = UNSET

    def to_dict(self) -> dict[str, Any]:
        from_ = self.from_

        to: list[str] | str
        if isinstance(self.to, list):
            to = self.to

        else:
            to = self.to

        cc: list[str] | str | Unset
        if isinstance(self.cc, Unset):
            cc = UNSET
        elif isinstance(self.cc, list):
            cc = self.cc

        else:
            cc = self.cc

        bcc: list[str] | str | Unset
        if isinstance(self.bcc, Unset):
            bcc = UNSET
        elif isinstance(self.bcc, list):
            bcc = self.bcc

        else:
            bcc = self.bcc

        subject = self.subject

        text = self.text

        html = self.html

        attachment_ids: list[str] | Unset = UNSET
        if not isinstance(self.attachment_ids, Unset):
            attachment_ids = []
            for attachment_ids_item_data in self.attachment_ids:
                attachment_ids_item = str(attachment_ids_item_data)
                attachment_ids.append(attachment_ids_item)

        in_reply_to: None | str | Unset
        if isinstance(self.in_reply_to, Unset):
            in_reply_to = UNSET
        elif isinstance(self.in_reply_to, UUID):
            in_reply_to = str(self.in_reply_to)
        else:
            in_reply_to = self.in_reply_to

        in_reply_to_message_id: None | str | Unset
        if isinstance(self.in_reply_to_message_id, Unset):
            in_reply_to_message_id = UNSET
        elif isinstance(self.in_reply_to_message_id, UUID):
            in_reply_to_message_id = str(self.in_reply_to_message_id)
        else:
            in_reply_to_message_id = self.in_reply_to_message_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "from": from_,
                "to": to,
            }
        )
        if cc is not UNSET:
            field_dict["cc"] = cc
        if bcc is not UNSET:
            field_dict["bcc"] = bcc
        if subject is not UNSET:
            field_dict["subject"] = subject
        if text is not UNSET:
            field_dict["text"] = text
        if html is not UNSET:
            field_dict["html"] = html
        if attachment_ids is not UNSET:
            field_dict["attachment_ids"] = attachment_ids
        if in_reply_to is not UNSET:
            field_dict["in_reply_to"] = in_reply_to
        if in_reply_to_message_id is not UNSET:
            field_dict["in_reply_to_message_id"] = in_reply_to_message_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        from_ = d.pop("from")

        def _parse_to(data: object) -> list[str] | str:
            try:
                if not isinstance(data, list):
                    raise TypeError()
                to_type_1 = cast(list[str], data)

                return to_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | str, data)

        to = _parse_to(d.pop("to"))

        def _parse_cc(data: object) -> list[str] | str | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                cc_type_1 = cast(list[str], data)

                return cc_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | str | Unset, data)

        cc = _parse_cc(d.pop("cc", UNSET))

        def _parse_bcc(data: object) -> list[str] | str | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                bcc_type_1 = cast(list[str], data)

                return bcc_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | str | Unset, data)

        bcc = _parse_bcc(d.pop("bcc", UNSET))

        subject = d.pop("subject", UNSET)

        text = d.pop("text", UNSET)

        html = d.pop("html", UNSET)

        _attachment_ids = d.pop("attachment_ids", UNSET)
        attachment_ids: list[UUID] | Unset = UNSET
        if _attachment_ids is not UNSET:
            attachment_ids = []
            for attachment_ids_item_data in _attachment_ids:
                attachment_ids_item = UUID(attachment_ids_item_data)

                attachment_ids.append(attachment_ids_item)

        def _parse_in_reply_to(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                in_reply_to_type_0 = UUID(data)

                return in_reply_to_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        in_reply_to = _parse_in_reply_to(d.pop("in_reply_to", UNSET))

        def _parse_in_reply_to_message_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                in_reply_to_message_id_type_0 = UUID(data)

                return in_reply_to_message_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        in_reply_to_message_id = _parse_in_reply_to_message_id(d.pop("in_reply_to_message_id", UNSET))

        messages_send_body = cls(
            from_=from_,
            to=to,
            cc=cc,
            bcc=bcc,
            subject=subject,
            text=text,
            html=html,
            attachment_ids=attachment_ids,
            in_reply_to=in_reply_to,
            in_reply_to_message_id=in_reply_to_message_id,
        )

        return messages_send_body
