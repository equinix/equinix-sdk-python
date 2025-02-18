# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)
"""

import unittest

from equinix.services.fabricv4.models.network_search_response import NetworkSearchResponse

class TestNetworkSearchResponse(unittest.TestCase):
    """NetworkSearchResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NetworkSearchResponse:
        """Test NetworkSearchResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NetworkSearchResponse`
        """
        model = NetworkSearchResponse()
        if include_optional:
            return NetworkSearchResponse(
                pagination = equinix.services.fabricv4.models.pagination.Pagination(
                    offset = 0, 
                    limit = 0, 
                    total = 0, 
                    next = '', 
                    previous = '', ),
                sort = [
                    equinix.services.fabricv4.models.network_sort_criteria_response.NetworkSortCriteriaResponse(
                        direction = 'DESC', 
                        property = '/changeLog/updatedDateTime', )
                    ],
                data = [
                    equinix.services.fabricv4.models.network.Network()
                    ]
            )
        else:
            return NetworkSearchResponse(
        )
        """

    def testNetworkSearchResponse(self):
        """Test NetworkSearchResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
