# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)
"""

import unittest

from equinix.services.fabricv4.models.route_filters_patch_request_item import RouteFiltersPatchRequestItem

class TestRouteFiltersPatchRequestItem(unittest.TestCase):
    """RouteFiltersPatchRequestItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RouteFiltersPatchRequestItem:
        """Test RouteFiltersPatchRequestItem
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RouteFiltersPatchRequestItem`
        """
        model = RouteFiltersPatchRequestItem()
        if include_optional:
            return RouteFiltersPatchRequestItem(
                op = 'replace',
                path = '/name',
                value = None
            )
        else:
            return RouteFiltersPatchRequestItem(
                op = 'replace',
                path = '/name',
                value = None,
        )
        """

    def testRouteFiltersPatchRequestItem(self):
        """Test RouteFiltersPatchRequestItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
