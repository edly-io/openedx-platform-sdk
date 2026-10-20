from enum import Enum


class V1XblocksRetrieveView(str, Enum):
    MINIMAL = "minimal"

    def __str__(self) -> str:
        return str(self.value)
