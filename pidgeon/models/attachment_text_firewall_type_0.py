from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.attachment_text_firewall_type_0_verdict import AttachmentTextFirewallType0Verdict

if TYPE_CHECKING:
    from ..models.attachment_text_firewall_type_0_signals_item import AttachmentTextFirewallType0SignalsItem


T = TypeVar("T", bound="AttachmentTextFirewallType0")


@_attrs_define
class AttachmentTextFirewallType0:
    """
    Attributes:
        verdict (AttachmentTextFirewallType0Verdict): `suspicious` when any signal fired. At an address that holds
            suspicious mail (`hold_suspicious`) the message is also held for a person: `is_held`.
        signals (list[AttachmentTextFirewallType0SignalsItem]): The rules that fired, most specific first. Empty when
            the verdict is `clean`.
        version (int): Bumped when the rules change in a way that could change a verdict.
    """

    verdict: AttachmentTextFirewallType0Verdict
    signals: list[AttachmentTextFirewallType0SignalsItem]
    version: int

    def to_dict(self) -> dict[str, Any]:
        verdict = self.verdict.value

        signals = []
        for signals_item_data in self.signals:
            signals_item = signals_item_data.to_dict()
            signals.append(signals_item)

        version = self.version

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "verdict": verdict,
                "signals": signals,
                "version": version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.attachment_text_firewall_type_0_signals_item import AttachmentTextFirewallType0SignalsItem  # noqa: PLC0415

        d = dict(src_dict)
        verdict = AttachmentTextFirewallType0Verdict(d.pop("verdict"))

        signals = []
        _signals = d.pop("signals")
        for signals_item_data in _signals:
            signals_item = AttachmentTextFirewallType0SignalsItem.from_dict(signals_item_data)

            signals.append(signals_item)

        version = d.pop("version")

        attachment_text_firewall_type_0 = cls(
            verdict=verdict,
            signals=signals,
            version=version,
        )

        return attachment_text_firewall_type_0
