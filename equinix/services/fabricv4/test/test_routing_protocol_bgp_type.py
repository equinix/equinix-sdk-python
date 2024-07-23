# coding: utf-8

"""
    Equinix Fabric API v4

    Equinix Fabric is an advanced software-defined interconnection solution that enables you to directly, securely and dynamically connect to distributed infrastructure and digital ecosystems on platform Equinix via a single port, Customers can use Fabric to connect to: </br> 1. Cloud Service Providers - Clouds, network and other service providers.  </br> 2. Enterprises - Other Equinix customers, vendors and partners.  </br> 3. Myself - Another customer instance deployed at Equinix. </br> </br> <b>Integrations (SDKs, Tools) links:</b> </br> <a href=\"https://deploy.equinix.com/labs/fabric-java\\\">Fabric Java SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-go\\\">Fabric Go SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-provider-equinix\\\">Equinix Terraform Provider</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-equinix-fabric\\\">Fabric Terraform Modules</a> </br> <a href=\"https://deploy.equinix.com/labs/pulumi-provider-equinix/\">Equinix Pulumi Provider</a> </br>

    The version of the OpenAPI document: 4.14
    Contact: api-support@equinix.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.fabricv4.models.routing_protocol_bgp_type import RoutingProtocolBGPType

class TestRoutingProtocolBGPType(unittest.TestCase):
    """RoutingProtocolBGPType unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RoutingProtocolBGPType:
        """Test RoutingProtocolBGPType
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RoutingProtocolBGPType`
        """
        model = RoutingProtocolBGPType()
        if include_optional:
            return RoutingProtocolBGPType(
                type = 'BGP',
                name = 'My-BGP-route-1',
                bgp_ipv4 = equinix.services.fabricv4.models.bgp_connection_ipv4.BGPConnectionIpv4(
                    customer_peer_ip = '10.1.1.2', 
                    equinix_peer_ip = '10.1.1.3', 
                    enabled = True, 
                    outbound_as_prepend_count = 3, 
                    operation = equinix.services.fabricv4.models.bgp_connection_operation.BGPConnectionOperation(
                        operational_status = 'UP', 
                        op_status_changed_at = '2021-10-30T07:21:39Z', ), ),
                bgp_ipv6 = equinix.services.fabricv4.models.bgp_connection_ipv6.BGPConnectionIpv6(
                    customer_peer_ip = '2001:db8:c59b::1', 
                    equinix_peer_ip = '2001:db8:c59b::1', 
                    enabled = True, 
                    outbound_as_prepend_count = 3, 
                    operation = equinix.services.fabricv4.models.bgp_connection_operation.BGPConnectionOperation(
                        operational_status = 'UP', 
                        op_status_changed_at = '2021-10-30T07:21:39Z', ), ),
                customer_asn = 56,
                equinix_asn = 56,
                bgp_auth_key = '',
                bfd = equinix.services.fabricv4.models.routing_protocol_bfd.RoutingProtocolBFD(
                    enabled = True, 
                    interval = '100', )
            )
        else:
            return RoutingProtocolBGPType(
                type = 'BGP',
        )
        """

    def testRoutingProtocolBGPType(self):
        """Test RoutingProtocolBGPType"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
