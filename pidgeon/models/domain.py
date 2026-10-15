from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="Domain")


@_attrs_define
class Domain:
    """
    Attributes:
        id (str):
        domain (str):
        status (str):
        catch_all_enabled (bool):
        inbound_enabled (bool):
        identity_count (int):
        verified_at (None | str):
        created_at (str): ISO-8601, UTC.
    """

    id: str
    domain: str
    status: str
    catch_all_enabled: bool
    inbound_enabled: bool
    identity_count: int
    verified_at: None | str
    created_at: str

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        domain = self.domain

        status = self.status

        catch_all_enabled = self.catch_all_enabled

        inbound_enabled = self.inbound_enabled

        identity_count = self.identity_count

        verified_at: None | str
        verified_at = self.verified_at

        created_at = self.created_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "domain": domain,
                "status": status,
                "catch_all_enabled": catch_all_enabled,
                "inbound_enabled": inbound_enabled,
                "identity_count": identity_count,
                "verified_at": verified_at,
                "created_at": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        domain = d.pop("domain")

        status = d.pop("status")

        catch_all_enabled = d.pop("catch_all_enabled")

        inbound_enabled = d.pop("inbound_enabled")

        identity_count = d.pop("identity_count")

        def _parse_verified_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        verified_at = _parse_verified_at(d.pop("verified_at"))

        created_at = d.pop("created_at")

        domain = cls(
            id=id,
            domain=domain,
            status=status,
            catch_all_enabled=catch_all_enabled,
            inbound_enabled=inbound_enabled,
            identity_count=identity_count,
            verified_at=verified_at,
            created_at=created_at,
        )

        return domain
