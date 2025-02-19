# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.fabricv4.models.network_sort_criteria_response import NetworkSortCriteriaResponse

class TestNetworkSortCriteriaResponse(unittest.TestCase):
    """NetworkSortCriteriaResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NetworkSortCriteriaResponse:
        """Test NetworkSortCriteriaResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NetworkSortCriteriaResponse`
        """
        model = NetworkSortCriteriaResponse()
        if include_optional:
            return NetworkSortCriteriaResponse(
                direction = 'DESC',
                var_property = '/changeLog/updatedDateTime'
            )
        else:
            return NetworkSortCriteriaResponse(
        )
        """

    def testNetworkSortCriteriaResponse(self):
        """Test NetworkSortCriteriaResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
