# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)
"""

from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class StreamAlertRuleState(str, Enum):
    """
    Steam subscription provision state
    """

    """
    allowed enum values
    """
    ACTIVE = 'ACTIVE'
    INACTIVE = 'INACTIVE'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of StreamAlertRuleState from a JSON string"""
        return cls(json.loads(json_str))


