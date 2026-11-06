from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.sign_in_approval_app import SignInApprovalApp


T = TypeVar("T", bound="SignInApproval")


@_attrs_define
class SignInApproval:
    """
    Attributes:
        redirect_url (str): The app’s callback, carrying a one-use code. Open it yourself, within a minute, in the
            session that started the sign-in; never hand it to anyone else.
        address (str): The address that signed in.
        app (SignInApprovalApp): The app the code is for. Approve only a sign-in your agent started.
        expires_at (str): When the code stops working.
    """

    redirect_url: str
    address: str
    app: SignInApprovalApp
    expires_at: str

    def to_dict(self) -> dict[str, Any]:
        redirect_url = self.redirect_url

        address = self.address

        app = self.app.to_dict()

        expires_at = self.expires_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "redirect_url": redirect_url,
                "address": address,
                "app": app,
                "expires_at": expires_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sign_in_approval_app import SignInApprovalApp  # noqa: PLC0415

        d = dict(src_dict)
        redirect_url = d.pop("redirect_url")

        address = d.pop("address")

        app = SignInApprovalApp.from_dict(d.pop("app"))

        expires_at = d.pop("expires_at")

        sign_in_approval = cls(
            redirect_url=redirect_url,
            address=address,
            app=app,
            expires_at=expires_at,
        )

        return sign_in_approval
