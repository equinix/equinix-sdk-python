# coding: utf-8

"""
    Equinix Fabric API v4
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
