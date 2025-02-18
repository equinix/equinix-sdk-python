# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)
"""

import unittest

from equinix.services.fabricv4.models.get_response import GetResponse

class TestGetResponse(unittest.TestCase):
    """GetResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetResponse:
        """Test GetResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetResponse`
        """
        model = GetResponse()
        if include_optional:
            return GetResponse(
                pagination = equinix.services.fabricv4.models.pagination.Pagination(
                    offset = 0, 
                    limit = 0, 
                    total = 0, 
                    next = '', 
                    previous = '', ),
                data = [
                    equinix.services.fabricv4.models.routing_protocol_data.RoutingProtocolData(
                        type = 'BGP', )
                    ]
            )
        else:
            return GetResponse(
        )
        """

    def testGetResponse(self):
        """Test GetResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
