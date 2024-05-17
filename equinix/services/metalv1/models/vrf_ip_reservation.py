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
from equinix.services.metalv1.models.metal_gateway_lite import MetalGatewayLite
from equinix.services.metalv1.models.metro import Metro
from equinix.services.metalv1.models.project import Project
from equinix.services.metalv1.models.vrf import Vrf
from typing import Optional, Set
from typing_extensions import Self

class VrfIpReservation(BaseModel):
    """
    VrfIpReservation
    """ # noqa: E501
    address: Optional[StrictStr] = None
    address_family: Optional[StrictInt] = None
    bill: Optional[StrictBool] = None
    cidr: Optional[StrictInt] = None
    created_at: Optional[datetime] = None
    created_by: Optional[Href] = None
    customdata: Optional[Dict[str, Any]] = None
    details: Optional[StrictStr] = None
    gateway: Optional[StrictStr] = None
    href: Optional[StrictStr] = None
    id: Optional[StrictStr] = None
    manageable: Optional[StrictBool] = None
    management: Optional[StrictBool] = None
    metal_gateway: Optional[MetalGatewayLite] = None
    metro: Optional[Metro] = None
    netmask: Optional[StrictStr] = None
    network: Optional[StrictStr] = None
    project: Optional[Project] = None
    project_lite: Optional[Project] = None
    public: Optional[StrictBool] = None
    state: Optional[StrictStr] = None
    tags: Optional[List[StrictStr]] = None
    type: StrictStr
    vrf: Vrf
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["address", "address_family", "bill", "cidr", "created_at", "created_by", "customdata", "details", "gateway", "href", "id", "manageable", "management", "metal_gateway", "metro", "netmask", "network", "project", "project_lite", "public", "state", "tags", "type", "vrf"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['vrf']):
            raise ValueError("must be one of enum values ('vrf')")
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
        """Create an instance of VrfIpReservation from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of created_by
        if self.created_by:
            _dict['created_by'] = self.created_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of metal_gateway
        if self.metal_gateway:
            _dict['metal_gateway'] = self.metal_gateway.to_dict()
        # override the default output from pydantic by calling `to_dict()` of metro
        if self.metro:
            _dict['metro'] = self.metro.to_dict()
        # override the default output from pydantic by calling `to_dict()` of project
        if self.project:
            _dict['project'] = self.project.to_dict()
        # override the default output from pydantic by calling `to_dict()` of project_lite
        if self.project_lite:
            _dict['project_lite'] = self.project_lite.to_dict()
        # override the default output from pydantic by calling `to_dict()` of vrf
        if self.vrf:
            _dict['vrf'] = self.vrf.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of VrfIpReservation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "address": obj.get("address"),
            "address_family": obj.get("address_family"),
            "bill": obj.get("bill"),
            "cidr": obj.get("cidr"),
            "created_at": obj.get("created_at"),
            "created_by": Href.from_dict(obj["created_by"]) if obj.get("created_by") is not None else None,
            "customdata": obj.get("customdata"),
            "details": obj.get("details"),
            "gateway": obj.get("gateway"),
            "href": obj.get("href"),
            "id": obj.get("id"),
            "manageable": obj.get("manageable"),
            "management": obj.get("management"),
            "metal_gateway": MetalGatewayLite.from_dict(obj["metal_gateway"]) if obj.get("metal_gateway") is not None else None,
            "metro": Metro.from_dict(obj["metro"]) if obj.get("metro") is not None else None,
            "netmask": obj.get("netmask"),
            "network": obj.get("network"),
            "project": Project.from_dict(obj["project"]) if obj.get("project") is not None else None,
            "project_lite": Project.from_dict(obj["project_lite"]) if obj.get("project_lite") is not None else None,
            "public": obj.get("public"),
            "state": obj.get("state"),
            "tags": obj.get("tags"),
            "type": obj.get("type"),
            "vrf": Vrf.from_dict(obj["vrf"]) if obj.get("vrf") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


