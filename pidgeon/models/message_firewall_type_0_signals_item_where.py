from enum import StrEnum


class MessageFirewallType0SignalsItemWhere(StrEnum):
    FROM = "from"
    HTML = "html"
    QUOTED = "quoted"
    SUBJECT = "subject"
    TEXT = "text"

    def __str__(self) -> str:
        return str(self.value)
