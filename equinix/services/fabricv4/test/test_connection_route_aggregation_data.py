# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.fabricv4.models.connection_route_aggregation_data import ConnectionRouteAggregationData

class TestConnectionRouteAggregationData(unittest.TestCase):
    """ConnectionRouteAggregationData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConnectionRouteAggregationData:
        """Test ConnectionRouteAggregationData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConnectionRouteAggregationData`
        """
        model = ConnectionRouteAggregationData()
        if include_optional:
            return ConnectionRouteAggregationData(
                href = 'https://api.equinix.com/fabric/v4/connections/81331c52-04c0-4656-a4a7-18c52669348f/routeAggregations/695a8471-6595-4ac6-a2f4-b3d96ed3a59d',
                type = 'BGP_IPv4_PREFIX_AGGREGATION',
                uuid = '695a8471-6595-4ac6-a2f4-b3d96ed3a59d',
                attachment_status = 'ATTACHING'
            )
        else:
            return ConnectionRouteAggregationData(
        )
        """

    def testConnectionRouteAggregationData(self):
        """Test ConnectionRouteAggregationData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
