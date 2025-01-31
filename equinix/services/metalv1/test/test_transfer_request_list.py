# coding: utf-8

"""
    Metal API

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.metalv1.models.transfer_request_list import TransferRequestList

class TestTransferRequestList(unittest.TestCase):
    """TransferRequestList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TransferRequestList:
        """Test TransferRequestList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TransferRequestList`
        """
        model = TransferRequestList()
        if include_optional:
            return TransferRequestList(
                href = '',
                transfers = [
                    equinix.services.metalv1.models.transfer_request.TransferRequest(
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        href = '', 
                        id = '', 
                        project = equinix.services.metalv1.models.href.Href(
                            href = '', ), 
                        target_organization = equinix.services.metalv1.models.href.Href(
                            href = '', ), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ]
            )
        else:
            return TransferRequestList(
        )
        """

    def testTransferRequestList(self):
        """Test TransferRequestList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
