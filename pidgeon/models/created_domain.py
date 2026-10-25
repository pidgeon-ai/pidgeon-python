from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.created_domain_dns_records_item import CreatedDomainDnsRecordsItem
    from ..models.created_domain_existing_mail_type_0 import CreatedDomainExistingMailType0


T = TypeVar("T", bound="CreatedDomain")


@_attrs_define
class CreatedDomain:
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
        dns_records (list[CreatedDomainDnsRecordsItem]):
        dns_complete (bool):
        existing_mail (CreatedDomainExistingMailType0 | None):
    """

    id: str
    domain: str
    status: str
    catch_all_enabled: bool
    inbound_enabled: bool
    identity_count: int
    verified_at: None | str
    created_at: str
    dns_records: list[CreatedDomainDnsRecordsItem]
    dns_complete: bool
    existing_mail: CreatedDomainExistingMailType0 | None

    def to_dict(self) -> dict[str, Any]:
        from ..models.created_domain_existing_mail_type_0 import CreatedDomainExistingMailType0  # noqa: PLC0415

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

        existing_mail: dict[str, Any] | None
        if isinstance(self.existing_mail, CreatedDomainExistingMailType0):
            existing_mail = self.existing_mail.to_dict()
        else:
            existing_mail = self.existing_mail

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
                "existing_mail": existing_mail,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.created_domain_dns_records_item import CreatedDomainDnsRecordsItem  # noqa: PLC0415
        from ..models.created_domain_existing_mail_type_0 import CreatedDomainExistingMailType0  # noqa: PLC0415

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
            dns_records_item = CreatedDomainDnsRecordsItem.from_dict(dns_records_item_data)

            dns_records.append(dns_records_item)

        dns_complete = d.pop("dns_complete")

        def _parse_existing_mail(data: object) -> CreatedDomainExistingMailType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                existing_mail_type_0 = CreatedDomainExistingMailType0.from_dict(data)

                return existing_mail_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreatedDomainExistingMailType0 | None, data)

        existing_mail = _parse_existing_mail(d.pop("existing_mail"))

        created_domain = cls(
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
            existing_mail=existing_mail,
        )

        return created_domain
