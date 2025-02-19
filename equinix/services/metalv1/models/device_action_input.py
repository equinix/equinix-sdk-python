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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class DeviceActionInput(BaseModel):
    """
    DeviceActionInput
    """ # noqa: E501
    deprovision_fast: Optional[StrictBool] = Field(default=None, description="When type is `reinstall`, enabling fast deprovisioning will bypass full disk wiping.")
    force_delete: Optional[StrictBool] = Field(default=None, description="May be required to perform actions under certain conditions")
    href: Optional[StrictStr] = None
    ipxe_script_url: Optional[StrictStr] = Field(default=None, description="When type is `reinstall`, use this `ipxe_script_url` (`operating_system` must be `custom_ipxe`, defaults to the current `ipxe_script_url`)")
    operating_system: Optional[StrictStr] = Field(default=None, description="When type is `reinstall`, use this `operating_system` (defaults to the current `operating system`)")
    preserve_data: Optional[StrictBool] = Field(default=None, description="When type is `reinstall`, preserve the existing data on all disks except the operating-system disk.")
    type: StrictStr = Field(description="Action to perform. See Device.actions for possible actions.")
    __properties: ClassVar[List[str]] = ["deprovision_fast", "force_delete", "href", "ipxe_script_url", "operating_system", "preserve_data", "type"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['power_on', 'power_off', 'reboot', 'rescue', 'reinstall']):
            raise ValueError("must be one of enum values ('power_on', 'power_off', 'reboot', 'rescue', 'reinstall')")
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
        """Create an instance of DeviceActionInput from a JSON string"""
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
        """Create an instance of DeviceActionInput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "deprovision_fast": obj.get("deprovision_fast"),
            "force_delete": obj.get("force_delete"),
            "href": obj.get("href"),
            "ipxe_script_url": obj.get("ipxe_script_url"),
            "operating_system": obj.get("operating_system"),
            "preserve_data": obj.get("preserve_data"),
            "type": obj.get("type")
        })
        return _obj


