from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.awaited_message_message_type_0_firewall_type_0_signals_item_kind import (
    AwaitedMessageMessageType0FirewallType0SignalsItemKind,
)
from ..models.awaited_message_message_type_0_firewall_type_0_signals_item_where import (
    AwaitedMessageMessageType0FirewallType0SignalsItemWhere,
)

T = TypeVar("T", bound="AwaitedMessageMessageType0FirewallType0SignalsItem")


@_attrs_define
class AwaitedMessageMessageType0FirewallType0SignalsItem:
    """
    Attributes:
        kind (AwaitedMessageMessageType0FirewallType0SignalsItemKind):
        detail (str): What was found, with a short quote of it.
        where (AwaitedMessageMessageType0FirewallType0SignalsItemWhere):
    """

    kind: AwaitedMessageMessageType0FirewallType0SignalsItemKind
    detail: str
    where: AwaitedMessageMessageType0FirewallType0SignalsItemWhere

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind.value

        detail = self.detail

        where = self.where.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "kind": kind,
                "detail": detail,
                "where": where,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = AwaitedMessageMessageType0FirewallType0SignalsItemKind(d.pop("kind"))

        detail = d.pop("detail")

        where = AwaitedMessageMessageType0FirewallType0SignalsItemWhere(d.pop("where"))

        awaited_message_message_type_0_firewall_type_0_signals_item = cls(
            kind=kind,
            detail=detail,
            where=where,
        )

        return awaited_message_message_type_0_firewall_type_0_signals_item
