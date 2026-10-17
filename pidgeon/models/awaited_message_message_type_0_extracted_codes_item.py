from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.awaited_message_message_type_0_extracted_codes_item_kind import (
    AwaitedMessageMessageType0ExtractedCodesItemKind,
)

T = TypeVar("T", bound="AwaitedMessageMessageType0ExtractedCodesItem")


@_attrs_define
class AwaitedMessageMessageType0ExtractedCodesItem:
    """
    Attributes:
        value (str): The code as it would be typed: spaces removed.
        kind (AwaitedMessageMessageType0ExtractedCodesItemKind):
        index (int): Where in the text it was found, or -1 when it was in the subject.
    """

    value: str
    kind: AwaitedMessageMessageType0ExtractedCodesItemKind
    index: int

    def to_dict(self) -> dict[str, Any]:
        value = self.value

        kind = self.kind.value

        index = self.index

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "value": value,
                "kind": kind,
                "index": index,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        value = d.pop("value")

        kind = AwaitedMessageMessageType0ExtractedCodesItemKind(d.pop("kind"))

        index = d.pop("index")

        awaited_message_message_type_0_extracted_codes_item = cls(
            value=value,
            kind=kind,
            index=index,
        )

        return awaited_message_message_type_0_extracted_codes_item
