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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class CapacityCheckPerMetroInfo(BaseModel):
    """
    CapacityCheckPerMetroInfo
    """ # noqa: E501
    available: Optional[StrictBool] = Field(default=None, description="Returns true if there is enough capacity in the metro to fulfill the quantity set. Returns false if there is not enough.")
    href: Optional[StrictStr] = None
    metro: Optional[StrictStr] = Field(default=None, description="The metro ID or code sent to check capacity.")
    plan: Optional[StrictStr] = Field(default=None, description="The plan ID or slug sent to check capacity.")
    quantity: Optional[StrictStr] = Field(default=None, description="The number of servers sent to check capacity.")
    __properties: ClassVar[List[str]] = ["available", "href", "metro", "plan", "quantity"]

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
        """Create an instance of CapacityCheckPerMetroInfo from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CapacityCheckPerMetroInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "available": obj.get("available"),
            "href": obj.get("href"),
            "metro": obj.get("metro"),
            "plan": obj.get("plan"),
            "quantity": obj.get("quantity")
        })
        return _obj


