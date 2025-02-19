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


class PriceErrorErrorCode(str, Enum):
    """
    PriceErrorErrorCode
    """

    """
    allowed enum values
    """
    EQ_MINUS_3038010 = 'EQ-3038010'
    EQ_MINUS_3038022 = 'EQ-3038022'
    EQ_MINUS_3038030 = 'EQ-3038030'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of PriceErrorErrorCode from a JSON string"""
        return cls(json.loads(json_str))


