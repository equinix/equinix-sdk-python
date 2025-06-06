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


class ProviderStatus(str, Enum):
    """
    Connection provider readiness status
    """

    """
    allowed enum values
    """
    AVAILABLE = 'AVAILABLE'
    DEPROVISIONED = 'DEPROVISIONED'
    DEPROVISIONING = 'DEPROVISIONING'
    FAILED = 'FAILED'
    NOT_AVAILABLE = 'NOT_AVAILABLE'
    PENDING_APPROVAL = 'PENDING_APPROVAL'
    PENDING_CONFIGURATION = 'PENDING_CONFIGURATION'
    PROVISIONED = 'PROVISIONED'
    PROVISIONING = 'PROVISIONING'
    REJECTED = 'REJECTED'
    PENDING_BGP = 'PENDING_BGP'
    OUT_OF_BANDWIDTH = 'OUT_OF_BANDWIDTH'
    DELETED = 'DELETED'
    ERROR = 'ERROR'
    ERRORED = 'ERRORED'
    NOTPROVISIONED = 'NOTPROVISIONED'
    NOT_PROVISIONED = 'NOT_PROVISIONED'
    ORDERING = 'ORDERING'
    DELETING = 'DELETING'
    PENDING_DELETE = 'PENDING DELETE'
    N_SLASH_A = 'N/A'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ProviderStatus from a JSON string"""
        return cls(json.loads(json_str))


