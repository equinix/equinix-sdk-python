# coding: utf-8

"""
    Metal API

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.metalv1.models.move_hardware_reservation_request import MoveHardwareReservationRequest

class TestMoveHardwareReservationRequest(unittest.TestCase):
    """MoveHardwareReservationRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MoveHardwareReservationRequest:
        """Test MoveHardwareReservationRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MoveHardwareReservationRequest`
        """
        model = MoveHardwareReservationRequest()
        if include_optional:
            return MoveHardwareReservationRequest(
                href = '',
                project_id = ''
            )
        else:
            return MoveHardwareReservationRequest(
        )
        """

    def testMoveHardwareReservationRequest(self):
        """Test MoveHardwareReservationRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
