# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.fabricv4.models.cloud_router_search_request import CloudRouterSearchRequest

class TestCloudRouterSearchRequest(unittest.TestCase):
    """CloudRouterSearchRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CloudRouterSearchRequest:
        """Test CloudRouterSearchRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CloudRouterSearchRequest`
        """
        model = CloudRouterSearchRequest()
        if include_optional:
            return CloudRouterSearchRequest(
                filter = equinix.services.fabricv4.models.cloud_router_filters.CloudRouterFilters(
                    and = [
                        equinix.services.fabricv4.models.cloud_router_filter.CloudRouterFilter()
                        ], ),
                pagination = equinix.services.fabricv4.models.pagination_request.PaginationRequest(
                    offset = 0, 
                    limit = 1, ),
                sort = [
                    equinix.services.fabricv4.models.cloud_router_sort_criteria.CloudRouterSortCriteria(
                        direction = 'DESC', 
                        property = '/changeLog/updatedDateTime', )
                    ]
            )
        else:
            return CloudRouterSearchRequest(
        )
        """

    def testCloudRouterSearchRequest(self):
        """Test CloudRouterSearchRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
