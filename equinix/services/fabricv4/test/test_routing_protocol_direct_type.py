# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.fabricv4.models.routing_protocol_direct_type import RoutingProtocolDirectType

class TestRoutingProtocolDirectType(unittest.TestCase):
    """RoutingProtocolDirectType unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RoutingProtocolDirectType:
        """Test RoutingProtocolDirectType
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RoutingProtocolDirectType`
        """
        model = RoutingProtocolDirectType()
        if include_optional:
            return RoutingProtocolDirectType(
                type = 'DIRECT',
                name = 'My-direct-route-1',
                direct_ipv4 = equinix.services.fabricv4.models.direct_connection_ipv4.DirectConnectionIpv4(
                    equinix_iface_ip = '192.168.100.0/30', ),
                direct_ipv6 = equinix.services.fabricv4.models.direct_connection_ipv6.DirectConnectionIpv6(
                    equinix_iface_ip = '2001:db8:c59b::/1', )
            )
        else:
            return RoutingProtocolDirectType(
                type = 'DIRECT',
        )
        """

    def testRoutingProtocolDirectType(self):
        """Test RoutingProtocolDirectType"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
