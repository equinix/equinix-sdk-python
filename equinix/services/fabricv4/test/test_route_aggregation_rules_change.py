# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)
"""

import unittest

from equinix.services.fabricv4.models.route_aggregation_rules_change import RouteAggregationRulesChange

class TestRouteAggregationRulesChange(unittest.TestCase):
    """RouteAggregationRulesChange unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RouteAggregationRulesChange:
        """Test RouteAggregationRulesChange
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RouteAggregationRulesChange`
        """
        model = RouteAggregationRulesChange()
        if include_optional:
            return RouteAggregationRulesChange(
                uuid = '',
                type = 'BGP_IPv4_PREFIX_AGGREGATION_RULE_UPDATE',
                href = ''
            )
        else:
            return RouteAggregationRulesChange(
                uuid = '',
                type = 'BGP_IPv4_PREFIX_AGGREGATION_RULE_UPDATE',
        )
        """

    def testRouteAggregationRulesChange(self):
        """Test RouteAggregationRulesChange"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
