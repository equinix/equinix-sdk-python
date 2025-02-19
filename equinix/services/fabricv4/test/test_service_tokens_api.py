# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.fabricv4.api.service_tokens_api import ServiceTokensApi


class TestServiceTokensApi(unittest.TestCase):
    """ServiceTokensApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ServiceTokensApi()

    def tearDown(self) -> None:
        pass

    def test_create_service_token(self) -> None:
        """Test case for create_service_token

        Create Service Token
        """
        pass

    def test_create_service_token_action(self) -> None:
        """Test case for create_service_token_action

        ServiceToken Actions
        """
        pass

    def test_delete_service_token_by_uuid(self) -> None:
        """Test case for delete_service_token_by_uuid

        Delete Token by uuid
        """
        pass

    def test_get_service_token_by_uuid(self) -> None:
        """Test case for get_service_token_by_uuid

        Get Token by uuid
        """
        pass

    def test_get_service_tokens(self) -> None:
        """Test case for get_service_tokens

        Get All Tokens
        """
        pass

    def test_search_service_tokens(self) -> None:
        """Test case for search_service_tokens

        Search servicetokens
        """
        pass

    def test_update_service_token_by_uuid(self) -> None:
        """Test case for update_service_token_by_uuid

        Update Token By ID
        """
        pass


if __name__ == '__main__':
    unittest.main()
