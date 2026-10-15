from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.threads_update_body_owner_type import ThreadsUpdateBodyOwnerType
from ..models.threads_update_body_status import ThreadsUpdateBodyStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ThreadsUpdateBody")


@_attrs_define
class ThreadsUpdateBody:
    """
    Attributes:
        status (ThreadsUpdateBodyStatus | Unset):
        owner_type (ThreadsUpdateBodyOwnerType | Unset):
        assignee_id (None | Unset | UUID):
    """

    status: ThreadsUpdateBodyStatus | Unset = UNSET
    owner_type: ThreadsUpdateBodyOwnerType | Unset = UNSET
    assignee_id: None | Unset | UUID = UNSET

    def to_dict(self) -> dict[str, Any]:
        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        owner_type: str | Unset = UNSET
        if not isinstance(self.owner_type, Unset):
            owner_type = self.owner_type.value

        assignee_id: None | str | Unset
        if isinstance(self.assignee_id, Unset):
            assignee_id = UNSET
        elif isinstance(self.assignee_id, UUID):
            assignee_id = str(self.assignee_id)
        else:
            assignee_id = self.assignee_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if owner_type is not UNSET:
            field_dict["owner_type"] = owner_type
        if assignee_id is not UNSET:
            field_dict["assignee_id"] = assignee_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _status = d.pop("status", UNSET)
        status: ThreadsUpdateBodyStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ThreadsUpdateBodyStatus(_status)

        _owner_type = d.pop("owner_type", UNSET)
        owner_type: ThreadsUpdateBodyOwnerType | Unset
        if isinstance(_owner_type, Unset):
            owner_type = UNSET
        else:
            owner_type = ThreadsUpdateBodyOwnerType(_owner_type)

        def _parse_assignee_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                assignee_id_type_0 = UUID(data)

                return assignee_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        assignee_id = _parse_assignee_id(d.pop("assignee_id", UNSET))

        threads_update_body = cls(
            status=status,
            owner_type=owner_type,
            assignee_id=assignee_id,
        )

        return threads_update_body
