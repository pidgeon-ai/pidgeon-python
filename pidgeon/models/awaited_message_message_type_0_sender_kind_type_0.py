from enum import StrEnum


class AwaitedMessageMessageType0SenderKindType0(StrEnum):
    AGENT = "agent"
    PERSON = "person"
    SERVICE = "service"

    def __str__(self) -> str:
        return str(self.value)
