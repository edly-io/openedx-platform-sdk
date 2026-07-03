from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.authoring_grading_course_grading_v0_grade_cutoffs import AuthoringGradingCourseGradingV0GradeCutoffs
    from ..models.authoring_grading_grace_period_v0 import AuthoringGradingGracePeriodV0
    from ..models.authoring_grading_graders_v0 import AuthoringGradingGradersV0


T = TypeVar("T", bound="AuthoringGradingCourseGradingV0")


@_attrs_define
class AuthoringGradingCourseGradingV0:
    """Serializer for course grading model data

    Attributes:
        graders (list[AuthoringGradingGradersV0] | None):
        grade_cutoffs (AuthoringGradingCourseGradingV0GradeCutoffs | Unset): Mapping of letter grade to minimum score
            (0.0–1.0). Required by CourseGradingModel.update_from_json — must be included in every PATCH.
        grace_period (AuthoringGradingGracePeriodV0 | None | Unset): Grace period duration. Pass null to clear the grace
            period.
        minimum_grade_credit (float | None | Unset): Minimum passing score for credit eligibility (0.0–1.0).
    """

    graders: list[AuthoringGradingGradersV0] | None
    grade_cutoffs: AuthoringGradingCourseGradingV0GradeCutoffs | Unset = UNSET
    grace_period: AuthoringGradingGracePeriodV0 | None | Unset = UNSET
    minimum_grade_credit: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.authoring_grading_grace_period_v0 import AuthoringGradingGracePeriodV0

        graders: list[dict[str, Any]] | None
        if isinstance(self.graders, list):
            graders = []
            for graders_type_0_item_data in self.graders:
                graders_type_0_item = graders_type_0_item_data.to_dict()
                graders.append(graders_type_0_item)

        else:
            graders = self.graders

        grade_cutoffs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.grade_cutoffs, Unset):
            grade_cutoffs = self.grade_cutoffs.to_dict()

        grace_period: dict[str, Any] | None | Unset
        if isinstance(self.grace_period, Unset):
            grace_period = UNSET
        elif isinstance(self.grace_period, AuthoringGradingGracePeriodV0):
            grace_period = self.grace_period.to_dict()
        else:
            grace_period = self.grace_period

        minimum_grade_credit: float | None | Unset
        if isinstance(self.minimum_grade_credit, Unset):
            minimum_grade_credit = UNSET
        else:
            minimum_grade_credit = self.minimum_grade_credit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "graders": graders,
            }
        )
        if grade_cutoffs is not UNSET:
            field_dict["grade_cutoffs"] = grade_cutoffs
        if grace_period is not UNSET:
            field_dict["grace_period"] = grace_period
        if minimum_grade_credit is not UNSET:
            field_dict["minimum_grade_credit"] = minimum_grade_credit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.authoring_grading_course_grading_v0_grade_cutoffs import (
            AuthoringGradingCourseGradingV0GradeCutoffs,
        )
        from ..models.authoring_grading_grace_period_v0 import AuthoringGradingGracePeriodV0
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

        _grade_cutoffs = d.pop("grade_cutoffs", UNSET)
        grade_cutoffs: AuthoringGradingCourseGradingV0GradeCutoffs | Unset
        if isinstance(_grade_cutoffs, Unset):
            grade_cutoffs = UNSET
        else:
            grade_cutoffs = AuthoringGradingCourseGradingV0GradeCutoffs.from_dict(_grade_cutoffs)

        def _parse_grace_period(data: object) -> AuthoringGradingGracePeriodV0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                grace_period_type_1 = AuthoringGradingGracePeriodV0.from_dict(data)

                return grace_period_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AuthoringGradingGracePeriodV0 | None | Unset, data)

        grace_period = _parse_grace_period(d.pop("grace_period", UNSET))

        def _parse_minimum_grade_credit(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        minimum_grade_credit = _parse_minimum_grade_credit(d.pop("minimum_grade_credit", UNSET))

        authoring_grading_course_grading_v0 = cls(
            graders=graders,
            grade_cutoffs=grade_cutoffs,
            grace_period=grace_period,
            minimum_grade_credit=minimum_grade_credit,
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
