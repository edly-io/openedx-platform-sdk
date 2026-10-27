from enum import Enum


class V3CoursesDetailsRetrieveView(str, Enum):
    MINIMAL = "minimal"

    def __str__(self) -> str:
        return str(self.value)
