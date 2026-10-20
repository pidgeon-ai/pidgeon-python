from enum import StrEnum


class AttachmentTextFirewallType0SignalsItemWhere(StrEnum):
    FROM = "from"
    HTML = "html"
    QUOTED = "quoted"
    SUBJECT = "subject"
    TEXT = "text"

    def __str__(self) -> str:
        return str(self.value)
