from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.sender_verification_sender_type_0_kind_type_0 import SenderVerificationSenderType0KindType0

T = TypeVar("T", bound="SenderVerificationSenderType0")


@_attrs_define
class SenderVerificationSenderType0:
    """
    Attributes:
        address (str):
        kind (None | SenderVerificationSenderType0KindType0):
        on_behalf_of (None | str):
    """

    address: str
    kind: None | SenderVerificationSenderType0KindType0
    on_behalf_of: None | str

    def to_dict(self) -> dict[str, Any]:
        address = self.address

        kind: None | str
        if isinstance(self.kind, SenderVerificationSenderType0KindType0):
            kind = self.kind.value
        else:
            kind = self.kind

        on_behalf_of: None | str
        on_behalf_of = self.on_behalf_of

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "address": address,
                "kind": kind,
                "on_behalf_of": on_behalf_of,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        address = d.pop("address")

        def _parse_kind(data: object) -> None | SenderVerificationSenderType0KindType0:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                kind_type_0 = SenderVerificationSenderType0KindType0(data)

                return kind_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SenderVerificationSenderType0KindType0, data)

        kind = _parse_kind(d.pop("kind"))

        def _parse_on_behalf_of(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        on_behalf_of = _parse_on_behalf_of(d.pop("on_behalf_of"))

        sender_verification_sender_type_0 = cls(
            address=address,
            kind=kind,
            on_behalf_of=on_behalf_of,
        )

        return sender_verification_sender_type_0
