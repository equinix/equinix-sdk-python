# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.fabricv4.models.bgp_connection_ipv6 import BGPConnectionIpv6

class TestBGPConnectionIpv6(unittest.TestCase):
    """BGPConnectionIpv6 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BGPConnectionIpv6:
        """Test BGPConnectionIpv6
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BGPConnectionIpv6`
        """
        model = BGPConnectionIpv6()
        if include_optional:
            return BGPConnectionIpv6(
                customer_peer_ip = '2001:db8:c59b::1',
                equinix_peer_ip = '2001:db8:c59b::1',
                enabled = True,
                outbound_as_prepend_count = 3,
                inbound_med = 1000,
                outbound_med = 2000,
                routes_max = 1000,
                operation = equinix.services.fabricv4.models.bgp_connection_operation.BGPConnectionOperation(
                    operational_status = 'UP', 
                    op_status_changed_at = '2021-10-30T07:21:39Z', )
            )
        else:
            return BGPConnectionIpv6(
                customer_peer_ip = '2001:db8:c59b::1',
                enabled = True,
        )
        """

    def testBGPConnectionIpv6(self):
        """Test BGPConnectionIpv6"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
