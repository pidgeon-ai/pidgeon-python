from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.message_extracted_links_item_kind import MessageExtractedLinksItemKind

T = TypeVar("T", bound="MessageExtractedLinksItem")


@_attrs_define
class MessageExtractedLinksItem:
    """
    Attributes:
        url (str):
        kind (MessageExtractedLinksItemKind): `verification` for confirm, verify, sign-in and magic links.
        text (None | str): The link text, when it had any.
    """

    url: str
    kind: MessageExtractedLinksItemKind
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

        kind = MessageExtractedLinksItemKind(d.pop("kind"))

        def _parse_text(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        text = _parse_text(d.pop("text"))

        message_extracted_links_item = cls(
            url=url,
            kind=kind,
            text=text,
        )

        return message_extracted_links_item
