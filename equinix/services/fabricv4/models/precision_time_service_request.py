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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from equinix.services.fabricv4.models.advance_configuration import AdvanceConfiguration
from equinix.services.fabricv4.models.fabric_connection_uuid import FabricConnectionUuid
from equinix.services.fabricv4.models.ipv4 import Ipv4
from equinix.services.fabricv4.models.precision_time_package_request import PrecisionTimePackageRequest
from equinix.services.fabricv4.models.precision_time_service_request_type import PrecisionTimeServiceRequestType
from equinix.services.fabricv4.models.project import Project
from typing import Optional, Set
from typing_extensions import Self

class PrecisionTimeServiceRequest(BaseModel):
    """
    EPT service instance
    """ # noqa: E501
    type: PrecisionTimeServiceRequestType
    name: StrictStr
    description: Optional[StrictStr] = None
    package: PrecisionTimePackageRequest
    connections: List[FabricConnectionUuid]
    ipv4: Ipv4
    advance_configuration: Optional[AdvanceConfiguration] = Field(default=None, alias="advanceConfiguration")
    project: Optional[Project] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["type", "name", "description", "package", "connections", "ipv4", "advanceConfiguration", "project"]

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
        """Create an instance of PrecisionTimeServiceRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of package
        if self.package:
            _dict['package'] = self.package.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in connections (list)
        _items = []
        if self.connections:
            for _item_connections in self.connections:
                if _item_connections:
                    _items.append(_item_connections.to_dict())
            _dict['connections'] = _items
        # override the default output from pydantic by calling `to_dict()` of ipv4
        if self.ipv4:
            _dict['ipv4'] = self.ipv4.to_dict()
        # override the default output from pydantic by calling `to_dict()` of advance_configuration
        if self.advance_configuration:
            _dict['advanceConfiguration'] = self.advance_configuration.to_dict()
        # override the default output from pydantic by calling `to_dict()` of project
        if self.project:
            _dict['project'] = self.project.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PrecisionTimeServiceRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "package": PrecisionTimePackageRequest.from_dict(obj["package"]) if obj.get("package") is not None else None,
            "connections": [FabricConnectionUuid.from_dict(_item) for _item in obj["connections"]] if obj.get("connections") is not None else None,
            "ipv4": Ipv4.from_dict(obj["ipv4"]) if obj.get("ipv4") is not None else None,
            "advanceConfiguration": AdvanceConfiguration.from_dict(obj["advanceConfiguration"]) if obj.get("advanceConfiguration") is not None else None,
            "project": Project.from_dict(obj["project"]) if obj.get("project") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


