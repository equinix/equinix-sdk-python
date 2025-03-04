# coding: utf-8

"""
    Metal API

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.metalv1.api.memberships_api import MembershipsApi


class TestMembershipsApi(unittest.TestCase):
    """MembershipsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = MembershipsApi()

    def tearDown(self) -> None:
        pass

    def test_delete_membership(self) -> None:
        """Test case for delete_membership

        Delete the membership
        """
        pass

    def test_find_membership_by_id(self) -> None:
        """Test case for find_membership_by_id

        Retrieve a membership
        """
        pass

    def test_update_membership(self) -> None:
        """Test case for update_membership

        Update the membership
        """
        pass


if __name__ == '__main__':
    unittest.main()
