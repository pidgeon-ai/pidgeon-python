from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.sender_verification_signatures_declaration_result import SenderVerificationSignaturesDeclarationResult

T = TypeVar("T", bound="SenderVerificationSignaturesDeclaration")


@_attrs_define
class SenderVerificationSignaturesDeclaration:
    """
    Attributes:
        result (SenderVerificationSignaturesDeclarationResult):
        domain (None | str):
        selector (None | str):
    """

    result: SenderVerificationSignaturesDeclarationResult
    domain: None | str
    selector: None | str

    def to_dict(self) -> dict[str, Any]:
        result = self.result.value

        domain: None | str
        domain = self.domain

        selector: None | str
        selector = self.selector

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "result": result,
                "domain": domain,
                "selector": selector,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        result = SenderVerificationSignaturesDeclarationResult(d.pop("result"))

        def _parse_domain(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        domain = _parse_domain(d.pop("domain"))

        def _parse_selector(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        selector = _parse_selector(d.pop("selector"))

        sender_verification_signatures_declaration = cls(
            result=result,
            domain=domain,
            selector=selector,
        )

        return sender_verification_signatures_declaration
