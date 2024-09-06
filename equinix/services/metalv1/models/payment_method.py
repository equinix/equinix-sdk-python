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
from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from equinix.services.metalv1.models.href import Href
from equinix.services.metalv1.models.payment_method_billing_address import PaymentMethodBillingAddress
from typing import Optional, Set
from typing_extensions import Self

class PaymentMethod(BaseModel):
    """
    PaymentMethod
    """ # noqa: E501
    billing_address: Optional[PaymentMethodBillingAddress] = None
    card_type: Optional[StrictStr] = None
    cardholder_name: Optional[StrictStr] = None
    created_at: Optional[datetime] = None
    created_by_user: Optional[Href] = None
    default: Optional[StrictBool] = None
    email: Optional[StrictStr] = None
    expiration_month: Optional[StrictStr] = None
    expiration_year: Optional[StrictStr] = None
    href: Optional[StrictStr] = None
    id: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    organization: Optional[Href] = None
    projects: Optional[List[Href]] = None
    type: Optional[StrictStr] = None
    updated_at: Optional[datetime] = None
    __properties: ClassVar[List[str]] = ["billing_address", "card_type", "cardholder_name", "created_at", "created_by_user", "default", "email", "expiration_month", "expiration_year", "href", "id", "name", "organization", "projects", "type", "updated_at"]

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
        """Create an instance of PaymentMethod from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of billing_address
        if self.billing_address:
            _dict['billing_address'] = self.billing_address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of created_by_user
        if self.created_by_user:
            _dict['created_by_user'] = self.created_by_user.to_dict()
        # override the default output from pydantic by calling `to_dict()` of organization
        if self.organization:
            _dict['organization'] = self.organization.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in projects (list)
        _items = []
        if self.projects:
            for _item in self.projects:
                if _item:
                    _items.append(_item.to_dict())
            _dict['projects'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PaymentMethod from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in PaymentMethod) in the input: " + _key)

        _obj = cls.model_validate({
            "billing_address": PaymentMethodBillingAddress.from_dict(obj["billing_address"]) if obj.get("billing_address") is not None else None,
            "card_type": obj.get("card_type"),
            "cardholder_name": obj.get("cardholder_name"),
            "created_at": obj.get("created_at"),
            "created_by_user": Href.from_dict(obj["created_by_user"]) if obj.get("created_by_user") is not None else None,
            "default": obj.get("default"),
            "email": obj.get("email"),
            "expiration_month": obj.get("expiration_month"),
            "expiration_year": obj.get("expiration_year"),
            "href": obj.get("href"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "organization": Href.from_dict(obj["organization"]) if obj.get("organization") is not None else None,
            "projects": [Href.from_dict(_item) for _item in obj["projects"]] if obj.get("projects") is not None else None,
            "type": obj.get("type"),
            "updated_at": obj.get("updated_at")
        })
        return _obj


