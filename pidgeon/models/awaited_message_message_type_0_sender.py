from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.awaited_message_message_type_0_sender_kind_type_0 import AwaitedMessageMessageType0SenderKindType0

T = TypeVar("T", bound="AwaitedMessageMessageType0Sender")


@_attrs_define
class AwaitedMessageMessageType0Sender:
    """Who this message says it is from. A Pidgeon sender declares it on every message it sends; mail from ordinary email
    has only the address.

        Attributes:
            address (str):
            kind (AwaitedMessageMessageType0SenderKindType0 | None): What the sender declared it is: a person, an agent or a
                service. Null when it declared nothing, as mail from ordinary email never does.
            on_behalf_of (None | str): Who the sender declared it writes for: the sending workspace’s name. Null when it
                declared nothing.
    """

    address: str
    kind: AwaitedMessageMessageType0SenderKindType0 | None
    on_behalf_of: None | str

    def to_dict(self) -> dict[str, Any]:
        address = self.address

        kind: None | str
        if isinstance(self.kind, AwaitedMessageMessageType0SenderKindType0):
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

        def _parse_kind(data: object) -> AwaitedMessageMessageType0SenderKindType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                kind_type_0 = AwaitedMessageMessageType0SenderKindType0(data)

                return kind_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AwaitedMessageMessageType0SenderKindType0 | None, data)

        kind = _parse_kind(d.pop("kind"))

        def _parse_on_behalf_of(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        on_behalf_of = _parse_on_behalf_of(d.pop("on_behalf_of"))

        awaited_message_message_type_0_sender = cls(
            address=address,
            kind=kind,
            on_behalf_of=on_behalf_of,
        )

        return awaited_message_message_type_0_sender
