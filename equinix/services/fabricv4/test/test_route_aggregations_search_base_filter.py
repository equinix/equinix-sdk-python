# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)
"""

import unittest

from equinix.services.fabricv4.models.route_aggregations_search_base_filter import RouteAggregationsSearchBaseFilter

class TestRouteAggregationsSearchBaseFilter(unittest.TestCase):
    """RouteAggregationsSearchBaseFilter unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RouteAggregationsSearchBaseFilter:
        """Test RouteAggregationsSearchBaseFilter
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RouteAggregationsSearchBaseFilter`
        """
        model = RouteAggregationsSearchBaseFilter()
        if include_optional:
            return RouteAggregationsSearchBaseFilter(
                var_and = [
                    equinix.services.fabricv4.models.route_aggregations_search_filter_item.RouteAggregationsSearchFilterItem(
                        property = '/type', 
                        operator = '', 
                        values = [
                            ''
                            ], )
                    ]
            )
        else:
            return RouteAggregationsSearchBaseFilter(
        )
        """

    def testRouteAggregationsSearchBaseFilter(self):
        """Test RouteAggregationsSearchBaseFilter"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
