# coding: utf-8

"""
    Equinix Fabric API v4

    Equinix Fabric is an advanced software-defined interconnection solution that enables you to directly, securely and dynamically connect to distributed infrastructure and digital ecosystems on platform Equinix via a single port, Customers can use Fabric to connect to: </br> 1. Cloud Service Providers - Clouds, network and other service providers.  </br> 2. Enterprises - Other Equinix customers, vendors and partners.  </br> 3. Myself - Another customer instance deployed at Equinix. </br> </br> <b>Integrations (SDKs, Tools) links:</b> </br> <a href=\"https://deploy.equinix.com/labs/fabric-java\\\">Fabric Java SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-go\\\">Fabric Go SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-provider-equinix\\\">Equinix Terraform Provider</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-equinix-fabric\\\">Fabric Terraform Modules</a> </br> <a href=\"https://deploy.equinix.com/labs/pulumi-provider-equinix/\">Equinix Pulumi Provider</a> </br>

    The version of the OpenAPI document: 4.14
    Contact: api-support@equinix.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from equinix.services.fabricv4.models.port_settings_package_type import PortSettingsPackageType
from equinix.services.fabricv4.models.port_settings_shared_port_product import PortSettingsSharedPortProduct
from typing import Optional, Set
from typing_extensions import Self

class PortSettings(BaseModel):
    """
    Port configuration settings
    """ # noqa: E501
    product: Optional[StrictStr] = Field(default=None, description="Product name")
    buyout: Optional[StrictBool] = None
    view_port_permission: Optional[StrictBool] = Field(default=None, alias="viewPortPermission")
    place_vc_order_permission: Optional[StrictBool] = Field(default=None, alias="placeVcOrderPermission")
    layer3_enabled: Optional[StrictBool] = Field(default=None, alias="layer3Enabled")
    product_code: Optional[StrictStr] = Field(default=None, alias="productCode")
    shared_port_type: Optional[StrictBool] = Field(default=None, alias="sharedPortType")
    shared_port_product: Optional[PortSettingsSharedPortProduct] = Field(default=None, alias="sharedPortProduct")
    package_type: Optional[PortSettingsPackageType] = Field(default=None, alias="packageType")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["product", "buyout", "viewPortPermission", "placeVcOrderPermission", "layer3Enabled", "productCode", "sharedPortType", "sharedPortProduct", "packageType"]

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
        """Create an instance of PortSettings from a JSON string"""
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
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PortSettings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "product": obj.get("product"),
            "buyout": obj.get("buyout"),
            "viewPortPermission": obj.get("viewPortPermission"),
            "placeVcOrderPermission": obj.get("placeVcOrderPermission"),
            "layer3Enabled": obj.get("layer3Enabled"),
            "productCode": obj.get("productCode"),
            "sharedPortType": obj.get("sharedPortType"),
            "sharedPortProduct": obj.get("sharedPortProduct"),
            "packageType": obj.get("packageType")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


