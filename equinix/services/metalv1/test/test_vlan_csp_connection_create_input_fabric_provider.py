# coding: utf-8

"""
    Metal API

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.metalv1.models.vlan_csp_connection_create_input_fabric_provider import VlanCSPConnectionCreateInputFabricProvider

class TestVlanCSPConnectionCreateInputFabricProvider(unittest.TestCase):
    """VlanCSPConnectionCreateInputFabricProvider unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VlanCSPConnectionCreateInputFabricProvider:
        """Test VlanCSPConnectionCreateInputFabricProvider
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VlanCSPConnectionCreateInputFabricProvider`
        """
        model = VlanCSPConnectionCreateInputFabricProvider()
        if include_optional:
            return VlanCSPConnectionCreateInputFabricProvider(
                account_id = '123412341234',
                href = '',
                location = 'us-west-1',
                type = 'CSP_AWS'
            )
        else:
            return VlanCSPConnectionCreateInputFabricProvider(
                account_id = '123412341234',
                type = 'CSP_AWS',
        )
        """

    def testVlanCSPConnectionCreateInputFabricProvider(self):
        """Test VlanCSPConnectionCreateInputFabricProvider"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
