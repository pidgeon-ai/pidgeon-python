from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="AwaitedMessageMessageType0DataType0")


@_attrs_define
class AwaitedMessageMessageType0DataType0:
    """
    Attributes:
        schema (str): A URL naming what `body` is.
        body (Any): The JSON itself, exactly as it was sent.
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

        awaited_message_message_type_0_data_type_0 = cls(
            schema=schema,
            body=body,
        )

        return awaited_message_message_type_0_data_type_0
