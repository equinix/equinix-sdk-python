# coding: utf-8

"""
    Metal API

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.metalv1.models.license_update_input import LicenseUpdateInput

class TestLicenseUpdateInput(unittest.TestCase):
    """LicenseUpdateInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LicenseUpdateInput:
        """Test LicenseUpdateInput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LicenseUpdateInput`
        """
        model = LicenseUpdateInput()
        if include_optional:
            return LicenseUpdateInput(
                description = '',
                href = '',
                size = 1.337
            )
        else:
            return LicenseUpdateInput(
        )
        """

    def testLicenseUpdateInput(self):
        """Test LicenseUpdateInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
