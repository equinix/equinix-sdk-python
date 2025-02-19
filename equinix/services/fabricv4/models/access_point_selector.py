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

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from equinix.services.fabricv4.models.access_point_selector_type import AccessPointSelectorType
from equinix.services.fabricv4.models.simplified_link_protocol import SimplifiedLinkProtocol
from equinix.services.fabricv4.models.simplified_metadata_entity import SimplifiedMetadataEntity
from equinix.services.fabricv4.models.simplified_token_network import SimplifiedTokenNetwork
from equinix.services.fabricv4.models.simplified_virtual_device import SimplifiedVirtualDevice
from equinix.services.fabricv4.models.virtual_device_interface import VirtualDeviceInterface
from typing import Optional, Set
from typing_extensions import Self

class AccessPointSelector(BaseModel):
    """
    List of criteria for selecting network access points with optimal efficiency, security, compatibility, and availability.
    """ # noqa: E501
    type: Optional[AccessPointSelectorType] = None
    hide_asset_info: Optional[StrictBool] = Field(default=None, alias="hideAssetInfo")
    port: Optional[SimplifiedMetadataEntity] = None
    link_protocol: Optional[SimplifiedLinkProtocol] = Field(default=None, alias="linkProtocol")
    virtual_device: Optional[SimplifiedVirtualDevice] = Field(default=None, alias="virtualDevice")
    interface: Optional[VirtualDeviceInterface] = None
    network: Optional[SimplifiedTokenNetwork] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["type", "hideAssetInfo", "port", "linkProtocol", "virtualDevice", "interface", "network"]

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
        """Create an instance of AccessPointSelector from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of port
        if self.port:
            _dict['port'] = self.port.to_dict()
        # override the default output from pydantic by calling `to_dict()` of link_protocol
        if self.link_protocol:
            _dict['linkProtocol'] = self.link_protocol.to_dict()
        # override the default output from pydantic by calling `to_dict()` of virtual_device
        if self.virtual_device:
            _dict['virtualDevice'] = self.virtual_device.to_dict()
        # override the default output from pydantic by calling `to_dict()` of interface
        if self.interface:
            _dict['interface'] = self.interface.to_dict()
        # override the default output from pydantic by calling `to_dict()` of network
        if self.network:
            _dict['network'] = self.network.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AccessPointSelector from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "hideAssetInfo": obj.get("hideAssetInfo"),
            "port": SimplifiedMetadataEntity.from_dict(obj["port"]) if obj.get("port") is not None else None,
            "linkProtocol": SimplifiedLinkProtocol.from_dict(obj["linkProtocol"]) if obj.get("linkProtocol") is not None else None,
            "virtualDevice": SimplifiedVirtualDevice.from_dict(obj["virtualDevice"]) if obj.get("virtualDevice") is not None else None,
            "interface": VirtualDeviceInterface.from_dict(obj["interface"]) if obj.get("interface") is not None else None,
            "network": SimplifiedTokenNetwork.from_dict(obj["network"]) if obj.get("network") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


