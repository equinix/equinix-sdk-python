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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class VrfFabricVcCreateInput(BaseModel):
    """
    VrfFabricVcCreateInput
    """ # noqa: E501
    contact_email: Optional[StrictStr] = Field(default=None, description="The preferred email used for communication and notifications about the Equinix Fabric interconnection. Optional and defaults to the primary user email address when using a User API key or the organization owner email address when using a Project API key.")
    description: Optional[StrictStr] = None
    facility_id: Optional[StrictStr] = None
    href: Optional[StrictStr] = None
    metro: StrictStr = Field(description="A Metro ID or code. When creating Fabric VCs (Metal Billed), this is where interconnection will be originating from, as we pre-authorize the use of one of our shared ports as the origin of the interconnection using A-Side service tokens. We only allow local connections for Fabric VCs (Metal Billed), so the destination location must be the same as the origin. For Fabric VCs (Fabric Billed), or shared connections, this will be the destination of the interconnection. We allow remote connections for Fabric VCs (Fabric Billed), so the origin of the interconnection can be a different metro set here.")
    name: StrictStr
    project: Optional[StrictStr] = None
    redundancy: StrictStr = Field(description="Either 'primary' or 'redundant'.")
    service_token_type: StrictStr = Field(description="Either 'a_side' or 'z_side'. Setting this field to 'a_side' will create an interconnection with Fabric VCs (Metal Billed). Setting this field to 'z_side' will create an interconnection with Fabric VCs (Fabric Billed). This is required when the 'type' is 'shared', but this is not applicable when the 'type' is 'dedicated'. This parameter is included in the specification as a developer preview and is generally unavailable. Please contact our Support team for more details.")
    speed: Optional[StrictStr] = Field(default=None, description="A interconnection speed, in bps, mbps, or gbps. For Fabric VCs, this represents the maximum speed of the interconnection. For Fabric VCs (Metal Billed), this can only be one of the following:  ''50mbps'', ''200mbps'', ''500mbps'', ''1gbps'', ''2gbps'', ''5gbps'' or ''10gbps'', and is required for creation. For Fabric VCs (Fabric Billed), this field will always default to ''10gbps'' even if it is not provided. For example, ''500000000'', ''50m'', or' ''500mbps'' will all work as valid inputs.")
    tags: Optional[List[StrictStr]] = None
    type: StrictStr = Field(description="When requesting for a Fabric VC, the value of this field should be 'shared'.")
    vrfs: List[StrictStr] = Field(description="This field holds a list of VRF UUIDs that will be set automatically on the virtual circuits of Fabric VCs on creation, and can hold up to two UUIDs. Two UUIDs are required when requesting redundant Fabric VCs. The first UUID will be set on the primary virtual circuit, while the second UUID will be set on the secondary. The two UUIDs can be the same if both the primary and secondary virtual circuits will be in the same VRF. This parameter is included in the specification as a developer preview and is generally unavailable. Please contact our Support team for more details.")
    __properties: ClassVar[List[str]] = ["contact_email", "description", "facility_id", "href", "metro", "name", "project", "redundancy", "service_token_type", "speed", "tags", "type", "vrfs"]

    @field_validator('service_token_type')
    def service_token_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['a_side', 'z_side']):
            raise ValueError("must be one of enum values ('a_side', 'z_side')")
        return value

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['shared']):
            raise ValueError("must be one of enum values ('shared')")
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
        """Create an instance of VrfFabricVcCreateInput from a JSON string"""
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
        """Create an instance of VrfFabricVcCreateInput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "contact_email": obj.get("contact_email"),
            "description": obj.get("description"),
            "facility_id": obj.get("facility_id"),
            "href": obj.get("href"),
            "metro": obj.get("metro"),
            "name": obj.get("name"),
            "project": obj.get("project"),
            "redundancy": obj.get("redundancy"),
            "service_token_type": obj.get("service_token_type"),
            "speed": obj.get("speed"),
            "tags": obj.get("tags"),
            "type": obj.get("type"),
            "vrfs": obj.get("vrfs")
        })
        return _obj


