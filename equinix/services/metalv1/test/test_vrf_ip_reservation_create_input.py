# coding: utf-8

"""
    Metal API

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.metalv1.models.vrf_ip_reservation_create_input import VrfIpReservationCreateInput

class TestVrfIpReservationCreateInput(unittest.TestCase):
    """VrfIpReservationCreateInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VrfIpReservationCreateInput:
        """Test VrfIpReservationCreateInput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VrfIpReservationCreateInput`
        """
        model = VrfIpReservationCreateInput()
        if include_optional:
            return VrfIpReservationCreateInput(
                cidr = 22,
                customdata = None,
                details = '',
                href = '',
                network = '10.1.2.0',
                tags = [
                    ''
                    ],
                type = 'vrf',
                vrf_id = ''
            )
        else:
            return VrfIpReservationCreateInput(
                cidr = 22,
                network = '10.1.2.0',
                type = 'vrf',
                vrf_id = '',
        )
        """

    def testVrfIpReservationCreateInput(self):
        """Test VrfIpReservationCreateInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
