# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)
"""

import unittest

from equinix.services.fabricv4.models.fabric_cloud_router_packages import FabricCloudRouterPackages

class TestFabricCloudRouterPackages(unittest.TestCase):
    """FabricCloudRouterPackages unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FabricCloudRouterPackages:
        """Test FabricCloudRouterPackages
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FabricCloudRouterPackages`
        """
        model = FabricCloudRouterPackages()
        if include_optional:
            return FabricCloudRouterPackages(
                code = 'LAB'
            )
        else:
            return FabricCloudRouterPackages(
        )
        """

    def testFabricCloudRouterPackages(self):
        """Test FabricCloudRouterPackages"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
