from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.messages_act_body_action import MessagesActBodyAction

T = TypeVar("T", bound="MessagesActBody")


@_attrs_define
class MessagesActBody:
    """
    Attributes:
        message_ids (list[UUID]):
        action (MessagesActBodyAction): `read` and `unread` are refused for an API key: read state belongs to a person
            and a key is not one. Every other action works.
    """

    message_ids: list[UUID]
    action: MessagesActBodyAction

    def to_dict(self) -> dict[str, Any]:
        message_ids = []
        for message_ids_item_data in self.message_ids:
            message_ids_item = str(message_ids_item_data)
            message_ids.append(message_ids_item)

        action = self.action.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "message_ids": message_ids,
                "action": action,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message_ids = []
        _message_ids = d.pop("message_ids")
        for message_ids_item_data in _message_ids:
            message_ids_item = UUID(message_ids_item_data)

            message_ids.append(message_ids_item)

        action = MessagesActBodyAction(d.pop("action"))

        messages_act_body = cls(
            message_ids=message_ids,
            action=action,
        )

        return messages_act_body
