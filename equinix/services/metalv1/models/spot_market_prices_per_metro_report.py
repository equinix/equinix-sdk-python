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
from equinix.services.metalv1.models.spot_prices_per_facility import SpotPricesPerFacility
from typing import Optional, Set
from typing_extensions import Self

class SpotMarketPricesPerMetroReport(BaseModel):
    """
    SpotMarketPricesPerMetroReport
    """ # noqa: E501
    am: Optional[SpotPricesPerFacility] = None
    ch: Optional[SpotPricesPerFacility] = None
    da: Optional[SpotPricesPerFacility] = None
    href: Optional[StrictStr] = None
    la: Optional[SpotPricesPerFacility] = None
    ny: Optional[SpotPricesPerFacility] = None
    sg: Optional[SpotPricesPerFacility] = None
    sv: Optional[SpotPricesPerFacility] = None
    __properties: ClassVar[List[str]] = ["am", "ch", "da", "href", "la", "ny", "sg", "sv"]

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
        """Create an instance of SpotMarketPricesPerMetroReport from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of am
        if self.am:
            _dict['am'] = self.am.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ch
        if self.ch:
            _dict['ch'] = self.ch.to_dict()
        # override the default output from pydantic by calling `to_dict()` of da
        if self.da:
            _dict['da'] = self.da.to_dict()
        # override the default output from pydantic by calling `to_dict()` of la
        if self.la:
            _dict['la'] = self.la.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ny
        if self.ny:
            _dict['ny'] = self.ny.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sg
        if self.sg:
            _dict['sg'] = self.sg.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sv
        if self.sv:
            _dict['sv'] = self.sv.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SpotMarketPricesPerMetroReport from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "am": SpotPricesPerFacility.from_dict(obj["am"]) if obj.get("am") is not None else None,
            "ch": SpotPricesPerFacility.from_dict(obj["ch"]) if obj.get("ch") is not None else None,
            "da": SpotPricesPerFacility.from_dict(obj["da"]) if obj.get("da") is not None else None,
            "href": obj.get("href"),
            "la": SpotPricesPerFacility.from_dict(obj["la"]) if obj.get("la") is not None else None,
            "ny": SpotPricesPerFacility.from_dict(obj["ny"]) if obj.get("ny") is not None else None,
            "sg": SpotPricesPerFacility.from_dict(obj["sg"]) if obj.get("sg") is not None else None,
            "sv": SpotPricesPerFacility.from_dict(obj["sv"]) if obj.get("sv") is not None else None
        })
        return _obj


