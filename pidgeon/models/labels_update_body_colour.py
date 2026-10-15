from enum import StrEnum


class LabelsUpdateBodyColour(StrEnum):
    AMBER = "amber"
    BLUE = "blue"
    GREEN = "green"
    PINK = "pink"
    RED = "red"
    SLATE = "slate"
    TEAL = "teal"
    VIOLET = "violet"

    def __str__(self) -> str:
        return str(self.value)
