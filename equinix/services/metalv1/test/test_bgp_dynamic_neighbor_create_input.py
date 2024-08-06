# coding: utf-8

"""
    Metal API

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.metalv1.models.bgp_dynamic_neighbor_create_input import BgpDynamicNeighborCreateInput

class TestBgpDynamicNeighborCreateInput(unittest.TestCase):
    """BgpDynamicNeighborCreateInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BgpDynamicNeighborCreateInput:
        """Test BgpDynamicNeighborCreateInput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BgpDynamicNeighborCreateInput`
        """
        model = BgpDynamicNeighborCreateInput()
        if include_optional:
            return BgpDynamicNeighborCreateInput(
                bgp_neighbor_asn = 12345,
                bgp_neighbor_range = '192.168.1.0/25',
                href = '',
                tags = [
                    ''
                    ]
            )
        else:
            return BgpDynamicNeighborCreateInput(
                bgp_neighbor_asn = 12345,
                bgp_neighbor_range = '192.168.1.0/25',
        )
        """

    def testBgpDynamicNeighborCreateInput(self):
        """Test BgpDynamicNeighborCreateInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
