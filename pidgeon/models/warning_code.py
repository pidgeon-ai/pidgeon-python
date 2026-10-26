from enum import StrEnum


class WarningCode(StrEnum):
    IMPLICIT_SCOPE = "implicit_scope"

    def __str__(self) -> str:
        return str(self.value)
