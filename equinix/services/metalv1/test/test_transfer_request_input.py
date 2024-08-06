# coding: utf-8

"""
    Metal API

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.metalv1.models.transfer_request_input import TransferRequestInput

class TestTransferRequestInput(unittest.TestCase):
    """TransferRequestInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TransferRequestInput:
        """Test TransferRequestInput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TransferRequestInput`
        """
        model = TransferRequestInput()
        if include_optional:
            return TransferRequestInput(
                href = '',
                target_organization_id = ''
            )
        else:
            return TransferRequestInput(
        )
        """

    def testTransferRequestInput(self):
        """Test TransferRequestInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
