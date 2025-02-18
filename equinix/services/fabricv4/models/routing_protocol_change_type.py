# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)
"""

from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class RoutingProtocolChangeType(str, Enum):
    """
    Type of change
    """

    """
    allowed enum values
    """
    ROUTING_PROTOCOL_UPDATE = 'ROUTING_PROTOCOL_UPDATE'
    ROUTING_PROTOCOL_CREATION = 'ROUTING_PROTOCOL_CREATION'
    ROUTING_PROTOCOL_DELETION = 'ROUTING_PROTOCOL_DELETION'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of RoutingProtocolChangeType from a JSON string"""
        return cls(json.loads(json_str))


