# coding: utf-8

"""
    Metal API

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.metalv1.models.capacity_check_per_facility_info import CapacityCheckPerFacilityInfo

class TestCapacityCheckPerFacilityInfo(unittest.TestCase):
    """CapacityCheckPerFacilityInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CapacityCheckPerFacilityInfo:
        """Test CapacityCheckPerFacilityInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CapacityCheckPerFacilityInfo`
        """
        model = CapacityCheckPerFacilityInfo()
        if include_optional:
            return CapacityCheckPerFacilityInfo(
                available = True,
                facility = '',
                href = '',
                plan = '',
                quantity = ''
            )
        else:
            return CapacityCheckPerFacilityInfo(
        )
        """

    def testCapacityCheckPerFacilityInfo(self):
        """Test CapacityCheckPerFacilityInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
