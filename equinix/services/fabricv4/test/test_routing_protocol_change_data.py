# coding: utf-8

"""
    Equinix Fabric API v4

    Equinix Fabric is an advanced software-defined interconnection solution that enables you to directly, securely and dynamically connect to distributed infrastructure and digital ecosystems on platform Equinix via a single port, Customers can use Fabric to connect to: </br> 1. Cloud Service Providers - Clouds, network and other service providers.  </br> 2. Enterprises - Other Equinix customers, vendors and partners.  </br> 3. Myself - Another customer instance deployed at Equinix. </br> </br> <b>Integrations (SDKs, Tools) links:</b> </br> <a href=\"https://deploy.equinix.com/labs/fabric-java\\\">Fabric Java SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-go\\\">Fabric Go SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-provider-equinix\\\">Equinix Terraform Provider</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-equinix-fabric\\\">Fabric Terraform Modules</a> </br> <a href=\"https://deploy.equinix.com/labs/pulumi-provider-equinix/\">Equinix Pulumi Provider</a> </br>

    The version of the OpenAPI document: 4.15
    Contact: api-support@equinix.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.fabricv4.models.routing_protocol_change_data import RoutingProtocolChangeData

class TestRoutingProtocolChangeData(unittest.TestCase):
    """RoutingProtocolChangeData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RoutingProtocolChangeData:
        """Test RoutingProtocolChangeData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RoutingProtocolChangeData`
        """
        model = RoutingProtocolChangeData()
        if include_optional:
            return RoutingProtocolChangeData(
                status = 'COMPLETED',
                created_by = '',
                created_date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_by = '',
                updated_date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                information = '',
                data = equinix.services.fabricv4.models.routing_protocol_change_operation.RoutingProtocolChangeOperation(
                    op = 'add', 
                    path = '/', 
                    value = equinix.services.fabricv4.models.routing_protocol_base.RoutingProtocolBase(
                        type = 'BGP', ), ),
                uuid = '',
                type = 'ROUTING_PROTOCOL_UPDATE',
                href = ''
            )
        else:
            return RoutingProtocolChangeData(
                uuid = '',
                type = 'ROUTING_PROTOCOL_UPDATE',
        )
        """

    def testRoutingProtocolChangeData(self):
        """Test RoutingProtocolChangeData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
