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
from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from equinix.services.metalv1.models.href import Href
from typing import Optional, Set
from typing_extensions import Self

class PortVlanAssignment(BaseModel):
    """
    PortVlanAssignment
    """ # noqa: E501
    created_at: Optional[datetime] = None
    href: Optional[StrictStr] = None
    id: Optional[StrictStr] = None
    native: Optional[StrictBool] = None
    port: Optional[Href] = None
    state: Optional[StrictStr] = None
    updated_at: Optional[datetime] = None
    virtual_network: Optional[Href] = None
    vlan: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["created_at", "href", "id", "native", "port", "state", "updated_at", "virtual_network", "vlan"]

    @field_validator('state')
    def state_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['assigned', 'unassigning']):
            raise ValueError("must be one of enum values ('assigned', 'unassigning')")
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
        """Create an instance of PortVlanAssignment from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of port
        if self.port:
            _dict['port'] = self.port.to_dict()
        # override the default output from pydantic by calling `to_dict()` of virtual_network
        if self.virtual_network:
            _dict['virtual_network'] = self.virtual_network.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PortVlanAssignment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "created_at": obj.get("created_at"),
            "href": obj.get("href"),
            "id": obj.get("id"),
            "native": obj.get("native"),
            "port": Href.from_dict(obj["port"]) if obj.get("port") is not None else None,
            "state": obj.get("state"),
            "updated_at": obj.get("updated_at"),
            "virtual_network": Href.from_dict(obj["virtual_network"]) if obj.get("virtual_network") is not None else None,
            "vlan": obj.get("vlan")
        })
        return _obj


