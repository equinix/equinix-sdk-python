# coding: utf-8

"""
    Equinix Fabric API v4

    Equinix Fabric is an advanced software-defined interconnection solution that enables you to directly, securely and dynamically connect to distributed infrastructure and digital ecosystems on platform Equinix via a single port, Customers can use Fabric to connect to: </br> 1. Cloud Service Providers - Clouds, network and other service providers.  </br> 2. Enterprises - Other Equinix customers, vendors and partners.  </br> 3. Myself - Another customer instance deployed at Equinix. </br> </br> <b>Integrations (SDKs, Tools) links:</b> </br> <a href=\"https://deploy.equinix.com/labs/fabric-java\\\">Fabric Java SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-go\\\">Fabric Go SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-provider-equinix\\\">Equinix Terraform Provider</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-equinix-fabric\\\">Fabric Terraform Modules</a> </br> <a href=\"https://deploy.equinix.com/labs/pulumi-provider-equinix/\">Equinix Pulumi Provider</a> </br>

    The version of the OpenAPI document: 4.15
    Contact: api-support@equinix.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.fabricv4.api.route_filters_api import RouteFiltersApi


class TestRouteFiltersApi(unittest.TestCase):
    """RouteFiltersApi unit test stubs"""

    def setUp(self) -> None:
        self.api = RouteFiltersApi()

    def tearDown(self) -> None:
        pass

    def test_attach_connection_route_filter(self) -> None:
        """Test case for attach_connection_route_filter

        Attach Route Filter
        """
        pass

    def test_create_route_filter(self) -> None:
        """Test case for create_route_filter

        Create Route Filters
        """
        pass

    def test_delete_route_filter_by_uuid(self) -> None:
        """Test case for delete_route_filter_by_uuid

        Delete Route Filter
        """
        pass

    def test_detach_connection_route_filter(self) -> None:
        """Test case for detach_connection_route_filter

        Detach Route Filter
        """
        pass

    def test_get_connection_route_filter_by_uuid(self) -> None:
        """Test case for get_connection_route_filter_by_uuid

        Get Route Filter
        """
        pass

    def test_get_connection_route_filters(self) -> None:
        """Test case for get_connection_route_filters

        Get All RouteFilters
        """
        pass

    def test_get_route_filter_by_uuid(self) -> None:
        """Test case for get_route_filter_by_uuid

        Get Filter By UUID
        """
        pass

    def test_get_route_filter_change_by_uuid(self) -> None:
        """Test case for get_route_filter_change_by_uuid

        Get Change By ID
        """
        pass

    def test_get_route_filter_changes(self) -> None:
        """Test case for get_route_filter_changes

        Get All Changes
        """
        pass

    def test_get_route_filter_connections(self) -> None:
        """Test case for get_route_filter_connections

        Get Connections
        """
        pass

    def test_patch_route_filter_by_uuid(self) -> None:
        """Test case for patch_route_filter_by_uuid

        Patch Route Filter
        """
        pass

    def test_search_route_filters(self) -> None:
        """Test case for search_route_filters

        Search Route Filters
        """
        pass


if __name__ == '__main__':
    unittest.main()
