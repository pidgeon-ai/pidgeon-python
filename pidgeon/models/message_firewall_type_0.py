from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.message_firewall_type_0_verdict import MessageFirewallType0Verdict

if TYPE_CHECKING:
    from ..models.message_firewall_type_0_signals_item import MessageFirewallType0SignalsItem


T = TypeVar("T", bound="MessageFirewallType0")


@_attrs_define
class MessageFirewallType0:
    """
    Attributes:
        verdict (MessageFirewallType0Verdict): `suspicious` when any signal fired. At an address that holds suspicious
            mail (`hold_suspicious`) the message is also held for a person: `is_held`.
        signals (list[MessageFirewallType0SignalsItem]): The rules that fired, most specific first. Empty when the
            verdict is `clean`.
        clean_text (str): What an agent should read: the new text with hidden content and invisible characters removed
            and lines posing as a chat turn marked, under a one-line note saying what changed. The new text unchanged when
            nothing needed it. Ask for `body=clean` to get it in place of the body.
        version (int): Bumped when the rules change in a way that could change a verdict.
    """

    verdict: MessageFirewallType0Verdict
    signals: list[MessageFirewallType0SignalsItem]
    clean_text: str
    version: int

    def to_dict(self) -> dict[str, Any]:
        verdict = self.verdict.value

        signals = []
        for signals_item_data in self.signals:
            signals_item = signals_item_data.to_dict()
            signals.append(signals_item)

        clean_text = self.clean_text

        version = self.version

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "verdict": verdict,
                "signals": signals,
                "clean_text": clean_text,
                "version": version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.message_firewall_type_0_signals_item import MessageFirewallType0SignalsItem  # noqa: PLC0415

        d = dict(src_dict)
        verdict = MessageFirewallType0Verdict(d.pop("verdict"))

        signals = []
        _signals = d.pop("signals")
        for signals_item_data in _signals:
            signals_item = MessageFirewallType0SignalsItem.from_dict(signals_item_data)

            signals.append(signals_item)

        clean_text = d.pop("clean_text")

        version = d.pop("version")

        message_firewall_type_0 = cls(
            verdict=verdict,
            signals=signals,
            clean_text=clean_text,
            version=version,
        )

        return message_firewall_type_0
