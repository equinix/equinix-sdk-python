# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.fabricv4.models.routing_protocol_data import RoutingProtocolData

class TestRoutingProtocolData(unittest.TestCase):
    """RoutingProtocolData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RoutingProtocolData:
        """Test RoutingProtocolData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RoutingProtocolData`
        """
        model = RoutingProtocolData()
        if include_optional:
            return RoutingProtocolData(
                type = 'BGP',
                name = 'My-direct-route-1',
                bgp_ipv4 = equinix.services.fabricv4.models.bgp_connection_ipv4.BGPConnectionIpv4(
                    customer_peer_ip = '10.1.1.2', 
                    equinix_peer_ip = '10.1.1.3', 
                    enabled = True, 
                    outbound_as_prepend_count = 3, 
                    inbound_med = 1000, 
                    outbound_med = 2000, 
                    routes_max = 1000, 
                    operation = equinix.services.fabricv4.models.bgp_connection_operation.BGPConnectionOperation(
                        operational_status = 'UP', 
                        op_status_changed_at = '2021-10-30T07:21:39Z', ), ),
                bgp_ipv6 = equinix.services.fabricv4.models.bgp_connection_ipv6.BGPConnectionIpv6(
                    customer_peer_ip = '2001:db8:c59b::1', 
                    equinix_peer_ip = '2001:db8:c59b::1', 
                    enabled = True, 
                    outbound_as_prepend_count = 3, 
                    inbound_med = 1000, 
                    outbound_med = 2000, 
                    routes_max = 1000, 
                    operation = equinix.services.fabricv4.models.bgp_connection_operation.BGPConnectionOperation(
                        operational_status = 'UP', 
                        op_status_changed_at = '2021-10-30T07:21:39Z', ), ),
                customer_asn = 65002,
                equinix_asn = 65002,
                bgp_auth_key = 'testAuthKey',
                as_override_enabled = True,
                bfd = equinix.services.fabricv4.models.routing_protocol_bfd.RoutingProtocolBFD(
                    enabled = True, 
                    interval = '100', ),
                href = 'https://api.equinix.com/fabric/v4/connections/81331c52-04c0-4656-a4a7-18c52669348f/routingProtocols/69762051-85ed-4d13-b6b4-e32e93c672b5',
                uuid = 'c9b8e7a2-f3b1-4576-a4a9-1366a63df170',
                state = 'PROVISIONED',
                operation = equinix.services.fabricv4.models.routing_protocol_operation.RoutingProtocolOperation(
                    errors = [
                        equinix.services.fabricv4.models.error.Error(
                            error_code = 'EQ-0480728', 
                            error_message = '', 
                            correlation_id = '', 
                            details = '', 
                            help = '', 
                            additional_info = [
                                equinix.services.fabricv4.models.price_error_additional_info.PriceError_additionalInfo(
                                    property = '', 
                                    reason = '', )
                                ], )
                        ], ),
                change = equinix.services.fabricv4.models.routing_protocol_change.RoutingProtocolChange(
                    uuid = '', 
                    type = 'ROUTING_PROTOCOL_UPDATE', 
                    href = '', ),
                changelog = equinix.services.fabricv4.models.changelog.Changelog(
                    created_by = 'johnsmith', 
                    created_by_full_name = 'John Smith', 
                    created_by_email = 'john.smith@example.com', 
                    created_date_time = '2020-11-06T07:00Z', 
                    updated_by = 'johnsmith', 
                    updated_by_full_name = 'John Smith', 
                    updated_by_email = 'john.smith@example.com', 
                    updated_date_time = '2020-11-06T07:00Z', 
                    deleted_by = 'johnsmith', 
                    deleted_by_full_name = 'John Smith', 
                    deleted_by_email = 'john.smith@example.com', 
                    deleted_date_time = '2020-11-06T07:00Z', ),
                direct_ipv4 = equinix.services.fabricv4.models.direct_connection_ipv4.DirectConnectionIpv4(
                    equinix_iface_ip = '192.168.100.0/30', ),
                direct_ipv6 = equinix.services.fabricv4.models.direct_connection_ipv6.DirectConnectionIpv6(
                    equinix_iface_ip = '2001:db8:c59b::/1', )
            )
        else:
            return RoutingProtocolData(
        )
        """

    def testRoutingProtocolData(self):
        """Test RoutingProtocolData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
