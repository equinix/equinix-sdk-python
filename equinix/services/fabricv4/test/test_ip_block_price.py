# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.fabricv4.models.ip_block_price import IpBlockPrice

class TestIpBlockPrice(unittest.TestCase):
    """IpBlockPrice unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IpBlockPrice:
        """Test IpBlockPrice
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IpBlockPrice`
        """
        model = IpBlockPrice()
        if include_optional:
            return IpBlockPrice(
                uuid = '',
                type = 'IPv4',
                prefix_length = 56,
                location = equinix.services.fabricv4.models.price_location.PriceLocation(
                    metro_code = '', 
                    ibx = '', )
            )
        else:
            return IpBlockPrice(
        )
        """

    def testIpBlockPrice(self):
        """Test IpBlockPrice"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
