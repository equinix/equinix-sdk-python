# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.fabricv4.models.simplified_location_without_ibx import SimplifiedLocationWithoutIBX

class TestSimplifiedLocationWithoutIBX(unittest.TestCase):
    """SimplifiedLocationWithoutIBX unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SimplifiedLocationWithoutIBX:
        """Test SimplifiedLocationWithoutIBX
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SimplifiedLocationWithoutIBX`
        """
        model = SimplifiedLocationWithoutIBX()
        if include_optional:
            return SimplifiedLocationWithoutIBX(
                metro_href = 'https://api.equinix.com/fabric/v4/metros/AM',
                region = 'AMER, APAC, EMEA',
                metro_name = 'Amsterdam',
                metro_code = 'AM'
            )
        else:
            return SimplifiedLocationWithoutIBX(
                metro_code = 'AM',
        )
        """

    def testSimplifiedLocationWithoutIBX(self):
        """Test SimplifiedLocationWithoutIBX"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
