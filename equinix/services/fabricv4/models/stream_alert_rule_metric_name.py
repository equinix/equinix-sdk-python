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


class StreamAlertRuleMetricName(str, Enum):
    """
    Stream alert rule metric name
    """

    """
    allowed enum values
    """
    EQUINIX_DOT_FABRIC_DOT_CONNECTION_DOT_BANDWIDTH_TX_DOT_USAGE = 'equinix.fabric.connection.bandwidth_tx.usage'
    EQUINIX_DOT_FABRIC_DOT_CONNECTION_DOT_BANDWIDTH_RX_DOT_USAGE = 'equinix.fabric.connection.bandwidth_rx.usage'
    EQUINIX_DOT_FABRIC_DOT_PORT_DOT_BANDWIDTH_TX_DOT_USAGE = 'equinix.fabric.port.bandwidth_tx.usage'
    EQUINIX_DOT_FABRIC_DOT_PORT_DOT_BANDWIDTH_RX_DOT_USAGE = 'equinix.fabric.port.bandwidth_rx.usage'
    EQUINIX_DOT_FABRIC_DOT_PORT_DOT_PACKETS_ERRED_TX_DOT_COUNT = 'equinix.fabric.port.packets_erred_tx.count'
    EQUINIX_DOT_FABRIC_DOT_PORT_DOT_PACKETS_ERRED_RX_DOT_COUNT = 'equinix.fabric.port.packets_erred_rx.count'
    EQUINIX_DOT_FABRIC_DOT_PORT_DOT_PACKETS_DROPPED_TX_DOT_COUNT = 'equinix.fabric.port.packets_dropped_tx.count'
    EQUINIX_DOT_FABRIC_DOT_PORT_DOT_PACKETS_DROPPED_RX_DOT_COUNT = 'equinix.fabric.port.packets_dropped_rx.count'
    EQUINIX_DOT_FABRIC_DOT_METRO_DOT_LESS_THAN_SOURCE_METRO_CODE_GREATER_THAN__LESS_THAN_DESTINATION_METRO_CODE_GREATER_THAN_DOT_LATENCY = 'equinix.fabric.metro.<source_metro_code>_<destination_metro_code>.latency'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of StreamAlertRuleMetricName from a JSON string"""
        return cls(json.loads(json_str))


