# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)
"""

import unittest

from equinix.services.fabricv4.models.sort_item import SortItem

class TestSortItem(unittest.TestCase):
    """SortItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SortItem:
        """Test SortItem
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SortItem`
        """
        model = SortItem()
        if include_optional:
            return SortItem(
                var_property = '/changeLog/updatedDateTime',
                direction = 'DESC'
            )
        else:
            return SortItem(
        )
        """

    def testSortItem(self):
        """Test SortItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
