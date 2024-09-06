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
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class Component(BaseModel):
    """
    Component
    """ # noqa: E501
    checksum: Optional[StrictStr] = Field(default=None, description="File checksum")
    component: Optional[StrictStr] = Field(default=None, description="Component type")
    created_at: Optional[datetime] = Field(default=None, description="Datetime when the block was created.")
    filename: Optional[StrictStr] = Field(default=None, description="name of the file")
    href: Optional[StrictStr] = None
    model: Optional[List[StrictStr]] = Field(default=None, description="List of models where this component version can be applied")
    repository_url: Optional[StrictStr] = Field(default=None, description="Location of the file in the repository")
    updated_at: Optional[datetime] = Field(default=None, description="Datetime when the block was updated.")
    upstream_url: Optional[StrictStr] = Field(default=None, description="Location of the file")
    uuid: Optional[StrictStr] = Field(default=None, description="Component UUID")
    vendor: Optional[StrictStr] = Field(default=None, description="Component vendor")
    version: Optional[StrictStr] = Field(default=None, description="Version of the component")
    __properties: ClassVar[List[str]] = ["checksum", "component", "created_at", "filename", "href", "model", "repository_url", "updated_at", "upstream_url", "uuid", "vendor", "version"]

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
        """Create an instance of Component from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "checksum",
            "component",
            "created_at",
            "filename",
            "model",
            "repository_url",
            "updated_at",
            "upstream_url",
            "uuid",
            "vendor",
            "version",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Component from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "checksum": obj.get("checksum"),
            "component": obj.get("component"),
            "created_at": obj.get("created_at"),
            "filename": obj.get("filename"),
            "href": obj.get("href"),
            "model": obj.get("model"),
            "repository_url": obj.get("repository_url"),
            "updated_at": obj.get("updated_at"),
            "upstream_url": obj.get("upstream_url"),
            "uuid": obj.get("uuid"),
            "vendor": obj.get("vendor"),
            "version": obj.get("version")
        })
        return _obj


