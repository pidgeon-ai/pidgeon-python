from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..models.grant_template_subject_type import GrantTemplateSubjectType

if TYPE_CHECKING:
    from ..models.grant_template_limit_type_0 import GrantTemplateLimitType0


T = TypeVar("T", bound="GrantTemplate")


@_attrs_define
class GrantTemplate:
    """
    Attributes:
        object_ (Literal['grant_template']):
        id (str):
        name (str):
        label (str):
        audience (None | str):
        audience_name (None | str):
        subject_type (GrantTemplateSubjectType):
        limit (GrantTemplateLimitType0 | None):
        max_days (int):
        created_at (str): ISO-8601, UTC.
    """

    object_: Literal["grant_template"]
    id: str
    name: str
    label: str
    audience: None | str
    audience_name: None | str
    subject_type: GrantTemplateSubjectType
    limit: GrantTemplateLimitType0 | None
    max_days: int
    created_at: str

    def to_dict(self) -> dict[str, Any]:
        from ..models.grant_template_limit_type_0 import GrantTemplateLimitType0  # noqa: PLC0415

        object_ = self.object_

        id = self.id

        name = self.name

        label = self.label

        audience: None | str
        audience = self.audience

        audience_name: None | str
        audience_name = self.audience_name

        subject_type = self.subject_type.value

        limit: dict[str, Any] | None
        if isinstance(self.limit, GrantTemplateLimitType0):
            limit = self.limit.to_dict()
        else:
            limit = self.limit

        max_days = self.max_days

        created_at = self.created_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "object": object_,
                "id": id,
                "name": name,
                "label": label,
                "audience": audience,
                "audience_name": audience_name,
                "subject_type": subject_type,
                "limit": limit,
                "max_days": max_days,
                "created_at": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.grant_template_limit_type_0 import GrantTemplateLimitType0  # noqa: PLC0415

        d = dict(src_dict)
        object_ = cast(Literal["grant_template"], d.pop("object"))
        if object_ != "grant_template":
            raise ValueError(f"object must match const 'grant_template', got '{object_}'")

        id = d.pop("id")

        name = d.pop("name")

        label = d.pop("label")

        def _parse_audience(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        audience = _parse_audience(d.pop("audience"))

        def _parse_audience_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        audience_name = _parse_audience_name(d.pop("audience_name"))

        subject_type = GrantTemplateSubjectType(d.pop("subject_type"))

        def _parse_limit(data: object) -> GrantTemplateLimitType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                limit_type_0 = GrantTemplateLimitType0.from_dict(data)

                return limit_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GrantTemplateLimitType0 | None, data)

        limit = _parse_limit(d.pop("limit"))

        max_days = d.pop("max_days")

        created_at = d.pop("created_at")

        grant_template = cls(
            object_=object_,
            id=id,
            name=name,
            label=label,
            audience=audience,
            audience_name=audience_name,
            subject_type=subject_type,
            limit=limit,
            max_days=max_days,
            created_at=created_at,
        )

        return grant_template
