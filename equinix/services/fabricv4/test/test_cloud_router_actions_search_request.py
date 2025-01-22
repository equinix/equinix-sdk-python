# coding: utf-8

"""
    Equinix Fabric API v4

    Equinix Fabric is an advanced software-defined interconnection solution that enables you to directly, securely and dynamically connect to distributed infrastructure and digital ecosystems on platform Equinix via a single port, Customers can use Fabric to connect to: </br> 1. Cloud Service Providers - Clouds, network and other service providers.  </br> 2. Enterprises - Other Equinix customers, vendors and partners.  </br> 3. Myself - Another customer instance deployed at Equinix. </br> </br> <b>Integrations (SDKs, Tools) links:</b> </br> <a href=\"https://deploy.equinix.com/labs/fabric-java\\\">Fabric Java SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-go\\\">Fabric Go SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-python\\\">Fabric Python SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-provider-equinix\\\">Equinix Terraform Provider</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-equinix-fabric\\\">Fabric Terraform Modules</a> </br> <a href=\"https://deploy.equinix.com/labs/pulumi-provider-equinix/\">Equinix Pulumi Provider</a> </br>

    The version of the OpenAPI document: 4.18
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.fabricv4.models.cloud_router_actions_search_request import CloudRouterActionsSearchRequest

class TestCloudRouterActionsSearchRequest(unittest.TestCase):
    """CloudRouterActionsSearchRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CloudRouterActionsSearchRequest:
        """Test CloudRouterActionsSearchRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CloudRouterActionsSearchRequest`
        """
        model = CloudRouterActionsSearchRequest()
        if include_optional:
            return CloudRouterActionsSearchRequest(
                filter = equinix.services.fabricv4.models.cloud_router_actions_search_filters.CloudRouterActionsSearchFilters(
                    and = [
                        equinix.services.fabricv4.models.cloud_router_actions_search_filter.CloudRouterActionsSearchFilter()
                        ], ),
                pagination = equinix.services.fabricv4.models.pagination_request.PaginationRequest(
                    offset = 0, 
                    limit = 1, ),
                sort = [
                    equinix.services.fabricv4.models.cloud_router_actions_search_sort_criteria.CloudRouterActionsSearchSortCriteria(
                        direction = 'DESC', 
                        property = '/changeLog/updatedDateTime', )
                    ]
            )
        else:
            return CloudRouterActionsSearchRequest(
        )
        """

    def testCloudRouterActionsSearchRequest(self):
        """Test CloudRouterActionsSearchRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
