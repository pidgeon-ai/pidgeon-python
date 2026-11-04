from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.grants_templates_create_body_subject_type import GrantsTemplatesCreateBodySubjectType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.grants_templates_create_body_limit import GrantsTemplatesCreateBodyLimit


T = TypeVar("T", bound="GrantsTemplatesCreateBody")


@_attrs_define
class GrantsTemplatesCreateBody:
    """
    Attributes:
        name (str): The scope’s stable name, for software: `bookings.change`.
        label (str): What the agent may do, as the consent screen says it after "wants to": `manage your bookings`.
        subject_type (GrantsTemplatesCreateBodySubjectType): What a grant is for: a customer, an account or an order.
        audience (str | Unset): The domain the agent will act with. A grant reaching anywhere else does not hold.
        audience_name (str | Unset): How people call it: `Delta`.
        limit (GrantsTemplatesCreateBodyLimit | Unset): A ceiling the grant states, such as "refunds up to $100".
        max_days (int | Unset): The longest a grant from this template may last. 90 when omitted.
    """

    name: str
    label: str
    subject_type: GrantsTemplatesCreateBodySubjectType
    audience: str | Unset = UNSET
    audience_name: str | Unset = UNSET
    limit: GrantsTemplatesCreateBodyLimit | Unset = UNSET
    max_days: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        label = self.label

        subject_type = self.subject_type.value

        audience = self.audience

        audience_name = self.audience_name

        limit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.limit, Unset):
            limit = self.limit.to_dict()

        max_days = self.max_days

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "label": label,
                "subject_type": subject_type,
            }
        )
        if audience is not UNSET:
            field_dict["audience"] = audience
        if audience_name is not UNSET:
            field_dict["audience_name"] = audience_name
        if limit is not UNSET:
            field_dict["limit"] = limit
        if max_days is not UNSET:
            field_dict["max_days"] = max_days

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.grants_templates_create_body_limit import GrantsTemplatesCreateBodyLimit  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name")

        label = d.pop("label")

        subject_type = GrantsTemplatesCreateBodySubjectType(d.pop("subject_type"))

        audience = d.pop("audience", UNSET)

        audience_name = d.pop("audience_name", UNSET)

        _limit = d.pop("limit", UNSET)
        limit: GrantsTemplatesCreateBodyLimit | Unset
        if isinstance(_limit, Unset):
            limit = UNSET
        else:
            limit = GrantsTemplatesCreateBodyLimit.from_dict(_limit)

        max_days = d.pop("max_days", UNSET)

        grants_templates_create_body = cls(
            name=name,
            label=label,
            subject_type=subject_type,
            audience=audience,
            audience_name=audience_name,
            limit=limit,
            max_days=max_days,
        )

        return grants_templates_create_body
