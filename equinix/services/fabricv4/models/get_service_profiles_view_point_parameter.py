# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)
"""

from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class GetServiceProfilesViewPointParameter(str, Enum):
    """
    GetServiceProfilesViewPointParameter
    """

    """
    allowed enum values
    """
    ASIDE = 'aSide'
    ZSIDE = 'zSide'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of GetServiceProfilesViewPointParameter from a JSON string"""
        return cls(json.loads(json_str))


