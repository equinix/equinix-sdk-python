# coding: utf-8

"""
    Metal API

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.metalv1.models.capacity_check_per_facility_list import CapacityCheckPerFacilityList

class TestCapacityCheckPerFacilityList(unittest.TestCase):
    """CapacityCheckPerFacilityList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CapacityCheckPerFacilityList:
        """Test CapacityCheckPerFacilityList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CapacityCheckPerFacilityList`
        """
        model = CapacityCheckPerFacilityList()
        if include_optional:
            return CapacityCheckPerFacilityList(
                href = '',
                servers = [
                    equinix.services.metalv1.models.capacity_check_per_facility_info.CapacityCheckPerFacilityInfo(
                        available = True, 
                        facility = '', 
                        href = '', 
                        plan = '', 
                        quantity = '', )
                    ]
            )
        else:
            return CapacityCheckPerFacilityList(
        )
        """

    def testCapacityCheckPerFacilityList(self):
        """Test CapacityCheckPerFacilityList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
