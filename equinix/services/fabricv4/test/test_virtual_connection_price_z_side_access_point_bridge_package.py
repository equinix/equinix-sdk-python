# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)
"""

import unittest

from equinix.services.fabricv4.models.virtual_connection_price_z_side_access_point_bridge_package import VirtualConnectionPriceZSideAccessPointBridgePackage

class TestVirtualConnectionPriceZSideAccessPointBridgePackage(unittest.TestCase):
    """VirtualConnectionPriceZSideAccessPointBridgePackage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VirtualConnectionPriceZSideAccessPointBridgePackage:
        """Test VirtualConnectionPriceZSideAccessPointBridgePackage
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VirtualConnectionPriceZSideAccessPointBridgePackage`
        """
        model = VirtualConnectionPriceZSideAccessPointBridgePackage()
        if include_optional:
            return VirtualConnectionPriceZSideAccessPointBridgePackage(
                code = 'REGIONAL'
            )
        else:
            return VirtualConnectionPriceZSideAccessPointBridgePackage(
        )
        """

    def testVirtualConnectionPriceZSideAccessPointBridgePackage(self):
        """Test VirtualConnectionPriceZSideAccessPointBridgePackage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
