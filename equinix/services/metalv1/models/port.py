# coding: utf-8

"""
    Metal API

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from equinix.services.metalv1.models.bond_port_data import BondPortData
from equinix.services.metalv1.models.port_data import PortData
from typing import Optional, Set
from typing_extensions import Self

class Port(BaseModel):
    """
    Port is a hardware port associated with a reserved or instantiated hardware device.
    """ # noqa: E501
    bond: Optional[BondPortData] = None
    data: Optional[PortData] = None
    disbond_operation_supported: Optional[StrictBool] = Field(default=None, description="Indicates whether or not the bond can be broken on the port (when applicable).")
    href: Optional[StrictStr] = None
    id: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    native_virtual_network: Optional[VirtualNetwork] = None
    network_type: Optional[StrictStr] = Field(default=None, description="Composite network type of the bond")
    type: Optional[StrictStr] = Field(default=None, description="Type is either \"NetworkBondPort\" for bond ports or \"NetworkPort\" for bondable ethernet ports")
    virtual_networks: Optional[List[VirtualNetwork]] = None
    __properties: ClassVar[List[str]] = ["bond", "data", "disbond_operation_supported", "href", "id", "name", "native_virtual_network", "network_type", "type", "virtual_networks"]

    @field_validator('network_type')
    def network_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['layer2-bonded', 'layer2-individual', 'layer3', 'hybrid', 'hybrid-bonded']):
            raise ValueError("must be one of enum values ('layer2-bonded', 'layer2-individual', 'layer3', 'hybrid', 'hybrid-bonded')")
        return value

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['NetworkPort', 'NetworkBondPort']):
            raise ValueError("must be one of enum values ('NetworkPort', 'NetworkBondPort')")
        return value

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
        """Create an instance of Port from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of bond
        if self.bond:
            _dict['bond'] = self.bond.to_dict()
        # override the default output from pydantic by calling `to_dict()` of data
        if self.data:
            _dict['data'] = self.data.to_dict()
        # override the default output from pydantic by calling `to_dict()` of native_virtual_network
        if self.native_virtual_network:
            _dict['native_virtual_network'] = self.native_virtual_network.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in virtual_networks (list)
        _items = []
        if self.virtual_networks:
            for _item_virtual_networks in self.virtual_networks:
                if _item_virtual_networks:
                    _items.append(_item_virtual_networks.to_dict())
            _dict['virtual_networks'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Port from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "bond": BondPortData.from_dict(obj["bond"]) if obj.get("bond") is not None else None,
            "data": PortData.from_dict(obj["data"]) if obj.get("data") is not None else None,
            "disbond_operation_supported": obj.get("disbond_operation_supported"),
            "href": obj.get("href"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "native_virtual_network": VirtualNetwork.from_dict(obj["native_virtual_network"]) if obj.get("native_virtual_network") is not None else None,
            "network_type": obj.get("network_type"),
            "type": obj.get("type"),
            "virtual_networks": [VirtualNetwork.from_dict(_item) for _item in obj["virtual_networks"]] if obj.get("virtual_networks") is not None else None
        })
        return _obj

from equinix.services.metalv1.models.virtual_network import VirtualNetwork
# TODO: Rewrite to not use raise_errors
Port.model_rebuild(raise_errors=False)

