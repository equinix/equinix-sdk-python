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

from equinix.services.fabricv4.models.search_response import SearchResponse

class TestSearchResponse(unittest.TestCase):
    """SearchResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SearchResponse:
        """Test SearchResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SearchResponse`
        """
        model = SearchResponse()
        if include_optional:
            return SearchResponse(
                pagination = equinix.services.fabricv4.models.pagination.Pagination(
                    offset = 0, 
                    limit = 0, 
                    total = 0, 
                    next = '', 
                    previous = '', ),
                data = [
                    equinix.services.fabricv4.models.cloud_router.CloudRouter(
                        href = 'https://api.equinix.com/fabric/v4/routers/3c9b8e7a2-f3b1-4576-a4a9-1366a63df170', 
                        uuid = 'c9b8e7a2-f3b1-4576-a4a9-1366a63df170', 
                        name = 'test-fg-1', 
                        state = 'PROVISIONED', 
                        equinix_asn = 30000, 
                        bgp_ipv4_routes_count = 0, 
                        bgp_ipv6_routes_count = 0, 
                        connections_count = 0, 
                        distinct_ipv4_prefixes_count = 0, 
                        distinct_ipv6_prefixes_count = 0, 
                        marketplace_subscription = equinix.services.fabricv4.models.marketplace_subscription.marketplaceSubscription(
                            href = 'https://api.equinix.com/fabric/v4/marketplaceSubscriptions/20d32a80-0d61-4333-bc03-707b591ae2f5', 
                            type = 'AWS_MARKETPLACE_SUBSCRIPTION', 
                            uuid = '20d32a80-0d61-4333-bc03-707b591ae2f5', ), 
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
                        change = equinix.services.fabricv4.models.cloud_router_change.CloudRouterChange(
                            uuid = '', 
                            type = 'ROUTER_UPDATE', 
                            status = 'COMPLETED', 
                            created_date_time = '2020-11-06T07:00Z', 
                            updated_date_time = '2020-11-06T07:00Z', 
                            information = '', 
                            data = equinix.services.fabricv4.models.cloud_router_change_operation.CloudRouterChangeOperation(
                                op = 'replace', 
                                path = '', 
                                value = null, ), ), )
                    ]
            )
        else:
            return SearchResponse(
        )
        """

    def testSearchResponse(self):
        """Test SearchResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
