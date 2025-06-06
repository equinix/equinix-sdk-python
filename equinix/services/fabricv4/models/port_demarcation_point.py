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
from typing import Optional, Set
from typing_extensions import Self

class PortDemarcationPoint(BaseModel):
    """
    Customer physical Port
    """ # noqa: E501
    cabinet_unique_space_id: Optional[StrictStr] = Field(default=None, description="Port cabinet unique space id", alias="cabinetUniqueSpaceId")
    cage_unique_space_id: Optional[StrictStr] = Field(default=None, description="Port cage unique space id", alias="cageUniqueSpaceId")
    patch_panel: Optional[StrictStr] = Field(default=None, description="Port patch panel", alias="patchPanel")
    patch_panel_name: Optional[StrictStr] = Field(default=None, description="Port patch panel", alias="patchPanelName")
    patch_panel_port_a: Optional[StrictStr] = Field(default=None, description="Port patch panel port A", alias="patchPanelPortA")
    patch_panel_port_b: Optional[StrictStr] = Field(default=None, description="Port patch panel port B", alias="patchPanelPortB")
    connector_type: Optional[StrictStr] = Field(default=None, description="Port connector type", alias="connectorType")
    ibx: Optional[StrictStr] = Field(default=None, description="Port ibx identifier")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["cabinetUniqueSpaceId", "cageUniqueSpaceId", "patchPanel", "patchPanelName", "patchPanelPortA", "patchPanelPortB", "connectorType", "ibx"]

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
        """Create an instance of PortDemarcationPoint from a JSON string"""
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
        """Create an instance of PortDemarcationPoint from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "cabinetUniqueSpaceId": obj.get("cabinetUniqueSpaceId"),
            "cageUniqueSpaceId": obj.get("cageUniqueSpaceId"),
            "patchPanel": obj.get("patchPanel"),
            "patchPanelName": obj.get("patchPanelName"),
            "patchPanelPortA": obj.get("patchPanelPortA"),
            "patchPanelPortB": obj.get("patchPanelPortB"),
            "connectorType": obj.get("connectorType"),
            "ibx": obj.get("ibx")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


