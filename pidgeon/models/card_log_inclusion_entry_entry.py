from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..models.card_log_inclusion_entry_entry_event import CardLogInclusionEntryEntryEvent
from ..models.card_log_inclusion_entry_entry_kind import CardLogInclusionEntryEntryKind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.card_log_inclusion_entry_entry_keys_item import CardLogInclusionEntryEntryKeysItem
    from ..models.card_log_inclusion_entry_entry_operator import CardLogInclusionEntryEntryOperator


T = TypeVar("T", bound="CardLogInclusionEntryEntry")


@_attrs_define
class CardLogInclusionEntryEntry:
    """`data`, parsed, for reading.

    Attributes:
        v (Literal['post0-log']):
        event (CardLogInclusionEntryEntryEvent):
        time (str):
        sub (str): The card’s `sub`: every entry about one address shares it.
        address (str):
        prev (int | Unset): The index of this subject’s previous entry.
        iss (str | Unset):
        kind (CardLogInclusionEntryEntryKind | Unset):
        on_behalf_of (str | Unset):
        operator (CardLogInclusionEntryEntryOperator | Unset):
        keys (list[CardLogInclusionEntryEntryKeysItem] | Unset):
    """

    v: Literal["post0-log"]
    event: CardLogInclusionEntryEntryEvent
    time: str
    sub: str
    address: str
    prev: int | Unset = UNSET
    iss: str | Unset = UNSET
    kind: CardLogInclusionEntryEntryKind | Unset = UNSET
    on_behalf_of: str | Unset = UNSET
    operator: CardLogInclusionEntryEntryOperator | Unset = UNSET
    keys: list[CardLogInclusionEntryEntryKeysItem] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        v = self.v

        event = self.event.value

        time = self.time

        sub = self.sub

        address = self.address

        prev = self.prev

        iss = self.iss

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        on_behalf_of = self.on_behalf_of

        operator: dict[str, Any] | Unset = UNSET
        if not isinstance(self.operator, Unset):
            operator = self.operator.to_dict()

        keys: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.keys, Unset):
            keys = []
            for keys_item_data in self.keys:
                keys_item = keys_item_data.to_dict()
                keys.append(keys_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "v": v,
                "event": event,
                "time": time,
                "sub": sub,
                "address": address,
            }
        )
        if prev is not UNSET:
            field_dict["prev"] = prev
        if iss is not UNSET:
            field_dict["iss"] = iss
        if kind is not UNSET:
            field_dict["kind"] = kind
        if on_behalf_of is not UNSET:
            field_dict["on_behalf_of"] = on_behalf_of
        if operator is not UNSET:
            field_dict["operator"] = operator
        if keys is not UNSET:
            field_dict["keys"] = keys

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.card_log_inclusion_entry_entry_keys_item import CardLogInclusionEntryEntryKeysItem  # noqa: PLC0415
        from ..models.card_log_inclusion_entry_entry_operator import CardLogInclusionEntryEntryOperator  # noqa: PLC0415

        d = dict(src_dict)
        v = cast(Literal["post0-log"], d.pop("v"))
        if v != "post0-log":
            raise ValueError(f"v must match const 'post0-log', got '{v}'")

        event = CardLogInclusionEntryEntryEvent(d.pop("event"))

        time = d.pop("time")

        sub = d.pop("sub")

        address = d.pop("address")

        prev = d.pop("prev", UNSET)

        iss = d.pop("iss", UNSET)

        _kind = d.pop("kind", UNSET)
        kind: CardLogInclusionEntryEntryKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = CardLogInclusionEntryEntryKind(_kind)

        on_behalf_of = d.pop("on_behalf_of", UNSET)

        _operator = d.pop("operator", UNSET)
        operator: CardLogInclusionEntryEntryOperator | Unset
        if isinstance(_operator, Unset):
            operator = UNSET
        else:
            operator = CardLogInclusionEntryEntryOperator.from_dict(_operator)

        _keys = d.pop("keys", UNSET)
        keys: list[CardLogInclusionEntryEntryKeysItem] | Unset = UNSET
        if _keys is not UNSET:
            keys = []
            for keys_item_data in _keys:
                keys_item = CardLogInclusionEntryEntryKeysItem.from_dict(keys_item_data)

                keys.append(keys_item)

        card_log_inclusion_entry_entry = cls(
            v=v,
            event=event,
            time=time,
            sub=sub,
            address=address,
            prev=prev,
            iss=iss,
            kind=kind,
            on_behalf_of=on_behalf_of,
            operator=operator,
            keys=keys,
        )

        return card_log_inclusion_entry_entry
