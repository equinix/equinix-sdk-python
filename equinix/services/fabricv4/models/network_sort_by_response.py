# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)
"""

from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class NetworkSortByResponse(str, Enum):
    """
    Possible field names to use on sorting
    """

    """
    allowed enum values
    """
    SLASH_NAME = '/name'
    SLASH_TYPE = '/type'
    SLASH_UUID = '/uuid'
    SLASH_STATE = '/state'
    SLASH_SCOPE = '/scope'
    SLASH_LOCATION_SLASH_REGION = '/location/region'
    SLASH_CHANGE_LOG_SLASH_CREATED_DATE_TIME = '/changeLog/createdDateTime'
    SLASH_CHANGE_LOG_SLASH_UPDATED_DATE_TIME = '/changeLog/updatedDateTime'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of NetworkSortByResponse from a JSON string"""
        return cls(json.loads(json_str))


