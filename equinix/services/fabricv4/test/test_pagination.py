# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)
"""

import unittest

from equinix.services.fabricv4.models.pagination import Pagination

class TestPagination(unittest.TestCase):
    """Pagination unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Pagination:
        """Test Pagination
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Pagination`
        """
        model = Pagination()
        if include_optional:
            return Pagination(
                offset = 0,
                limit = 0,
                total = 0,
                next = '',
                previous = ''
            )
        else:
            return Pagination(
                limit = 0,
                total = 0,
        )
        """

    def testPagination(self):
        """Test Pagination"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
