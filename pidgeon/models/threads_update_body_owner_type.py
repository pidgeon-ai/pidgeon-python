from enum import StrEnum


class ThreadsUpdateBodyOwnerType(StrEnum):
    AGENT = "agent"
    AUTOMATION = "automation"
    HUMAN = "human"

    def __str__(self) -> str:
        return str(self.value)
