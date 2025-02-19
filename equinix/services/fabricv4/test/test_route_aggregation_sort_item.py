# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.fabricv4.models.route_aggregation_sort_item import RouteAggregationSortItem

class TestRouteAggregationSortItem(unittest.TestCase):
    """RouteAggregationSortItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RouteAggregationSortItem:
        """Test RouteAggregationSortItem
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RouteAggregationSortItem`
        """
        model = RouteAggregationSortItem()
        if include_optional:
            return RouteAggregationSortItem(
                var_property = '/changeLog/updatedDateTime',
                direction = 'DESC'
            )
        else:
            return RouteAggregationSortItem(
        )
        """

    def testRouteAggregationSortItem(self):
        """Test RouteAggregationSortItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
