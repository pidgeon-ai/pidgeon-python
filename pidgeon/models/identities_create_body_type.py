from enum import StrEnum


class IdentitiesCreateBodyType(StrEnum):
    AGENT = "agent"
    APPLICATION = "application"
    HUMAN = "human"
    TEAM = "team"
    WORKFLOW = "workflow"

    def __str__(self) -> str:
        return str(self.value)
