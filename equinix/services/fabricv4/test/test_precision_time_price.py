# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)
"""

import unittest

from equinix.services.fabricv4.models.precision_time_price import PrecisionTimePrice

class TestPrecisionTimePrice(unittest.TestCase):
    """PrecisionTimePrice unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PrecisionTimePrice:
        """Test PrecisionTimePrice
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PrecisionTimePrice`
        """
        model = PrecisionTimePrice()
        if include_optional:
            return PrecisionTimePrice(
                currency = '',
                charges = [
                    equinix.services.fabricv4.models.price_charge.PriceCharge(
                        type = 'MONTHLY_RECURRING', 
                        price = 0, )
                    ]
            )
        else:
            return PrecisionTimePrice(
        )
        """

    def testPrecisionTimePrice(self):
        """Test PrecisionTimePrice"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
