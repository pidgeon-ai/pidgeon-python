from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pod_created import PodCreated
    from ..models.warning import Warning_


T = TypeVar("T", bound="PodsCreateResponse201")


@_attrs_define
class PodsCreateResponse201:
    """
    Attributes:
        data (PodCreated):
        warnings (list[Warning_] | Unset): Present only when the request used something deprecated: what it left out and
            the date it stops working. Answered with `Deprecation` and `Sunset` headers too.
    """

    data: PodCreated
    warnings: list[Warning_] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        warnings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = []
            for warnings_item_data in self.warnings:
                warnings_item = warnings_item_data.to_dict()
                warnings.append(warnings_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pod_created import PodCreated  # noqa: PLC0415
        from ..models.warning import Warning_  # noqa: PLC0415

        d = dict(src_dict)
        data = PodCreated.from_dict(d.pop("data"))

        _warnings = d.pop("warnings", UNSET)
        warnings: list[Warning_] | Unset = UNSET
        if _warnings is not UNSET:
            warnings = []
            for warnings_item_data in _warnings:
                warnings_item = Warning_.from_dict(warnings_item_data)

                warnings.append(warnings_item)

        pods_create_response_201 = cls(
            data=data,
            warnings=warnings,
        )

        pods_create_response_201.additional_properties = d
        return pods_create_response_201

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
