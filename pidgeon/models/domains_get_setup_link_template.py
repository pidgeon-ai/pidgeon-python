from enum import StrEnum


class DomainsGetSetupLinkTemplate(StrEnum):
    MAIL = "mail"
    MX = "mx"

    def __str__(self) -> str:
        return str(self.value)
