# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from equinix.services.fabricv4.models.changelog import Changelog
from equinix.services.fabricv4.models.direct_connection_ipv4 import DirectConnectionIpv4
from equinix.services.fabricv4.models.direct_connection_ipv6 import DirectConnectionIpv6
from equinix.services.fabricv4.models.routing_protocol_bgp_data_state import RoutingProtocolBGPDataState
from equinix.services.fabricv4.models.routing_protocol_change import RoutingProtocolChange
from equinix.services.fabricv4.models.routing_protocol_direct_type_type import RoutingProtocolDirectTypeType
from equinix.services.fabricv4.models.routing_protocol_operation import RoutingProtocolOperation
from typing import Optional, Set
from typing_extensions import Self

class RoutingProtocolDirectData(BaseModel):
    """
    RoutingProtocolDirectData
    """ # noqa: E501
    type: Optional[RoutingProtocolDirectTypeType] = None
    name: Optional[StrictStr] = None
    direct_ipv4: Optional[DirectConnectionIpv4] = Field(default=None, alias="directIpv4")
    direct_ipv6: Optional[DirectConnectionIpv6] = Field(default=None, alias="directIpv6")
    href: Optional[StrictStr] = Field(default=None, description="Routing Protocol URI")
    uuid: Optional[StrictStr] = Field(default=None, description="Routing protocol identifier")
    state: Optional[RoutingProtocolBGPDataState] = None
    operation: Optional[RoutingProtocolOperation] = None
    change: Optional[RoutingProtocolChange] = None
    changelog: Optional[Changelog] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["type", "name", "directIpv4", "directIpv6", "href", "uuid", "state", "operation", "change", "changelog"]

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
        """Create an instance of RoutingProtocolDirectData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of direct_ipv4
        if self.direct_ipv4:
            _dict['directIpv4'] = self.direct_ipv4.to_dict()
        # override the default output from pydantic by calling `to_dict()` of direct_ipv6
        if self.direct_ipv6:
            _dict['directIpv6'] = self.direct_ipv6.to_dict()
        # override the default output from pydantic by calling `to_dict()` of operation
        if self.operation:
            _dict['operation'] = self.operation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of change
        if self.change:
            _dict['change'] = self.change.to_dict()
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
        """Create an instance of RoutingProtocolDirectData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "name": obj.get("name"),
            "directIpv4": DirectConnectionIpv4.from_dict(obj["directIpv4"]) if obj.get("directIpv4") is not None else None,
            "directIpv6": DirectConnectionIpv6.from_dict(obj["directIpv6"]) if obj.get("directIpv6") is not None else None,
            "href": obj.get("href"),
            "uuid": obj.get("uuid"),
            "state": obj.get("state"),
            "operation": RoutingProtocolOperation.from_dict(obj["operation"]) if obj.get("operation") is not None else None,
            "change": RoutingProtocolChange.from_dict(obj["change"]) if obj.get("change") is not None else None,
            "changelog": Changelog.from_dict(obj["changelog"]) if obj.get("changelog") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


