from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.messages_reply_all_body_data import MessagesReplyAllBodyData


T = TypeVar("T", bound="MessagesReplyAllBody")


@_attrs_define
class MessagesReplyAllBody:
    """
    Attributes:
        text (str | Unset): The plain-text body. Send this even when you send `html` — some clients only read it.
            Default: ''.
        html (str | Unset): The rich body. Sanitised on the way in; scripts and remote content are removed.
        data (MessagesReplyAllBodyData | Unset): Typed data: structured JSON sent beside the text, for software at the
            other end to read as fields. Travels as its own part; it is never mixed into the text.
        to (list[str] | str | Unset): One address or several. A string is accepted for the single case.
        cc (list[str] | str | Unset): Copied, and visible to everybody who receives the message.
        bcc (list[str] | str | Unset): Copied, and visible to nobody else.
        attachment_ids (list[UUID] | Unset): Ids from `POST /attachments`, uploaded before the message that carries
            them. Up to 20.
    """

    text: str | Unset = ""
    html: str | Unset = UNSET
    data: MessagesReplyAllBodyData | Unset = UNSET
    to: list[str] | str | Unset = UNSET
    cc: list[str] | str | Unset = UNSET
    bcc: list[str] | str | Unset = UNSET
    attachment_ids: list[UUID] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        text = self.text

        html = self.html

        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        to: list[str] | str | Unset
        if isinstance(self.to, Unset):
            to = UNSET
        elif isinstance(self.to, list):
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

        attachment_ids: list[str] | Unset = UNSET
        if not isinstance(self.attachment_ids, Unset):
            attachment_ids = []
            for attachment_ids_item_data in self.attachment_ids:
                attachment_ids_item = str(attachment_ids_item_data)
                attachment_ids.append(attachment_ids_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if text is not UNSET:
            field_dict["text"] = text
        if html is not UNSET:
            field_dict["html"] = html
        if data is not UNSET:
            field_dict["data"] = data
        if to is not UNSET:
            field_dict["to"] = to
        if cc is not UNSET:
            field_dict["cc"] = cc
        if bcc is not UNSET:
            field_dict["bcc"] = bcc
        if attachment_ids is not UNSET:
            field_dict["attachment_ids"] = attachment_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.messages_reply_all_body_data import MessagesReplyAllBodyData  # noqa: PLC0415

        d = dict(src_dict)
        text = d.pop("text", UNSET)

        html = d.pop("html", UNSET)

        _data = d.pop("data", UNSET)
        data: MessagesReplyAllBodyData | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = MessagesReplyAllBodyData.from_dict(_data)

        def _parse_to(data: object) -> list[str] | str | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                to_type_1 = cast(list[str], data)

                return to_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | str | Unset, data)

        to = _parse_to(d.pop("to", UNSET))

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

        _attachment_ids = d.pop("attachment_ids", UNSET)
        attachment_ids: list[UUID] | Unset = UNSET
        if _attachment_ids is not UNSET:
            attachment_ids = []
            for attachment_ids_item_data in _attachment_ids:
                attachment_ids_item = UUID(attachment_ids_item_data)

                attachment_ids.append(attachment_ids_item)

        messages_reply_all_body = cls(
            text=text,
            html=html,
            data=data,
            to=to,
            cc=cc,
            bcc=bcc,
            attachment_ids=attachment_ids,
        )

        messages_reply_all_body.additional_properties = d
        return messages_reply_all_body

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
