# coding: utf-8

"""
    Equinix Fabric API v4

    Equinix Fabric is an advanced software-defined interconnection solution that enables you to directly, securely and dynamically connect to distributed infrastructure and digital ecosystems on platform Equinix via a single port, Customers can use Fabric to connect to: </br> 1. Cloud Service Providers - Clouds, network and other service providers.  </br> 2. Enterprises - Other Equinix customers, vendors and partners.  </br> 3. Myself - Another customer instance deployed at Equinix. </br> </br> <b>Integrations (SDKs, Tools) links:</b> </br> <a href=\"https://deploy.equinix.com/labs/fabric-java\\\">Fabric Java SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-go\\\">Fabric Go SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-python\\\">Fabric Python SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-provider-equinix\\\">Equinix Terraform Provider</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-equinix-fabric\\\">Fabric Terraform Modules</a> </br> <a href=\"https://deploy.equinix.com/labs/pulumi-provider-equinix/\">Equinix Pulumi Provider</a> </br>

    The version of the OpenAPI document: 4.20
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


