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

from equinix.services.fabricv4.models.virtual_port_price import VirtualPortPrice

class TestVirtualPortPrice(unittest.TestCase):
    """VirtualPortPrice unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VirtualPortPrice:
        """Test VirtualPortPrice
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VirtualPortPrice`
        """
        model = VirtualPortPrice()
        if include_optional:
            return VirtualPortPrice(
                uuid = '',
                type = 'XF_PORT',
                location = equinix.services.fabricv4.models.virtual_port_location.VirtualPortLocation(
                    ibx = '', ),
                lag = equinix.services.fabricv4.models.link_aggregation_group.LinkAggregationGroup(
                    enabled = True, ),
                physical_ports_quantity = 56,
                bandwidth = 56,
                redundancy = equinix.services.fabricv4.models.virtual_port_redundancy.VirtualPortRedundancy(
                    enabled = True, ),
                connectivity_source = equinix.services.fabricv4.models.connectivity_source.ConnectivitySource(
                    type = 'COLO', ),
                service_type = 'MSP',
                settings = equinix.services.fabricv4.models.virtual_port_configuration.VirtualPortConfiguration(
                    buyout = True, )
            )
        else:
            return VirtualPortPrice(
        )
        """

    def testVirtualPortPrice(self):
        """Test VirtualPortPrice"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
