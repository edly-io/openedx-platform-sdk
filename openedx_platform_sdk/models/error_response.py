from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error_response_errors import ErrorResponseErrors


T = TypeVar("T", bound="ErrorResponse")


@_attrs_define
class ErrorResponse:
    """Plain-DRF serializer describing the ADR 0029 error envelope.

    Intended for OpenAPI response declarations so error responses are
    documented with their real shape, e.g. with drf-spectacular::

        @extend_schema(responses={
            200: MyResourceSerializer,
            404: ErrorResponseSerializer,
        })

    It is a documentation serializer: nothing deserializes through it, so it
    implements no ``create``/``update``.

        Attributes:
            type_ (str): Error-type URI (https://docs.openedx.org/errors/<slug>).
            title (str): Human-readable error title.
            status (int): HTTP status code, repeated from the response.
            detail (str): Flattened human-readable error message.
            instance (str | Unset): Path of the request that produced the error.
            user_message (str | Unset): End-user-facing message, when the raising code supplied one.
            errors (ErrorResponseErrors | Unset): Per-field validation errors (validation errors only).
    """

    type_: str
    title: str
    status: int
    detail: str
    instance: str | Unset = UNSET
    user_message: str | Unset = UNSET
    errors: ErrorResponseErrors | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        title = self.title

        status = self.status

        detail = self.detail

        instance = self.instance

        user_message = self.user_message

        errors: dict[str, Any] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = self.errors.to_dict() if not isinstance(self.errors, dict) else dict(self.errors)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "title": title,
                "status": status,
                "detail": detail,
            }
        )
        if instance is not UNSET:
            field_dict["instance"] = instance
        if user_message is not UNSET:
            field_dict["user_message"] = user_message
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.error_response_errors import ErrorResponseErrors

        d = dict(src_dict)
        type_ = d.pop("type")

        title = d.pop("title")

        status = d.pop("status")

        detail = d.pop("detail")

        instance = d.pop("instance", UNSET)

        user_message = d.pop("user_message", UNSET)

        _errors = d.pop("errors", UNSET)
        errors: ErrorResponseErrors | Unset
        if isinstance(_errors, Unset):
            errors = UNSET
        else:
            errors = ErrorResponseErrors.from_dict(_errors)

        error_response = cls(
            type_=type_,
            title=title,
            status=status,
            detail=detail,
            instance=instance,
            user_message=user_message,
            errors=errors,
        )

        error_response.additional_properties = d
        return error_response

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
