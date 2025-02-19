# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.fabricv4.models.cloud_router_actions_search_expression import CloudRouterActionsSearchExpression

class TestCloudRouterActionsSearchExpression(unittest.TestCase):
    """CloudRouterActionsSearchExpression unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CloudRouterActionsSearchExpression:
        """Test CloudRouterActionsSearchExpression
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CloudRouterActionsSearchExpression`
        """
        model = CloudRouterActionsSearchExpression()
        if include_optional:
            return CloudRouterActionsSearchExpression(
                var_property = '/type',
                operator = '=',
                values = [
                    'ROUTE_TABLE_ENTRY_UPDATE'
                    ]
            )
        else:
            return CloudRouterActionsSearchExpression(
        )
        """

    def testCloudRouterActionsSearchExpression(self):
        """Test CloudRouterActionsSearchExpression"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
