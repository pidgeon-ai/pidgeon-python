from enum import StrEnum


class AttachmentTextFormat(StrEnum):
    DOCX = "docx"
    PDF = "pdf"
    TEXT = "text"
    XLSX = "xlsx"

    def __str__(self) -> str:
        return str(self.value)
