# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.fabricv4.models.connection_route_entry_filters import ConnectionRouteEntryFilters

class TestConnectionRouteEntryFilters(unittest.TestCase):
    """ConnectionRouteEntryFilters unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConnectionRouteEntryFilters:
        """Test ConnectionRouteEntryFilters
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConnectionRouteEntryFilters`
        """
        model = ConnectionRouteEntryFilters()
        if include_optional:
            return ConnectionRouteEntryFilters(
                var_and = [
                    equinix.services.fabricv4.models.connection_route_entry_filter.ConnectionRouteEntryFilter()
                    ]
            )
        else:
            return ConnectionRouteEntryFilters(
        )
        """

    def testConnectionRouteEntryFilters(self):
        """Test ConnectionRouteEntryFilters"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
