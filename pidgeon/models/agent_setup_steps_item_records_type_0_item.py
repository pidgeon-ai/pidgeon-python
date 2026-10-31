from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.agent_setup_steps_item_records_type_0_item_state_type_0 import (
    AgentSetupStepsItemRecordsType0ItemStateType0,
)
from ..models.agent_setup_steps_item_records_type_0_item_status import AgentSetupStepsItemRecordsType0ItemStatus

T = TypeVar("T", bound="AgentSetupStepsItemRecordsType0Item")


@_attrs_define
class AgentSetupStepsItemRecordsType0Item:
    """
    Attributes:
        type_ (str):
        record_type (str):
        name (str): Relative to the domain: `@` is the domain itself. Kept as it was; see `host_relative`.
        zone (str): The registrable domain the record is published in, from the Public Suffix List: `example.com` for
            `agents.example.com`.
        fqdn (str): The full name, no trailing dot: `_dmarc.agents.example.com`.
        host_relative (str): The name relative to `zone`, which is what most DNS panels ask for: `_dmarc.agents`, or `@`
            for the zone itself.
        value (str):
        priority (int | None):
        status (AgentSetupStepsItemRecordsType0ItemStatus):
        state (AgentSetupStepsItemRecordsType0ItemStateType0 | None): Why `status` is what it is. `published`: correct
            in public DNS, waiting on the mail provider to confirm (DKIM; usually under an hour), or on its certificate
            (`signing_host`; usually ten minutes). `wrong_name`: our value is at `found_at` instead, often the zone typed
            twice. Null before the first check.
        found (None | str):
        found_at (None | str): Where `found` was read, when that was not `fqdn`.
        optional (bool): Not needed for mail: `signing` and `signing_host`, which let receivers check a signed sender
            from this domain. Its own `status`; never counted towards whether the domain is configured.
        description (str):
        checked_at (None | str):
    """

    type_: str
    record_type: str
    name: str
    zone: str
    fqdn: str
    host_relative: str
    value: str
    priority: int | None
    status: AgentSetupStepsItemRecordsType0ItemStatus
    state: AgentSetupStepsItemRecordsType0ItemStateType0 | None
    found: None | str
    found_at: None | str
    optional: bool
    description: str
    checked_at: None | str

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        record_type = self.record_type

        name = self.name

        zone = self.zone

        fqdn = self.fqdn

        host_relative = self.host_relative

        value = self.value

        priority: int | None
        priority = self.priority

        status = self.status.value

        state: None | str
        if isinstance(self.state, AgentSetupStepsItemRecordsType0ItemStateType0):
            state = self.state.value
        else:
            state = self.state

        found: None | str
        found = self.found

        found_at: None | str
        found_at = self.found_at

        optional = self.optional

        description = self.description

        checked_at: None | str
        checked_at = self.checked_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
                "record_type": record_type,
                "name": name,
                "zone": zone,
                "fqdn": fqdn,
                "host_relative": host_relative,
                "value": value,
                "priority": priority,
                "status": status,
                "state": state,
                "found": found,
                "found_at": found_at,
                "optional": optional,
                "description": description,
                "checked_at": checked_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        record_type = d.pop("record_type")

        name = d.pop("name")

        zone = d.pop("zone")

        fqdn = d.pop("fqdn")

        host_relative = d.pop("host_relative")

        value = d.pop("value")

        def _parse_priority(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        priority = _parse_priority(d.pop("priority"))

        status = AgentSetupStepsItemRecordsType0ItemStatus(d.pop("status"))

        def _parse_state(data: object) -> AgentSetupStepsItemRecordsType0ItemStateType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                state_type_0 = AgentSetupStepsItemRecordsType0ItemStateType0(data)

                return state_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AgentSetupStepsItemRecordsType0ItemStateType0 | None, data)

        state = _parse_state(d.pop("state"))

        def _parse_found(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        found = _parse_found(d.pop("found"))

        def _parse_found_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        found_at = _parse_found_at(d.pop("found_at"))

        optional = d.pop("optional")

        description = d.pop("description")

        def _parse_checked_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        checked_at = _parse_checked_at(d.pop("checked_at"))

        agent_setup_steps_item_records_type_0_item = cls(
            type_=type_,
            record_type=record_type,
            name=name,
            zone=zone,
            fqdn=fqdn,
            host_relative=host_relative,
            value=value,
            priority=priority,
            status=status,
            state=state,
            found=found,
            found_at=found_at,
            optional=optional,
            description=description,
            checked_at=checked_at,
        )

        return agent_setup_steps_item_records_type_0_item
