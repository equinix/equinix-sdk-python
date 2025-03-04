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
from equinix.services.metalv1.models.bgp_session import BgpSession
from typing import Optional, Set
from typing_extensions import Self

class BgpSessionList(BaseModel):
    """
    BgpSessionList
    """ # noqa: E501
    bgp_sessions: Optional[List[BgpSession]] = None
    href: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["bgp_sessions", "href"]

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
        """Create an instance of BgpSessionList from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in bgp_sessions (list)
        _items = []
        if self.bgp_sessions:
            for _item_bgp_sessions in self.bgp_sessions:
                if _item_bgp_sessions:
                    _items.append(_item_bgp_sessions.to_dict())
            _dict['bgp_sessions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BgpSessionList from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "bgp_sessions": [BgpSession.from_dict(_item) for _item in obj["bgp_sessions"]] if obj.get("bgp_sessions") is not None else None,
            "href": obj.get("href")
        })
        return _obj


