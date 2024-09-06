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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from equinix.services.metalv1.models.href import Href
from typing import Optional, Set
from typing_extensions import Self

class Event(BaseModel):
    """
    Event
    """ # noqa: E501
    body: Optional[StrictStr] = None
    created_at: Optional[datetime] = None
    href: Optional[StrictStr] = None
    id: Optional[StrictStr] = None
    interpolated: Optional[StrictStr] = None
    ip: Optional[StrictStr] = None
    modified_by: Optional[Dict[str, Any]] = None
    relationships: Optional[List[Href]] = None
    state: Optional[StrictStr] = None
    type: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["body", "created_at", "href", "id", "interpolated", "ip", "modified_by", "relationships", "state", "type"]

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
        """Create an instance of Event from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in relationships (list)
        _items = []
        if self.relationships:
            for _item in self.relationships:
                if _item:
                    _items.append(_item.to_dict())
            _dict['relationships'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Event from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "body": obj.get("body"),
            "created_at": obj.get("created_at"),
            "href": obj.get("href"),
            "id": obj.get("id"),
            "interpolated": obj.get("interpolated"),
            "ip": obj.get("ip"),
            "modified_by": obj.get("modified_by"),
            "relationships": [Href.from_dict(_item) for _item in obj["relationships"]] if obj.get("relationships") is not None else None,
            "state": obj.get("state"),
            "type": obj.get("type")
        })
        return _obj


