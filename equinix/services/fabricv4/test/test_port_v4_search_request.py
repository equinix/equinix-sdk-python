# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.fabricv4.models.port_v4_search_request import PortV4SearchRequest

class TestPortV4SearchRequest(unittest.TestCase):
    """PortV4SearchRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PortV4SearchRequest:
        """Test PortV4SearchRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PortV4SearchRequest`
        """
        model = PortV4SearchRequest()
        if include_optional:
            return PortV4SearchRequest(
                filter = equinix.services.fabricv4.models.port_expression.PortExpression(
                    and = [
                        equinix.services.fabricv4.models.port_expression.PortExpression(
                            or = [
                                
                                ], 
                            property = '/project/projectId', 
                            operator = '=', 
                            values = [
                                ''
                                ], )
                        ], 
                    or = , 
                    property = '/project/projectId', 
                    operator = '=', 
                    values = [
                        ''
                        ], ),
                pagination = equinix.services.fabricv4.models.pagination_request.PaginationRequest(
                    offset = 0, 
                    limit = 1, ),
                sort = [
                    equinix.services.fabricv4.models.port_sort_criteria.PortSortCriteria(
                        direction = 'DESC', 
                        property = '/device/name', )
                    ]
            )
        else:
            return PortV4SearchRequest(
        )
        """

    def testPortV4SearchRequest(self):
        """Test PortV4SearchRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
