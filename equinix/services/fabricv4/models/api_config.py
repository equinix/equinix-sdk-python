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
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class ApiConfig(BaseModel):
    """
    Configuration for API based Integration for Service Profile
    """ # noqa: E501
    api_available: Optional[StrictBool] = Field(default=False, description="Setting indicating whether the API is available (true) or not (false).", alias="apiAvailable")
    integration_id: Optional[StrictStr] = Field(default=None, alias="integrationId")
    equinix_managed_port: Optional[StrictBool] = Field(default=False, description="Setting indicating that the port is managed by Equinix (true) or not (false).", alias="equinixManagedPort")
    equinix_managed_vlan: Optional[StrictBool] = Field(default=False, description="Setting indicating that the VLAN is managed by Equinix (true) or not (false).", alias="equinixManagedVlan")
    allow_over_subscription: Optional[StrictBool] = Field(default=False, description="Setting showing that oversubscription support is available (true) or not (false). The default is false. Oversubscription is the sale of more than the available network bandwidth. This practice is common and legitimate. After all, many customers use less bandwidth than they've purchased. And network users don't consume bandwidth all at the same time. The leftover bandwidth can be sold to other customers. When demand surges, operational and engineering resources can be shifted to accommodate the load. ", alias="allowOverSubscription")
    over_subscription_limit: Optional[Annotated[int, Field(le=20, strict=True, ge=1)]] = Field(default=1, description="A cap on oversubscription.", alias="overSubscriptionLimit")
    bandwidth_from_api: Optional[StrictBool] = Field(default=False, alias="bandwidthFromApi")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["apiAvailable", "integrationId", "equinixManagedPort", "equinixManagedVlan", "allowOverSubscription", "overSubscriptionLimit", "bandwidthFromApi"]

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
        """Create an instance of ApiConfig from a JSON string"""
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
        """Create an instance of ApiConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "apiAvailable": obj.get("apiAvailable") if obj.get("apiAvailable") is not None else False,
            "integrationId": obj.get("integrationId"),
            "equinixManagedPort": obj.get("equinixManagedPort") if obj.get("equinixManagedPort") is not None else False,
            "equinixManagedVlan": obj.get("equinixManagedVlan") if obj.get("equinixManagedVlan") is not None else False,
            "allowOverSubscription": obj.get("allowOverSubscription") if obj.get("allowOverSubscription") is not None else False,
            "overSubscriptionLimit": obj.get("overSubscriptionLimit") if obj.get("overSubscriptionLimit") is not None else 1,
            "bandwidthFromApi": obj.get("bandwidthFromApi") if obj.get("bandwidthFromApi") is not None else False
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


