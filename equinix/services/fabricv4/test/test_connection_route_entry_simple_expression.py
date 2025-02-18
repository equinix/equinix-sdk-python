# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)
"""

import unittest

from equinix.services.fabricv4.models.connection_route_entry_simple_expression import ConnectionRouteEntrySimpleExpression

class TestConnectionRouteEntrySimpleExpression(unittest.TestCase):
    """ConnectionRouteEntrySimpleExpression unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConnectionRouteEntrySimpleExpression:
        """Test ConnectionRouteEntrySimpleExpression
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConnectionRouteEntrySimpleExpression`
        """
        model = ConnectionRouteEntrySimpleExpression()
        if include_optional:
            return ConnectionRouteEntrySimpleExpression(
                var_property = '/type',
                operator = '=',
                values = [
                    'IPv4_BGP_ROUTE'
                    ]
            )
        else:
            return ConnectionRouteEntrySimpleExpression(
        )
        """

    def testConnectionRouteEntrySimpleExpression(self):
        """Test ConnectionRouteEntrySimpleExpression"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
