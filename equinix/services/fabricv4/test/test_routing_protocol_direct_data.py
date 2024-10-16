# coding: utf-8

"""
    Equinix Fabric API v4

    Equinix Fabric is an advanced software-defined interconnection solution that enables you to directly, securely and dynamically connect to distributed infrastructure and digital ecosystems on platform Equinix via a single port, Customers can use Fabric to connect to: </br> 1. Cloud Service Providers - Clouds, network and other service providers.  </br> 2. Enterprises - Other Equinix customers, vendors and partners.  </br> 3. Myself - Another customer instance deployed at Equinix. </br> </br> <b>Integrations (SDKs, Tools) links:</b> </br> <a href=\"https://deploy.equinix.com/labs/fabric-java\\\">Fabric Java SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-go\\\">Fabric Go SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-python\\\">Fabric Python SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-provider-equinix\\\">Equinix Terraform Provider</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-equinix-fabric\\\">Fabric Terraform Modules</a> </br> <a href=\"https://deploy.equinix.com/labs/pulumi-provider-equinix/\">Equinix Pulumi Provider</a> </br>

    The version of the OpenAPI document: 4.17
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.fabricv4.models.routing_protocol_direct_data import RoutingProtocolDirectData

class TestRoutingProtocolDirectData(unittest.TestCase):
    """RoutingProtocolDirectData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RoutingProtocolDirectData:
        """Test RoutingProtocolDirectData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RoutingProtocolDirectData`
        """
        model = RoutingProtocolDirectData()
        if include_optional:
            return RoutingProtocolDirectData(
                type = 'DIRECT',
                name = 'My-direct-route-1',
                direct_ipv4 = equinix.services.fabricv4.models.direct_connection_ipv4.DirectConnectionIpv4(
                    equinix_iface_ip = '192.168.100.0/30', ),
                direct_ipv6 = equinix.services.fabricv4.models.direct_connection_ipv6.DirectConnectionIpv6(
                    equinix_iface_ip = '2001:db8:c59b::/1', ),
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
                    deleted_date_time = '2020-11-06T07:00Z', )
            )
        else:
            return RoutingProtocolDirectData(
        )
        """

    def testRoutingProtocolDirectData(self):
        """Test RoutingProtocolDirectData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
