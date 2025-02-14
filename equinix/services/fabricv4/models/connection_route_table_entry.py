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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from equinix.services.fabricv4.models.changelog import Changelog
from equinix.services.fabricv4.models.connection_route_table_entry_connection import ConnectionRouteTableEntryConnection
from equinix.services.fabricv4.models.connection_route_table_entry_state import ConnectionRouteTableEntryState
from equinix.services.fabricv4.models.route_table_entry_protocol_type import RouteTableEntryProtocolType
from equinix.services.fabricv4.models.route_table_entry_type import RouteTableEntryType
from typing import Optional, Set
from typing_extensions import Self

class ConnectionRouteTableEntry(BaseModel):
    """
    Advertised and received route table entry object
    """ # noqa: E501
    type: RouteTableEntryType
    protocol_type: Optional[RouteTableEntryProtocolType] = Field(default=None, alias="protocolType")
    state: ConnectionRouteTableEntryState
    age: Optional[StrictStr] = None
    prefix: Optional[StrictStr] = None
    next_hop: Optional[StrictStr] = Field(default=None, alias="nextHop")
    med: Optional[StrictInt] = Field(default=None, alias="MED")
    local_preference: Optional[StrictInt] = Field(default=None, alias="localPreference")
    as_path: Optional[List[StrictStr]] = Field(default=None, alias="asPath")
    connection: Optional[ConnectionRouteTableEntryConnection] = None
    change_log: Changelog = Field(alias="changeLog")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["type", "protocolType", "state", "age", "prefix", "nextHop", "MED", "localPreference", "asPath", "connection", "changeLog"]

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
        """Create an instance of ConnectionRouteTableEntry from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of connection
        if self.connection:
            _dict['connection'] = self.connection.to_dict()
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
        """Create an instance of ConnectionRouteTableEntry from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "protocolType": obj.get("protocolType"),
            "state": obj.get("state"),
            "age": obj.get("age"),
            "prefix": obj.get("prefix"),
            "nextHop": obj.get("nextHop"),
            "MED": obj.get("MED"),
            "localPreference": obj.get("localPreference"),
            "asPath": obj.get("asPath"),
            "connection": ConnectionRouteTableEntryConnection.from_dict(obj["connection"]) if obj.get("connection") is not None else None,
            "changeLog": Changelog.from_dict(obj["changeLog"]) if obj.get("changeLog") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


