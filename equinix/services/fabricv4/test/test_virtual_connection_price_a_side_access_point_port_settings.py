# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)
"""

import unittest

from equinix.services.fabricv4.models.virtual_connection_price_a_side_access_point_port_settings import VirtualConnectionPriceASideAccessPointPortSettings

class TestVirtualConnectionPriceASideAccessPointPortSettings(unittest.TestCase):
    """VirtualConnectionPriceASideAccessPointPortSettings unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VirtualConnectionPriceASideAccessPointPortSettings:
        """Test VirtualConnectionPriceASideAccessPointPortSettings
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VirtualConnectionPriceASideAccessPointPortSettings`
        """
        model = VirtualConnectionPriceASideAccessPointPortSettings()
        if include_optional:
            return VirtualConnectionPriceASideAccessPointPortSettings(
                buyout = True
            )
        else:
            return VirtualConnectionPriceASideAccessPointPortSettings(
        )
        """

    def testVirtualConnectionPriceASideAccessPointPortSettings(self):
        """Test VirtualConnectionPriceASideAccessPointPortSettings"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
