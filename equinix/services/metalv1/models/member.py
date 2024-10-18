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

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from equinix.services.metalv1.models.href import Href
from typing import Optional, Set
from typing_extensions import Self

class Member(BaseModel):
    """
    Member
    """ # noqa: E501
    bound_roles: Optional[List[StrictStr]] = None
    href: Optional[StrictStr] = None
    id: Optional[StrictStr] = None
    organization: Optional[Href] = None
    projects: Optional[List[Href]] = None
    projects_count: Optional[StrictInt] = None
    roles: Optional[List[StrictStr]] = None
    user: Optional[Href] = None
    __properties: ClassVar[List[str]] = ["bound_roles", "href", "id", "organization", "projects", "projects_count", "roles", "user"]

    @field_validator('roles')
    def roles_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['admin', 'billing', 'collaborator', 'limited_collaborator']):
                raise ValueError("each list item must be one of ('admin', 'billing', 'collaborator', 'limited_collaborator')")
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
        """Create an instance of Member from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of user
        if self.user:
            _dict['user'] = self.user.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Member from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "bound_roles": obj.get("bound_roles"),
            "href": obj.get("href"),
            "id": obj.get("id"),
            "organization": Href.from_dict(obj["organization"]) if obj.get("organization") is not None else None,
            "projects": [Href.from_dict(_item) for _item in obj["projects"]] if obj.get("projects") is not None else None,
            "projects_count": obj.get("projects_count"),
            "roles": obj.get("roles"),
            "user": Href.from_dict(obj["user"]) if obj.get("user") is not None else None
        })
        return _obj


