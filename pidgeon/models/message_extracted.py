from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.message_extracted_codes_item import MessageExtractedCodesItem
    from ..models.message_extracted_forwarded_type_0 import MessageExtractedForwardedType0
    from ..models.message_extracted_links_item import MessageExtractedLinksItem


T = TypeVar("T", bound="MessageExtracted")


@_attrs_define
class MessageExtracted:
    """Verification codes and links found in the message, most likely first — read from the new text, never the quoted
    history — and the original inside a forward. Empty lists when nothing was found.

        Attributes:
            codes (list[MessageExtractedCodesItem]): Verification codes, most likely first. Empty when nothing looked like
                one.
            links (list[MessageExtractedLinksItem]): Links, verification links first. Unsubscribe and social links are left
                out.
            forwarded (MessageExtractedForwardedType0 | None): The email somebody forwarded, when this message is an inline
                forward (Gmail, Apple Mail or Outlook, in English or German): `from` here is the original sender, where the
                message’s own `from` is the person who forwarded it. `null` when this is not a forward, or the original names no
                sender address. With `body=clean`, `null` when the Firewall found the message suspicious.
    """

    codes: list[MessageExtractedCodesItem]
    links: list[MessageExtractedLinksItem]
    forwarded: MessageExtractedForwardedType0 | None

    def to_dict(self) -> dict[str, Any]:
        from ..models.message_extracted_forwarded_type_0 import MessageExtractedForwardedType0  # noqa: PLC0415

        codes = []
        for codes_item_data in self.codes:
            codes_item = codes_item_data.to_dict()
            codes.append(codes_item)

        links = []
        for links_item_data in self.links:
            links_item = links_item_data.to_dict()
            links.append(links_item)

        forwarded: dict[str, Any] | None
        if isinstance(self.forwarded, MessageExtractedForwardedType0):
            forwarded = self.forwarded.to_dict()
        else:
            forwarded = self.forwarded

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "codes": codes,
                "links": links,
                "forwarded": forwarded,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.message_extracted_codes_item import MessageExtractedCodesItem  # noqa: PLC0415
        from ..models.message_extracted_forwarded_type_0 import MessageExtractedForwardedType0  # noqa: PLC0415
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

        def _parse_forwarded(data: object) -> MessageExtractedForwardedType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                forwarded_type_0 = MessageExtractedForwardedType0.from_dict(data)

                return forwarded_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MessageExtractedForwardedType0 | None, data)

        forwarded = _parse_forwarded(d.pop("forwarded"))

        message_extracted = cls(
            codes=codes,
            links=links,
            forwarded=forwarded,
        )

        return message_extracted
