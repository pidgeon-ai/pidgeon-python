from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="AwaitedMessageMessageType0AuthenticationArcType0")


@_attrs_define
class AwaitedMessageMessageType0AuthenticationArcType0:
    """
    Attributes:
        sealer (str): The forwarder that sealed it, such as `google.com`.
        dmarc (Literal['pass']):
    """

    sealer: str
    dmarc: Literal["pass"]

    def to_dict(self) -> dict[str, Any]:
        sealer = self.sealer

        dmarc = self.dmarc

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "sealer": sealer,
                "dmarc": dmarc,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sealer = d.pop("sealer")

        dmarc = cast(Literal["pass"], d.pop("dmarc"))
        if dmarc != "pass":
            raise ValueError(f"dmarc must match const 'pass', got '{dmarc}'")

        awaited_message_message_type_0_authentication_arc_type_0 = cls(
            sealer=sealer,
            dmarc=dmarc,
        )

        return awaited_message_message_type_0_authentication_arc_type_0
