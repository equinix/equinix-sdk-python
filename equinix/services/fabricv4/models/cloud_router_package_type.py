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


class CloudRouterPackageType(str, Enum):
    """
    Type of Router package
    """

    """
    allowed enum values
    """
    ROUTER_PACKAGE = 'ROUTER_PACKAGE'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of CloudRouterPackageType from a JSON string"""
        return cls(json.loads(json_str))


