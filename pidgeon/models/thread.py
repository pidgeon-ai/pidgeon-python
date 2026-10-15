from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.thread_owner_type import ThreadOwnerType
from ..models.thread_status import ThreadStatus

T = TypeVar("T", bound="Thread")


@_attrs_define
class Thread:
    """
    Attributes:
        id (str):
        identity (str):
        subject (None | str):
        status (ThreadStatus):
        owner_type (ThreadOwnerType):
        assignee_id (None | UUID):
        assigned_at (None | str):
        message_count (int):
        last_message_at (None | str):
        created_at (str): ISO-8601, UTC.
    """

    id: str
    identity: str
    subject: None | str
    status: ThreadStatus
    owner_type: ThreadOwnerType
    assignee_id: None | UUID
    assigned_at: None | str
    message_count: int
    last_message_at: None | str
    created_at: str

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        identity = self.identity

        subject: None | str
        subject = self.subject

        status = self.status.value

        owner_type = self.owner_type.value

        assignee_id: None | str
        if isinstance(self.assignee_id, UUID):
            assignee_id = str(self.assignee_id)
        else:
            assignee_id = self.assignee_id

        assigned_at: None | str
        assigned_at = self.assigned_at

        message_count = self.message_count

        last_message_at: None | str
        last_message_at = self.last_message_at

        created_at = self.created_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "identity": identity,
                "subject": subject,
                "status": status,
                "owner_type": owner_type,
                "assignee_id": assignee_id,
                "assigned_at": assigned_at,
                "message_count": message_count,
                "last_message_at": last_message_at,
                "created_at": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        identity = d.pop("identity")

        def _parse_subject(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        subject = _parse_subject(d.pop("subject"))

        status = ThreadStatus(d.pop("status"))

        owner_type = ThreadOwnerType(d.pop("owner_type"))

        def _parse_assignee_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                assignee_id_type_0 = UUID(data)

                return assignee_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        assignee_id = _parse_assignee_id(d.pop("assignee_id"))

        def _parse_assigned_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        assigned_at = _parse_assigned_at(d.pop("assigned_at"))

        message_count = d.pop("message_count")

        def _parse_last_message_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_message_at = _parse_last_message_at(d.pop("last_message_at"))

        created_at = d.pop("created_at")

        thread = cls(
            id=id,
            identity=identity,
            subject=subject,
            status=status,
            owner_type=owner_type,
            assignee_id=assignee_id,
            assigned_at=assigned_at,
            message_count=message_count,
            last_message_at=last_message_at,
            created_at=created_at,
        )

        return thread
