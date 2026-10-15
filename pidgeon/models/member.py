from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.member_role import MemberRole

T = TypeVar("T", bound="Member")


@_attrs_define
class Member:
    """
    Attributes:
        id (str): The person’s user id. This is what `user_id` takes when granting access to an address. On a workspace
            nobody was invited to it equals the workspace’s own id, because a personal workspace is created with its
            founder’s id — the two matching is expected and the value is still the user id.
        email (str):
        name (None | str):
        role (MemberRole):
        joined_at (str): ISO-8601, UTC.
    """

    id: str
    email: str
    name: None | str
    role: MemberRole
    joined_at: str

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        email = self.email

        name: None | str
        name = self.name

        role = self.role.value

        joined_at = self.joined_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "email": email,
                "name": name,
                "role": role,
                "joined_at": joined_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        email = d.pop("email")

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        role = MemberRole(d.pop("role"))

        joined_at = d.pop("joined_at")

        member = cls(
            id=id,
            email=email,
            name=name,
            role=role,
            joined_at=joined_at,
        )

        return member
