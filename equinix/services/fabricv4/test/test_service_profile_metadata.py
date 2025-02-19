# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.fabricv4.models.service_profile_metadata import ServiceProfileMetadata

class TestServiceProfileMetadata(unittest.TestCase):
    """ServiceProfileMetadata unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServiceProfileMetadata:
        """Test ServiceProfileMetadata
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServiceProfileMetadata`
        """
        model = ServiceProfileMetadata()
        if include_optional:
            return ServiceProfileMetadata(
                props = '',
                reg_ex = '',
                reg_ex_msg = '',
                vlan_range_max_value = 56,
                vlan_range_min_value = 56,
                max_qinq = '',
                max_dot1q = 56,
                variable_billing = True,
                global_organization = '',
                limit_auth_key_conn = True,
                allow_secondary_location = True,
                redundant_profile_id = '',
                allow_vc_migration = True,
                connection_editable = True,
                release_vlan = True,
                max_connections_on_port = 56,
                port_assignment_strategy = '',
                eqx_managed_port = True,
                connection_name_editable = True
            )
        else:
            return ServiceProfileMetadata(
        )
        """

    def testServiceProfileMetadata(self):
        """Test ServiceProfileMetadata"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
