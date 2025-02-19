# coding: utf-8

"""
    Metal API

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.metalv1.api.spot_market_api import SpotMarketApi


class TestSpotMarketApi(unittest.TestCase):
    """SpotMarketApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SpotMarketApi()

    def tearDown(self) -> None:
        pass

    def test_create_spot_market_request(self) -> None:
        """Test case for create_spot_market_request

        Create a spot market request
        """
        pass

    def test_delete_spot_market_request(self) -> None:
        """Test case for delete_spot_market_request

        Delete the spot market request
        """
        pass

    def test_find_metro_spot_market_prices(self) -> None:
        """Test case for find_metro_spot_market_prices

        Get current spot market prices for metros
        """
        pass

    def test_find_spot_market_prices(self) -> None:
        """Test case for find_spot_market_prices

        Get current spot market prices
        """
        pass

    def test_find_spot_market_prices_history(self) -> None:
        """Test case for find_spot_market_prices_history

        Get spot market prices for a given period of time
        """
        pass

    def test_find_spot_market_request_by_id(self) -> None:
        """Test case for find_spot_market_request_by_id

        Retrieve a spot market request
        """
        pass

    def test_list_spot_market_requests(self) -> None:
        """Test case for list_spot_market_requests

        List spot market requests
        """
        pass


if __name__ == '__main__':
    unittest.main()
