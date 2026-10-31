from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.agent_setup_addresses_item import AgentSetupAddressesItem
    from ..models.agent_setup_next_type_0 import AgentSetupNextType0
    from ..models.agent_setup_steps_item import AgentSetupStepsItem


T = TypeVar("T", bound="AgentSetup")


@_attrs_define
class AgentSetup:
    """
    Attributes:
        ready_to_send (bool): True when every step is done for the address below. A test key is never ready: its mail
            stays inside Pidgeon.
        identity_id (None | str): The address `steps` are about: the one you named, or the one nearest to sending. Null
            when the key reaches none.
        address (None | str):
        next_ (AgentSetupNextType0 | None): The first step not done. Null when there is nothing left to do.
        steps (list[AgentSetupStepsItem]): In the order to clear them, done ones included.
        addresses (list[AgentSetupAddressesItem]): Every address the key reaches, nearest to sending first, up to 20.
            Call again with one’s `identity_id` for its steps, or to ask about an address past the first 20.
        addresses_total (int): How many addresses the key reaches.
    """

    ready_to_send: bool
    identity_id: None | str
    address: None | str
    next_: AgentSetupNextType0 | None
    steps: list[AgentSetupStepsItem]
    addresses: list[AgentSetupAddressesItem]
    addresses_total: int

    def to_dict(self) -> dict[str, Any]:
        from ..models.agent_setup_next_type_0 import AgentSetupNextType0  # noqa: PLC0415

        ready_to_send = self.ready_to_send

        identity_id: None | str
        identity_id = self.identity_id

        address: None | str
        address = self.address

        next_: dict[str, Any] | None
        if isinstance(self.next_, AgentSetupNextType0):
            next_ = self.next_.to_dict()
        else:
            next_ = self.next_

        steps = []
        for steps_item_data in self.steps:
            steps_item = steps_item_data.to_dict()
            steps.append(steps_item)

        addresses = []
        for addresses_item_data in self.addresses:
            addresses_item = addresses_item_data.to_dict()
            addresses.append(addresses_item)

        addresses_total = self.addresses_total

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "ready_to_send": ready_to_send,
                "identity_id": identity_id,
                "address": address,
                "next": next_,
                "steps": steps,
                "addresses": addresses,
                "addresses_total": addresses_total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_setup_addresses_item import AgentSetupAddressesItem  # noqa: PLC0415
        from ..models.agent_setup_next_type_0 import AgentSetupNextType0  # noqa: PLC0415
        from ..models.agent_setup_steps_item import AgentSetupStepsItem  # noqa: PLC0415

        d = dict(src_dict)
        ready_to_send = d.pop("ready_to_send")

        def _parse_identity_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        identity_id = _parse_identity_id(d.pop("identity_id"))

        def _parse_address(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        address = _parse_address(d.pop("address"))

        def _parse_next_(data: object) -> AgentSetupNextType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                next_type_0 = AgentSetupNextType0.from_dict(data)

                return next_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AgentSetupNextType0 | None, data)

        next_ = _parse_next_(d.pop("next"))

        steps = []
        _steps = d.pop("steps")
        for steps_item_data in _steps:
            steps_item = AgentSetupStepsItem.from_dict(steps_item_data)

            steps.append(steps_item)

        addresses = []
        _addresses = d.pop("addresses")
        for addresses_item_data in _addresses:
            addresses_item = AgentSetupAddressesItem.from_dict(addresses_item_data)

            addresses.append(addresses_item)

        addresses_total = d.pop("addresses_total")

        agent_setup = cls(
            ready_to_send=ready_to_send,
            identity_id=identity_id,
            address=address,
            next_=next_,
            steps=steps,
            addresses=addresses,
            addresses_total=addresses_total,
        )

        return agent_setup
