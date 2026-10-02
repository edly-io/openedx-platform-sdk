from enum import Enum


class V3CourseDetailsRetrieveView(str, Enum):
    MINIMAL = "minimal"

    def __str__(self) -> str:
        return str(self.value)
