# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.fabricv4.models.connection_route_search_request import ConnectionRouteSearchRequest

class TestConnectionRouteSearchRequest(unittest.TestCase):
    """ConnectionRouteSearchRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConnectionRouteSearchRequest:
        """Test ConnectionRouteSearchRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConnectionRouteSearchRequest`
        """
        model = ConnectionRouteSearchRequest()
        if include_optional:
            return ConnectionRouteSearchRequest(
                filter = equinix.services.fabricv4.models.connection_route_entry_filters.ConnectionRouteEntryFilters(
                    and = [
                        equinix.services.fabricv4.models.connection_route_entry_filter.ConnectionRouteEntryFilter()
                        ], ),
                pagination = equinix.services.fabricv4.models.pagination_request.PaginationRequest(
                    offset = 0, 
                    limit = 1, ),
                sort = [
                    equinix.services.fabricv4.models.connection_route_sort_criteria.ConnectionRouteSortCriteria(
                        direction = 'DESC', 
                        property = '/changeLog/updatedDateTime', )
                    ]
            )
        else:
            return ConnectionRouteSearchRequest(
        )
        """

    def testConnectionRouteSearchRequest(self):
        """Test ConnectionRouteSearchRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
