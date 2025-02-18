# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)
"""

import unittest

from equinix.services.fabricv4.models.port_device_redundancy import PortDeviceRedundancy

class TestPortDeviceRedundancy(unittest.TestCase):
    """PortDeviceRedundancy unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PortDeviceRedundancy:
        """Test PortDeviceRedundancy
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PortDeviceRedundancy`
        """
        model = PortDeviceRedundancy()
        if include_optional:
            return PortDeviceRedundancy(
                group = '',
                priority = 'PRIMARY'
            )
        else:
            return PortDeviceRedundancy(
        )
        """

    def testPortDeviceRedundancy(self):
        """Test PortDeviceRedundancy"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
