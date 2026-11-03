from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.sender_verification_signatures_envelope_result import SenderVerificationSignaturesEnvelopeResult

T = TypeVar("T", bound="SenderVerificationSignaturesEnvelope")


@_attrs_define
class SenderVerificationSignaturesEnvelope:
    """
    Attributes:
        result (SenderVerificationSignaturesEnvelopeResult):
        domain (None | str):
        kid (None | str):
        reason (None | str):
    """

    result: SenderVerificationSignaturesEnvelopeResult
    domain: None | str
    kid: None | str
    reason: None | str

    def to_dict(self) -> dict[str, Any]:
        result = self.result.value

        domain: None | str
        domain = self.domain

        kid: None | str
        kid = self.kid

        reason: None | str
        reason = self.reason

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "result": result,
                "domain": domain,
                "kid": kid,
                "reason": reason,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        result = SenderVerificationSignaturesEnvelopeResult(d.pop("result"))

        def _parse_domain(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        domain = _parse_domain(d.pop("domain"))

        def _parse_kid(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        kid = _parse_kid(d.pop("kid"))

        def _parse_reason(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        reason = _parse_reason(d.pop("reason"))

        sender_verification_signatures_envelope = cls(
            result=result,
            domain=domain,
            kid=kid,
            reason=reason,
        )

        return sender_verification_signatures_envelope
