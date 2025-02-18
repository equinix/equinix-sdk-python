# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)
"""

from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class RouteFiltersDataNotMatchedRuleAction(str, Enum):
    """
    RouteFiltersDataNotMatchedRuleAction
    """

    """
    allowed enum values
    """
    ALLOW = 'ALLOW'
    DENY = 'DENY'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of RouteFiltersDataNotMatchedRuleAction from a JSON string"""
        return cls(json.loads(json_str))


