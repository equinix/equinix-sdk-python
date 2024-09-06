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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from equinix.services.metalv1.models.href import Href
from typing import Optional, Set
from typing_extensions import Self

class AuthTokenProject(BaseModel):
    """
    AuthTokenProject
    """ # noqa: E501
    backend_transfer_enabled: Optional[StrictBool] = None
    bgp_config: Optional[Href] = None
    created_at: Optional[datetime] = None
    customdata: Optional[Dict[str, Any]] = None
    devices: Optional[List[Href]] = None
    href: Optional[StrictStr] = None
    id: Optional[StrictStr] = None
    invitations: Optional[List[Href]] = None
    max_devices: Optional[Dict[str, Any]] = None
    members: Optional[List[Href]] = None
    memberships: Optional[List[Href]] = None
    name: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=80)]] = Field(default=None, description="The name of the project. Cannot contain characters encoded in greater than 3 bytes such as emojis.")
    network_status: Optional[Dict[str, Any]] = None
    organization: Optional[Href] = None
    payment_method: Optional[Href] = None
    ssh_keys: Optional[List[Href]] = None
    tags: Optional[List[StrictStr]] = None
    type: Optional[StrictStr] = Field(default=None, description="The type of the project. Projects of type `vmce` are part of an in development feature and not available to all customers.")
    updated_at: Optional[datetime] = None
    url: Optional[StrictStr] = None
    volumes: Optional[List[Href]] = None
    __properties: ClassVar[List[str]] = ["backend_transfer_enabled", "bgp_config", "created_at", "customdata", "devices", "href", "id", "invitations", "max_devices", "members", "memberships", "name", "network_status", "organization", "payment_method", "ssh_keys", "tags", "type", "updated_at", "url", "volumes"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['default', 'vmce']):
            raise ValueError("must be one of enum values ('default', 'vmce')")
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
        """Create an instance of AuthTokenProject from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of bgp_config
        if self.bgp_config:
            _dict['bgp_config'] = self.bgp_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in devices (list)
        _items = []
        if self.devices:
            for _item in self.devices:
                if _item:
                    _items.append(_item.to_dict())
            _dict['devices'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in invitations (list)
        _items = []
        if self.invitations:
            for _item in self.invitations:
                if _item:
                    _items.append(_item.to_dict())
            _dict['invitations'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in members (list)
        _items = []
        if self.members:
            for _item in self.members:
                if _item:
                    _items.append(_item.to_dict())
            _dict['members'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in memberships (list)
        _items = []
        if self.memberships:
            for _item in self.memberships:
                if _item:
                    _items.append(_item.to_dict())
            _dict['memberships'] = _items
        # override the default output from pydantic by calling `to_dict()` of organization
        if self.organization:
            _dict['organization'] = self.organization.to_dict()
        # override the default output from pydantic by calling `to_dict()` of payment_method
        if self.payment_method:
            _dict['payment_method'] = self.payment_method.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in ssh_keys (list)
        _items = []
        if self.ssh_keys:
            for _item in self.ssh_keys:
                if _item:
                    _items.append(_item.to_dict())
            _dict['ssh_keys'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in volumes (list)
        _items = []
        if self.volumes:
            for _item in self.volumes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['volumes'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AuthTokenProject from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "backend_transfer_enabled": obj.get("backend_transfer_enabled"),
            "bgp_config": Href.from_dict(obj["bgp_config"]) if obj.get("bgp_config") is not None else None,
            "created_at": obj.get("created_at"),
            "customdata": obj.get("customdata"),
            "devices": [Href.from_dict(_item) for _item in obj["devices"]] if obj.get("devices") is not None else None,
            "href": obj.get("href"),
            "id": obj.get("id"),
            "invitations": [Href.from_dict(_item) for _item in obj["invitations"]] if obj.get("invitations") is not None else None,
            "max_devices": obj.get("max_devices"),
            "members": [Href.from_dict(_item) for _item in obj["members"]] if obj.get("members") is not None else None,
            "memberships": [Href.from_dict(_item) for _item in obj["memberships"]] if obj.get("memberships") is not None else None,
            "name": obj.get("name"),
            "network_status": obj.get("network_status"),
            "organization": Href.from_dict(obj["organization"]) if obj.get("organization") is not None else None,
            "payment_method": Href.from_dict(obj["payment_method"]) if obj.get("payment_method") is not None else None,
            "ssh_keys": [Href.from_dict(_item) for _item in obj["ssh_keys"]] if obj.get("ssh_keys") is not None else None,
            "tags": obj.get("tags"),
            "type": obj.get("type"),
            "updated_at": obj.get("updated_at"),
            "url": obj.get("url"),
            "volumes": [Href.from_dict(_item) for _item in obj["volumes"]] if obj.get("volumes") is not None else None
        })
        return _obj


