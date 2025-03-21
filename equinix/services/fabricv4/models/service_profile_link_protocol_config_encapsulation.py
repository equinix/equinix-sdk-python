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


class ServiceProfileLinkProtocolConfigEncapsulation(str, Enum):
    """
    Port encapsulation - Derived response attribute. Ignored on request payloads.
    """

    """
    allowed enum values
    """
    QINQ = 'QINQ'
    DOT1Q = 'DOT1Q'
    UNTAGGED = 'UNTAGGED'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ServiceProfileLinkProtocolConfigEncapsulation from a JSON string"""
        return cls(json.loads(json_str))


