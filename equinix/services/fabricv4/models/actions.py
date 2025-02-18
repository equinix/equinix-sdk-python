# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)
"""

from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class Actions(str, Enum):
    """
    Connection action type
    """

    """
    allowed enum values
    """
    CONNECTION_CREATION_ACCEPTANCE = 'CONNECTION_CREATION_ACCEPTANCE'
    CONNECTION_CREATION_REJECTION = 'CONNECTION_CREATION_REJECTION'
    CONNECTION_UPDATE_ACCEPTANCE = 'CONNECTION_UPDATE_ACCEPTANCE'
    CONNECTION_UPDATE_REJECTION = 'CONNECTION_UPDATE_REJECTION'
    CONNECTION_DELETION_ACCEPTANCE = 'CONNECTION_DELETION_ACCEPTANCE'
    CONNECTION_REJECTION_ACCEPTANCE = 'CONNECTION_REJECTION_ACCEPTANCE'
    CONNECTION_UPDATE_REQUEST = 'CONNECTION_UPDATE_REQUEST'
    MIGRATION_EVPL_VC = 'MIGRATION_EVPL_VC'
    CONNECTION_PROVIDER_STATUS_REQUEST = 'CONNECTION_PROVIDER_STATUS_REQUEST'
    CONNECTION_PROVIDER_BANDWIDTH_REQUEST = 'CONNECTION_PROVIDER_BANDWIDTH_REQUEST'
    ACCEPT_HOSTED_CONNECTION = 'ACCEPT_HOSTED_CONNECTION'
    CANCEL_EVPL_VC_DRAFT_ORDERS = 'CANCEL_EVPL_VC_DRAFT_ORDERS'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Actions from a JSON string"""
        return cls(json.loads(json_str))


