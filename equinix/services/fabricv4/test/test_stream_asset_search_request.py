# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.fabricv4.models.stream_asset_search_request import StreamAssetSearchRequest

class TestStreamAssetSearchRequest(unittest.TestCase):
    """StreamAssetSearchRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StreamAssetSearchRequest:
        """Test StreamAssetSearchRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StreamAssetSearchRequest`
        """
        model = StreamAssetSearchRequest()
        if include_optional:
            return StreamAssetSearchRequest(
                filter = equinix.services.fabricv4.models.stream_asset_filters.StreamAssetFilters(
                    and = [
                        equinix.services.fabricv4.models.stream_asset_filter.StreamAssetFilter()
                        ], ),
                pagination = equinix.services.fabricv4.models.pagination_request.PaginationRequest(
                    offset = 0, 
                    limit = 1, ),
                sort = [
                    equinix.services.fabricv4.models.stream_asset_sort_criteria.StreamAssetSortCriteria(
                        direction = 'DESC', 
                        property = '/uuid', )
                    ]
            )
        else:
            return StreamAssetSearchRequest(
        )
        """

    def testStreamAssetSearchRequest(self):
        """Test StreamAssetSearchRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
