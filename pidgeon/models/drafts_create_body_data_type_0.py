from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="DraftsCreateBodyDataType0")


@_attrs_define
class DraftsCreateBodyDataType0:
    """Typed data: structured JSON sent beside the text, for software at the other end to read as fields. Travels as its
    own part; it is never mixed into the text.

        Attributes:
            schema (str): A URL naming what `body` is, such as `https://schema.org/Invoice`.
            body (Any): The JSON itself. Up to 64 KB once serialised.
    """

    schema: str
    body: Any

    def to_dict(self) -> dict[str, Any]:
        schema = self.schema

        body = self.body

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "schema": schema,
                "body": body,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        schema = d.pop("schema")

        body = d.pop("body")

        drafts_create_body_data_type_0 = cls(
            schema=schema,
            body=body,
        )

        return drafts_create_body_data_type_0
