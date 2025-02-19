# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.fabricv4.models.get_route_aggregation_get_connections_response import GetRouteAggregationGetConnectionsResponse

class TestGetRouteAggregationGetConnectionsResponse(unittest.TestCase):
    """GetRouteAggregationGetConnectionsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetRouteAggregationGetConnectionsResponse:
        """Test GetRouteAggregationGetConnectionsResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetRouteAggregationGetConnectionsResponse`
        """
        model = GetRouteAggregationGetConnectionsResponse()
        if include_optional:
            return GetRouteAggregationGetConnectionsResponse(
                pagination = equinix.services.fabricv4.models.pagination.Pagination(
                    offset = 0, 
                    limit = 0, 
                    total = 0, 
                    next = '', 
                    previous = '', ),
                data = [
                    equinix.services.fabricv4.models.route_aggregation_connections_data.RouteAggregationConnectionsData(
                        href = 'https://api.equinix.com/fabric/v4/connections/81331c52-04c0-4656-a4a7-18c52669348f', 
                        type = 'EVPL_VC', 
                        uuid = '695a8471-6595-4ac6-a2f4-b3d96ed3a59d', 
                        name = 'connection-1', )
                    ]
            )
        else:
            return GetRouteAggregationGetConnectionsResponse(
        )
        """

    def testGetRouteAggregationGetConnectionsResponse(self):
        """Test GetRouteAggregationGetConnectionsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
