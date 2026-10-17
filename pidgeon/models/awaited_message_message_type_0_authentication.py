from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="AwaitedMessageMessageType0Authentication")


@_attrs_define
class AwaitedMessageMessageType0Authentication:
    """What the receiving transport said about the sending domain. Null means it did not report, not that the check failed
    — normal on outbound, and on inbound it is the difference between unknown and forged.

        Attributes:
            spf (None | str):
            dkim (None | str):
            dmarc (None | str):
    """

    spf: None | str
    dkim: None | str
    dmarc: None | str

    def to_dict(self) -> dict[str, Any]:
        spf: None | str
        spf = self.spf

        dkim: None | str
        dkim = self.dkim

        dmarc: None | str
        dmarc = self.dmarc

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "spf": spf,
                "dkim": dkim,
                "dmarc": dmarc,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_spf(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        spf = _parse_spf(d.pop("spf"))

        def _parse_dkim(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        dkim = _parse_dkim(d.pop("dkim"))

        def _parse_dmarc(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        dmarc = _parse_dmarc(d.pop("dmarc"))

        awaited_message_message_type_0_authentication = cls(
            spf=spf,
            dkim=dkim,
            dmarc=dmarc,
        )

        return awaited_message_message_type_0_authentication
