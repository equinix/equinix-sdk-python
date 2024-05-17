# coding: utf-8

"""
    Metal API

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from equinix.services.metalv1.models.href import Href
from typing import Optional, Set
from typing_extensions import Self

class BgpSession(BaseModel):
    """
    BgpSession
    """ # noqa: E501
    address_family: StrictStr
    created_at: Optional[datetime] = None
    default_route: Optional[StrictBool] = None
    device: Optional[Href] = None
    href: Optional[StrictStr] = None
    id: Optional[StrictStr] = None
    learned_routes: Optional[List[StrictStr]] = None
    status: Optional[StrictStr] = Field(default=None, description=" The status of the BGP Session. Multiple status values may be reported when the device is connected to multiple switches, one value per switch. Each status will start with \"unknown\" and progress to \"up\" or \"down\" depending on the connected device. Subsequent \"unknown\" values indicate a problem acquiring status from the switch. ")
    updated_at: Optional[datetime] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["address_family", "created_at", "default_route", "device", "href", "id", "learned_routes", "status", "updated_at"]

    @field_validator('address_family')
    def address_family_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['ipv4', 'ipv6']):
            raise ValueError("must be one of enum values ('ipv4', 'ipv6')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of BgpSession from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of device
        if self.device:
            _dict['device'] = self.device.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BgpSession from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "address_family": obj.get("address_family"),
            "created_at": obj.get("created_at"),
            "default_route": obj.get("default_route"),
            "device": Href.from_dict(obj["device"]) if obj.get("device") is not None else None,
            "href": obj.get("href"),
            "id": obj.get("id"),
            "learned_routes": obj.get("learned_routes"),
            "status": obj.get("status"),
            "updated_at": obj.get("updated_at")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


