from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthoringGradingGracePeriodV0")


@_attrs_define
class AuthoringGradingGracePeriodV0:
    """Serializer for grace period (hours / minutes / seconds).

    Attributes:
        hours (int | Unset):  Default: 0.
        minutes (int | Unset):  Default: 0.
        seconds (int | Unset):  Default: 0.
    """

    hours: int | Unset = 0
    minutes: int | Unset = 0
    seconds: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hours = self.hours

        minutes = self.minutes

        seconds = self.seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hours is not UNSET:
            field_dict["hours"] = hours
        if minutes is not UNSET:
            field_dict["minutes"] = minutes
        if seconds is not UNSET:
            field_dict["seconds"] = seconds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        hours = d.pop("hours", UNSET)

        minutes = d.pop("minutes", UNSET)

        seconds = d.pop("seconds", UNSET)

        authoring_grading_grace_period_v0 = cls(
            hours=hours,
            minutes=minutes,
            seconds=seconds,
        )

        authoring_grading_grace_period_v0.additional_properties = d
        return authoring_grading_grace_period_v0

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
