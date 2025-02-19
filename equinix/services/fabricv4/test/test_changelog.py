# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.fabricv4.models.changelog import Changelog

class TestChangelog(unittest.TestCase):
    """Changelog unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Changelog:
        """Test Changelog
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Changelog`
        """
        model = Changelog()
        if include_optional:
            return Changelog(
                created_by = 'johnsmith',
                created_by_full_name = 'John Smith',
                created_by_email = 'john.smith@example.com',
                created_date_time = '2020-11-06T07:00Z',
                updated_by = 'johnsmith',
                updated_by_full_name = 'John Smith',
                updated_by_email = 'john.smith@example.com',
                updated_date_time = '2020-11-06T07:00Z',
                deleted_by = 'johnsmith',
                deleted_by_full_name = 'John Smith',
                deleted_by_email = 'john.smith@example.com',
                deleted_date_time = '2020-11-06T07:00Z'
            )
        else:
            return Changelog(
        )
        """

    def testChangelog(self):
        """Test Changelog"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
