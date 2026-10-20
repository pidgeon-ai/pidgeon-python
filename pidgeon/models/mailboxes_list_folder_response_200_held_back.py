from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MailboxesListFolderResponse200HeldBack")


@_attrs_define
class MailboxesListFolderResponse200HeldBack:
    """On `inbox` only. Spam is never in the inbox, so an inbox that looks empty may not be: `spam` counts the unread
    messages filed there.

        Attributes:
            spam (int): Unread messages filed as spam.
            how_to_include (None | str): What to do about them, in a sentence. Null when there are none.
    """

    spam: int
    how_to_include: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        spam = self.spam

        how_to_include: None | str
        how_to_include = self.how_to_include

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "spam": spam,
                "how_to_include": how_to_include,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        spam = d.pop("spam")

        def _parse_how_to_include(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        how_to_include = _parse_how_to_include(d.pop("how_to_include"))

        mailboxes_list_folder_response_200_held_back = cls(
            spam=spam,
            how_to_include=how_to_include,
        )

        mailboxes_list_folder_response_200_held_back.additional_properties = d
        return mailboxes_list_folder_response_200_held_back

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
