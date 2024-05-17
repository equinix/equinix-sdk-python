# coding: utf-8

"""
    Metal API

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.metalv1.models.create_self_service_reservation_request_period import CreateSelfServiceReservationRequestPeriod

class TestCreateSelfServiceReservationRequestPeriod(unittest.TestCase):
    """CreateSelfServiceReservationRequestPeriod unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateSelfServiceReservationRequestPeriod:
        """Test CreateSelfServiceReservationRequestPeriod
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateSelfServiceReservationRequestPeriod`
        """
        model = CreateSelfServiceReservationRequestPeriod()
        if include_optional:
            return CreateSelfServiceReservationRequestPeriod(
                count = 12,
                href = '',
                unit = 'monthly'
            )
        else:
            return CreateSelfServiceReservationRequestPeriod(
        )
        """

    def testCreateSelfServiceReservationRequestPeriod(self):
        """Test CreateSelfServiceReservationRequestPeriod"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
