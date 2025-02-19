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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class IPAddress(BaseModel):
    """
    IPAddress
    """ # noqa: E501
    address_family: Optional[StrictInt] = Field(default=None, description="Address Family for IP Address")
    cidr: Optional[StrictInt] = Field(default=None, description="Cidr Size for the IP Block created. Valid values depends on the operating system being provisioned. (28..32 for IPv4 addresses, 124..127 for IPv6 addresses)")
    href: Optional[StrictStr] = None
    ip_reservations: Optional[List[StrictStr]] = Field(default=None, description="UUIDs of any IP reservations to use when assigning IPs")
    public: Optional[StrictBool] = Field(default=True, description="Address Type for IP Address")
    __properties: ClassVar[List[str]] = ["address_family", "cidr", "href", "ip_reservations", "public"]

    @field_validator('address_family')
    def address_family_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set([4, 6]):
            raise ValueError("must be one of enum values (4, 6)")
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
        """Create an instance of IPAddress from a JSON string"""
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
        """Create an instance of IPAddress from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "address_family": obj.get("address_family"),
            "cidr": obj.get("cidr"),
            "href": obj.get("href"),
            "ip_reservations": obj.get("ip_reservations"),
            "public": obj.get("public") if obj.get("public") is not None else True
        })
        return _obj


