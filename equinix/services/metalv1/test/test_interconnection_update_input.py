# coding: utf-8

"""
    Metal API

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.metalv1.models.interconnection_update_input import InterconnectionUpdateInput

class TestInterconnectionUpdateInput(unittest.TestCase):
    """InterconnectionUpdateInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InterconnectionUpdateInput:
        """Test InterconnectionUpdateInput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InterconnectionUpdateInput`
        """
        model = InterconnectionUpdateInput()
        if include_optional:
            return InterconnectionUpdateInput(
                contact_email = '',
                description = '',
                href = '',
                mode = 'standard',
                name = '',
                tags = [
                    ''
                    ]
            )
        else:
            return InterconnectionUpdateInput(
        )
        """

    def testInterconnectionUpdateInput(self):
        """Test InterconnectionUpdateInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
