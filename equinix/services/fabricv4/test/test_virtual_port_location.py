# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.fabricv4.models.virtual_port_location import VirtualPortLocation

class TestVirtualPortLocation(unittest.TestCase):
    """VirtualPortLocation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VirtualPortLocation:
        """Test VirtualPortLocation
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VirtualPortLocation`
        """
        model = VirtualPortLocation()
        if include_optional:
            return VirtualPortLocation(
                ibx = ''
            )
        else:
            return VirtualPortLocation(
        )
        """

    def testVirtualPortLocation(self):
        """Test VirtualPortLocation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
