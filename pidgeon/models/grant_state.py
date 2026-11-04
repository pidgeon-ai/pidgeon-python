from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..models.grant_state_status import GrantStateStatus

T = TypeVar("T", bound="GrantState")


@_attrs_define
class GrantState:
    """
    Attributes:
        object_ (Literal['grant_status']):
        id (str):
        status (GrantStateStatus):
        expires_at (str): ISO-8601, UTC.
        revoked_at (None | str):
    """

    object_: Literal["grant_status"]
    id: str
    status: GrantStateStatus
    expires_at: str
    revoked_at: None | str

    def to_dict(self) -> dict[str, Any]:
        object_ = self.object_

        id = self.id

        status = self.status.value

        expires_at = self.expires_at

        revoked_at: None | str
        revoked_at = self.revoked_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "object": object_,
                "id": id,
                "status": status,
                "expires_at": expires_at,
                "revoked_at": revoked_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        object_ = cast(Literal["grant_status"], d.pop("object"))
        if object_ != "grant_status":
            raise ValueError(f"object must match const 'grant_status', got '{object_}'")

        id = d.pop("id")

        status = GrantStateStatus(d.pop("status"))

        expires_at = d.pop("expires_at")

        def _parse_revoked_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        revoked_at = _parse_revoked_at(d.pop("revoked_at"))

        grant_state = cls(
            object_=object_,
            id=id,
            status=status,
            expires_at=expires_at,
            revoked_at=revoked_at,
        )

        return grant_state
