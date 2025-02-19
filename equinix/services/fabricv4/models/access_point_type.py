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


class AccessPointType(str, Enum):
    """
    Access point type
    """

    """
    allowed enum values
    """
    VD = 'VD'
    VG = 'VG'
    SP = 'SP'
    IGW = 'IGW'
    COLO = 'COLO'
    SUBNET = 'SUBNET'
    CLOUD_ROUTER = 'CLOUD_ROUTER'
    NETWORK = 'NETWORK'
    METAL_NETWORK = 'METAL_NETWORK'
    VPIC_INTERFACE = 'VPIC_INTERFACE'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of AccessPointType from a JSON string"""
        return cls(json.loads(json_str))


