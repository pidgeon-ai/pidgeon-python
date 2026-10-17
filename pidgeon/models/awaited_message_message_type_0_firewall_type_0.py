from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.awaited_message_message_type_0_firewall_type_0_verdict import (
    AwaitedMessageMessageType0FirewallType0Verdict,
)

if TYPE_CHECKING:
    from ..models.awaited_message_message_type_0_firewall_type_0_signals_item import (
        AwaitedMessageMessageType0FirewallType0SignalsItem,
    )


T = TypeVar("T", bound="AwaitedMessageMessageType0FirewallType0")


@_attrs_define
class AwaitedMessageMessageType0FirewallType0:
    """
    Attributes:
        verdict (AwaitedMessageMessageType0FirewallType0Verdict): `suspicious` when any signal fired. Observe-only:
            nothing is held or changed.
        signals (list[AwaitedMessageMessageType0FirewallType0SignalsItem]): The rules that fired, most specific first.
            Empty when the verdict is `clean`.
        clean_text (str): What an agent should read: the new text with hidden content and invisible characters removed
            and lines posing as a chat turn marked, under a one-line note saying what changed. The new text unchanged when
            nothing needed it. Ask for `body=clean` to get it in place of the body.
        version (int): Bumped when the rules change in a way that could change a verdict.
    """

    verdict: AwaitedMessageMessageType0FirewallType0Verdict
    signals: list[AwaitedMessageMessageType0FirewallType0SignalsItem]
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
        from ..models.awaited_message_message_type_0_firewall_type_0_signals_item import (
            AwaitedMessageMessageType0FirewallType0SignalsItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        verdict = AwaitedMessageMessageType0FirewallType0Verdict(d.pop("verdict"))

        signals = []
        _signals = d.pop("signals")
        for signals_item_data in _signals:
            signals_item = AwaitedMessageMessageType0FirewallType0SignalsItem.from_dict(signals_item_data)

            signals.append(signals_item)

        clean_text = d.pop("clean_text")

        version = d.pop("version")

        awaited_message_message_type_0_firewall_type_0 = cls(
            verdict=verdict,
            signals=signals,
            clean_text=clean_text,
            version=version,
        )

        return awaited_message_message_type_0_firewall_type_0
