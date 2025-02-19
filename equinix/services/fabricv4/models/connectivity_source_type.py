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


class ConnectivitySourceType(str, Enum):
    """
    Type of connectivity. COLO, colocation; BMMR, building meet-me room. The default is COLO. <br> A building meet-me room (BMMR) is a room within the same building where an Equinix IBX customer can connect with a non-Equinix IBX customer.
    """

    """
    allowed enum values
    """
    COLO = 'COLO'
    BMMR = 'BMMR'
    REMOTE = 'REMOTE'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ConnectivitySourceType from a JSON string"""
        return cls(json.loads(json_str))


