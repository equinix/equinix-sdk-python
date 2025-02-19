# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.fabricv4.models.cloud_router_post_request_package import CloudRouterPostRequestPackage

class TestCloudRouterPostRequestPackage(unittest.TestCase):
    """CloudRouterPostRequestPackage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CloudRouterPostRequestPackage:
        """Test CloudRouterPostRequestPackage
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CloudRouterPostRequestPackage`
        """
        model = CloudRouterPostRequestPackage()
        if include_optional:
            return CloudRouterPostRequestPackage(
                href = 'https://api.equinix.com/fabric/v4/routerPackages/LAB',
                type = 'ROUTER_PACKAGE',
                code = 'LAB'
            )
        else:
            return CloudRouterPostRequestPackage(
                code = 'LAB',
        )
        """

    def testCloudRouterPostRequestPackage(self):
        """Test CloudRouterPostRequestPackage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
