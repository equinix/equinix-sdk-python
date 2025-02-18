# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)
"""

from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class RouteFilterRulesDataType(str, Enum):
    """
    Route filter type
    """

    """
    allowed enum values
    """
    BGP_IPV4_PREFIX_FILTER_RULE = 'BGP_IPv4_PREFIX_FILTER_RULE'
    BGP_IPV6_PREFIX_FILTER_RULE = 'BGP_IPv6_PREFIX_FILTER_RULE'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of RouteFilterRulesDataType from a JSON string"""
        return cls(json.loads(json_str))


