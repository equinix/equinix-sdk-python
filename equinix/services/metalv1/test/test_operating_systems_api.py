# coding: utf-8

"""
    Metal API

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.metalv1.api.operating_systems_api import OperatingSystemsApi


class TestOperatingSystemsApi(unittest.TestCase):
    """OperatingSystemsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = OperatingSystemsApi()

    def tearDown(self) -> None:
        pass

    def test_find_operating_system_version(self) -> None:
        """Test case for find_operating_system_version

        Retrieve all operating system versions
        """
        pass

    def test_find_operating_systems(self) -> None:
        """Test case for find_operating_systems

        Retrieve all operating systems
        """
        pass


if __name__ == '__main__':
    unittest.main()
