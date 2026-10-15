from enum import StrEnum


class RoutingRuleDestinationType(StrEnum):
    IDENTITY = "identity"
    WEBHOOK = "webhook"

    def __str__(self) -> str:
        return str(self.value)
