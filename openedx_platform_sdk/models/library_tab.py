from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.library_view import LibraryView


T = TypeVar("T", bound="LibraryTab")


@_attrs_define
class LibraryTab:
    """
    Attributes:
        libraries (list[LibraryView] | None | Unset):
    """

    libraries: list[LibraryView] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        libraries: list[dict[str, Any]] | None | Unset
        if isinstance(self.libraries, Unset):
            libraries = UNSET
        elif isinstance(self.libraries, list):
            libraries = []
            for libraries_type_0_item_data in self.libraries:
                libraries_type_0_item = libraries_type_0_item_data.to_dict()
                libraries.append(libraries_type_0_item)

        else:
            libraries = self.libraries

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if libraries is not UNSET:
            field_dict["libraries"] = libraries

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.library_view import LibraryView

        d = dict(src_dict)

        def _parse_libraries(data: object) -> list[LibraryView] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                libraries_type_0 = []
                _libraries_type_0 = data
                for libraries_type_0_item_data in _libraries_type_0:
                    libraries_type_0_item = LibraryView.from_dict(libraries_type_0_item_data)

                    libraries_type_0.append(libraries_type_0_item)

                return libraries_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[LibraryView] | None | Unset, data)

        libraries = _parse_libraries(d.pop("libraries", UNSET))

        library_tab = cls(
            libraries=libraries,
        )

        library_tab.additional_properties = d
        return library_tab

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
