# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)
"""

import unittest

from equinix.services.fabricv4.models.precision_time_service_connections_response import PrecisionTimeServiceConnectionsResponse

class TestPrecisionTimeServiceConnectionsResponse(unittest.TestCase):
    """PrecisionTimeServiceConnectionsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PrecisionTimeServiceConnectionsResponse:
        """Test PrecisionTimeServiceConnectionsResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PrecisionTimeServiceConnectionsResponse`
        """
        model = PrecisionTimeServiceConnectionsResponse()
        if include_optional:
            return PrecisionTimeServiceConnectionsResponse(
                pagination = equinix.services.fabricv4.models.pagination.Pagination(
                    offset = 0, 
                    limit = 0, 
                    total = 0, 
                    next = '', 
                    previous = '', ),
                data = [
                    equinix.services.fabricv4.models.connection_link.connectionLink(
                        href = 'https://api.equinix.com/fabric/v4/timeServices/92dc376a-a932-43aa-a6a2-c806dedbd784/connections', 
                        type = 'EVPL_VC', 
                        uuid = '', )
                    ]
            )
        else:
            return PrecisionTimeServiceConnectionsResponse(
        )
        """

    def testPrecisionTimeServiceConnectionsResponse(self):
        """Test PrecisionTimeServiceConnectionsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
