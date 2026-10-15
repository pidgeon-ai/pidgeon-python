from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RoutingCreateBodyType1")


@_attrs_define
class RoutingCreateBodyType1:
    """
    Attributes:
        match_type (Literal['pattern']):
        local_part (str):
        domain_id (UUID | Unset):
        destination_identity_id (UUID | Unset):
        destination_webhook_id (UUID | Unset):
    """

    match_type: Literal["pattern"]
    local_part: str
    domain_id: UUID | Unset = UNSET
    destination_identity_id: UUID | Unset = UNSET
    destination_webhook_id: UUID | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        match_type = self.match_type

        local_part = self.local_part

        domain_id: str | Unset = UNSET
        if not isinstance(self.domain_id, Unset):
            domain_id = str(self.domain_id)

        destination_identity_id: str | Unset = UNSET
        if not isinstance(self.destination_identity_id, Unset):
            destination_identity_id = str(self.destination_identity_id)

        destination_webhook_id: str | Unset = UNSET
        if not isinstance(self.destination_webhook_id, Unset):
            destination_webhook_id = str(self.destination_webhook_id)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "match_type": match_type,
                "local_part": local_part,
            }
        )
        if domain_id is not UNSET:
            field_dict["domain_id"] = domain_id
        if destination_identity_id is not UNSET:
            field_dict["destination_identity_id"] = destination_identity_id
        if destination_webhook_id is not UNSET:
            field_dict["destination_webhook_id"] = destination_webhook_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        match_type = cast(Literal["pattern"], d.pop("match_type"))
        if match_type != "pattern":
            raise ValueError(f"match_type must match const 'pattern', got '{match_type}'")

        local_part = d.pop("local_part")

        _domain_id = d.pop("domain_id", UNSET)
        domain_id: UUID | Unset
        if isinstance(_domain_id, Unset):
            domain_id = UNSET
        else:
            domain_id = UUID(_domain_id)

        _destination_identity_id = d.pop("destination_identity_id", UNSET)
        destination_identity_id: UUID | Unset
        if isinstance(_destination_identity_id, Unset):
            destination_identity_id = UNSET
        else:
            destination_identity_id = UUID(_destination_identity_id)

        _destination_webhook_id = d.pop("destination_webhook_id", UNSET)
        destination_webhook_id: UUID | Unset
        if isinstance(_destination_webhook_id, Unset):
            destination_webhook_id = UNSET
        else:
            destination_webhook_id = UUID(_destination_webhook_id)

        routing_create_body_type_1 = cls(
            match_type=match_type,
            local_part=local_part,
            domain_id=domain_id,
            destination_identity_id=destination_identity_id,
            destination_webhook_id=destination_webhook_id,
        )

        return routing_create_body_type_1
