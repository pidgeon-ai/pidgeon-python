from enum import StrEnum


class CreatedDomainExistingMailType0Provider(StrEnum):
    FASTMAIL = "fastmail"
    GODADDY = "godaddy"
    GOOGLE = "google"
    ICLOUD = "icloud"
    MICROSOFT = "microsoft"
    OTHER = "other"
    PROTON = "proton"
    ZOHO = "zoho"

    def __str__(self) -> str:
        return str(self.value)
