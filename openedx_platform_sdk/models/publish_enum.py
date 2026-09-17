from enum import Enum


class PublishEnum(str, Enum):
    DISCARD_CHANGES = "discard_changes"
    MAKE_PUBLIC = "make_public"
    REPUBLISH = "republish"

    def __str__(self) -> str:
        return str(self.value)
