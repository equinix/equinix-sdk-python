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


class PrecisionTimeServiceRequestType(str, Enum):
    """
    Precision Time Service Type refers to the corresponding Protocol.
    """

    """
    allowed enum values
    """
    NTP = 'NTP'
    PTP = 'PTP'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of PrecisionTimeServiceRequestType from a JSON string"""
        return cls(json.loads(json_str))


