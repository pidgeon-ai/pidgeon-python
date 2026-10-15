from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.setup_link_reason_type_0 import SetupLinkReasonType0

T = TypeVar("T", bound="SetupLink")


@_attrs_define
class SetupLink:
    """
    Attributes:
        supported (bool):
        provider_name (None | str): The DNS provider’s own name, for a button label. Null when it is not known.
        url (None | str): The signed Domain Connect apply URL, at the domain’s DNS provider. Open it in a browser: the
            owner signs in, reviews the records and approves. Null when unsupported.
        width (float | None): The popup size the provider asks for, when it states one.
        height (float | None):
        reason (None | SetupLinkReasonType0): `provider` — that zone’s DNS provider does not support Domain Connect,
            which is the common case. `unconfigured` — it does, and this deployment is not registered as a service provider,
            which is ours to fix. Null when `supported` is true.
    """

    supported: bool
    provider_name: None | str
    url: None | str
    width: float | None
    height: float | None
    reason: None | SetupLinkReasonType0

    def to_dict(self) -> dict[str, Any]:
        supported = self.supported

        provider_name: None | str
        provider_name = self.provider_name

        url: None | str
        url = self.url

        width: float | None
        width = self.width

        height: float | None
        height = self.height

        reason: None | str
        if isinstance(self.reason, SetupLinkReasonType0):
            reason = self.reason.value
        else:
            reason = self.reason

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "supported": supported,
                "provider_name": provider_name,
                "url": url,
                "width": width,
                "height": height,
                "reason": reason,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        supported = d.pop("supported")

        def _parse_provider_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        provider_name = _parse_provider_name(d.pop("provider_name"))

        def _parse_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        url = _parse_url(d.pop("url"))

        def _parse_width(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        width = _parse_width(d.pop("width"))

        def _parse_height(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        height = _parse_height(d.pop("height"))

        def _parse_reason(data: object) -> None | SetupLinkReasonType0:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reason_type_0 = SetupLinkReasonType0(data)

                return reason_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SetupLinkReasonType0, data)

        reason = _parse_reason(d.pop("reason"))

        setup_link = cls(
            supported=supported,
            provider_name=provider_name,
            url=url,
            width=width,
            height=height,
            reason=reason,
        )

        return setup_link
