from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.awaited_message_message_type_0_authentication_arc_type_0 import (
        AwaitedMessageMessageType0AuthenticationArcType0,
    )


T = TypeVar("T", bound="AwaitedMessageMessageType0Authentication")


@_attrs_define
class AwaitedMessageMessageType0Authentication:
    """What the receiving transport said about the sending domain. Null means it did not report, not that the check failed
    — normal on outbound, and on inbound it is the difference between unknown and forged. A `From:` is the sending
    domain's own word when `dmarc` or `signature` is `pass`, or `arc` is set.

        Attributes:
            spf (None | str):
            dkim (None | str):
            dmarc (None | str):
            signature (None | str): `pass` when the message came from another Pidgeon address directly, and its signed
                sender verified against the sending domain's published key. Null on mail that came through SMTP, which DMARC
                speaks for instead.
            arc (AwaitedMessageMessageType0AuthenticationArcType0 | None): Set when `dmarc` did not pass here, but the
                message was forwarded by a sealer Pidgeon trusts (Google, for a Gmail or Workspace forward), its ARC chain
                verified, and that sealer recorded DMARC pass for the `From:` domain. Null otherwise.
    """

    spf: None | str
    dkim: None | str
    dmarc: None | str
    signature: None | str
    arc: AwaitedMessageMessageType0AuthenticationArcType0 | None

    def to_dict(self) -> dict[str, Any]:
        from ..models.awaited_message_message_type_0_authentication_arc_type_0 import (
            AwaitedMessageMessageType0AuthenticationArcType0,  # noqa: PLC0415
        )

        spf: None | str
        spf = self.spf

        dkim: None | str
        dkim = self.dkim

        dmarc: None | str
        dmarc = self.dmarc

        signature: None | str
        signature = self.signature

        arc: dict[str, Any] | None
        if isinstance(self.arc, AwaitedMessageMessageType0AuthenticationArcType0):
            arc = self.arc.to_dict()
        else:
            arc = self.arc

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "spf": spf,
                "dkim": dkim,
                "dmarc": dmarc,
                "signature": signature,
                "arc": arc,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.awaited_message_message_type_0_authentication_arc_type_0 import (
            AwaitedMessageMessageType0AuthenticationArcType0,  # noqa: PLC0415
        )

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

        def _parse_signature(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        signature = _parse_signature(d.pop("signature"))

        def _parse_arc(data: object) -> AwaitedMessageMessageType0AuthenticationArcType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                arc_type_0 = AwaitedMessageMessageType0AuthenticationArcType0.from_dict(data)

                return arc_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AwaitedMessageMessageType0AuthenticationArcType0 | None, data)

        arc = _parse_arc(d.pop("arc"))

        awaited_message_message_type_0_authentication = cls(
            spf=spf,
            dkim=dkim,
            dmarc=dmarc,
            signature=signature,
            arc=arc,
        )

        return awaited_message_message_type_0_authentication
