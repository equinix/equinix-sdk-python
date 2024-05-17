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
from equinix.services.metalv1.models.email_input import EmailInput
from typing import Optional, Set
from typing_extensions import Self

class UserCreateInput(BaseModel):
    """
    UserCreateInput
    """ # noqa: E501
    company_name: Optional[StrictStr] = None
    company_url: Optional[StrictStr] = None
    customdata: Optional[Dict[str, Any]] = None
    emails: List[EmailInput]
    first_name: StrictStr
    href: Optional[StrictStr] = None
    invitation_id: Optional[StrictStr] = None
    last_name: StrictStr
    level: Optional[StrictStr] = None
    nonce: Optional[StrictStr] = None
    password: Optional[StrictStr] = None
    phone_number: Optional[StrictStr] = None
    social_accounts: Optional[Dict[str, Any]] = None
    timezone: Optional[StrictStr] = None
    title: Optional[StrictStr] = None
    two_factor_auth: Optional[StrictStr] = None
    verified_at: Optional[datetime] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["company_name", "company_url", "customdata", "emails", "first_name", "href", "invitation_id", "last_name", "level", "nonce", "password", "phone_number", "social_accounts", "timezone", "title", "two_factor_auth", "verified_at"]

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
        """Create an instance of UserCreateInput from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in emails (list)
        _items = []
        if self.emails:
            for _item in self.emails:
                if _item:
                    _items.append(_item.to_dict())
            _dict['emails'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UserCreateInput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "company_name": obj.get("company_name"),
            "company_url": obj.get("company_url"),
            "customdata": obj.get("customdata"),
            "emails": [EmailInput.from_dict(_item) for _item in obj["emails"]] if obj.get("emails") is not None else None,
            "first_name": obj.get("first_name"),
            "href": obj.get("href"),
            "invitation_id": obj.get("invitation_id"),
            "last_name": obj.get("last_name"),
            "level": obj.get("level"),
            "nonce": obj.get("nonce"),
            "password": obj.get("password"),
            "phone_number": obj.get("phone_number"),
            "social_accounts": obj.get("social_accounts"),
            "timezone": obj.get("timezone"),
            "title": obj.get("title"),
            "two_factor_auth": obj.get("two_factor_auth"),
            "verified_at": obj.get("verified_at")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


