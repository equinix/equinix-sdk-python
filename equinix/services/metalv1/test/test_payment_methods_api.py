# coding: utf-8

"""
    Metal API

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.metalv1.api.payment_methods_api import PaymentMethodsApi


class TestPaymentMethodsApi(unittest.TestCase):
    """PaymentMethodsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PaymentMethodsApi()

    def tearDown(self) -> None:
        pass

    def test_delete_payment_method(self) -> None:
        """Test case for delete_payment_method

        Delete the payment method
        """
        pass

    def test_find_payment_method_by_id(self) -> None:
        """Test case for find_payment_method_by_id

        Retrieve a payment method
        """
        pass

    def test_update_payment_method(self) -> None:
        """Test case for update_payment_method

        Update the payment method
        """
        pass


if __name__ == '__main__':
    unittest.main()
