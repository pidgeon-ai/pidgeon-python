from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.agent_setup_steps_item_id import AgentSetupStepsItemId
from ..models.agent_setup_steps_item_owner import AgentSetupStepsItemOwner

if TYPE_CHECKING:
    from ..models.agent_setup_steps_item_records_type_0_item import AgentSetupStepsItemRecordsType0Item


T = TypeVar("T", bound="AgentSetupStepsItem")


@_attrs_define
class AgentSetupStepsItem:
    """
    Attributes:
        id (AgentSetupStepsItemId): Stable: branch on this, not on `what`. `address` (the key reaches none),
            `human_code` (a signup waiting for its code), `domain` (DNS), `address_active`, `allowance` (the account may
            send nothing a day), `key_send` (the key is below `send` here), `live_key` (a test key), `send_policy` (a list
            with nobody on it), `daily_limit`.
        done (bool):
        owner (AgentSetupStepsItemOwner): Who acts: you, or a person you have to ask.
        what (str): The step, in a few words.
        how (str): What to do, or, when it is done, what is true.
        records (list[AgentSetupStepsItemRecordsType0Item] | None): On `domain` while it is not verified: the records
            still to publish. Else null.
        resets_at (None | str): On `daily_limit` while it refuses: when sending frees up. Else null.
    """

    id: AgentSetupStepsItemId
    done: bool
    owner: AgentSetupStepsItemOwner
    what: str
    how: str
    records: list[AgentSetupStepsItemRecordsType0Item] | None
    resets_at: None | str

    def to_dict(self) -> dict[str, Any]:
        id = self.id.value

        done = self.done

        owner = self.owner.value

        what = self.what

        how = self.how

        records: list[dict[str, Any]] | None
        if isinstance(self.records, list):
            records = []
            for records_type_0_item_data in self.records:
                records_type_0_item = records_type_0_item_data.to_dict()
                records.append(records_type_0_item)

        else:
            records = self.records

        resets_at: None | str
        resets_at = self.resets_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "done": done,
                "owner": owner,
                "what": what,
                "how": how,
                "records": records,
                "resets_at": resets_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_setup_steps_item_records_type_0_item import AgentSetupStepsItemRecordsType0Item  # noqa: PLC0415

        d = dict(src_dict)
        id = AgentSetupStepsItemId(d.pop("id"))

        done = d.pop("done")

        owner = AgentSetupStepsItemOwner(d.pop("owner"))

        what = d.pop("what")

        how = d.pop("how")

        def _parse_records(data: object) -> list[AgentSetupStepsItemRecordsType0Item] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                records_type_0 = []
                _records_type_0 = data
                for records_type_0_item_data in _records_type_0:
                    records_type_0_item = AgentSetupStepsItemRecordsType0Item.from_dict(records_type_0_item_data)

                    records_type_0.append(records_type_0_item)

                return records_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AgentSetupStepsItemRecordsType0Item] | None, data)

        records = _parse_records(d.pop("records"))

        def _parse_resets_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        resets_at = _parse_resets_at(d.pop("resets_at"))

        agent_setup_steps_item = cls(
            id=id,
            done=done,
            owner=owner,
            what=what,
            how=how,
            records=records,
            resets_at=resets_at,
        )

        return agent_setup_steps_item
