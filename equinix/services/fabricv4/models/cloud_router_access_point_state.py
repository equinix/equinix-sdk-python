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


class CloudRouterAccessPointState(str, Enum):
    """
    Access point lifecycle state
    """

    """
    allowed enum values
    """
    PROVISIONED = 'PROVISIONED'
    PROVISIONING = 'PROVISIONING'
    DEPROVISIONING = 'DEPROVISIONING'
    DEPROVISIONED = 'DEPROVISIONED'
    REPROVISIONING = 'REPROVISIONING'
    NOT_PROVISIONED = 'NOT_PROVISIONED'
    NOT_DEPROVISIONED = 'NOT_DEPROVISIONED'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of CloudRouterAccessPointState from a JSON string"""
        return cls(json.loads(json_str))


