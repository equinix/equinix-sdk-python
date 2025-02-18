# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)
"""

import unittest

from equinix.services.fabricv4.models.virtual_connection_price import VirtualConnectionPrice

class TestVirtualConnectionPrice(unittest.TestCase):
    """VirtualConnectionPrice unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VirtualConnectionPrice:
        """Test VirtualConnectionPrice
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VirtualConnectionPrice`
        """
        model = VirtualConnectionPrice()
        if include_optional:
            return VirtualConnectionPrice(
                uuid = '',
                type = 'EVPL_VC',
                bandwidth = 0,
                a_side = equinix.services.fabricv4.models.virtual_connection_price_a_side.VirtualConnectionPriceASide(
                    access_point = equinix.services.fabricv4.models.virtual_connection_price_a_side_access_point.VirtualConnectionPriceASide_accessPoint(
                        uuid = '', 
                        type = 'VD', 
                        location = equinix.services.fabricv4.models.price_location.PriceLocation(
                            metro_code = '', 
                            ibx = '', ), 
                        port = equinix.services.fabricv4.models.virtual_connection_price_a_side_access_point_port.VirtualConnectionPriceASide_accessPoint_port(
                            settings = equinix.services.fabricv4.models.virtual_connection_price_a_side_access_point_port_settings.VirtualConnectionPriceASide_accessPoint_port_settings(
                                buyout = True, ), ), ), ),
                z_side = equinix.services.fabricv4.models.virtual_connection_price_z_side.VirtualConnectionPriceZSide(
                    access_point = equinix.services.fabricv4.models.virtual_connection_price_z_side_access_point.VirtualConnectionPriceZSide_accessPoint(
                        uuid = '', 
                        type = 'VD', 
                        location = equinix.services.fabricv4.models.price_location.PriceLocation(
                            metro_code = '', 
                            ibx = '', ), 
                        port = equinix.services.fabricv4.models.virtual_connection_price_a_side_access_point_port.VirtualConnectionPriceASide_accessPoint_port(
                            settings = equinix.services.fabricv4.models.virtual_connection_price_a_side_access_point_port_settings.VirtualConnectionPriceASide_accessPoint_port_settings(
                                buyout = True, ), ), 
                        profile = equinix.services.fabricv4.models.virtual_connection_price_z_side_access_point_profile.VirtualConnectionPriceZSide_accessPoint_profile(
                            uuid = '', ), 
                        bridge = equinix.services.fabricv4.models.virtual_connection_price_z_side_access_point_bridge.VirtualConnectionPriceZSide_accessPoint_bridge(
                            package = equinix.services.fabricv4.models.virtual_connection_price_z_side_access_point_bridge_package.VirtualConnectionPriceZSide_accessPoint_bridge_package(
                                code = 'REGIONAL', ), ), ), )
            )
        else:
            return VirtualConnectionPrice(
        )
        """

    def testVirtualConnectionPrice(self):
        """Test VirtualConnectionPrice"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
