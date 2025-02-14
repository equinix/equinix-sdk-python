# coding: utf-8

"""
    Equinix Fabric API v4

    Equinix Fabric is an advanced software-defined interconnection solution that enables you to directly, securely and dynamically connect to distributed infrastructure and digital ecosystems on platform Equinix via a single port, Customers can use Fabric to connect to: </br> 1. Cloud Service Providers - Clouds, network and other service providers.  </br> 2. Enterprises - Other Equinix customers, vendors and partners.  </br> 3. Myself - Another customer instance deployed at Equinix. </br> </br> <b>Integrations (SDKs, Tools) links:</b> </br> <a href=\"https://deploy.equinix.com/labs/fabric-java\\\">Fabric Java SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-go\\\">Fabric Go SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-python\\\">Fabric Python SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-provider-equinix\\\">Equinix Terraform Provider</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-equinix-fabric\\\">Fabric Terraform Modules</a> </br> <a href=\"https://deploy.equinix.com/labs/pulumi-provider-equinix/\">Equinix Pulumi Provider</a> </br>

    Generated by OpenAPI Generator (https://openapi-generator.tech)
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from equinix.services.fabricv4.models.cloud_router_package_type import CloudRouterPackageType
from equinix.services.fabricv4.models.code import Code
from equinix.services.fabricv4.models.package_change_log import PackageChangeLog
from typing import Optional, Set
from typing_extensions import Self

class CloudRouterPackage(BaseModel):
    """
    Fabric Cloud Router Package
    """ # noqa: E501
    href: Optional[StrictStr] = Field(default=None, description="Cloud Router package URI")
    type: Optional[CloudRouterPackageType] = None
    code: Optional[Code] = None
    description: Optional[StrictStr] = Field(default=None, description="Fabric Cloud Router Package description")
    total_ipv4_routes_max: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="Cloud Router package BGP IPv4 routes limit", alias="totalIPv4RoutesMax")
    total_ipv6_routes_max: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="Cloud Router package BGP IPv6 routes limit", alias="totalIPv6RoutesMax")
    route_filter_supported: Optional[StrictBool] = Field(default=None, description="CloudRouter package route filter support", alias="routeFilterSupported")
    vc_count_max: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="CloudRouter package Max Connection limit", alias="vcCountMax")
    cr_count_max: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="CloudRouter package Max CloudRouter limit", alias="crCountMax")
    vc_bandwidth_max: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="CloudRouter package Max Bandwidth limit", alias="vcBandwidthMax")
    change_log: Optional[PackageChangeLog] = Field(default=None, alias="changeLog")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["href", "type", "code", "description", "totalIPv4RoutesMax", "totalIPv6RoutesMax", "routeFilterSupported", "vcCountMax", "crCountMax", "vcBandwidthMax", "changeLog"]

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
        """Create an instance of CloudRouterPackage from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "href",
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of change_log
        if self.change_log:
            _dict['changeLog'] = self.change_log.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CloudRouterPackage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "href": obj.get("href"),
            "type": obj.get("type"),
            "code": obj.get("code"),
            "description": obj.get("description"),
            "totalIPv4RoutesMax": obj.get("totalIPv4RoutesMax"),
            "totalIPv6RoutesMax": obj.get("totalIPv6RoutesMax"),
            "routeFilterSupported": obj.get("routeFilterSupported"),
            "vcCountMax": obj.get("vcCountMax"),
            "crCountMax": obj.get("crCountMax"),
            "vcBandwidthMax": obj.get("vcBandwidthMax"),
            "changeLog": PackageChangeLog.from_dict(obj["changeLog"]) if obj.get("changeLog") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


