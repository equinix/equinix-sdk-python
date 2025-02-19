# coding: utf-8

"""
    Metal API

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.metalv1.models.port_convert_layer3_input_request_ips_inner import PortConvertLayer3InputRequestIpsInner

class TestPortConvertLayer3InputRequestIpsInner(unittest.TestCase):
    """PortConvertLayer3InputRequestIpsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PortConvertLayer3InputRequestIpsInner:
        """Test PortConvertLayer3InputRequestIpsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PortConvertLayer3InputRequestIpsInner`
        """
        model = PortConvertLayer3InputRequestIpsInner()
        if include_optional:
            return PortConvertLayer3InputRequestIpsInner(
                address_family = 56,
                href = '',
                public = True
            )
        else:
            return PortConvertLayer3InputRequestIpsInner(
        )
        """

    def testPortConvertLayer3InputRequestIpsInner(self):
        """Test PortConvertLayer3InputRequestIpsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
