# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)
"""

import unittest

from equinix.services.fabricv4.models.time_services_search_request import TimeServicesSearchRequest

class TestTimeServicesSearchRequest(unittest.TestCase):
    """TimeServicesSearchRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TimeServicesSearchRequest:
        """Test TimeServicesSearchRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TimeServicesSearchRequest`
        """
        model = TimeServicesSearchRequest()
        if include_optional:
            return TimeServicesSearchRequest(
                filter = equinix.services.fabricv4.models.time_service_filters.TimeServiceFilters(
                    and = [
                        equinix.services.fabricv4.models.time_service_filter.TimeServiceFilter()
                        ], ),
                pagination = equinix.services.fabricv4.models.pagination_request.PaginationRequest(
                    offset = 0, 
                    limit = 1, ),
                sort = [
                    equinix.services.fabricv4.models.time_service_sort_criteria.TimeServiceSortCriteria(
                        direction = 'DESC', 
                        property = '/changeLog/updatedDateTime', )
                    ]
            )
        else:
            return TimeServicesSearchRequest(
        )
        """

    def testTimeServicesSearchRequest(self):
        """Test TimeServicesSearchRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
