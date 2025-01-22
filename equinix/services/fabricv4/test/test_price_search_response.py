# coding: utf-8

"""
    Equinix Fabric API v4

    Equinix Fabric is an advanced software-defined interconnection solution that enables you to directly, securely and dynamically connect to distributed infrastructure and digital ecosystems on platform Equinix via a single port, Customers can use Fabric to connect to: </br> 1. Cloud Service Providers - Clouds, network and other service providers.  </br> 2. Enterprises - Other Equinix customers, vendors and partners.  </br> 3. Myself - Another customer instance deployed at Equinix. </br> </br> <b>Integrations (SDKs, Tools) links:</b> </br> <a href=\"https://deploy.equinix.com/labs/fabric-java\\\">Fabric Java SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-go\\\">Fabric Go SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-python\\\">Fabric Python SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-provider-equinix\\\">Equinix Terraform Provider</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-equinix-fabric\\\">Fabric Terraform Modules</a> </br> <a href=\"https://deploy.equinix.com/labs/pulumi-provider-equinix/\">Equinix Pulumi Provider</a> </br>

    The version of the OpenAPI document: 4.18
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.fabricv4.models.price_search_response import PriceSearchResponse

class TestPriceSearchResponse(unittest.TestCase):
    """PriceSearchResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PriceSearchResponse:
        """Test PriceSearchResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PriceSearchResponse`
        """
        model = PriceSearchResponse()
        if include_optional:
            return PriceSearchResponse(
                data = [
                    equinix.services.fabricv4.models.price.Price(
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
                                price = 0, )
                            ], 
                        currency = '', 
                        term_length = 12, 
                        catgory = 'COUNTRY', 
                        connection = equinix.services.fabricv4.models.virtual_connection_price.VirtualConnectionPrice(
                            uuid = '', 
                            bandwidth = 0, 
                            a_side = equinix.services.fabricv4.models.virtual_connection_price_a_side.VirtualConnectionPriceASide(
                                access_point = equinix.services.fabricv4.models.virtual_connection_price_a_side_access_point.VirtualConnectionPriceASide_accessPoint(
                                    uuid = '', 
                                    location = equinix.services.fabricv4.models.price_location.PriceLocation(
                                        metro_code = '', 
                                        ibx = '', ), 
                                    port = equinix.services.fabricv4.models.virtual_connection_price_a_side_access_point_port.VirtualConnectionPriceASide_accessPoint_port(
                                        settings = equinix.services.fabricv4.models.virtual_connection_price_a_side_access_point_port_settings.VirtualConnectionPriceASide_accessPoint_port_settings(
                                            buyout = True, ), ), ), ), 
                            z_side = equinix.services.fabricv4.models.virtual_connection_price_z_side.VirtualConnectionPriceZSide(), ), 
                        ip_block = equinix.services.fabricv4.models.ip_block_price.IpBlockPrice(
                            uuid = '', 
                            prefix_length = 56, ), 
                        router = equinix.services.fabricv4.models.fabric_cloud_router_price.FabricCloudRouterPrice(
                            uuid = '', 
                            package = equinix.services.fabricv4.models.fabric_cloud_router_packages.FabricCloudRouterPackages(
                                code = 'LAB', ), ), 
                        port = equinix.services.fabricv4.models.virtual_port_price.VirtualPortPrice(
                            uuid = '', 
                            lag = equinix.services.fabricv4.models.link_aggregation_group.LinkAggregationGroup(
                                enabled = True, ), 
                            physical_ports_quantity = 56, 
                            bandwidth = 56, 
                            redundancy = equinix.services.fabricv4.models.virtual_port_redundancy.VirtualPortRedundancy(
                                enabled = True, ), 
                            connectivity_source = equinix.services.fabricv4.models.connectivity_source.ConnectivitySource(), 
                            service_type = 'MSP', ), 
                        time_service = equinix.services.fabricv4.models.time_service_price.TimeServicePrice(), )
                    ],
                pagination = equinix.services.fabricv4.models.pagination.Pagination(
                    offset = 0, 
                    limit = 0, 
                    total = 0, 
                    next = '', 
                    previous = '', )
            )
        else:
            return PriceSearchResponse(
        )
        """

    def testPriceSearchResponse(self):
        """Test PriceSearchResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
