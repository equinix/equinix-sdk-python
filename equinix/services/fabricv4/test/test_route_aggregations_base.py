# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.fabricv4.models.route_aggregations_base import RouteAggregationsBase

class TestRouteAggregationsBase(unittest.TestCase):
    """RouteAggregationsBase unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RouteAggregationsBase:
        """Test RouteAggregationsBase
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RouteAggregationsBase`
        """
        model = RouteAggregationsBase()
        if include_optional:
            return RouteAggregationsBase(
                type = 'BGP_IPv4_PREFIX_AGGREGATION',
                name = 'My-direct-route-1',
                description = '',
                project = equinix.services.fabricv4.models.project.Project(
                    project_id = '44f4c4f8-2f39-494e-838c-d8e640591be5', )
            )
        else:
            return RouteAggregationsBase(
                type = 'BGP_IPv4_PREFIX_AGGREGATION',
                name = 'My-direct-route-1',
                project = equinix.services.fabricv4.models.project.Project(
                    project_id = '44f4c4f8-2f39-494e-838c-d8e640591be5', ),
        )
        """

    def testRouteAggregationsBase(self):
        """Test RouteAggregationsBase"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
