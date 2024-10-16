# coding: utf-8

"""
    Equinix Fabric API v4

    Equinix Fabric is an advanced software-defined interconnection solution that enables you to directly, securely and dynamically connect to distributed infrastructure and digital ecosystems on platform Equinix via a single port, Customers can use Fabric to connect to: </br> 1. Cloud Service Providers - Clouds, network and other service providers.  </br> 2. Enterprises - Other Equinix customers, vendors and partners.  </br> 3. Myself - Another customer instance deployed at Equinix. </br> </br> <b>Integrations (SDKs, Tools) links:</b> </br> <a href=\"https://deploy.equinix.com/labs/fabric-java\\\">Fabric Java SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-go\\\">Fabric Go SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-python\\\">Fabric Python SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-provider-equinix\\\">Equinix Terraform Provider</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-equinix-fabric\\\">Fabric Terraform Modules</a> </br> <a href=\"https://deploy.equinix.com/labs/pulumi-provider-equinix/\">Equinix Pulumi Provider</a> </br>

    The version of the OpenAPI document: 4.17
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from equinix.services.fabricv4.models.changelog import Changelog
from equinix.services.fabricv4.models.get_time_services_package_by_code_package_code_parameter import GetTimeServicesPackageByCodePackageCodeParameter
from equinix.services.fabricv4.models.precision_time_package_response_type import PrecisionTimePackageResponseType
from typing import Optional, Set
from typing_extensions import Self

class PrecisionTimePackageResponse(BaseModel):
    """
    EPT Service Package Information
    """ # noqa: E501
    href: Optional[StrictStr] = None
    type: PrecisionTimePackageResponseType
    code: GetTimeServicesPackageByCodePackageCodeParameter
    bandwidth: StrictInt = Field(description="Connection bandwidth in Mbps.")
    clients_per_second_max: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="Max. number of clients that can be synchronized per second at a packet rate of 1 per second.", alias="clientsPerSecondMax")
    redundancy_supported: Optional[StrictBool] = Field(default=None, description="Is Redundant virtual connection supported for the package code.", alias="redundancySupported")
    multi_subnet_supported: Optional[StrictBool] = Field(default=None, description="Is Multiple subnet supported for the package code.", alias="multiSubnetSupported")
    accuracy_sla_unit: Optional[StrictStr] = Field(default=None, description="Accuracy SLA unit.", alias="accuracySlaUnit")
    accuracy_sla: Optional[StrictInt] = Field(default=None, description="Accuracy SLA for the package code, -1 value denotes the accuracySla is not published.", alias="accuracySla")
    accuracy_sla_min: Optional[Annotated[int, Field(strict=True, ge=1)]] = Field(default=None, description="Typical minimum Accuracy for the package code.", alias="accuracySlaMin")
    accuracy_sla_max: Optional[Annotated[int, Field(strict=True, ge=1)]] = Field(default=None, description="Typical maximum Accuracy for the package code.", alias="accuracySlaMax")
    changelog: Optional[Changelog] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["href", "type", "code", "bandwidth", "clientsPerSecondMax", "redundancySupported", "multiSubnetSupported", "accuracySlaUnit", "accuracySla", "accuracySlaMin", "accuracySlaMax", "changelog"]

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
        """Create an instance of PrecisionTimePackageResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of changelog
        if self.changelog:
            _dict['changelog'] = self.changelog.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PrecisionTimePackageResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "href": obj.get("href"),
            "type": obj.get("type"),
            "code": obj.get("code"),
            "bandwidth": obj.get("bandwidth"),
            "clientsPerSecondMax": obj.get("clientsPerSecondMax"),
            "redundancySupported": obj.get("redundancySupported"),
            "multiSubnetSupported": obj.get("multiSubnetSupported"),
            "accuracySlaUnit": obj.get("accuracySlaUnit"),
            "accuracySla": obj.get("accuracySla"),
            "accuracySlaMin": obj.get("accuracySlaMin"),
            "accuracySlaMax": obj.get("accuracySlaMax"),
            "changelog": Changelog.from_dict(obj["changelog"]) if obj.get("changelog") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


