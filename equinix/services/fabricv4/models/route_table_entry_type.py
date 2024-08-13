# coding: utf-8

"""
    Equinix Fabric API v4

    Equinix Fabric is an advanced software-defined interconnection solution that enables you to directly, securely and dynamically connect to distributed infrastructure and digital ecosystems on platform Equinix via a single port, Customers can use Fabric to connect to: </br> 1. Cloud Service Providers - Clouds, network and other service providers.  </br> 2. Enterprises - Other Equinix customers, vendors and partners.  </br> 3. Myself - Another customer instance deployed at Equinix. </br> </br> <b>Integrations (SDKs, Tools) links:</b> </br> <a href=\"https://deploy.equinix.com/labs/fabric-java\\\">Fabric Java SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-go\\\">Fabric Go SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-provider-equinix\\\">Equinix Terraform Provider</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-equinix-fabric\\\">Fabric Terraform Modules</a> </br> <a href=\"https://deploy.equinix.com/labs/pulumi-provider-equinix/\">Equinix Pulumi Provider</a> </br>

    The version of the OpenAPI document: 4.15
    Contact: api-support@equinix.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class RouteTableEntryType(str, Enum):
    """
    Route table entry type
    """

    """
    allowed enum values
    """
    IPV4_BGP_ROUTE = 'IPv4_BGP_ROUTE'
    IPV4_STATIC_ROUTE = 'IPv4_STATIC_ROUTE'
    IPV4_DIRECT_ROUTE = 'IPv4_DIRECT_ROUTE'
    IPV6_BGP_ROUTE = 'IPv6_BGP_ROUTE'
    IPV6_STATIC_ROUTE = 'IPv6_STATIC_ROUTE'
    IPV6_DIRECT_ROUTE = 'IPv6_DIRECT_ROUTE'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of RouteTableEntryType from a JSON string"""
        return cls(json.loads(json_str))


