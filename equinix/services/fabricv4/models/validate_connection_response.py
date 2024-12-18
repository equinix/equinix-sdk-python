# coding: utf-8

"""
    Equinix Fabric API v4

    Equinix Fabric is an advanced software-defined interconnection solution that enables you to directly, securely and dynamically connect to distributed infrastructure and digital ecosystems on platform Equinix via a single port, Customers can use Fabric to connect to: </br> 1. Cloud Service Providers - Clouds, network and other service providers.  </br> 2. Enterprises - Other Equinix customers, vendors and partners.  </br> 3. Myself - Another customer instance deployed at Equinix. </br> </br> <b>Integrations (SDKs, Tools) links:</b> </br> <a href=\"https://deploy.equinix.com/labs/fabric-java\\\">Fabric Java SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-go\\\">Fabric Go SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-python\\\">Fabric Python SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-provider-equinix\\\">Equinix Terraform Provider</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-equinix-fabric\\\">Fabric Terraform Modules</a> </br> <a href=\"https://deploy.equinix.com/labs/pulumi-provider-equinix/\">Equinix Pulumi Provider</a> </br>

    The version of the OpenAPI document: 4.18
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from equinix.services.fabricv4.models.connection_redundancy import ConnectionRedundancy
from equinix.services.fabricv4.models.connection_side import ConnectionSide
from typing import Optional, Set
from typing_extensions import Self

class ValidateConnectionResponse(BaseModel):
    """
    Validate Connection specification
    """ # noqa: E501
    uuid: Optional[StrictStr] = Field(default=None, description="Equinix-assigned connection identifier")
    bandwidth: Optional[Annotated[int, Field(le=50000, strict=True, ge=0)]] = Field(default=None, description="Connection bandwidth in Mbps")
    redundancy: Optional[ConnectionRedundancy] = None
    a_side: Optional[ConnectionSide] = Field(default=None, alias="aSide")
    z_side: Optional[ConnectionSide] = Field(default=None, alias="zSide")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["uuid", "bandwidth", "redundancy", "aSide", "zSide"]

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
        """Create an instance of ValidateConnectionResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of redundancy
        if self.redundancy:
            _dict['redundancy'] = self.redundancy.to_dict()
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
        """Create an instance of ValidateConnectionResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "uuid": obj.get("uuid"),
            "bandwidth": obj.get("bandwidth"),
            "redundancy": ConnectionRedundancy.from_dict(obj["redundancy"]) if obj.get("redundancy") is not None else None,
            "aSide": ConnectionSide.from_dict(obj["aSide"]) if obj.get("aSide") is not None else None,
            "zSide": ConnectionSide.from_dict(obj["zSide"]) if obj.get("zSide") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


