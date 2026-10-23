from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.drafts_update_body_data_type_0 import DraftsUpdateBodyDataType0


T = TypeVar("T", bound="DraftsUpdateBody")


@_attrs_define
class DraftsUpdateBody:
    """
    Attributes:
        from_ (str | Unset): An address on a domain you own, and one this key may send from.
        to (list[str] | Unset): One address or several. A string is accepted for the single case.
        cc (list[str] | Unset): Copied, and visible to everybody who receives the message.
        bcc (list[str] | Unset): Copied, and visible to nobody else.
        subject (None | str | Unset): Left off a reply, where the thread already has one.
        text (None | str | Unset): The plain-text body. Send this even when you send `html` — some clients only read it.
        data (DraftsUpdateBodyDataType0 | None | Unset): Typed data: `{ schema, body }`, where `schema` is a URL naming
            what `body` is and `body` is up to 64 KB of JSON. Sent as its own part beside the text, never mixed into it.
        attachment_ids (list[UUID] | Unset): Ids from `POST /attachments`, uploaded before the message that carries
            them. Up to 20.
    """

    from_: str | Unset = UNSET
    to: list[str] | Unset = UNSET
    cc: list[str] | Unset = UNSET
    bcc: list[str] | Unset = UNSET
    subject: None | str | Unset = UNSET
    text: None | str | Unset = UNSET
    data: DraftsUpdateBodyDataType0 | None | Unset = UNSET
    attachment_ids: list[UUID] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.drafts_update_body_data_type_0 import DraftsUpdateBodyDataType0  # noqa: PLC0415

        from_ = self.from_

        to: list[str] | Unset = UNSET
        if not isinstance(self.to, Unset):
            to = self.to

        cc: list[str] | Unset = UNSET
        if not isinstance(self.cc, Unset):
            cc = self.cc

        bcc: list[str] | Unset = UNSET
        if not isinstance(self.bcc, Unset):
            bcc = self.bcc

        subject: None | str | Unset
        if isinstance(self.subject, Unset):
            subject = UNSET
        else:
            subject = self.subject

        text: None | str | Unset
        if isinstance(self.text, Unset):
            text = UNSET
        else:
            text = self.text

        data: dict[str, Any] | None | Unset
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, DraftsUpdateBodyDataType0):
            data = self.data.to_dict()
        else:
            data = self.data

        attachment_ids: list[str] | Unset = UNSET
        if not isinstance(self.attachment_ids, Unset):
            attachment_ids = []
            for attachment_ids_item_data in self.attachment_ids:
                attachment_ids_item = str(attachment_ids_item_data)
                attachment_ids.append(attachment_ids_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to
        if cc is not UNSET:
            field_dict["cc"] = cc
        if bcc is not UNSET:
            field_dict["bcc"] = bcc
        if subject is not UNSET:
            field_dict["subject"] = subject
        if text is not UNSET:
            field_dict["text"] = text
        if data is not UNSET:
            field_dict["data"] = data
        if attachment_ids is not UNSET:
            field_dict["attachment_ids"] = attachment_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.drafts_update_body_data_type_0 import DraftsUpdateBodyDataType0  # noqa: PLC0415

        d = dict(src_dict)
        from_ = d.pop("from", UNSET)

        to = cast(list[str], d.pop("to", UNSET))

        cc = cast(list[str], d.pop("cc", UNSET))

        bcc = cast(list[str], d.pop("bcc", UNSET))

        def _parse_subject(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subject = _parse_subject(d.pop("subject", UNSET))

        def _parse_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        text = _parse_text(d.pop("text", UNSET))

        def _parse_data(data: object) -> DraftsUpdateBodyDataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = DraftsUpdateBodyDataType0.from_dict(data)

                return data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DraftsUpdateBodyDataType0 | None | Unset, data)

        data = _parse_data(d.pop("data", UNSET))

        _attachment_ids = d.pop("attachment_ids", UNSET)
        attachment_ids: list[UUID] | Unset = UNSET
        if _attachment_ids is not UNSET:
            attachment_ids = []
            for attachment_ids_item_data in _attachment_ids:
                attachment_ids_item = UUID(attachment_ids_item_data)

                attachment_ids.append(attachment_ids_item)

        drafts_update_body = cls(
            from_=from_,
            to=to,
            cc=cc,
            bcc=bcc,
            subject=subject,
            text=text,
            data=data,
            attachment_ids=attachment_ids,
        )

        drafts_update_body.additional_properties = d
        return drafts_update_body

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
