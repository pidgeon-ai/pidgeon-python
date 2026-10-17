from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.awaited_message_message_type_0_extracted_links_item_kind import (
    AwaitedMessageMessageType0ExtractedLinksItemKind,
)

T = TypeVar("T", bound="AwaitedMessageMessageType0ExtractedLinksItem")


@_attrs_define
class AwaitedMessageMessageType0ExtractedLinksItem:
    """
    Attributes:
        url (str):
        kind (AwaitedMessageMessageType0ExtractedLinksItemKind): `verification` for confirm, verify, sign-in and magic
            links.
        text (None | str): The link text, when it had any.
    """

    url: str
    kind: AwaitedMessageMessageType0ExtractedLinksItemKind
    text: None | str

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        kind = self.kind.value

        text: None | str
        text = self.text

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "url": url,
                "kind": kind,
                "text": text,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")

        kind = AwaitedMessageMessageType0ExtractedLinksItemKind(d.pop("kind"))

        def _parse_text(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        text = _parse_text(d.pop("text"))

        awaited_message_message_type_0_extracted_links_item = cls(
            url=url,
            kind=kind,
            text=text,
        )

        return awaited_message_message_type_0_extracted_links_item
