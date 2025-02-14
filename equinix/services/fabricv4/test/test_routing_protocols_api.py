# coding: utf-8

"""
    Equinix Fabric API v4

    Equinix Fabric is an advanced software-defined interconnection solution that enables you to directly, securely and dynamically connect to distributed infrastructure and digital ecosystems on platform Equinix via a single port, Customers can use Fabric to connect to: </br> 1. Cloud Service Providers - Clouds, network and other service providers.  </br> 2. Enterprises - Other Equinix customers, vendors and partners.  </br> 3. Myself - Another customer instance deployed at Equinix. </br> </br> <b>Integrations (SDKs, Tools) links:</b> </br> <a href=\"https://deploy.equinix.com/labs/fabric-java\\\">Fabric Java SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-go\\\">Fabric Go SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-python\\\">Fabric Python SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-provider-equinix\\\">Equinix Terraform Provider</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-equinix-fabric\\\">Fabric Terraform Modules</a> </br> <a href=\"https://deploy.equinix.com/labs/pulumi-provider-equinix/\">Equinix Pulumi Provider</a> </br>

    Generated by OpenAPI Generator (https://openapi-generator.tech)
"""


import unittest

from equinix.services.fabricv4.api.routing_protocols_api import RoutingProtocolsApi


class TestRoutingProtocolsApi(unittest.TestCase):
    """RoutingProtocolsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = RoutingProtocolsApi()

    def tearDown(self) -> None:
        pass

    def test_create_connection_routing_protocol(self) -> None:
        """Test case for create_connection_routing_protocol

        Create Protocol
        """
        pass

    def test_create_connection_routing_protocols_in_bulk(self) -> None:
        """Test case for create_connection_routing_protocols_in_bulk

        Bulk Create Protocol
        """
        pass

    def test_delete_connection_routing_protocol_by_uuid(self) -> None:
        """Test case for delete_connection_routing_protocol_by_uuid

        Delete Protocol
        """
        pass

    def test_get_connection_routing_protocol_all_bgp_actions(self) -> None:
        """Test case for get_connection_routing_protocol_all_bgp_actions

        Get BGP Actions
        """
        pass

    def test_get_connection_routing_protocol_by_uuid(self) -> None:
        """Test case for get_connection_routing_protocol_by_uuid

        Get Protocol
        """
        pass

    def test_get_connection_routing_protocols(self) -> None:
        """Test case for get_connection_routing_protocols

        GetRoutingProtocols
        """
        pass

    def test_get_connection_routing_protocols_bgp_action_by_uuid(self) -> None:
        """Test case for get_connection_routing_protocols_bgp_action_by_uuid

        Get BGP Action
        """
        pass

    def test_get_connection_routing_protocols_change_by_uuid(self) -> None:
        """Test case for get_connection_routing_protocols_change_by_uuid

        Get Change By ID
        """
        pass

    def test_get_connection_routing_protocols_changes(self) -> None:
        """Test case for get_connection_routing_protocols_changes

        Get Changes
        """
        pass

    def test_patch_connection_routing_protocol_by_uuid(self) -> None:
        """Test case for patch_connection_routing_protocol_by_uuid

        Patch Protocol
        """
        pass

    def test_post_connection_routing_protocol_bgp_action_by_uuid(self) -> None:
        """Test case for post_connection_routing_protocol_bgp_action_by_uuid

        Clear/Reset BGP
        """
        pass

    def test_replace_connection_routing_protocol_by_uuid(self) -> None:
        """Test case for replace_connection_routing_protocol_by_uuid

        Replace Protocol
        """
        pass

    def test_validate_routing_protocol(self) -> None:
        """Test case for validate_routing_protocol

        Validate Subnet
        """
        pass


if __name__ == '__main__':
    unittest.main()
