# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.fabricv4.models.cloud_router_simple_expression import CloudRouterSimpleExpression

class TestCloudRouterSimpleExpression(unittest.TestCase):
    """CloudRouterSimpleExpression unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CloudRouterSimpleExpression:
        """Test CloudRouterSimpleExpression
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CloudRouterSimpleExpression`
        """
        model = CloudRouterSimpleExpression()
        if include_optional:
            return CloudRouterSimpleExpression(
                var_property = '/name',
                operator = '=',
                values = [
                    'FabricCloudRouter-1'
                    ]
            )
        else:
            return CloudRouterSimpleExpression(
        )
        """

    def testCloudRouterSimpleExpression(self):
        """Test CloudRouterSimpleExpression"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
