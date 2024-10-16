# coding: utf-8

"""
    Equinix Fabric API v4

    Equinix Fabric is an advanced software-defined interconnection solution that enables you to directly, securely and dynamically connect to distributed infrastructure and digital ecosystems on platform Equinix via a single port, Customers can use Fabric to connect to: </br> 1. Cloud Service Providers - Clouds, network and other service providers.  </br> 2. Enterprises - Other Equinix customers, vendors and partners.  </br> 3. Myself - Another customer instance deployed at Equinix. </br> </br> <b>Integrations (SDKs, Tools) links:</b> </br> <a href=\"https://deploy.equinix.com/labs/fabric-java\\\">Fabric Java SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-go\\\">Fabric Go SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-python\\\">Fabric Python SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-provider-equinix\\\">Equinix Terraform Provider</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-equinix-fabric\\\">Fabric Terraform Modules</a> </br> <a href=\"https://deploy.equinix.com/labs/pulumi-provider-equinix/\">Equinix Pulumi Provider</a> </br>

    The version of the OpenAPI document: 4.17
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.fabricv4.models.service_token import ServiceToken

class TestServiceToken(unittest.TestCase):
    """ServiceToken unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServiceToken:
        """Test ServiceToken
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServiceToken`
        """
        model = ServiceToken()
        if include_optional:
            return ServiceToken(
                type = 'VC_TOKEN',
                href = '',
                uuid = '',
                issuer_side = 'ASIDE',
                name = '',
                description = '',
                expiration_date_time = '2020-11-06T07:00Z',
                connection = equinix.services.fabricv4.models.service_token_connection.ServiceTokenConnection(
                    type = 'EVPL_VC', 
                    href = '', 
                    uuid = '', 
                    allow_remote_connection = True, 
                    allow_custom_bandwidth = True, 
                    bandwidth_limit = 0, 
                    supported_bandwidths = [
                        56
                        ], 
                    a_side = equinix.services.fabricv4.models.service_token_side.ServiceTokenSide(
                        access_point_selectors = [
                            equinix.services.fabricv4.models.access_point_selector.AccessPointSelector(
                                port = equinix.services.fabricv4.models.simplified_metadata_entity.SimplifiedMetadataEntity(
                                    href = '', 
                                    uuid = '', 
                                    cvp_id = 56, 
                                    bandwidth = 1.337, 
                                    port_name = '', 
                                    encapsulation_protocol_type = '', 
                                    account_name = '', 
                                    priority = '', 
                                    location = equinix.services.fabricv4.models.simplified_location.SimplifiedLocation(
                                        region = 'AMER, APAC, EMEA', 
                                        metro_name = 'Amsterdam', 
                                        metro_code = 'AM', 
                                        metro_href = 'https://api.equinix.com/fabric/v4/metros/AM', 
                                        ibx = 'AM1', ), ), 
                                link_protocol = equinix.services.fabricv4.models.simplified_link_protocol.SimplifiedLinkProtocol(
                                    vlan_tag = 2, 
                                    vlan_s_tag = 2, 
                                    vlan_c_tag = 2, ), 
                                virtual_device = equinix.services.fabricv4.models.simplified_virtual_device.SimplifiedVirtualDevice(
                                    href = '', 
                                    uuid = '', 
                                    name = '', 
                                    cluster = '', ), 
                                interface = equinix.services.fabricv4.models.virtual_device_interface.VirtualDeviceInterface(
                                    id = 56, 
                                    uuid = '', ), 
                                network = equinix.services.fabricv4.models.simplified_token_network.SimplifiedTokenNetwork(
                                    href = '', 
                                    uuid = '', 
                                    name = '', 
                                    scope = 'LOCAL', ), )
                            ], ), 
                    z_side = equinix.services.fabricv4.models.service_token_side.ServiceTokenSide(), ),
                state = 'ACTIVE',
                notifications = [
                    equinix.services.fabricv4.models.simplified_notification.SimplifiedNotification(
                        type = 'BANDWIDTH_ALERT', 
                        send_interval = '', 
                        emails = [
                            ''
                            ], 
                        registered_users = [
                            ''
                            ], )
                    ],
                account = equinix.services.fabricv4.models.simplified_account.SimplifiedAccount(
                    account_number = 56, 
                    account_name = '', 
                    org_id = 56, 
                    organization_name = '', 
                    global_org_id = '', 
                    global_organization_name = '', 
                    ucm_id = '', 
                    global_cust_id = '', 
                    reseller_account_number = 56, 
                    reseller_account_name = '', 
                    reseller_ucm_id = '', 
                    reseller_org_id = 56, ),
                changelog = equinix.services.fabricv4.models.changelog.Changelog(
                    created_by = 'johnsmith', 
                    created_by_full_name = 'John Smith', 
                    created_by_email = 'john.smith@example.com', 
                    created_date_time = '2020-11-06T07:00Z', 
                    updated_by = 'johnsmith', 
                    updated_by_full_name = 'John Smith', 
                    updated_by_email = 'john.smith@example.com', 
                    updated_date_time = '2020-11-06T07:00Z', 
                    deleted_by = 'johnsmith', 
                    deleted_by_full_name = 'John Smith', 
                    deleted_by_email = 'john.smith@example.com', 
                    deleted_date_time = '2020-11-06T07:00Z', ),
                project = equinix.services.fabricv4.models.project.Project(
                    project_id = '44f4c4f8-2f39-494e-838c-d8e640591be5', )
            )
        else:
            return ServiceToken(
        )
        """

    def testServiceToken(self):
        """Test ServiceToken"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
