# coding: utf-8

"""
    Metal API

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.metalv1.models.create_self_service_reservation_request import CreateSelfServiceReservationRequest

class TestCreateSelfServiceReservationRequest(unittest.TestCase):
    """CreateSelfServiceReservationRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateSelfServiceReservationRequest:
        """Test CreateSelfServiceReservationRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateSelfServiceReservationRequest`
        """
        model = CreateSelfServiceReservationRequest()
        if include_optional:
            return CreateSelfServiceReservationRequest(
                href = '',
                item = [
                    equinix.services.metalv1.models.self_service_reservation_item_request.SelfServiceReservationItemRequest(
                        href = '', 
                        metro_id = '', 
                        plan_id = '', 
                        quantity = 56, 
                        term = '', )
                    ],
                notes = '',
                period = equinix.services.metalv1.models.create_self_service_reservation_request_period.CreateSelfServiceReservationRequest_period(
                    count = 12, 
                    href = '', 
                    unit = 'monthly', ),
                start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return CreateSelfServiceReservationRequest(
        )
        """

    def testCreateSelfServiceReservationRequest(self):
        """Test CreateSelfServiceReservationRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
