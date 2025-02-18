# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)
"""

import unittest

from equinix.services.fabricv4.models.route_filters_base import RouteFiltersBase

class TestRouteFiltersBase(unittest.TestCase):
    """RouteFiltersBase unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RouteFiltersBase:
        """Test RouteFiltersBase
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RouteFiltersBase`
        """
        model = RouteFiltersBase()
        if include_optional:
            return RouteFiltersBase(
                type = 'BGP_IPv4_PREFIX_FILTER',
                name = 'My-direct-route-1',
                description = '',
                project = equinix.services.fabricv4.models.project.Project(
                    project_id = '44f4c4f8-2f39-494e-838c-d8e640591be5', )
            )
        else:
            return RouteFiltersBase(
                type = 'BGP_IPv4_PREFIX_FILTER',
                name = 'My-direct-route-1',
                project = equinix.services.fabricv4.models.project.Project(
                    project_id = '44f4c4f8-2f39-494e-838c-d8e640591be5', ),
        )
        """

    def testRouteFiltersBase(self):
        """Test RouteFiltersBase"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
