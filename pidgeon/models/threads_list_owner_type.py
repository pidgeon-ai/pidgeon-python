from enum import StrEnum


class ThreadsListOwnerType(StrEnum):
    AGENT = "agent"
    AUTOMATION = "automation"
    HUMAN = "human"

    def __str__(self) -> str:
        return str(self.value)
