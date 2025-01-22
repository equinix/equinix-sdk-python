# coding: utf-8

"""
    Metal API

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.metalv1.models.ip_reservation_metro import IPReservationMetro

class TestIPReservationMetro(unittest.TestCase):
    """IPReservationMetro unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IPReservationMetro:
        """Test IPReservationMetro
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IPReservationMetro`
        """
        model = IPReservationMetro()
        if include_optional:
            return IPReservationMetro(
                code = '',
                country = '',
                href = '',
                id = '',
                name = ''
            )
        else:
            return IPReservationMetro(
        )
        """

    def testIPReservationMetro(self):
        """Test IPReservationMetro"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
