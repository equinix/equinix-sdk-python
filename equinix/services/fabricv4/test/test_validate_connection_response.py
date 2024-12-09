# coding: utf-8

"""
    Equinix Fabric API v4

    Equinix Fabric is an advanced software-defined interconnection solution that enables you to directly, securely and dynamically connect to distributed infrastructure and digital ecosystems on platform Equinix via a single port, Customers can use Fabric to connect to: </br> 1. Cloud Service Providers - Clouds, network and other service providers.  </br> 2. Enterprises - Other Equinix customers, vendors and partners.  </br> 3. Myself - Another customer instance deployed at Equinix. </br> </br> <b>Integrations (SDKs, Tools) links:</b> </br> <a href=\"https://deploy.equinix.com/labs/fabric-java\\\">Fabric Java SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-go\\\">Fabric Go SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-python\\\">Fabric Python SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-provider-equinix\\\">Equinix Terraform Provider</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-equinix-fabric\\\">Fabric Terraform Modules</a> </br> <a href=\"https://deploy.equinix.com/labs/pulumi-provider-equinix/\">Equinix Pulumi Provider</a> </br>

    The version of the OpenAPI document: 4.17
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.fabricv4.models.validate_connection_response import ValidateConnectionResponse

class TestValidateConnectionResponse(unittest.TestCase):
    """ValidateConnectionResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ValidateConnectionResponse:
        """Test ValidateConnectionResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ValidateConnectionResponse`
        """
        model = ValidateConnectionResponse()
        if include_optional:
            return ValidateConnectionResponse(
                uuid = '',
                bandwidth = 0,
                redundancy = equinix.services.fabricv4.models.connection_redundancy.ConnectionRedundancy(
                    group = '', 
                    priority = 'PRIMARY', ),
                a_side = equinix.services.fabricv4.models.connection_side.ConnectionSide(
                    service_token = equinix.services.fabricv4.models.service_token.ServiceToken(
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
                            z_side = equinix.services.fabricv4.models.service_token_side.ServiceTokenSide(
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
                                    ], ), ), 
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
                            project_id = '44f4c4f8-2f39-494e-838c-d8e640591be5', ), ), 
                    access_point = equinix.services.fabricv4.models.access_point.AccessPoint(
                        profile = equinix.services.fabricv4.models.simplified_service_profile.SimplifiedServiceProfile(
                            href = '', 
                            name = 'Sample Service Profile', 
                            uuid = '', 
                            description = 'offering connectivity to my-network', 
                            tags = [
                                ''
                                ], 
                            visibility = 'PRIVATE', 
                            allowed_emails = [
                                ''
                                ], 
                            access_point_type_configs = [
                                equinix.services.fabricv4.models.service_profile_access_point_type.ServiceProfileAccessPointType()
                                ], 
                            custom_fields = [
                                equinix.services.fabricv4.models.custom_field.CustomField(
                                    label = 'Account Number', 
                                    description = 'Provide a valid account number', 
                                    required = True, 
                                    data_type = 'STRING', 
                                    options = [
                                        ''
                                        ], 
                                    capture_in_email = True, )
                                ], 
                            marketing_info = equinix.services.fabricv4.models.marketing_info.MarketingInfo(
                                logo = '', 
                                promotion = True, 
                                process_steps = [
                                    equinix.services.fabricv4.models.process_step.ProcessStep(
                                        title = '', 
                                        sub_title = '', 
                                        description = '', )
                                    ], ), 
                            ports = [
                                equinix.services.fabricv4.models.service_profile_access_point_colo.ServiceProfileAccessPointCOLO(
                                    type = 'XF_PORT', 
                                    uuid = '94662143-e21b-4098-bfcf-e9416f47eae1', 
                                    seller_region = '', 
                                    seller_region_description = '', 
                                    cross_connect_id = '', )
                                ], 
                            virtual_devices = [
                                equinix.services.fabricv4.models.service_profile_access_point_vd.ServiceProfileAccessPointVD(
                                    type = 'VD', 
                                    uuid = '94662143-e21b-4098-bfcf-e9416f47eae1', 
                                    interface_uuid = '94662143-e21b-4098-bfcf-e9416f47eae1', )
                                ], 
                            metros = [
                                equinix.services.fabricv4.models.service_metro.ServiceMetro(
                                    code = '', 
                                    name = '', 
                                    vc_bandwidth_max = 56, 
                                    ibxs = [
                                        ''
                                        ], 
                                    in_trail = True, 
                                    display_name = '', 
                                    seller_regions = {
                                        'key' : ''
                                        }, )
                                ], 
                            self_profile = True, 
                            project_id = '', ), 
                        router = equinix.services.fabricv4.models.cloud_router.CloudRouter(
                            href = 'https://api.equinix.com/fabric/v4/routers/3c9b8e7a2-f3b1-4576-a4a9-1366a63df170', 
                            uuid = 'c9b8e7a2-f3b1-4576-a4a9-1366a63df170', 
                            name = 'test-fg-1', 
                            equinix_asn = 30000, 
                            bgp_ipv4_routes_count = 0, 
                            bgp_ipv6_routes_count = 0, 
                            connections_count = 0, 
                            distinct_ipv4_prefixes_count = 0, 
                            distinct_ipv6_prefixes_count = 0, 
                            marketplace_subscription = equinix.services.fabricv4.models.marketplace_subscription.marketplaceSubscription(
                                href = 'https://api.equinix.com/fabric/v4/marketplaceSubscriptions/20d32a80-0d61-4333-bc03-707b591ae2f5', 
                                uuid = '20d32a80-0d61-4333-bc03-707b591ae2f5', ), 
                            change_log = equinix.services.fabricv4.models.changelog.Changelog(
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
                            change = equinix.services.fabricv4.models.cloud_router_change.CloudRouterChange(
                                uuid = '', 
                                type = 'ROUTER_UPDATE', 
                                status = 'COMPLETED', 
                                created_date_time = '2020-11-06T07:00Z', 
                                updated_date_time = '2020-11-06T07:00Z', 
                                information = '', 
                                data = equinix.services.fabricv4.models.cloud_router_change_operation.CloudRouterChangeOperation(
                                    op = 'replace', 
                                    path = '', 
                                    value = equinix.services.fabricv4.models.value.value(), ), ), ), 
                        seller_region = '', 
                        peering_type = 'PRIVATE', 
                        authentication_key = '', 
                        provider_connection_id = '', 
                        virtual_network = equinix.services.fabricv4.models.virtual_network.VirtualNetwork(
                            href = '', 
                            uuid = '', ), 
                        interconnection = equinix.services.fabricv4.models.metal_interconnection.MetalInterconnection(
                            uuid = '', ), 
                        vpic_interface = equinix.services.fabricv4.models.vpic_interface.VpicInterface(
                            href = '', 
                            uuid = '', ), ), 
                    internet_access = equinix.services.fabricv4.models.internet_access.InternetAccess(
                        uuid = '', ), 
                    company_profile = equinix.services.fabricv4.models.connection_company_profile.ConnectionCompanyProfile(
                        id = 1, 
                        name = 'Company-1', 
                        global_org_id = '', ), 
                    invitation = equinix.services.fabricv4.models.connection_invitation.ConnectionInvitation(
                        email = 'test@equinix.com', 
                        message = 'Hello, Please accept my invitation', 
                        ctr_draft_order_id = '', ), 
                    additional_info = [
                        equinix.services.fabricv4.models.connection_side_additional_info.ConnectionSideAdditionalInfo(
                            key = '', 
                            value = '', )
                        ], ),
                z_side = equinix.services.fabricv4.models.connection_side.ConnectionSide(
                    service_token = equinix.services.fabricv4.models.service_token.ServiceToken(
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
                                    ], ), ), 
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
                            project_id = '44f4c4f8-2f39-494e-838c-d8e640591be5', ), ), 
                    access_point = equinix.services.fabricv4.models.access_point.AccessPoint(
                        profile = equinix.services.fabricv4.models.simplified_service_profile.SimplifiedServiceProfile(
                            href = '', 
                            name = 'Sample Service Profile', 
                            uuid = '', 
                            description = 'offering connectivity to my-network', 
                            tags = [
                                ''
                                ], 
                            visibility = 'PRIVATE', 
                            allowed_emails = [
                                ''
                                ], 
                            access_point_type_configs = [
                                equinix.services.fabricv4.models.service_profile_access_point_type.ServiceProfileAccessPointType()
                                ], 
                            custom_fields = [
                                equinix.services.fabricv4.models.custom_field.CustomField(
                                    label = 'Account Number', 
                                    description = 'Provide a valid account number', 
                                    required = True, 
                                    data_type = 'STRING', 
                                    options = [
                                        ''
                                        ], 
                                    capture_in_email = True, )
                                ], 
                            marketing_info = equinix.services.fabricv4.models.marketing_info.MarketingInfo(
                                logo = '', 
                                promotion = True, 
                                process_steps = [
                                    equinix.services.fabricv4.models.process_step.ProcessStep(
                                        title = '', 
                                        sub_title = '', 
                                        description = '', )
                                    ], ), 
                            ports = [
                                equinix.services.fabricv4.models.service_profile_access_point_colo.ServiceProfileAccessPointCOLO(
                                    type = 'XF_PORT', 
                                    uuid = '94662143-e21b-4098-bfcf-e9416f47eae1', 
                                    seller_region = '', 
                                    seller_region_description = '', 
                                    cross_connect_id = '', )
                                ], 
                            virtual_devices = [
                                equinix.services.fabricv4.models.service_profile_access_point_vd.ServiceProfileAccessPointVD(
                                    type = 'VD', 
                                    uuid = '94662143-e21b-4098-bfcf-e9416f47eae1', 
                                    interface_uuid = '94662143-e21b-4098-bfcf-e9416f47eae1', )
                                ], 
                            metros = [
                                equinix.services.fabricv4.models.service_metro.ServiceMetro(
                                    code = '', 
                                    name = '', 
                                    vc_bandwidth_max = 56, 
                                    ibxs = [
                                        ''
                                        ], 
                                    in_trail = True, 
                                    display_name = '', 
                                    seller_regions = {
                                        'key' : ''
                                        }, )
                                ], 
                            self_profile = True, 
                            project_id = '', ), 
                        router = equinix.services.fabricv4.models.cloud_router.CloudRouter(
                            href = 'https://api.equinix.com/fabric/v4/routers/3c9b8e7a2-f3b1-4576-a4a9-1366a63df170', 
                            uuid = 'c9b8e7a2-f3b1-4576-a4a9-1366a63df170', 
                            name = 'test-fg-1', 
                            equinix_asn = 30000, 
                            bgp_ipv4_routes_count = 0, 
                            bgp_ipv6_routes_count = 0, 
                            connections_count = 0, 
                            distinct_ipv4_prefixes_count = 0, 
                            distinct_ipv6_prefixes_count = 0, 
                            marketplace_subscription = equinix.services.fabricv4.models.marketplace_subscription.marketplaceSubscription(
                                href = 'https://api.equinix.com/fabric/v4/marketplaceSubscriptions/20d32a80-0d61-4333-bc03-707b591ae2f5', 
                                uuid = '20d32a80-0d61-4333-bc03-707b591ae2f5', ), 
                            change_log = equinix.services.fabricv4.models.changelog.Changelog(
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
                            change = equinix.services.fabricv4.models.cloud_router_change.CloudRouterChange(
                                uuid = '', 
                                type = 'ROUTER_UPDATE', 
                                status = 'COMPLETED', 
                                created_date_time = '2020-11-06T07:00Z', 
                                updated_date_time = '2020-11-06T07:00Z', 
                                information = '', 
                                data = equinix.services.fabricv4.models.cloud_router_change_operation.CloudRouterChangeOperation(
                                    op = 'replace', 
                                    path = '', 
                                    value = equinix.services.fabricv4.models.value.value(), ), ), ), 
                        seller_region = '', 
                        peering_type = 'PRIVATE', 
                        authentication_key = '', 
                        provider_connection_id = '', 
                        virtual_network = equinix.services.fabricv4.models.virtual_network.VirtualNetwork(
                            href = '', 
                            uuid = '', ), 
                        interconnection = equinix.services.fabricv4.models.metal_interconnection.MetalInterconnection(
                            uuid = '', ), 
                        vpic_interface = equinix.services.fabricv4.models.vpic_interface.VpicInterface(
                            href = '', 
                            uuid = '', ), ), 
                    internet_access = equinix.services.fabricv4.models.internet_access.InternetAccess(
                        uuid = '', ), 
                    company_profile = equinix.services.fabricv4.models.connection_company_profile.ConnectionCompanyProfile(
                        id = 1, 
                        name = 'Company-1', 
                        global_org_id = '', ), 
                    invitation = equinix.services.fabricv4.models.connection_invitation.ConnectionInvitation(
                        email = 'test@equinix.com', 
                        message = 'Hello, Please accept my invitation', 
                        ctr_draft_order_id = '', ), 
                    additional_info = [
                        equinix.services.fabricv4.models.connection_side_additional_info.ConnectionSideAdditionalInfo(
                            key = '', 
                            value = '', )
                        ], )
            )
        else:
            return ValidateConnectionResponse(
        )
        """

    def testValidateConnectionResponse(self):
        """Test ValidateConnectionResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()