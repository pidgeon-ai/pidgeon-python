from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="SignInApprovalApp")


@_attrs_define
class SignInApprovalApp:
    """The app the code is for. Approve only a sign-in your agent started.

    Attributes:
        name (str):
        host (str):
        verified (bool): True when the app is identified by a URL it controls (a metadata document).
    """

    name: str
    host: str
    verified: bool

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        host = self.host

        verified = self.verified

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "host": host,
                "verified": verified,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        host = d.pop("host")

        verified = d.pop("verified")

        sign_in_approval_app = cls(
            name=name,
            host=host,
            verified=verified,
        )

        return sign_in_approval_app
