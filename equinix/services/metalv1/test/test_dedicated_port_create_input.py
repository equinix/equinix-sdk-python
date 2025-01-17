# coding: utf-8

"""
    Metal API

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.metalv1.models.dedicated_port_create_input import DedicatedPortCreateInput

class TestDedicatedPortCreateInput(unittest.TestCase):
    """DedicatedPortCreateInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DedicatedPortCreateInput:
        """Test DedicatedPortCreateInput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DedicatedPortCreateInput`
        """
        model = DedicatedPortCreateInput()
        if include_optional:
            return DedicatedPortCreateInput(
                billing_account_name = '',
                contact_email = '',
                description = '',
                facility_id = '',
                href = '',
                metro = '',
                mode = 'standard',
                name = '',
                project = '',
                redundancy = '',
                speed = '10000000000',
                tags = [
                    ''
                    ],
                type = 'dedicated',
                use_case = ''
            )
        else:
            return DedicatedPortCreateInput(
                metro = '',
                name = '',
                redundancy = '',
                type = 'dedicated',
        )
        """

    def testDedicatedPortCreateInput(self):
        """Test DedicatedPortCreateInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
