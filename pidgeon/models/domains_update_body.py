from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="DomainsUpdateBody")


@_attrs_define
class DomainsUpdateBody:
    """
    Attributes:
        catch_all_enabled (bool):
    """

    catch_all_enabled: bool

    def to_dict(self) -> dict[str, Any]:
        catch_all_enabled = self.catch_all_enabled

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "catch_all_enabled": catch_all_enabled,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        catch_all_enabled = d.pop("catch_all_enabled")

        domains_update_body = cls(
            catch_all_enabled=catch_all_enabled,
        )

        return domains_update_body
