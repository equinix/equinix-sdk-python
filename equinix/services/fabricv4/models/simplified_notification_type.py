# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)
"""

from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class SimplifiedNotificationType(str, Enum):
    """
    Notification Type
    """

    """
    allowed enum values
    """
    NOTIFICATION = 'NOTIFICATION'
    BANDWIDTH_ALERT = 'BANDWIDTH_ALERT'
    CONNECTION_APPROVAL = 'CONNECTION_APPROVAL'
    PROFILE_LIFECYCLE = 'PROFILE_LIFECYCLE'
    ALL = 'ALL'
    SALES_REP_NOTIFICATIONS = 'SALES_REP_NOTIFICATIONS'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of SimplifiedNotificationType from a JSON string"""
        return cls(json.loads(json_str))


