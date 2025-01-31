# coding: utf-8

"""
    Metal API

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.metalv1.models.ip_reservation_request_input import IPReservationRequestInput

class TestIPReservationRequestInput(unittest.TestCase):
    """IPReservationRequestInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IPReservationRequestInput:
        """Test IPReservationRequestInput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IPReservationRequestInput`
        """
        model = IPReservationRequestInput()
        if include_optional:
            return IPReservationRequestInput(
                comments = '',
                customdata = None,
                details = '',
                facility = '',
                fail_on_approval_required = True,
                href = '',
                metro = 'SV',
                quantity = 56,
                tags = [
                    ''
                    ],
                type = ''
            )
        else:
            return IPReservationRequestInput(
                quantity = 56,
                type = '',
        )
        """

    def testIPReservationRequestInput(self):
        """Test IPReservationRequestInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
