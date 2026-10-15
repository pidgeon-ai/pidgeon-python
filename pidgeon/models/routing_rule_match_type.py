from enum import StrEnum


class RoutingRuleMatchType(StrEnum):
    ADDRESS = "address"
    CATCH_ALL = "catch_all"
    PATTERN = "pattern"

    def __str__(self) -> str:
        return str(self.value)
