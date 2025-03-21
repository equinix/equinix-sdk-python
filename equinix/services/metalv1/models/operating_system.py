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

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class OperatingSystem(BaseModel):
    """
    OperatingSystem
    """ # noqa: E501
    build_date: Optional[date] = Field(default=None, description="The date on which the current OS image was build and released")
    default_operating_system: Optional[StrictBool] = Field(default=None, description="Default operating system for the distro.")
    deprecation_date: Optional[date] = Field(default=None, description="The date when the OS is deprecated")
    distro: Optional[StrictStr] = None
    distro_label: Optional[StrictStr] = None
    end_of_life_date: Optional[date] = Field(default=None, description="The OS no longer receives any updates and may be disabled at any time")
    end_of_service_date: Optional[date] = Field(default=None, description="When the OS is nearing end of life, typically 30 days before end of life")
    href: Optional[StrictStr] = None
    id: Optional[StrictStr] = None
    licensed: Optional[StrictBool] = Field(default=None, description="Licenced OS is priced according to pricing property")
    lifecycle_state: Optional[StrictStr] = Field(default=None, description="Where in the support lifecycle the OS is")
    name: Optional[StrictStr] = None
    preinstallable: Optional[StrictBool] = Field(default=None, description="Servers can be already preinstalled with OS in order to shorten provision time.")
    pricing: Optional[Dict[str, Any]] = Field(default=None, description="This object contains price per time unit and optional multiplier value if licence price depends on hardware plan or components (e.g. number of cores)")
    provisionable_on: Optional[List[StrictStr]] = None
    release_date: Optional[date] = Field(default=None, description="The date when the OS was released")
    release_notes: Optional[StrictStr] = Field(default=None, description="The current release notes for this OS image, typically in Markdown format")
    slug: Optional[StrictStr] = None
    version: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["build_date", "default_operating_system", "deprecation_date", "distro", "distro_label", "end_of_life_date", "end_of_service_date", "href", "id", "licensed", "lifecycle_state", "name", "preinstallable", "pricing", "provisionable_on", "release_date", "release_notes", "slug", "version"]

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
        """Create an instance of OperatingSystem from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "default_operating_system",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OperatingSystem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "build_date": obj.get("build_date"),
            "default_operating_system": obj.get("default_operating_system"),
            "deprecation_date": obj.get("deprecation_date"),
            "distro": obj.get("distro"),
            "distro_label": obj.get("distro_label"),
            "end_of_life_date": obj.get("end_of_life_date"),
            "end_of_service_date": obj.get("end_of_service_date"),
            "href": obj.get("href"),
            "id": obj.get("id"),
            "licensed": obj.get("licensed"),
            "lifecycle_state": obj.get("lifecycle_state"),
            "name": obj.get("name"),
            "preinstallable": obj.get("preinstallable"),
            "pricing": obj.get("pricing"),
            "provisionable_on": obj.get("provisionable_on"),
            "release_date": obj.get("release_date"),
            "release_notes": obj.get("release_notes"),
            "slug": obj.get("slug"),
            "version": obj.get("version")
        })
        return _obj


