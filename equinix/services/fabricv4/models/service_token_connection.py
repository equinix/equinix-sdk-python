# coding: utf-8

"""
    Equinix Fabric API v4

    Equinix Fabric is an advanced software-defined interconnection solution that enables you to directly, securely and dynamically connect to distributed infrastructure and digital ecosystems on platform Equinix via a single port, Customers can use Fabric to connect to: </br> 1. Cloud Service Providers - Clouds, network and other service providers.  </br> 2. Enterprises - Other Equinix customers, vendors and partners.  </br> 3. Myself - Another customer instance deployed at Equinix. </br> </br> <b>Integrations (SDKs, Tools) links:</b> </br> <a href=\"https://deploy.equinix.com/labs/fabric-java\\\">Fabric Java SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-go\\\">Fabric Go SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-python\\\">Fabric Python SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-provider-equinix\\\">Equinix Terraform Provider</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-equinix-fabric\\\">Fabric Terraform Modules</a> </br> <a href=\"https://deploy.equinix.com/labs/pulumi-provider-equinix/\">Equinix Pulumi Provider</a> </br>

    The version of the OpenAPI document: 4.20
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
from equinix.services.fabricv4.models.service_token_connection_type import ServiceTokenConnectionType
from equinix.services.fabricv4.models.service_token_side import ServiceTokenSide
from typing import Optional, Set
from typing_extensions import Self

class ServiceTokenConnection(BaseModel):
    """
    Service Token Connection Type Information
    """ # noqa: E501
    type: Optional[ServiceTokenConnectionType] = None
    href: Optional[StrictStr] = Field(default=None, description="An absolute URL that is the subject of the link's context.")
    uuid: Optional[StrictStr] = Field(default=None, description="Equinix-assigned connection identifier")
    allow_remote_connection: Optional[StrictBool] = Field(default=False, description="Authorization to connect remotely", alias="allowRemoteConnection")
    allow_custom_bandwidth: Optional[StrictBool] = Field(default=False, description="Allow custom bandwidth value", alias="allowCustomBandwidth")
    bandwidth_limit: Optional[Annotated[int, Field(le=100000, strict=True, ge=0)]] = Field(default=None, description="Connection bandwidth limit in Mbps", alias="bandwidthLimit")
    supported_bandwidths: Optional[List[StrictInt]] = Field(default=None, description="List of permitted bandwidths.", alias="supportedBandwidths")
    a_side: Optional[ServiceTokenSide] = Field(default=None, alias="aSide")
    z_side: Optional[ServiceTokenSide] = Field(default=None, alias="zSide")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["type", "href", "uuid", "allowRemoteConnection", "allowCustomBandwidth", "bandwidthLimit", "supportedBandwidths", "aSide", "zSide"]

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
        """Create an instance of ServiceTokenConnection from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of a_side
        if self.a_side:
            _dict['aSide'] = self.a_side.to_dict()
        # override the default output from pydantic by calling `to_dict()` of z_side
        if self.z_side:
            _dict['zSide'] = self.z_side.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ServiceTokenConnection from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "href": obj.get("href"),
            "uuid": obj.get("uuid"),
            "allowRemoteConnection": obj.get("allowRemoteConnection") if obj.get("allowRemoteConnection") is not None else False,
            "allowCustomBandwidth": obj.get("allowCustomBandwidth") if obj.get("allowCustomBandwidth") is not None else False,
            "bandwidthLimit": obj.get("bandwidthLimit"),
            "supportedBandwidths": obj.get("supportedBandwidths"),
            "aSide": ServiceTokenSide.from_dict(obj["aSide"]) if obj.get("aSide") is not None else None,
            "zSide": ServiceTokenSide.from_dict(obj["zSide"]) if obj.get("zSide") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


