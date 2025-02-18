# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)
"""

import unittest

from equinix.services.fabricv4.api.route_aggregations_api import RouteAggregationsApi


class TestRouteAggregationsApi(unittest.TestCase):
    """RouteAggregationsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = RouteAggregationsApi()

    def tearDown(self) -> None:
        pass

    def test_attach_connection_route_aggregation(self) -> None:
        """Test case for attach_connection_route_aggregation

        Attach Aggregation
        """
        pass

    def test_create_route_aggregation(self) -> None:
        """Test case for create_route_aggregation

        Create Aggregations
        """
        pass

    def test_delete_route_aggregation_by_uuid(self) -> None:
        """Test case for delete_route_aggregation_by_uuid

        Delete Aggregation
        """
        pass

    def test_detach_connection_route_aggregation(self) -> None:
        """Test case for detach_connection_route_aggregation

        Detach Aggregation
        """
        pass

    def test_get_connection_route_aggregation_by_uuid(self) -> None:
        """Test case for get_connection_route_aggregation_by_uuid

        Get Aggregation
        """
        pass

    def test_get_connection_route_aggregations(self) -> None:
        """Test case for get_connection_route_aggregations

        Get All Aggregations
        """
        pass

    def test_get_route_aggregation_by_uuid(self) -> None:
        """Test case for get_route_aggregation_by_uuid

        Get Aggregation
        """
        pass

    def test_get_route_aggregation_change_by_uuid(self) -> None:
        """Test case for get_route_aggregation_change_by_uuid

        Get Change By ID
        """
        pass

    def test_get_route_aggregation_changes(self) -> None:
        """Test case for get_route_aggregation_changes

        Get All Changes
        """
        pass

    def test_get_route_aggregation_connections(self) -> None:
        """Test case for get_route_aggregation_connections

        Get All Connections on Route Aggregation
        """
        pass

    def test_patch_route_aggregation_by_uuid(self) -> None:
        """Test case for patch_route_aggregation_by_uuid

        Patch Aggregation
        """
        pass

    def test_search_route_aggregations(self) -> None:
        """Test case for search_route_aggregations

        Search Aggregations
        """
        pass


if __name__ == '__main__':
    unittest.main()
