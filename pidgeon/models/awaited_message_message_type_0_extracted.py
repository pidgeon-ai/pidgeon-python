from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.awaited_message_message_type_0_extracted_codes_item import (
        AwaitedMessageMessageType0ExtractedCodesItem,
    )
    from ..models.awaited_message_message_type_0_extracted_forwarded_type_0 import (
        AwaitedMessageMessageType0ExtractedForwardedType0,
    )
    from ..models.awaited_message_message_type_0_extracted_links_item import (
        AwaitedMessageMessageType0ExtractedLinksItem,
    )


T = TypeVar("T", bound="AwaitedMessageMessageType0Extracted")


@_attrs_define
class AwaitedMessageMessageType0Extracted:
    """Verification codes and links found in the message, most likely first — read from the new text, never the quoted
    history — and the original inside a forward. Empty lists when nothing was found.

        Attributes:
            codes (list[AwaitedMessageMessageType0ExtractedCodesItem]): Verification codes, most likely first. Empty when
                nothing looked like one.
            links (list[AwaitedMessageMessageType0ExtractedLinksItem]): Links, verification links first. Unsubscribe and
                social links are left out.
            forwarded (AwaitedMessageMessageType0ExtractedForwardedType0 | None): The email somebody forwarded, when this
                message is an inline forward (Gmail, Apple Mail or Outlook, in English or German): `from` here is the original
                sender, where the message’s own `from` is the person who forwarded it. `null` when this is not a forward, or the
                original names no sender address. With `body=clean`, `null` when the Firewall found the message suspicious.
    """

    codes: list[AwaitedMessageMessageType0ExtractedCodesItem]
    links: list[AwaitedMessageMessageType0ExtractedLinksItem]
    forwarded: AwaitedMessageMessageType0ExtractedForwardedType0 | None

    def to_dict(self) -> dict[str, Any]:
        from ..models.awaited_message_message_type_0_extracted_forwarded_type_0 import (
            AwaitedMessageMessageType0ExtractedForwardedType0,  # noqa: PLC0415
        )

        codes = []
        for codes_item_data in self.codes:
            codes_item = codes_item_data.to_dict()
            codes.append(codes_item)

        links = []
        for links_item_data in self.links:
            links_item = links_item_data.to_dict()
            links.append(links_item)

        forwarded: dict[str, Any] | None
        if isinstance(self.forwarded, AwaitedMessageMessageType0ExtractedForwardedType0):
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
        from ..models.awaited_message_message_type_0_extracted_codes_item import (
            AwaitedMessageMessageType0ExtractedCodesItem,  # noqa: PLC0415
        )
        from ..models.awaited_message_message_type_0_extracted_forwarded_type_0 import (
            AwaitedMessageMessageType0ExtractedForwardedType0,  # noqa: PLC0415
        )
        from ..models.awaited_message_message_type_0_extracted_links_item import (
            AwaitedMessageMessageType0ExtractedLinksItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        codes = []
        _codes = d.pop("codes")
        for codes_item_data in _codes:
            codes_item = AwaitedMessageMessageType0ExtractedCodesItem.from_dict(codes_item_data)

            codes.append(codes_item)

        links = []
        _links = d.pop("links")
        for links_item_data in _links:
            links_item = AwaitedMessageMessageType0ExtractedLinksItem.from_dict(links_item_data)

            links.append(links_item)

        def _parse_forwarded(data: object) -> AwaitedMessageMessageType0ExtractedForwardedType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                forwarded_type_0 = AwaitedMessageMessageType0ExtractedForwardedType0.from_dict(data)

                return forwarded_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AwaitedMessageMessageType0ExtractedForwardedType0 | None, data)

        forwarded = _parse_forwarded(d.pop("forwarded"))

        awaited_message_message_type_0_extracted = cls(
            codes=codes,
            links=links,
            forwarded=forwarded,
        )

        return awaited_message_message_type_0_extracted
