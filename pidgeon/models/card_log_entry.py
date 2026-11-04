from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.card_log_entry_entry import CardLogEntryEntry


T = TypeVar("T", bound="CardLogEntry")


@_attrs_define
class CardLogEntry:
    """
    Attributes:
        object_ (Literal['card_log_entry']):
        index (int):
        data (str): The exact bytes the leaf hashes: canonical JSON (RFC 8785).
        leaf_hash (str): SHA-256 of 0x00 and `data`, base64.
        entry (CardLogEntryEntry): `data`, parsed, for reading.
    """

    object_: Literal["card_log_entry"]
    index: int
    data: str
    leaf_hash: str
    entry: CardLogEntryEntry

    def to_dict(self) -> dict[str, Any]:
        object_ = self.object_

        index = self.index

        data = self.data

        leaf_hash = self.leaf_hash

        entry = self.entry.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "object": object_,
                "index": index,
                "data": data,
                "leaf_hash": leaf_hash,
                "entry": entry,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.card_log_entry_entry import CardLogEntryEntry  # noqa: PLC0415

        d = dict(src_dict)
        object_ = cast(Literal["card_log_entry"], d.pop("object"))
        if object_ != "card_log_entry":
            raise ValueError(f"object must match const 'card_log_entry', got '{object_}'")

        index = d.pop("index")

        data = d.pop("data")

        leaf_hash = d.pop("leaf_hash")

        entry = CardLogEntryEntry.from_dict(d.pop("entry"))

        card_log_entry = cls(
            object_=object_,
            index=index,
            data=data,
            leaf_hash=leaf_hash,
            entry=entry,
        )

        return card_log_entry
