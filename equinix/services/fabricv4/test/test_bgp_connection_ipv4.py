# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)
"""

import unittest

from equinix.services.fabricv4.models.bgp_connection_ipv4 import BGPConnectionIpv4

class TestBGPConnectionIpv4(unittest.TestCase):
    """BGPConnectionIpv4 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BGPConnectionIpv4:
        """Test BGPConnectionIpv4
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BGPConnectionIpv4`
        """
        model = BGPConnectionIpv4()
        if include_optional:
            return BGPConnectionIpv4(
                customer_peer_ip = '10.1.1.2',
                equinix_peer_ip = '10.1.1.3',
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
            return BGPConnectionIpv4(
                customer_peer_ip = '10.1.1.2',
                enabled = True,
        )
        """

    def testBGPConnectionIpv4(self):
        """Test BGPConnectionIpv4"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
