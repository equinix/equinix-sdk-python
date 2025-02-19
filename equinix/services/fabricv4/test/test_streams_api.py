# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.fabricv4.api.streams_api import StreamsApi


class TestStreamsApi(unittest.TestCase):
    """StreamsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = StreamsApi()

    def tearDown(self) -> None:
        pass

    def test_create_streams(self) -> None:
        """Test case for create_streams

        Create Stream
        """
        pass

    def test_delete_stream_asset_by_uuid(self) -> None:
        """Test case for delete_stream_asset_by_uuid

        Detach Asset
        """
        pass

    def test_delete_stream_by_uuid(self) -> None:
        """Test case for delete_stream_by_uuid

        Delete Stream
        """
        pass

    def test_get_stream_asset_by_uuid(self) -> None:
        """Test case for get_stream_asset_by_uuid

        Get Asset
        """
        pass

    def test_get_stream_by_uuid(self) -> None:
        """Test case for get_stream_by_uuid

        Get Stream
        """
        pass

    def test_get_streams(self) -> None:
        """Test case for get_streams

        Get Streams
        """
        pass

    def test_get_streams_assets(self) -> None:
        """Test case for get_streams_assets

        Get Assets
        """
        pass

    def test_update_stream_asset_by_uuid(self) -> None:
        """Test case for update_stream_asset_by_uuid

        Attach Asset
        """
        pass

    def test_update_stream_by_uuid(self) -> None:
        """Test case for update_stream_by_uuid

        Update Stream
        """
        pass


if __name__ == '__main__':
    unittest.main()
