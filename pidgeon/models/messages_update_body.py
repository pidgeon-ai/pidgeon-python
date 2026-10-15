from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.messages_update_body_folder import MessagesUpdateBodyFolder
from ..types import UNSET, Unset

T = TypeVar("T", bound="MessagesUpdateBody")


@_attrs_define
class MessagesUpdateBody:
    """
    Attributes:
        is_read (bool | Unset): Refused for an API key: read state belongs to a person and a key is not one. Archive the
            message, or track what you have seen with `GET /v1/mailboxes/changes`. A person signed in to the dashboard sets
            this.
        is_starred (bool | Unset):
        folder (MessagesUpdateBodyFolder | Unset):
    """

    is_read: bool | Unset = UNSET
    is_starred: bool | Unset = UNSET
    folder: MessagesUpdateBodyFolder | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        is_read = self.is_read

        is_starred = self.is_starred

        folder: str | Unset = UNSET
        if not isinstance(self.folder, Unset):
            folder = self.folder.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if is_read is not UNSET:
            field_dict["is_read"] = is_read
        if is_starred is not UNSET:
            field_dict["is_starred"] = is_starred
        if folder is not UNSET:
            field_dict["folder"] = folder

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_read = d.pop("is_read", UNSET)

        is_starred = d.pop("is_starred", UNSET)

        _folder = d.pop("folder", UNSET)
        folder: MessagesUpdateBodyFolder | Unset
        if isinstance(_folder, Unset):
            folder = UNSET
        else:
            folder = MessagesUpdateBodyFolder(_folder)

        messages_update_body = cls(
            is_read=is_read,
            is_starred=is_starred,
            folder=folder,
        )

        return messages_update_body
