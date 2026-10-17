from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.message_firewall_type_0_signals_item_kind import MessageFirewallType0SignalsItemKind
from ..models.message_firewall_type_0_signals_item_where import MessageFirewallType0SignalsItemWhere

T = TypeVar("T", bound="MessageFirewallType0SignalsItem")


@_attrs_define
class MessageFirewallType0SignalsItem:
    """
    Attributes:
        kind (MessageFirewallType0SignalsItemKind):
        detail (str): What was found, with a short quote of it.
        where (MessageFirewallType0SignalsItemWhere):
    """

    kind: MessageFirewallType0SignalsItemKind
    detail: str
    where: MessageFirewallType0SignalsItemWhere

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
        kind = MessageFirewallType0SignalsItemKind(d.pop("kind"))

        detail = d.pop("detail")

        where = MessageFirewallType0SignalsItemWhere(d.pop("where"))

        message_firewall_type_0_signals_item = cls(
            kind=kind,
            detail=detail,
            where=where,
        )

        return message_firewall_type_0_signals_item
