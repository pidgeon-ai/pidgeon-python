from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.message_extracted_codes_item import MessageExtractedCodesItem
    from ..models.message_extracted_links_item import MessageExtractedLinksItem


T = TypeVar("T", bound="MessageExtracted")


@_attrs_define
class MessageExtracted:
    """Verification codes and links found in the message, most likely first — read from the new text, never the quoted
    history. Empty lists when nothing was found.

        Attributes:
            codes (list[MessageExtractedCodesItem]): Verification codes, most likely first. Empty when nothing looked like
                one.
            links (list[MessageExtractedLinksItem]): Links, verification links first. Unsubscribe and social links are left
                out.
    """

    codes: list[MessageExtractedCodesItem]
    links: list[MessageExtractedLinksItem]

    def to_dict(self) -> dict[str, Any]:
        codes = []
        for codes_item_data in self.codes:
            codes_item = codes_item_data.to_dict()
            codes.append(codes_item)

        links = []
        for links_item_data in self.links:
            links_item = links_item_data.to_dict()
            links.append(links_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "codes": codes,
                "links": links,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.message_extracted_codes_item import MessageExtractedCodesItem  # noqa: PLC0415
        from ..models.message_extracted_links_item import MessageExtractedLinksItem  # noqa: PLC0415

        d = dict(src_dict)
        codes = []
        _codes = d.pop("codes")
        for codes_item_data in _codes:
            codes_item = MessageExtractedCodesItem.from_dict(codes_item_data)

            codes.append(codes_item)

        links = []
        _links = d.pop("links")
        for links_item_data in _links:
            links_item = MessageExtractedLinksItem.from_dict(links_item_data)

            links.append(links_item)

        message_extracted = cls(
            codes=codes,
            links=links,
        )

        return message_extracted
