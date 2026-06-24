from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.authoring_grading_graders_v0 import AuthoringGradingGradersV0


T = TypeVar("T", bound="AuthoringGradingCourseGradingV0")


@_attrs_define
class AuthoringGradingCourseGradingV0:
    """Serializer for course grading model data

    Attributes:
        graders (list[AuthoringGradingGradersV0] | None):
    """

    graders: list[AuthoringGradingGradersV0] | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        graders: list[dict[str, Any]] | None
        if isinstance(self.graders, list):
            graders = []
            for graders_type_0_item_data in self.graders:
                graders_type_0_item = graders_type_0_item_data.to_dict()
                graders.append(graders_type_0_item)

        else:
            graders = self.graders

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "graders": graders,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.authoring_grading_graders_v0 import AuthoringGradingGradersV0

        d = dict(src_dict)

        def _parse_graders(data: object) -> list[AuthoringGradingGradersV0] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                graders_type_0 = []
                _graders_type_0 = data
                for graders_type_0_item_data in _graders_type_0:
                    graders_type_0_item = AuthoringGradingGradersV0.from_dict(graders_type_0_item_data)

                    graders_type_0.append(graders_type_0_item)

                return graders_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AuthoringGradingGradersV0] | None, data)

        graders = _parse_graders(d.pop("graders"))

        authoring_grading_course_grading_v0 = cls(
            graders=graders,
        )

        authoring_grading_course_grading_v0.additional_properties = d
        return authoring_grading_course_grading_v0

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
