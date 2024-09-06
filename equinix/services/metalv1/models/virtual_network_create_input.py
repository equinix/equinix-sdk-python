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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class VirtualNetworkCreateInput(BaseModel):
    """
    VirtualNetworkCreateInput
    """ # noqa: E501
    description: Optional[StrictStr] = None
    facility: Optional[StrictStr] = Field(default=None, description="The UUID (or facility code) for the Facility in which to create this Virtual network.")
    href: Optional[StrictStr] = None
    metro: Optional[StrictStr] = Field(default=None, description="The UUID (or metro code) for the Metro in which to create this Virtual Network.")
    tags: Optional[List[StrictStr]] = None
    vxlan: Optional[StrictInt] = Field(default=None, description="VLAN ID between 2-3999. Must be unique for the project within the Metro in which this Virtual Network is being created. If no value is specified, the next-available VLAN ID in the range 1000-1999 will be automatically selected.")
    __properties: ClassVar[List[str]] = ["description", "facility", "href", "metro", "tags", "vxlan"]

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
        """Create an instance of VirtualNetworkCreateInput from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of VirtualNetworkCreateInput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in VirtualNetworkCreateInput) in the input: " + _key)

        _obj = cls.model_validate({
            "description": obj.get("description"),
            "facility": obj.get("facility"),
            "href": obj.get("href"),
            "metro": obj.get("metro"),
            "tags": obj.get("tags"),
            "vxlan": obj.get("vxlan")
        })
        return _obj


