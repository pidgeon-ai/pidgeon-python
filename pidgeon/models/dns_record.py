from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.dns_record_status import DnsRecordStatus

T = TypeVar("T", bound="DnsRecord")


@_attrs_define
class DnsRecord:
    """
    Attributes:
        type_ (str):
        record_type (str):
        name (str):
        value (str):
        priority (int | None):
        status (DnsRecordStatus):
        found (None | str):
        description (str):
        checked_at (None | str):
    """

    type_: str
    record_type: str
    name: str
    value: str
    priority: int | None
    status: DnsRecordStatus
    found: None | str
    description: str
    checked_at: None | str

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        record_type = self.record_type

        name = self.name

        value = self.value

        priority: int | None
        priority = self.priority

        status = self.status.value

        found: None | str
        found = self.found

        description = self.description

        checked_at: None | str
        checked_at = self.checked_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
                "record_type": record_type,
                "name": name,
                "value": value,
                "priority": priority,
                "status": status,
                "found": found,
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

        value = d.pop("value")

        def _parse_priority(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        priority = _parse_priority(d.pop("priority"))

        status = DnsRecordStatus(d.pop("status"))

        def _parse_found(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        found = _parse_found(d.pop("found"))

        description = d.pop("description")

        def _parse_checked_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        checked_at = _parse_checked_at(d.pop("checked_at"))

        dns_record = cls(
            type_=type_,
            record_type=record_type,
            name=name,
            value=value,
            priority=priority,
            status=status,
            found=found,
            description=description,
            checked_at=checked_at,
        )

        return dns_record
