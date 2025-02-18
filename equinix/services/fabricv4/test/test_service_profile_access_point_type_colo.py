# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)
"""

import unittest

from equinix.services.fabricv4.models.service_profile_access_point_type_colo import ServiceProfileAccessPointTypeCOLO

class TestServiceProfileAccessPointTypeCOLO(unittest.TestCase):
    """ServiceProfileAccessPointTypeCOLO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServiceProfileAccessPointTypeCOLO:
        """Test ServiceProfileAccessPointTypeCOLO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServiceProfileAccessPointTypeCOLO`
        """
        model = ServiceProfileAccessPointTypeCOLO()
        if include_optional:
            return ServiceProfileAccessPointTypeCOLO(
                uuid = '',
                type = 'VD',
                supported_bandwidths = [
                    50
                    ],
                allow_remote_connections = True,
                allow_custom_bandwidth = True,
                bandwidth_alert_threshold = 1.337,
                allow_bandwidth_auto_approval = True,
                allow_bandwidth_upgrade = True,
                link_protocol_config = equinix.services.fabricv4.models.service_profile_link_protocol_config.ServiceProfileLinkProtocolConfig(
                    encapsulation_strategy = 'CTAGED', 
                    named_tags = [
                        ''
                        ], 
                    vlan_c_tag_label = '', 
                    reuse_vlan_s_tag = True, 
                    encapsulation = 'QINQ', ),
                enable_auto_generate_service_key = True,
                connection_redundancy_required = True,
                api_config = equinix.services.fabricv4.models.api_config.ApiConfig(
                    api_available = True, 
                    integration_id = '', 
                    equinix_managed_port = True, 
                    equinix_managed_vlan = True, 
                    allow_over_subscription = False, 
                    over_subscription_limit = 1, 
                    bandwidth_from_api = True, ),
                connection_label = '',
                authentication_key = equinix.services.fabricv4.models.authentication_key.AuthenticationKey(
                    required = True, 
                    label = 'Service Key', 
                    description = 'description for the authentication key', ),
                metadata = equinix.services.fabricv4.models.service_profile_metadata.ServiceProfileMetadata(
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
                    connection_name_editable = True, )
            )
        else:
            return ServiceProfileAccessPointTypeCOLO(
                type = 'VD',
        )
        """

    def testServiceProfileAccessPointTypeCOLO(self):
        """Test ServiceProfileAccessPointTypeCOLO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
