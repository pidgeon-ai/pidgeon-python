from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.attachment_text_format import AttachmentTextFormat

if TYPE_CHECKING:
    from ..models.attachment_text_firewall_type_0 import AttachmentTextFirewallType0


T = TypeVar("T", bound="AttachmentText")


@_attrs_define
class AttachmentText:
    """
    Attributes:
        id (str):
        filename (str):
        content_type (str):
        size (int): Bytes, as stored.
        format_ (AttachmentTextFormat): How it was read. `pdf`: the text layer, a form feed between pages. `docx`:
            headers, body and footers, table rows tab-separated; footnotes and comments left out. `xlsx`: each sheet as `##
            Sheet: <name>` and CSV, dates as Excel serial numbers.
        text (str): The file as text. With `body=clean`, hidden characters removed and lines posing as a chat turn
            marked, under a first line saying what changed; for a document, also what it hid from a person opening it (a
            hidden Word run, a hidden sheet, row or column).
        truncated (bool): True when the file ran past 200,000 characters and the rest was cut.
        firewall (AttachmentTextFirewallType0 | None): Whether the text tries to steer the agent reading it, judged with
            the sender of the message it came with. Null on mail this account sent.
    """

    id: str
    filename: str
    content_type: str
    size: int
    format_: AttachmentTextFormat
    text: str
    truncated: bool
    firewall: AttachmentTextFirewallType0 | None

    def to_dict(self) -> dict[str, Any]:
        from ..models.attachment_text_firewall_type_0 import AttachmentTextFirewallType0  # noqa: PLC0415

        id = self.id

        filename = self.filename

        content_type = self.content_type

        size = self.size

        format_ = self.format_.value

        text = self.text

        truncated = self.truncated

        firewall: dict[str, Any] | None
        if isinstance(self.firewall, AttachmentTextFirewallType0):
            firewall = self.firewall.to_dict()
        else:
            firewall = self.firewall

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "filename": filename,
                "content_type": content_type,
                "size": size,
                "format": format_,
                "text": text,
                "truncated": truncated,
                "firewall": firewall,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.attachment_text_firewall_type_0 import AttachmentTextFirewallType0  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id")

        filename = d.pop("filename")

        content_type = d.pop("content_type")

        size = d.pop("size")

        format_ = AttachmentTextFormat(d.pop("format"))

        text = d.pop("text")

        truncated = d.pop("truncated")

        def _parse_firewall(data: object) -> AttachmentTextFirewallType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                firewall_type_0 = AttachmentTextFirewallType0.from_dict(data)

                return firewall_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AttachmentTextFirewallType0 | None, data)

        firewall = _parse_firewall(d.pop("firewall"))

        attachment_text = cls(
            id=id,
            filename=filename,
            content_type=content_type,
            size=size,
            format_=format_,
            text=text,
            truncated=truncated,
            firewall=firewall,
        )

        return attachment_text
