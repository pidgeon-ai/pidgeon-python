from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.sender_verification_signatures_declaration import SenderVerificationSignaturesDeclaration
    from ..models.sender_verification_signatures_envelope import SenderVerificationSignaturesEnvelope
    from ..models.sender_verification_signatures_request import SenderVerificationSignaturesRequest


T = TypeVar("T", bound="SenderVerificationSignatures")


@_attrs_define
class SenderVerificationSignatures:
    """
    Attributes:
        declaration (SenderVerificationSignaturesDeclaration):
        envelope (SenderVerificationSignaturesEnvelope):
        request (SenderVerificationSignaturesRequest): An HTTP request’s signature (RFC 9421, Web Bot Auth), when
            `request` was sent. `none` for a message.
    """

    declaration: SenderVerificationSignaturesDeclaration
    envelope: SenderVerificationSignaturesEnvelope
    request: SenderVerificationSignaturesRequest

    def to_dict(self) -> dict[str, Any]:
        declaration = self.declaration.to_dict()

        envelope = self.envelope.to_dict()

        request = self.request.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "declaration": declaration,
                "envelope": envelope,
                "request": request,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sender_verification_signatures_declaration import SenderVerificationSignaturesDeclaration  # noqa: PLC0415
        from ..models.sender_verification_signatures_envelope import SenderVerificationSignaturesEnvelope  # noqa: PLC0415
        from ..models.sender_verification_signatures_request import SenderVerificationSignaturesRequest  # noqa: PLC0415

        d = dict(src_dict)
        declaration = SenderVerificationSignaturesDeclaration.from_dict(d.pop("declaration"))

        envelope = SenderVerificationSignaturesEnvelope.from_dict(d.pop("envelope"))

        request = SenderVerificationSignaturesRequest.from_dict(d.pop("request"))

        sender_verification_signatures = cls(
            declaration=declaration,
            envelope=envelope,
            request=request,
        )

        return sender_verification_signatures
