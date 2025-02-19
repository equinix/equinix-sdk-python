# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.fabricv4.models.route_filter_rules_change_data import RouteFilterRulesChangeData

class TestRouteFilterRulesChangeData(unittest.TestCase):
    """RouteFilterRulesChangeData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RouteFilterRulesChangeData:
        """Test RouteFilterRulesChangeData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RouteFilterRulesChangeData`
        """
        model = RouteFilterRulesChangeData()
        if include_optional:
            return RouteFilterRulesChangeData(
                status = 'COMPLETED',
                created_by = '',
                created_date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_by = '',
                updated_date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                data = equinix.services.fabricv4.models.route_filter_rules_change_operation.RouteFilterRulesChangeOperation(
                    op = 'add', 
                    path = '/', 
                    value = equinix.services.fabricv4.models.route_filter_rules_base.RouteFilterRulesBase(
                        name = 'Private-subnet-filter', 
                        description = '', 
                        prefix = '192.168.0.0/24', 
                        prefix_match = 'orlonger', ), ),
                uuid = '',
                type = 'BGP_IPv4_PREFIX_FILTER_RULE_UPDATE',
                href = ''
            )
        else:
            return RouteFilterRulesChangeData(
                uuid = '',
                type = 'BGP_IPv4_PREFIX_FILTER_RULE_UPDATE',
        )
        """

    def testRouteFilterRulesChangeData(self):
        """Test RouteFilterRulesChangeData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
