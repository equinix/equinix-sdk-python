# coding: utf-8

"""
    Metal API

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.metalv1.models.vrf_metal_gateway_create_input import VrfMetalGatewayCreateInput

class TestVrfMetalGatewayCreateInput(unittest.TestCase):
    """VrfMetalGatewayCreateInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VrfMetalGatewayCreateInput:
        """Test VrfMetalGatewayCreateInput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VrfMetalGatewayCreateInput`
        """
        model = VrfMetalGatewayCreateInput()
        if include_optional:
            return VrfMetalGatewayCreateInput(
                href = '',
                ip_reservation_id = '',
                virtual_network_id = ''
            )
        else:
            return VrfMetalGatewayCreateInput(
                ip_reservation_id = '',
                virtual_network_id = '',
        )
        """

    def testVrfMetalGatewayCreateInput(self):
        """Test VrfMetalGatewayCreateInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
