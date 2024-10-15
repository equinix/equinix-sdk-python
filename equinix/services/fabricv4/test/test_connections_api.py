# coding: utf-8

"""
    Equinix Fabric API v4

    Equinix Fabric is an advanced software-defined interconnection solution that enables you to directly, securely and dynamically connect to distributed infrastructure and digital ecosystems on platform Equinix via a single port, Customers can use Fabric to connect to: </br> 1. Cloud Service Providers - Clouds, network and other service providers.  </br> 2. Enterprises - Other Equinix customers, vendors and partners.  </br> 3. Myself - Another customer instance deployed at Equinix. </br> </br> <b>Integrations (SDKs, Tools) links:</b> </br> <a href=\"https://deploy.equinix.com/labs/fabric-java\\\">Fabric Java SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-go\\\">Fabric Go SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-python\\\">Fabric Python SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-provider-equinix\\\">Equinix Terraform Provider</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-equinix-fabric\\\">Fabric Terraform Modules</a> </br> <a href=\"https://deploy.equinix.com/labs/pulumi-provider-equinix/\">Equinix Pulumi Provider</a> </br>

    The version of the OpenAPI document: 4.17
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.fabricv4.api.connections_api import ConnectionsApi


class TestConnectionsApi(unittest.TestCase):
    """ConnectionsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ConnectionsApi()

    def tearDown(self) -> None:
        pass

    def test_create_connection(self) -> None:
        """Test case for create_connection

        Create Connection
        """
        pass

    def test_create_connection_action(self) -> None:
        """Test case for create_connection_action

        Connection Actions
        """
        pass

    def test_delete_connection_by_uuid(self) -> None:
        """Test case for delete_connection_by_uuid

        Delete by ID
        """
        pass

    def test_get_connection_by_uuid(self) -> None:
        """Test case for get_connection_by_uuid

        Get Connection by ID
        """
        pass

    def test_search_connections(self) -> None:
        """Test case for search_connections

        Search connections
        """
        pass

    def test_update_connection_by_uuid(self) -> None:
        """Test case for update_connection_by_uuid

        Update by ID
        """
        pass

    def test_validate_connections(self) -> None:
        """Test case for validate_connections

        Validate Connection
        """
        pass


if __name__ == '__main__':
    unittest.main()
