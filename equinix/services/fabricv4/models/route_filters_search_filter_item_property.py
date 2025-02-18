# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)
"""

from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class RouteFiltersSearchFilterItemProperty(str, Enum):
    """
    RouteFiltersSearchFilterItemProperty
    """

    """
    allowed enum values
    """
    SLASH_TYPE = '/type'
    SLASH_NAME = '/name'
    SLASH_PROJECT_SLASH_PROJECT_ID = '/project/projectId'
    SLASH_UUID = '/uuid'
    SLASH_STATE = '/state'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of RouteFiltersSearchFilterItemProperty from a JSON string"""
        return cls(json.loads(json_str))


