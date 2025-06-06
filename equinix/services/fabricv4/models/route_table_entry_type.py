# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class RouteTableEntryType(str, Enum):
    """
    Route table entry type
    """

    """
    allowed enum values
    """
    IPV4_BGP_ROUTE = 'IPv4_BGP_ROUTE'
    IPV4_STATIC_ROUTE = 'IPv4_STATIC_ROUTE'
    IPV4_DIRECT_ROUTE = 'IPv4_DIRECT_ROUTE'
    IPV6_BGP_ROUTE = 'IPv6_BGP_ROUTE'
    IPV6_STATIC_ROUTE = 'IPv6_STATIC_ROUTE'
    IPV6_DIRECT_ROUTE = 'IPv6_DIRECT_ROUTE'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of RouteTableEntryType from a JSON string"""
        return cls(json.loads(json_str))


