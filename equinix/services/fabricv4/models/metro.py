# coding: utf-8

"""
    Equinix Fabric API v4

    Equinix Fabric is an advanced software-defined interconnection solution that enables you to directly, securely and dynamically connect to distributed infrastructure and digital ecosystems on platform Equinix via a single port, Customers can use Fabric to connect to: </br> 1. Cloud Service Providers - Clouds, network and other service providers.  </br> 2. Enterprises - Other Equinix customers, vendors and partners.  </br> 3. Myself - Another customer instance deployed at Equinix. </br> </br> <b>Integrations (SDKs, Tools) links:</b> </br> <a href=\"https://deploy.equinix.com/labs/fabric-java\\\">Fabric Java SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-go\\\">Fabric Go SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-provider-equinix\\\">Equinix Terraform Provider</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-equinix-fabric\\\">Fabric Terraform Modules</a> </br> <a href=\"https://deploy.equinix.com/labs/pulumi-provider-equinix/\">Equinix Pulumi Provider</a> </br>

    The version of the OpenAPI document: 4.15
    Contact: api-support@equinix.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from equinix.services.fabricv4.models.connected_metro import ConnectedMetro
from equinix.services.fabricv4.models.geo_coordinates import GeoCoordinates
from equinix.services.fabricv4.models.geo_scope_type import GeoScopeType
from typing import Optional, Set
from typing_extensions import Self

class Metro(BaseModel):
    """
    GET Metros retrieves all Equinix? Fabric? metros, as well as latency data for each location.This performance data helps network planning engineers and administrators make strategic decisions about port locations and traffic routes.
    """ # noqa: E501
    href: Optional[StrictStr] = Field(default=None, description="The Canonical URL at which the resource resides.")
    type: Optional[StrictStr] = Field(default=None, description="Indicator of a Fabric Metro")
    code: Optional[StrictStr] = Field(default=None, description="Code Assigned to an Equinix IBX data center in a specified metropolitan area.")
    region: Optional[StrictStr] = Field(default=None, description="Board geographic area in which the data center is located")
    name: Optional[StrictStr] = Field(default=None, description="Name of the region in which the data center is located.")
    equinix_asn: Optional[StrictInt] = Field(default=None, description="Autonomous system number (ASN) for a specified Fabric metro. The ASN is a unique identifier that carries the network routing protocol and exchanges that data with other internal systems via border gateway protocol.", alias="equinixAsn")
    local_vc_bandwidth_max: Optional[StrictInt] = Field(default=None, description="This field holds Max Connection speed with in the metro", alias="localVCBandwidthMax")
    geo_coordinates: Optional[GeoCoordinates] = Field(default=None, alias="geoCoordinates")
    connected_metros: Optional[List[ConnectedMetro]] = Field(default=None, alias="connectedMetros")
    geo_scopes: Optional[List[GeoScopeType]] = Field(default=None, description="List of supported geographic boundaries of a Fabric Metro.", alias="geoScopes")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["href", "type", "code", "region", "name", "equinixAsn", "localVCBandwidthMax", "geoCoordinates", "connectedMetros", "geoScopes"]

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
        """Create an instance of Metro from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of geo_coordinates
        if self.geo_coordinates:
            _dict['geoCoordinates'] = self.geo_coordinates.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in connected_metros (list)
        _items = []
        if self.connected_metros:
            for _item in self.connected_metros:
                if _item:
                    _items.append(_item.to_dict())
            _dict['connectedMetros'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Metro from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "href": obj.get("href"),
            "type": obj.get("type"),
            "code": obj.get("code"),
            "region": obj.get("region"),
            "name": obj.get("name"),
            "equinixAsn": obj.get("equinixAsn"),
            "localVCBandwidthMax": obj.get("localVCBandwidthMax"),
            "geoCoordinates": GeoCoordinates.from_dict(obj["geoCoordinates"]) if obj.get("geoCoordinates") is not None else None,
            "connectedMetros": [ConnectedMetro.from_dict(_item) for _item in obj["connectedMetros"]] if obj.get("connectedMetros") is not None else None,
            "geoScopes": obj.get("geoScopes")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


