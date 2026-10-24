from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.test_inbound_body_data import TestInboundBodyData


T = TypeVar("T", bound="TestInboundBody")


@_attrs_define
class TestInboundBody:
    """
    Attributes:
        to (str): One of the addresses this test key reaches, at `send`.
        from_ (str): Who it is from. Any address: nothing is sent to it.
        from_name (str | Unset):
        subject (str | Unset): Left off a reply, where the thread already has one. Default: ''.
        text (str | Unset): The plain-text body. Send this even when you send `html` — some clients only read it.
            Default: ''.
        html (str | Unset): The rich body. Sanitised on the way in; scripts and remote content are removed.
        data (TestInboundBodyData | Unset): Typed data: structured JSON sent beside the text, for software at the other
            end to read as fields. Travels as its own part; it is never mixed into the text.
        in_reply_to (None | Unset | UUID): A message id: this arrives as a reply to it, in its thread.
    """

    to: str
    from_: str
    from_name: str | Unset = UNSET
    subject: str | Unset = ""
    text: str | Unset = ""
    html: str | Unset = UNSET
    data: TestInboundBodyData | Unset = UNSET
    in_reply_to: None | Unset | UUID = UNSET

    def to_dict(self) -> dict[str, Any]:
        to = self.to

        from_ = self.from_

        from_name = self.from_name

        subject = self.subject

        text = self.text

        html = self.html

        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        in_reply_to: None | str | Unset
        if isinstance(self.in_reply_to, Unset):
            in_reply_to = UNSET
        elif isinstance(self.in_reply_to, UUID):
            in_reply_to = str(self.in_reply_to)
        else:
            in_reply_to = self.in_reply_to

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "to": to,
                "from": from_,
            }
        )
        if from_name is not UNSET:
            field_dict["from_name"] = from_name
        if subject is not UNSET:
            field_dict["subject"] = subject
        if text is not UNSET:
            field_dict["text"] = text
        if html is not UNSET:
            field_dict["html"] = html
        if data is not UNSET:
            field_dict["data"] = data
        if in_reply_to is not UNSET:
            field_dict["in_reply_to"] = in_reply_to

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.test_inbound_body_data import TestInboundBodyData  # noqa: PLC0415

        d = dict(src_dict)
        to = d.pop("to")

        from_ = d.pop("from")

        from_name = d.pop("from_name", UNSET)

        subject = d.pop("subject", UNSET)

        text = d.pop("text", UNSET)

        html = d.pop("html", UNSET)

        _data = d.pop("data", UNSET)
        data: TestInboundBodyData | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = TestInboundBodyData.from_dict(_data)

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

        test_inbound_body = cls(
            to=to,
            from_=from_,
            from_name=from_name,
            subject=subject,
            text=text,
            html=html,
            data=data,
            in_reply_to=in_reply_to,
        )

        return test_inbound_body
