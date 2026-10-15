from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.domain_detail_dns_records_item import DomainDetailDnsRecordsItem


T = TypeVar("T", bound="DomainDetail")


@_attrs_define
class DomainDetail:
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
        dns_records (list[DomainDetailDnsRecordsItem]):
        dns_complete (bool):
    """

    id: str
    domain: str
    status: str
    catch_all_enabled: bool
    inbound_enabled: bool
    identity_count: int
    verified_at: None | str
    created_at: str
    dns_records: list[DomainDetailDnsRecordsItem]
    dns_complete: bool

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

        dns_records = []
        for dns_records_item_data in self.dns_records:
            dns_records_item = dns_records_item_data.to_dict()
            dns_records.append(dns_records_item)

        dns_complete = self.dns_complete

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
                "dns_records": dns_records,
                "dns_complete": dns_complete,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domain_detail_dns_records_item import DomainDetailDnsRecordsItem  # noqa: PLC0415

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

        dns_records = []
        _dns_records = d.pop("dns_records")
        for dns_records_item_data in _dns_records:
            dns_records_item = DomainDetailDnsRecordsItem.from_dict(dns_records_item_data)

            dns_records.append(dns_records_item)

        dns_complete = d.pop("dns_complete")

        domain_detail = cls(
            id=id,
            domain=domain,
            status=status,
            catch_all_enabled=catch_all_enabled,
            inbound_enabled=inbound_enabled,
            identity_count=identity_count,
            verified_at=verified_at,
            created_at=created_at,
            dns_records=dns_records,
            dns_complete=dns_complete,
        )

        return domain_detail
