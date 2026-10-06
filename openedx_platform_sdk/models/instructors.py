from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.instructor_info import InstructorInfo


T = TypeVar("T", bound="Instructors")


@_attrs_define
class Instructors:
    """Serializer for instructors

    Attributes:
        instructors (list[InstructorInfo] | None | Unset):
    """

    instructors: list[InstructorInfo] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instructors: list[dict[str, Any]] | None | Unset
        if isinstance(self.instructors, Unset):
            instructors = UNSET
        elif isinstance(self.instructors, list):
            instructors = []
            for instructors_type_0_item_data in self.instructors:
                instructors_type_0_item = instructors_type_0_item_data.to_dict()
                instructors.append(instructors_type_0_item)

        else:
            instructors = self.instructors

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instructors is not UNSET:
            field_dict["instructors"] = instructors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.instructor_info import InstructorInfo

        d = dict(src_dict)

        def _parse_instructors(data: object) -> list[InstructorInfo] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                instructors_type_0 = []
                _instructors_type_0 = data
                for instructors_type_0_item_data in _instructors_type_0:
                    instructors_type_0_item = InstructorInfo.from_dict(instructors_type_0_item_data)

                    instructors_type_0.append(instructors_type_0_item)

                return instructors_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[InstructorInfo] | None | Unset, data)

        instructors = _parse_instructors(d.pop("instructors", UNSET))

        instructors = cls(
            instructors=instructors,
        )

        instructors.additional_properties = d
        return instructors

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
