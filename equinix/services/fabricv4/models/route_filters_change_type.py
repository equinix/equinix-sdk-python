# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)
"""

from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class RouteFiltersChangeType(str, Enum):
    """
    Type of change
    """

    """
    allowed enum values
    """
    BGP_IPV4_PREFIX_FILTER_UPDATE = 'BGP_IPv4_PREFIX_FILTER_UPDATE'
    BGP_IPV4_PREFIX_FILTER_CREATION = 'BGP_IPv4_PREFIX_FILTER_CREATION'
    BGP_IPV4_PREFIX_FILTER_DELETION = 'BGP_IPv4_PREFIX_FILTER_DELETION'
    BGP_IPV6_PREFIX_FILTER_UPDATE = 'BGP_IPv6_PREFIX_FILTER_UPDATE'
    BGP_IPV6_PREFIX_FILTER_CREATION = 'BGP_IPv6_PREFIX_FILTER_CREATION'
    BGP_IPV6_PREFIX_FILTER_DELETION = 'BGP_IPv6_PREFIX_FILTER_DELETION'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of RouteFiltersChangeType from a JSON string"""
        return cls(json.loads(json_str))


