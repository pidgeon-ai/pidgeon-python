from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.verification_dns_records_item import VerificationDnsRecordsItem


T = TypeVar("T", bound="Verification")


@_attrs_define
class Verification:
    """
    Attributes:
        verified (bool):
        mail_configured (bool):
        message (str):
        dns_records (list[VerificationDnsRecordsItem]):
        dns_complete (bool):
    """

    verified: bool
    mail_configured: bool
    message: str
    dns_records: list[VerificationDnsRecordsItem]
    dns_complete: bool

    def to_dict(self) -> dict[str, Any]:
        verified = self.verified

        mail_configured = self.mail_configured

        message = self.message

        dns_records = []
        for dns_records_item_data in self.dns_records:
            dns_records_item = dns_records_item_data.to_dict()
            dns_records.append(dns_records_item)

        dns_complete = self.dns_complete

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "verified": verified,
                "mail_configured": mail_configured,
                "message": message,
                "dns_records": dns_records,
                "dns_complete": dns_complete,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.verification_dns_records_item import VerificationDnsRecordsItem  # noqa: PLC0415

        d = dict(src_dict)
        verified = d.pop("verified")

        mail_configured = d.pop("mail_configured")

        message = d.pop("message")

        dns_records = []
        _dns_records = d.pop("dns_records")
        for dns_records_item_data in _dns_records:
            dns_records_item = VerificationDnsRecordsItem.from_dict(dns_records_item_data)

            dns_records.append(dns_records_item)

        dns_complete = d.pop("dns_complete")

        verification = cls(
            verified=verified,
            mail_configured=mail_configured,
            message=message,
            dns_records=dns_records,
            dns_complete=dns_complete,
        )

        return verification
