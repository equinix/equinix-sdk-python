# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)
"""

import unittest

from equinix.services.fabricv4.models.route_aggregation_rules_base import RouteAggregationRulesBase

class TestRouteAggregationRulesBase(unittest.TestCase):
    """RouteAggregationRulesBase unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RouteAggregationRulesBase:
        """Test RouteAggregationRulesBase
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RouteAggregationRulesBase`
        """
        model = RouteAggregationRulesBase()
        if include_optional:
            return RouteAggregationRulesBase(
                name = 'Private-subnet-Aggregation',
                description = '',
                prefix = '192.168.0.0/24'
            )
        else:
            return RouteAggregationRulesBase(
                prefix = '192.168.0.0/24',
        )
        """

    def testRouteAggregationRulesBase(self):
        """Test RouteAggregationRulesBase"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
