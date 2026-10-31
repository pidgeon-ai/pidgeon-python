from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.agent_setup_addresses_item_next_type_0 import AgentSetupAddressesItemNextType0

T = TypeVar("T", bound="AgentSetupAddressesItem")


@_attrs_define
class AgentSetupAddressesItem:
    """
    Attributes:
        identity_id (str):
        address (str):
        ready_to_send (bool):
        next_ (AgentSetupAddressesItemNextType0 | None): The `id` of its first step not done, or null when it is ready.
    """

    identity_id: str
    address: str
    ready_to_send: bool
    next_: AgentSetupAddressesItemNextType0 | None

    def to_dict(self) -> dict[str, Any]:
        identity_id = self.identity_id

        address = self.address

        ready_to_send = self.ready_to_send

        next_: None | str
        if isinstance(self.next_, AgentSetupAddressesItemNextType0):
            next_ = self.next_.value
        else:
            next_ = self.next_

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "identity_id": identity_id,
                "address": address,
                "ready_to_send": ready_to_send,
                "next": next_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        identity_id = d.pop("identity_id")

        address = d.pop("address")

        ready_to_send = d.pop("ready_to_send")

        def _parse_next_(data: object) -> AgentSetupAddressesItemNextType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_type_0 = AgentSetupAddressesItemNextType0(data)

                return next_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AgentSetupAddressesItemNextType0 | None, data)

        next_ = _parse_next_(d.pop("next"))

        agent_setup_addresses_item = cls(
            identity_id=identity_id,
            address=address,
            ready_to_send=ready_to_send,
            next_=next_,
        )

        return agent_setup_addresses_item
