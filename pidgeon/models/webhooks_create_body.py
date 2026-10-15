from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.webhooks_create_body_event_types_item import WebhooksCreateBodyEventTypesItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="WebhooksCreateBody")


@_attrs_define
class WebhooksCreateBody:
    """
    Attributes:
        url (str): Where we POST. HTTPS, and it has to answer within a few seconds.
        identity_id (None | Unset | UUID): The address this belongs to.
        event_types (list[WebhooksCreateBodyEventTypesItem] | Unset):
    """

    url: str
    identity_id: None | Unset | UUID = UNSET
    event_types: list[WebhooksCreateBodyEventTypesItem] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        identity_id: None | str | Unset
        if isinstance(self.identity_id, Unset):
            identity_id = UNSET
        elif isinstance(self.identity_id, UUID):
            identity_id = str(self.identity_id)
        else:
            identity_id = self.identity_id

        event_types: list[str] | Unset = UNSET
        if not isinstance(self.event_types, Unset):
            event_types = []
            for event_types_item_data in self.event_types:
                event_types_item = event_types_item_data.value
                event_types.append(event_types_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "url": url,
            }
        )
        if identity_id is not UNSET:
            field_dict["identity_id"] = identity_id
        if event_types is not UNSET:
            field_dict["event_types"] = event_types

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")

        def _parse_identity_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                identity_id_type_0 = UUID(data)

                return identity_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        identity_id = _parse_identity_id(d.pop("identity_id", UNSET))

        _event_types = d.pop("event_types", UNSET)
        event_types: list[WebhooksCreateBodyEventTypesItem] | Unset = UNSET
        if _event_types is not UNSET:
            event_types = []
            for event_types_item_data in _event_types:
                event_types_item = WebhooksCreateBodyEventTypesItem(event_types_item_data)

                event_types.append(event_types_item)

        webhooks_create_body = cls(
            url=url,
            identity_id=identity_id,
            event_types=event_types,
        )

        return webhooks_create_body
