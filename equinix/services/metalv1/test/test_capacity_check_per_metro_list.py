# coding: utf-8

"""
    Metal API

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.metalv1.models.capacity_check_per_metro_list import CapacityCheckPerMetroList

class TestCapacityCheckPerMetroList(unittest.TestCase):
    """CapacityCheckPerMetroList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CapacityCheckPerMetroList:
        """Test CapacityCheckPerMetroList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CapacityCheckPerMetroList`
        """
        model = CapacityCheckPerMetroList()
        if include_optional:
            return CapacityCheckPerMetroList(
                href = '',
                servers = [
                    equinix.services.metalv1.models.capacity_check_per_metro_info.CapacityCheckPerMetroInfo(
                        available = True, 
                        href = '', 
                        metro = '', 
                        plan = '', 
                        quantity = '', )
                    ]
            )
        else:
            return CapacityCheckPerMetroList(
        )
        """

    def testCapacityCheckPerMetroList(self):
        """Test CapacityCheckPerMetroList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
