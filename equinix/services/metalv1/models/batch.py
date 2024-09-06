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
from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from equinix.services.metalv1.models.href import Href
from typing import Optional, Set
from typing_extensions import Self

class Batch(BaseModel):
    """
    Batch
    """ # noqa: E501
    created_at: Optional[datetime] = None
    devices: Optional[List[Href]] = None
    error_messages: Optional[List[StrictStr]] = None
    href: Optional[StrictStr] = None
    id: Optional[StrictStr] = None
    project: Optional[Href] = None
    quantity: Optional[StrictInt] = None
    state: Optional[StrictStr] = None
    updated_at: Optional[datetime] = None
    __properties: ClassVar[List[str]] = ["created_at", "devices", "error_messages", "href", "id", "project", "quantity", "state", "updated_at"]

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
        """Create an instance of Batch from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in devices (list)
        _items = []
        if self.devices:
            for _item in self.devices:
                if _item:
                    _items.append(_item.to_dict())
            _dict['devices'] = _items
        # override the default output from pydantic by calling `to_dict()` of project
        if self.project:
            _dict['project'] = self.project.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Batch from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "created_at": obj.get("created_at"),
            "devices": [Href.from_dict(_item) for _item in obj["devices"]] if obj.get("devices") is not None else None,
            "error_messages": obj.get("error_messages"),
            "href": obj.get("href"),
            "id": obj.get("id"),
            "project": Href.from_dict(obj["project"]) if obj.get("project") is not None else None,
            "quantity": obj.get("quantity"),
            "state": obj.get("state"),
            "updated_at": obj.get("updated_at")
        })
        return _obj


