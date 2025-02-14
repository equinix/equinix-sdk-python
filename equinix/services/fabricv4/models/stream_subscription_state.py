# coding: utf-8

"""
    Equinix Fabric API v4

    Equinix Fabric is an advanced software-defined interconnection solution that enables you to directly, securely and dynamically connect to distributed infrastructure and digital ecosystems on platform Equinix via a single port, Customers can use Fabric to connect to: </br> 1. Cloud Service Providers - Clouds, network and other service providers.  </br> 2. Enterprises - Other Equinix customers, vendors and partners.  </br> 3. Myself - Another customer instance deployed at Equinix. </br> </br> <b>Integrations (SDKs, Tools) links:</b> </br> <a href=\"https://deploy.equinix.com/labs/fabric-java\\\">Fabric Java SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-go\\\">Fabric Go SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-python\\\">Fabric Python SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-provider-equinix\\\">Equinix Terraform Provider</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-equinix-fabric\\\">Fabric Terraform Modules</a> </br> <a href=\"https://deploy.equinix.com/labs/pulumi-provider-equinix/\">Equinix Pulumi Provider</a> </br>

    Generated by OpenAPI Generator (https://openapi-generator.tech)
"""


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class StreamSubscriptionState(str, Enum):
    """
    Steam subscription provision state
    """

    """
    allowed enum values
    """
    PROVISIONING = 'PROVISIONING'
    PROVISIONED = 'PROVISIONED'
    REPROVISIONING = 'REPROVISIONING'
    DEPROVISIONING = 'DEPROVISIONING'
    DEPROVISIONED = 'DEPROVISIONED'
    FAILED = 'FAILED'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of StreamSubscriptionState from a JSON string"""
        return cls(json.loads(json_str))


