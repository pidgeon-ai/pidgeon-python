from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.send_check_recipients_item_kind_type_0 import SendCheckRecipientsItemKindType0

T = TypeVar("T", bound="SendCheckRecipientsItem")


@_attrs_define
class SendCheckRecipientsItem:
    """
    Attributes:
        address (str):
        network (bool): True when this message would go to them from Pidgeon to Pidgeon: signed by your domain and
            verified before it is stored, so your `data` arrives with a checked sender and you get `message.delivered`. Only
            an agent or a service address on Pidgeon answers true. False for everyone else, and for everyone in test mode or
            when your domain does not sign yet: write for a person.
        kind (None | SendCheckRecipientsItemKindType0): What the address declares on its own mail, when it is an agent
            or a service. Null otherwise: a person, an address not on Pidgeon, and one we cannot say all read the same.
        on_behalf_of (None | str): Whom the address declares it acts for, when it has a `kind` and says so.
    """

    address: str
    network: bool
    kind: None | SendCheckRecipientsItemKindType0
    on_behalf_of: None | str

    def to_dict(self) -> dict[str, Any]:
        address = self.address

        network = self.network

        kind: None | str
        if isinstance(self.kind, SendCheckRecipientsItemKindType0):
            kind = self.kind.value
        else:
            kind = self.kind

        on_behalf_of: None | str
        on_behalf_of = self.on_behalf_of

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "address": address,
                "network": network,
                "kind": kind,
                "on_behalf_of": on_behalf_of,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        address = d.pop("address")

        network = d.pop("network")

        def _parse_kind(data: object) -> None | SendCheckRecipientsItemKindType0:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                kind_type_0 = SendCheckRecipientsItemKindType0(data)

                return kind_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SendCheckRecipientsItemKindType0, data)

        kind = _parse_kind(d.pop("kind"))

        def _parse_on_behalf_of(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        on_behalf_of = _parse_on_behalf_of(d.pop("on_behalf_of"))

        send_check_recipients_item = cls(
            address=address,
            network=network,
            kind=kind,
            on_behalf_of=on_behalf_of,
        )

        return send_check_recipients_item
