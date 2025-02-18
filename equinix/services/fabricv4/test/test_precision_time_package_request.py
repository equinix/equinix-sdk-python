# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)
"""

import unittest

from equinix.services.fabricv4.models.precision_time_package_request import PrecisionTimePackageRequest

class TestPrecisionTimePackageRequest(unittest.TestCase):
    """PrecisionTimePackageRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PrecisionTimePackageRequest:
        """Test PrecisionTimePackageRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PrecisionTimePackageRequest`
        """
        model = PrecisionTimePackageRequest()
        if include_optional:
            return PrecisionTimePackageRequest(
                code = 'NTP_STANDARD'
            )
        else:
            return PrecisionTimePackageRequest(
                code = 'NTP_STANDARD',
        )
        """

    def testPrecisionTimePackageRequest(self):
        """Test PrecisionTimePackageRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
