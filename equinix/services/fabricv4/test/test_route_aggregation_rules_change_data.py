# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.fabricv4.models.route_aggregation_rules_change_data import RouteAggregationRulesChangeData

class TestRouteAggregationRulesChangeData(unittest.TestCase):
    """RouteAggregationRulesChangeData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RouteAggregationRulesChangeData:
        """Test RouteAggregationRulesChangeData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RouteAggregationRulesChangeData`
        """
        model = RouteAggregationRulesChangeData()
        if include_optional:
            return RouteAggregationRulesChangeData(
                status = 'COMPLETED',
                created_by = '',
                created_date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_by = '',
                updated_date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                data = equinix.services.fabricv4.models.route_aggregation_rules_change_operation.RouteAggregationRulesChangeOperation(
                    op = 'add', 
                    path = '/', 
                    value = equinix.services.fabricv4.models.route_aggregation_rules_base.RouteAggregationRulesBase(
                        name = 'Private-subnet-Aggregation', 
                        description = '', 
                        prefix = '192.168.0.0/24', ), ),
                uuid = '',
                type = 'BGP_IPv4_PREFIX_AGGREGATION_RULE_UPDATE',
                href = ''
            )
        else:
            return RouteAggregationRulesChangeData(
                uuid = '',
                type = 'BGP_IPv4_PREFIX_AGGREGATION_RULE_UPDATE',
        )
        """

    def testRouteAggregationRulesChangeData(self):
        """Test RouteAggregationRulesChangeData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
