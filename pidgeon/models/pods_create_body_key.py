from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.pods_create_body_key_access import PodsCreateBodyKeyAccess
from ..types import UNSET, Unset

T = TypeVar("T", bound="PodsCreateBodyKey")


@_attrs_define
class PodsCreateBodyKey:
    """A key for the new pod, reaching its addresses and nothing else. Its token is in this response once; a replay returns
    the key with `token: null`.

        Attributes:
            access (PodsCreateBodyKeyAccess):
            name (str | Unset):
            expires_at (datetime.datetime | None | Unset):
            test (bool | Unset): Mint a test-mode key (`pgn_test_`) for the pod instead of a live one.
    """

    access: PodsCreateBodyKeyAccess
    name: str | Unset = UNSET
    expires_at: datetime.datetime | None | Unset = UNSET
    test: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        access = self.access.value

        name = self.name

        expires_at: None | str | Unset
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        elif isinstance(self.expires_at, datetime.datetime):
            expires_at = self.expires_at.isoformat()
        else:
            expires_at = self.expires_at

        test = self.test

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "access": access,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if test is not UNSET:
            field_dict["test"] = test

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        access = PodsCreateBodyKeyAccess(d.pop("access"))

        name = d.pop("name", UNSET)

        def _parse_expires_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_at_type_0 = datetime.datetime.fromisoformat(data)

                return expires_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        expires_at = _parse_expires_at(d.pop("expires_at", UNSET))

        test = d.pop("test", UNSET)

        pods_create_body_key = cls(
            access=access,
            name=name,
            expires_at=expires_at,
            test=test,
        )

        return pods_create_body_key
