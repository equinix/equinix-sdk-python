# coding: utf-8

"""
    Metal API

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.metalv1.models.ip_reservation_list import IPReservationList

class TestIPReservationList(unittest.TestCase):
    """IPReservationList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IPReservationList:
        """Test IPReservationList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IPReservationList`
        """
        model = IPReservationList()
        if include_optional:
            return IPReservationList(
                href = '',
                ip_addresses = [
                    null
                    ],
                meta = equinix.services.metalv1.models.meta.Meta(
                    current_page = 56, 
                    first = equinix.services.metalv1.models.href.Href(
                        href = '', ), 
                    href = '', 
                    last = equinix.services.metalv1.models.href.Href(
                        href = '', ), 
                    last_page = 56, 
                    next = , 
                    previous = , 
                    self = , 
                    total = 56, )
            )
        else:
            return IPReservationList(
        )
        """

    def testIPReservationList(self):
        """Test IPReservationList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
