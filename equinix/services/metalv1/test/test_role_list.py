# coding: utf-8

"""
    Metal API

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.metalv1.models.role_list import RoleList

class TestRoleList(unittest.TestCase):
    """RoleList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RoleList:
        """Test RoleList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RoleList`
        """
        model = RoleList()
        if include_optional:
            return RoleList(
                href = '',
                roles = [
                    equinix.services.metalv1.models.role_list_roles_inner.RoleList_roles_inner(
                        id = '', 
                        name = '', )
                    ]
            )
        else:
            return RoleList(
        )
        """

    def testRoleList(self):
        """Test RoleList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
