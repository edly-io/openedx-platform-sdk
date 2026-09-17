from enum import Enum


class V1XblockRetrieveView(str, Enum):
    MINIMAL = "minimal"

    def __str__(self) -> str:
        return str(self.value)
