from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.api_key_created_access import ApiKeyCreatedAccess

T = TypeVar("T", bound="ApiKeyCreated")


@_attrs_define
class ApiKeyCreated:
    """
    Attributes:
        id (str):
        name (str):
        prefix (str):
        identity_ids (list[str]):
        pod_id (None | str): The pod this key belongs to, or null. A pod key reaches every address in the pod —
            `identity_ids` lists them today — and the addresses the pod gains later.
        access (ApiKeyCreatedAccess): The highest rung on any address. Composed with the grant; lower wins.
        created_by_key_id (None | str):
        last_used_at (None | str):
        revoked_at (None | str):
        created_at (str): ISO-8601, UTC.
        rotated_at (None | str): When the key was last given a new secret by `POST /api-keys/{id}/rotate`, or null.
        test (bool): A test-mode key: its mail never leaves Pidgeon and counts against nothing.
        previous_token_expires_at (None | str): While the secret it had before its last rotation still works, when that
            stops. Null when it has stopped or there was no grace period.
        token (str): The secret. Shown once, here, and never again.
    """

    id: str
    name: str
    prefix: str
    identity_ids: list[str]
    pod_id: None | str
    access: ApiKeyCreatedAccess
    created_by_key_id: None | str
    last_used_at: None | str
    revoked_at: None | str
    created_at: str
    rotated_at: None | str
    test: bool
    previous_token_expires_at: None | str
    token: str

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        prefix = self.prefix

        identity_ids = self.identity_ids

        pod_id: None | str
        pod_id = self.pod_id

        access = self.access.value

        created_by_key_id: None | str
        created_by_key_id = self.created_by_key_id

        last_used_at: None | str
        last_used_at = self.last_used_at

        revoked_at: None | str
        revoked_at = self.revoked_at

        created_at = self.created_at

        rotated_at: None | str
        rotated_at = self.rotated_at

        test = self.test

        previous_token_expires_at: None | str
        previous_token_expires_at = self.previous_token_expires_at

        token = self.token

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
                "prefix": prefix,
                "identity_ids": identity_ids,
                "pod_id": pod_id,
                "access": access,
                "created_by_key_id": created_by_key_id,
                "last_used_at": last_used_at,
                "revoked_at": revoked_at,
                "created_at": created_at,
                "rotated_at": rotated_at,
                "test": test,
                "previous_token_expires_at": previous_token_expires_at,
                "token": token,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        prefix = d.pop("prefix")

        identity_ids = cast(list[str], d.pop("identity_ids"))

        def _parse_pod_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        pod_id = _parse_pod_id(d.pop("pod_id"))

        access = ApiKeyCreatedAccess(d.pop("access"))

        def _parse_created_by_key_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        created_by_key_id = _parse_created_by_key_id(d.pop("created_by_key_id"))

        def _parse_last_used_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_used_at = _parse_last_used_at(d.pop("last_used_at"))

        def _parse_revoked_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        revoked_at = _parse_revoked_at(d.pop("revoked_at"))

        created_at = d.pop("created_at")

        def _parse_rotated_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        rotated_at = _parse_rotated_at(d.pop("rotated_at"))

        test = d.pop("test")

        def _parse_previous_token_expires_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        previous_token_expires_at = _parse_previous_token_expires_at(d.pop("previous_token_expires_at"))

        token = d.pop("token")

        api_key_created = cls(
            id=id,
            name=name,
            prefix=prefix,
            identity_ids=identity_ids,
            pod_id=pod_id,
            access=access,
            created_by_key_id=created_by_key_id,
            last_used_at=last_used_at,
            revoked_at=revoked_at,
            created_at=created_at,
            rotated_at=rotated_at,
            test=test,
            previous_token_expires_at=previous_token_expires_at,
            token=token,
        )

        return api_key_created
