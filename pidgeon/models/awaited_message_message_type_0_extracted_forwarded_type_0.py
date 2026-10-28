from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="AwaitedMessageMessageType0ExtractedForwardedType0")


@_attrs_define
class AwaitedMessageMessageType0ExtractedForwardedType0:
    """
    Attributes:
        from_ (str): The original sender’s address, lower-cased.
        from_name (None | str):
        date (None | str): As the forwarding client printed it, not parsed.
        subject (None | str):
        text (str): The original’s text, without its header block.
    """

    from_: str
    from_name: None | str
    date: None | str
    subject: None | str
    text: str

    def to_dict(self) -> dict[str, Any]:
        from_ = self.from_

        from_name: None | str
        from_name = self.from_name

        date: None | str
        date = self.date

        subject: None | str
        subject = self.subject

        text = self.text

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "from": from_,
                "from_name": from_name,
                "date": date,
                "subject": subject,
                "text": text,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        from_ = d.pop("from")

        def _parse_from_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        from_name = _parse_from_name(d.pop("from_name"))

        def _parse_date(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        date = _parse_date(d.pop("date"))

        def _parse_subject(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        subject = _parse_subject(d.pop("subject"))

        text = d.pop("text")

        awaited_message_message_type_0_extracted_forwarded_type_0 = cls(
            from_=from_,
            from_name=from_name,
            date=date,
            subject=subject,
            text=text,
        )

        return awaited_message_message_type_0_extracted_forwarded_type_0
