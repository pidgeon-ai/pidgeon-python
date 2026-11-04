from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="LogMonitorsCreateBody")


@_attrs_define
class LogMonitorsCreateBody:
    """
    Attributes:
        term (str): A name or a domain to watch for, such as `meta` or `acme.com`. Look-alikes match too.
        email (bool | Unset): Email the workspace’s owners on a match, beside the `card_log.matched` event. Default:
            True.
    """

    term: str
    email: bool | Unset = True

    def to_dict(self) -> dict[str, Any]:
        term = self.term

        email = self.email

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "term": term,
            }
        )
        if email is not UNSET:
            field_dict["email"] = email

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        term = d.pop("term")

        email = d.pop("email", UNSET)

        log_monitors_create_body = cls(
            term=term,
            email=email,
        )

        return log_monitors_create_body
