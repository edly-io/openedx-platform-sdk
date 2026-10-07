from enum import Enum


class ApiEnrollmentV2EnrollmentListView(str, Enum):
    MINIMAL = "minimal"

    def __str__(self) -> str:
        return str(self.value)
