# coding: utf-8

"""
    Metal API

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.metalv1.models.vlan_virtual_circuit_create_input import VlanVirtualCircuitCreateInput

class TestVlanVirtualCircuitCreateInput(unittest.TestCase):
    """VlanVirtualCircuitCreateInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VlanVirtualCircuitCreateInput:
        """Test VlanVirtualCircuitCreateInput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VlanVirtualCircuitCreateInput`
        """
        model = VlanVirtualCircuitCreateInput()
        if include_optional:
            return VlanVirtualCircuitCreateInput(
                description = '',
                href = '',
                name = '',
                nni_vlan = 2,
                project_id = '',
                speed = '',
                tags = [
                    ''
                    ],
                vnid = ''
            )
        else:
            return VlanVirtualCircuitCreateInput(
                project_id = '',
        )
        """

    def testVlanVirtualCircuitCreateInput(self):
        """Test VlanVirtualCircuitCreateInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
