# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)
"""

from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class NetworkChangeStatus(str, Enum):
    """
    Current outcome of the change flow
    """

    """
    allowed enum values
    """
    APPROVED = 'APPROVED'
    COMPLETED = 'COMPLETED'
    FAILED = 'FAILED'
    REJECTED = 'REJECTED'
    REQUESTED = 'REQUESTED'
    SUBMITTED_FOR_APPROVAL = 'SUBMITTED_FOR_APPROVAL'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of NetworkChangeStatus from a JSON string"""
        return cls(json.loads(json_str))


