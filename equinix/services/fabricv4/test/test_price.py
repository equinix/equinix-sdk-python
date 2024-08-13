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

from equinix.services.fabricv4.models.price import Price

class TestPrice(unittest.TestCase):
    """Price unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Price:
        """Test Price
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Price`
        """
        model = Price()
        if include_optional:
            return Price(
                href = '',
                type = 'VIRTUAL_CONNECTION_PRODUCT',
                code = '',
                name = '',
                description = '',
                account = equinix.services.fabricv4.models.simplified_account.SimplifiedAccount(
                    account_number = 56, 
                    account_name = '', 
                    org_id = 56, 
                    organization_name = '', 
                    global_org_id = '', 
                    global_organization_name = '', 
                    ucm_id = '', 
                    global_cust_id = '', 
                    reseller_account_number = 56, 
                    reseller_account_name = '', 
                    reseller_ucm_id = '', 
                    reseller_org_id = 56, ),
                charges = [
                    equinix.services.fabricv4.models.price_charge.PriceCharge(
                        type = 'MONTHLY_RECURRING', 
                        price = 0, )
                    ],
                currency = '',
                term_length = 12,
                catgory = 'COUNTRY',
                connection = equinix.services.fabricv4.models.virtual_connection_price.VirtualConnectionPrice(
                    uuid = '', 
                    type = 'EVPL_VC', 
                    bandwidth = 0, 
                    a_side = equinix.services.fabricv4.models.virtual_connection_price_a_side.VirtualConnectionPriceASide(
                        access_point = equinix.services.fabricv4.models.virtual_connection_price_a_side_access_point.VirtualConnectionPriceASide_accessPoint(
                            uuid = '', 
                            location = equinix.services.fabricv4.models.price_location.PriceLocation(
                                metro_code = '', ), 
                            port = equinix.services.fabricv4.models.virtual_connection_price_a_side_access_point_port.VirtualConnectionPriceASide_accessPoint_port(
                                settings = equinix.services.fabricv4.models.virtual_connection_price_a_side_access_point_port_settings.VirtualConnectionPriceASide_accessPoint_port_settings(
                                    buyout = True, ), ), ), ), 
                    z_side = equinix.services.fabricv4.models.virtual_connection_price_z_side.VirtualConnectionPriceZSide(), ),
                ip_block = equinix.services.fabricv4.models.ip_block_price.IpBlockPrice(
                    uuid = '', 
                    type = 'IPv4', 
                    prefix_length = 56, 
                    location = equinix.services.fabricv4.models.price_location.PriceLocation(
                        metro_code = '', ), ),
                router = equinix.services.fabricv4.models.fabric_cloud_router_price.FabricCloudRouterPrice(
                    uuid = '', 
                    location = equinix.services.fabricv4.models.price_location.PriceLocation(
                        metro_code = '', ), 
                    package = equinix.services.fabricv4.models.fabric_cloud_router_packages.FabricCloudRouterPackages(
                        code = 'LAB', ), ),
                port = equinix.services.fabricv4.models.virtual_port_price.VirtualPortPrice(
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
                    connectivity_source = equinix.services.fabricv4.models.connectivity_source.ConnectivitySource(), 
                    service_type = 'MSP', 
                    settings = equinix.services.fabricv4.models.virtual_port_configuration.VirtualPortConfiguration(
                        buyout = True, ), )
            )
        else:
            return Price(
        )
        """

    def testPrice(self):
        """Test Price"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
