from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.me_key_type_0_access import MeKeyType0Access

T = TypeVar("T", bound="MeKeyType0")


@_attrs_define
class MeKeyType0:
    """
    Attributes:
        id (str):
        name (str): What somebody called it, for telling two keys apart.
        prefix (str): The visible start of the token, e.g. `pgn_live_a1b2`.
        access (MeKeyType0Access): The highest rung this key reaches on any address. Composed with the grant on the
            address itself — the lower of the two wins — so this is a ceiling, not a promise.
        reaches_all_addresses (bool): True when it reaches every address the workspace owns, including ones created
            after it. False when it reaches a fixed list.
        expires_at (None | str): When it stops authenticating, or null.
        created_at (str): ISO-8601, UTC.
        test (bool): A test-mode key (`pgn_test_`): its mail never leaves Pidgeon and counts against nothing. Read this
            rather than the token’s prefix.
        rotated_at (None | str): When the key was last given a new secret by `POST /api-keys/{id}/rotate`, or null.
        previous_token_expires_at (None | str): While the secret it had before its last rotation still works, when that
            stops. Null when it has stopped or there was no grace period.
    """

    id: str
    name: str
    prefix: str
    access: MeKeyType0Access
    reaches_all_addresses: bool
    expires_at: None | str
    created_at: str
    test: bool
    rotated_at: None | str
    previous_token_expires_at: None | str

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        prefix = self.prefix

        access = self.access.value

        reaches_all_addresses = self.reaches_all_addresses

        expires_at: None | str
        expires_at = self.expires_at

        created_at = self.created_at

        test = self.test

        rotated_at: None | str
        rotated_at = self.rotated_at

        previous_token_expires_at: None | str
        previous_token_expires_at = self.previous_token_expires_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
                "prefix": prefix,
                "access": access,
                "reaches_all_addresses": reaches_all_addresses,
                "expires_at": expires_at,
                "created_at": created_at,
                "test": test,
                "rotated_at": rotated_at,
                "previous_token_expires_at": previous_token_expires_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        prefix = d.pop("prefix")

        access = MeKeyType0Access(d.pop("access"))

        reaches_all_addresses = d.pop("reaches_all_addresses")

        def _parse_expires_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        expires_at = _parse_expires_at(d.pop("expires_at"))

        created_at = d.pop("created_at")

        test = d.pop("test")

        def _parse_rotated_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        rotated_at = _parse_rotated_at(d.pop("rotated_at"))

        def _parse_previous_token_expires_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        previous_token_expires_at = _parse_previous_token_expires_at(d.pop("previous_token_expires_at"))

        me_key_type_0 = cls(
            id=id,
            name=name,
            prefix=prefix,
            access=access,
            reaches_all_addresses=reaches_all_addresses,
            expires_at=expires_at,
            created_at=created_at,
            test=test,
            rotated_at=rotated_at,
            previous_token_expires_at=previous_token_expires_at,
        )

        return me_key_type_0
