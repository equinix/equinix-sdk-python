# coding: utf-8

"""
    Equinix Fabric API v4

    Equinix Fabric is an advanced software-defined interconnection solution that enables you to directly, securely and dynamically connect to distributed infrastructure and digital ecosystems on platform Equinix via a single port, Customers can use Fabric to connect to: </br> 1. Cloud Service Providers - Clouds, network and other service providers.  </br> 2. Enterprises - Other Equinix customers, vendors and partners.  </br> 3. Myself - Another customer instance deployed at Equinix. </br> </br> <b>Integrations (SDKs, Tools) links:</b> </br> <a href=\"https://deploy.equinix.com/labs/fabric-java\\\">Fabric Java SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-go\\\">Fabric Go SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-python\\\">Fabric Python SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-provider-equinix\\\">Equinix Terraform Provider</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-equinix-fabric\\\">Fabric Terraform Modules</a> </br> <a href=\"https://deploy.equinix.com/labs/pulumi-provider-equinix/\">Equinix Pulumi Provider</a> </br>

    The version of the OpenAPI document: 4.18
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.fabricv4.models.cloud_router_actions_search_response import CloudRouterActionsSearchResponse

class TestCloudRouterActionsSearchResponse(unittest.TestCase):
    """CloudRouterActionsSearchResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CloudRouterActionsSearchResponse:
        """Test CloudRouterActionsSearchResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CloudRouterActionsSearchResponse`
        """
        model = CloudRouterActionsSearchResponse()
        if include_optional:
            return CloudRouterActionsSearchResponse(
                pagination = equinix.services.fabricv4.models.pagination.Pagination(
                    offset = 0, 
                    limit = 0, 
                    total = 0, 
                    next = '', 
                    previous = '', ),
                data = [
                    equinix.services.fabricv4.models.cloud_router_action_response.CloudRouterActionResponse(
                        type = 'BGP_SESSION_STATUS_UPDATE', 
                        uuid = '557400f8-d360-11e9-bb65-2a2ae2dbcce4', 
                        description = 'description', 
                        state = 'SUCCEEDED', 
                        change_log = equinix.services.fabricv4.models.changelog.Changelog(
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
                        href = 'https://api.equinix.com//fabric/v4/routers/a1c6b7fd-aead-410a-96b4-b1dfa1071700/actions/1e9414f1-763e-4c0a-86c6-0bc8336048d9', 
                        connection = equinix.services.fabricv4.models.router_actions_connection.RouterActionsConnection(
                            uuid = '557400f8-d360-11e9-bb65-2a2ae2dbcce4', ), 
                        operation = equinix.services.fabricv4.models.operation.Operation(
                            bgp_ipv4_routes_count = 6, 
                            bgp_ipv6_routes_count = 6, ), )
                    ]
            )
        else:
            return CloudRouterActionsSearchResponse(
        )
        """

    def testCloudRouterActionsSearchResponse(self):
        """Test CloudRouterActionsSearchResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
