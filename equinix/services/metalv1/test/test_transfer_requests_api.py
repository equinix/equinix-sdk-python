# coding: utf-8

"""
    Metal API

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.metalv1.api.transfer_requests_api import TransferRequestsApi


class TestTransferRequestsApi(unittest.TestCase):
    """TransferRequestsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = TransferRequestsApi()

    def tearDown(self) -> None:
        pass

    def test_accept_transfer_request(self) -> None:
        """Test case for accept_transfer_request

        Accept a transfer request
        """
        pass

    def test_decline_transfer_request(self) -> None:
        """Test case for decline_transfer_request

        Decline a transfer request
        """
        pass

    def test_find_transfer_request_by_id(self) -> None:
        """Test case for find_transfer_request_by_id

        View a transfer request
        """
        pass


if __name__ == '__main__':
    unittest.main()
