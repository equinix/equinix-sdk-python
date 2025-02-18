# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)
"""

import unittest

from equinix.services.fabricv4.models.cloud_router_action_request import CloudRouterActionRequest

class TestCloudRouterActionRequest(unittest.TestCase):
    """CloudRouterActionRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CloudRouterActionRequest:
        """Test CloudRouterActionRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CloudRouterActionRequest`
        """
        model = CloudRouterActionRequest()
        if include_optional:
            return CloudRouterActionRequest(
                type = 'BGP_SESSION_STATUS_UPDATE',
                connection = equinix.services.fabricv4.models.router_actions_connection.RouterActionsConnection(
                    uuid = '557400f8-d360-11e9-bb65-2a2ae2dbcce4', )
            )
        else:
            return CloudRouterActionRequest(
                type = 'BGP_SESSION_STATUS_UPDATE',
        )
        """

    def testCloudRouterActionRequest(self):
        """Test CloudRouterActionRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
