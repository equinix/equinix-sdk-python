# coding: utf-8

"""
    Metal API

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.metalv1.models.port_convert_layer3_input import PortConvertLayer3Input

class TestPortConvertLayer3Input(unittest.TestCase):
    """PortConvertLayer3Input unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PortConvertLayer3Input:
        """Test PortConvertLayer3Input
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PortConvertLayer3Input`
        """
        model = PortConvertLayer3Input()
        if include_optional:
            return PortConvertLayer3Input(
                href = '',
                request_ips = [
                    equinix.services.metalv1.models.port_convert_layer3_input_request_ips_inner.PortConvertLayer3Input_request_ips_inner(
                        address_family = 56, 
                        href = '', 
                        public = True, )
                    ]
            )
        else:
            return PortConvertLayer3Input(
        )
        """

    def testPortConvertLayer3Input(self):
        """Test PortConvertLayer3Input"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
