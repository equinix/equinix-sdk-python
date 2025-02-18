# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)
"""

from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class PtpAdvanceConfigurationLogAnnounceInterval(int, Enum):
    """
    Logarithmic value that controls the rate of PTP Announce packets from the PTP time server. Default is 1 (1 packet every 2 seconds), Unit packets/second.
    """

    """
    allowed enum values
    """
    NUMBER_MINUS_3 = -3
    NUMBER_MINUS_2 = -2
    NUMBER_MINUS_1 = -1
    NUMBER_0 = 0
    NUMBER_1 = 1

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of PtpAdvanceConfigurationLogAnnounceInterval from a JSON string"""
        return cls(json.loads(json_str))


