# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.fabricv4.models.virtual_connection_price_a_side import VirtualConnectionPriceASide

class TestVirtualConnectionPriceASide(unittest.TestCase):
    """VirtualConnectionPriceASide unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VirtualConnectionPriceASide:
        """Test VirtualConnectionPriceASide
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VirtualConnectionPriceASide`
        """
        model = VirtualConnectionPriceASide()
        if include_optional:
            return VirtualConnectionPriceASide(
                access_point = equinix.services.fabricv4.models.virtual_connection_price_a_side_access_point.VirtualConnectionPriceASide_accessPoint(
                    uuid = '', 
                    type = 'VD', 
                    location = equinix.services.fabricv4.models.price_location.PriceLocation(
                        metro_code = '', 
                        ibx = '', ), 
                    port = equinix.services.fabricv4.models.virtual_connection_price_a_side_access_point_port.VirtualConnectionPriceASide_accessPoint_port(
                        settings = equinix.services.fabricv4.models.virtual_connection_price_a_side_access_point_port_settings.VirtualConnectionPriceASide_accessPoint_port_settings(
                            buyout = True, ), ), )
            )
        else:
            return VirtualConnectionPriceASide(
        )
        """

    def testVirtualConnectionPriceASide(self):
        """Test VirtualConnectionPriceASide"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
