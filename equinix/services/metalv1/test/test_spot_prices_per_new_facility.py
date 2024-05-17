# coding: utf-8

"""
    Metal API

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.metalv1.models.spot_prices_per_new_facility import SpotPricesPerNewFacility

class TestSpotPricesPerNewFacility(unittest.TestCase):
    """SpotPricesPerNewFacility unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SpotPricesPerNewFacility:
        """Test SpotPricesPerNewFacility
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SpotPricesPerNewFacility`
        """
        model = SpotPricesPerNewFacility()
        if include_optional:
            return SpotPricesPerNewFacility(
                baremetal_1e = equinix.services.metalv1.models.spot_prices_per_baremetal.SpotPricesPerBaremetal(
                    href = '', 
                    price = 1.337, ),
                href = ''
            )
        else:
            return SpotPricesPerNewFacility(
        )
        """

    def testSpotPricesPerNewFacility(self):
        """Test SpotPricesPerNewFacility"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
