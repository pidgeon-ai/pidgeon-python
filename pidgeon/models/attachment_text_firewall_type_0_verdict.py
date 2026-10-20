from enum import StrEnum


class AttachmentTextFirewallType0Verdict(StrEnum):
    CLEAN = "clean"
    SUSPICIOUS = "suspicious"

    def __str__(self) -> str:
        return str(self.value)
