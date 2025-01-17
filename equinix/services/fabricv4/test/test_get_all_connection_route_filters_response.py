# coding: utf-8

"""
    Equinix Fabric API v4

    Equinix Fabric is an advanced software-defined interconnection solution that enables you to directly, securely and dynamically connect to distributed infrastructure and digital ecosystems on platform Equinix via a single port, Customers can use Fabric to connect to: </br> 1. Cloud Service Providers - Clouds, network and other service providers.  </br> 2. Enterprises - Other Equinix customers, vendors and partners.  </br> 3. Myself - Another customer instance deployed at Equinix. </br> </br> <b>Integrations (SDKs, Tools) links:</b> </br> <a href=\"https://deploy.equinix.com/labs/fabric-java\\\">Fabric Java SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-go\\\">Fabric Go SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-python\\\">Fabric Python SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-provider-equinix\\\">Equinix Terraform Provider</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-equinix-fabric\\\">Fabric Terraform Modules</a> </br> <a href=\"https://deploy.equinix.com/labs/pulumi-provider-equinix/\">Equinix Pulumi Provider</a> </br>

    The version of the OpenAPI document: 4.18
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.fabricv4.models.get_all_connection_route_filters_response import GetAllConnectionRouteFiltersResponse

class TestGetAllConnectionRouteFiltersResponse(unittest.TestCase):
    """GetAllConnectionRouteFiltersResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetAllConnectionRouteFiltersResponse:
        """Test GetAllConnectionRouteFiltersResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetAllConnectionRouteFiltersResponse`
        """
        model = GetAllConnectionRouteFiltersResponse()
        if include_optional:
            return GetAllConnectionRouteFiltersResponse(
                pagination = equinix.services.fabricv4.models.pagination.Pagination(
                    offset = 0, 
                    limit = 0, 
                    total = 0, 
                    next = '', 
                    previous = '', ),
                data = [
                    equinix.services.fabricv4.models.connection_route_filter_data.ConnectionRouteFilterData(
                        href = 'https://api.equinix.com/fabric/v4/connections/81331c52-04c0-4656-a4a7-18c52669348f/routeFilters/695a8471-6595-4ac6-a2f4-b3d96ed3a59d', 
                        type = 'BGP_IPv4_PREFIX_FILTER', 
                        uuid = '695a8471-6595-4ac6-a2f4-b3d96ed3a59d', 
                        attachment_status = 'ATTACHING', 
                        direction = 'INBOUND', )
                    ]
            )
        else:
            return GetAllConnectionRouteFiltersResponse(
        )
        """

    def testGetAllConnectionRouteFiltersResponse(self):
        """Test GetAllConnectionRouteFiltersResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
