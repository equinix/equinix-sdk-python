# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.fabricv4.models.sub_interface import SubInterface

class TestSubInterface(unittest.TestCase):
    """SubInterface unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SubInterface:
        """Test SubInterface
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SubInterface`
        """
        model = SubInterface()
        if include_optional:
            return SubInterface(
                name = '',
                unit = 200
            )
        else:
            return SubInterface(
        )
        """

    def testSubInterface(self):
        """Test SubInterface"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
