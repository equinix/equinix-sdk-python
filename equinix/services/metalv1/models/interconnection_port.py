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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from equinix.services.metalv1.models.href import Href
from typing import Optional, Set
from typing_extensions import Self

class InterconnectionPort(BaseModel):
    """
    InterconnectionPort
    """ # noqa: E501
    href: Optional[StrictStr] = None
    id: Optional[StrictStr] = None
    link_status: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    organization: Optional[Href] = None
    role: Optional[StrictStr] = Field(default=None, description="Either 'primary' or 'secondary'.")
    speed: Optional[StrictInt] = None
    status: Optional[StrictStr] = Field(default=None, description="For both Fabric VCs and Dedicated Ports, this will be 'requested' on creation and 'deleting' on deletion. Once the Fabric VC has found its corresponding Fabric connection, this will turn to 'active'. For Dedicated Ports, once the dedicated port is associated, this will also turn to 'active'. For Fabric VCs, this can turn into an 'expired' state if the service token associated is expired.")
    switch_id: Optional[StrictStr] = Field(default=None, description="A switch 'short ID'")
    virtual_circuits: Optional[List[VirtualCircuit]] = None
    __properties: ClassVar[List[str]] = ["href", "id", "link_status", "name", "organization", "role", "speed", "status", "switch_id", "virtual_circuits"]

    @field_validator('role')
    def role_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['primary', 'secondary']):
            raise ValueError("must be one of enum values ('primary', 'secondary')")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['requested', 'active', 'deleting', 'expired', 'delete_failed']):
            raise ValueError("must be one of enum values ('requested', 'active', 'deleting', 'expired', 'delete_failed')")
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
        """Create an instance of InterconnectionPort from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of organization
        if self.organization:
            _dict['organization'] = self.organization.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in virtual_circuits (list)
        _items = []
        if self.virtual_circuits:
            for _item in self.virtual_circuits:
                if _item:
                    _items.append(_item.to_dict())
            _dict['virtual_circuits'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of InterconnectionPort from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "href": obj.get("href"),
            "id": obj.get("id"),
            "link_status": obj.get("link_status"),
            "name": obj.get("name"),
            "organization": Href.from_dict(obj["organization"]) if obj.get("organization") is not None else None,
            "role": obj.get("role"),
            "speed": obj.get("speed"),
            "status": obj.get("status"),
            "switch_id": obj.get("switch_id"),
            "virtual_circuits": [VirtualCircuit.from_dict(_item) for _item in obj["virtual_circuits"]] if obj.get("virtual_circuits") is not None else None
        })
        return _obj

from equinix.services.metalv1.models.virtual_circuit import VirtualCircuit
# TODO: Rewrite to not use raise_errors
InterconnectionPort.model_rebuild(raise_errors=False)

