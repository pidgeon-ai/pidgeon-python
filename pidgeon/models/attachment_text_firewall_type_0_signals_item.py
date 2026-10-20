from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.attachment_text_firewall_type_0_signals_item_kind import AttachmentTextFirewallType0SignalsItemKind
from ..models.attachment_text_firewall_type_0_signals_item_where import AttachmentTextFirewallType0SignalsItemWhere

T = TypeVar("T", bound="AttachmentTextFirewallType0SignalsItem")


@_attrs_define
class AttachmentTextFirewallType0SignalsItem:
    """
    Attributes:
        kind (AttachmentTextFirewallType0SignalsItemKind):
        detail (str): What was found, with a short quote of it.
        where (AttachmentTextFirewallType0SignalsItemWhere):
    """

    kind: AttachmentTextFirewallType0SignalsItemKind
    detail: str
    where: AttachmentTextFirewallType0SignalsItemWhere

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
        kind = AttachmentTextFirewallType0SignalsItemKind(d.pop("kind"))

        detail = d.pop("detail")

        where = AttachmentTextFirewallType0SignalsItemWhere(d.pop("where"))

        attachment_text_firewall_type_0_signals_item = cls(
            kind=kind,
            detail=detail,
            where=where,
        )

        return attachment_text_firewall_type_0_signals_item
