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

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from equinix.services.metalv1.models.virtual_network import VirtualNetwork
from typing import Optional, Set
from typing_extensions import Self

class VirtualNetworkList(BaseModel):
    """
    VirtualNetworkList
    """ # noqa: E501
    href: Optional[StrictStr] = None
    virtual_networks: Optional[List[VirtualNetwork]] = None
    __properties: ClassVar[List[str]] = ["href", "virtual_networks"]

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
        """Create an instance of VirtualNetworkList from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in virtual_networks (list)
        _items = []
        if self.virtual_networks:
            for _item in self.virtual_networks:
                if _item:
                    _items.append(_item.to_dict())
            _dict['virtual_networks'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of VirtualNetworkList from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in VirtualNetworkList) in the input: " + _key)

        _obj = cls.model_validate({
            "href": obj.get("href"),
            "virtual_networks": [VirtualNetwork.from_dict(_item) for _item in obj["virtual_networks"]] if obj.get("virtual_networks") is not None else None
        })
        return _obj


