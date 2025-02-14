# coding: utf-8

"""
    Equinix Fabric API v4

    Equinix Fabric is an advanced software-defined interconnection solution that enables you to directly, securely and dynamically connect to distributed infrastructure and digital ecosystems on platform Equinix via a single port, Customers can use Fabric to connect to: </br> 1. Cloud Service Providers - Clouds, network and other service providers.  </br> 2. Enterprises - Other Equinix customers, vendors and partners.  </br> 3. Myself - Another customer instance deployed at Equinix. </br> </br> <b>Integrations (SDKs, Tools) links:</b> </br> <a href=\"https://deploy.equinix.com/labs/fabric-java\\\">Fabric Java SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-go\\\">Fabric Go SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-python\\\">Fabric Python SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-provider-equinix\\\">Equinix Terraform Provider</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-equinix-fabric\\\">Fabric Terraform Modules</a> </br> <a href=\"https://deploy.equinix.com/labs/pulumi-provider-equinix/\">Equinix Pulumi Provider</a> </br>

    Generated by OpenAPI Generator (https://openapi-generator.tech)
"""


import unittest

from equinix.services.fabricv4.models.service_search_response import ServiceSearchResponse

class TestServiceSearchResponse(unittest.TestCase):
    """ServiceSearchResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServiceSearchResponse:
        """Test ServiceSearchResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServiceSearchResponse`
        """
        model = ServiceSearchResponse()
        if include_optional:
            return ServiceSearchResponse(
                pagination = equinix.services.fabricv4.models.pagination.Pagination(
                    offset = 0, 
                    limit = 0, 
                    total = 0, 
                    next = '', 
                    previous = '', ),
                data = [
                    equinix.services.fabricv4.models.precision_time_service_response.precisionTimeServiceResponse(
                        href = '', 
                        type = 'NTP', 
                        name = '', 
                        uuid = '', 
                        state = 'CANCELLED', 
                        package = {"href":"https://api.equinix.com/fabric/v4/timeServicePackage/NTP_STANDARD","type":"TIME_SERVICE_PACKAGE","code":"NTP_STANDARD","bandwidth":10,"accuracySlaUnit":"microseconds","accuracySla":50,"accuracySlaMin":1,"accuracySlaMax":10,"clientsPerSecondMax":100,"redundancySupported":true,"multiSubnetSupported":true,"changeLog":{"createdDateTime":"2023-05-16T07:50:49.749Z","updatedDateTime":"2023-05-17T07:50:49.749Z"}}, 
                        connections = [
                            equinix.services.fabricv4.models.fabric_connection_response.fabricConnectionResponse(
                                href = '', 
                                type = '', 
                                uuid = '', 
                                a_side = equinix.services.fabricv4.models.fabric_connection_access_point.fabricConnectionAccessPoint(
                                    access_point = equinix.services.fabricv4.models.access_point.AccessPoint(
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
                                        location = equinix.services.fabricv4.models.simplified_location.SimplifiedLocation(
                                            metro_href = 'https://api.equinix.com/fabric/v4/metros/AM', 
                                            region = 'AMER, APAC, EMEA', 
                                            metro_name = 'Amsterdam', 
                                            metro_code = 'AM', 
                                            ibx = 'AM1', ), 
                                        port = equinix.services.fabricv4.models.simplified_port.SimplifiedPort(
                                            href = '', 
                                            id = 56, 
                                            uuid = '', 
                                            name = '', 
                                            description = '', 
                                            physical_ports_speed = 0, 
                                            connections_count = 0, 
                                            project = equinix.services.fabricv4.models.project.Project(
                                                project_id = '44f4c4f8-2f39-494e-838c-d8e640591be5', ), 
                                            operation = equinix.services.fabricv4.models.port_operation.PortOperation(
                                                operational_status = 'UP', 
                                                connection_count = 56, 
                                                evpl_vc_count = 56, 
                                                fg_vc_count = 56, 
                                                access_vc_count = 56, 
                                                op_status_changed_at = '2020-11-06T07:00Z', ), 
                                            service_type = 'EPL', 
                                            bandwidth = 0, 
                                            available_bandwidth = 0, 
                                            used_bandwidth = 0, 
                                            device = equinix.services.fabricv4.models.port_device.PortDevice(
                                                name = '', 
                                                redundancy = equinix.services.fabricv4.models.port_device_redundancy.PortDeviceRedundancy(
                                                    group = '', 
                                                    priority = 'PRIMARY', ), ), 
                                            interface = equinix.services.fabricv4.models.port_interface.PortInterface(), 
                                            tether = equinix.services.fabricv4.models.port_tether.PortTether(
                                                cross_connect_id = '', 
                                                cabinet_number = '', 
                                                system_name = '', 
                                                patch_panel = '', 
                                                patch_panel_port_a = '', 
                                                patch_panel_port_b = '', 
                                                ibx = '', ), 
                                            demarcation_point = equinix.services.fabricv4.models.port_demarcation_point.PortDemarcationPoint(
                                                cabinet_unique_space_id = '', 
                                                cage_unique_space_id = '', 
                                                patch_panel = '', 
                                                patch_panel_name = '', 
                                                patch_panel_port_a = '', 
                                                patch_panel_port_b = '', 
                                                connector_type = '', 
                                                ibx = '', ), 
                                            redundancy = equinix.services.fabricv4.models.port_redundancy.PortRedundancy(
                                                enabled = True, 
                                                group = '', ), 
                                            encapsulation = equinix.services.fabricv4.models.port_encapsulation.PortEncapsulation(
                                                tag_protocol_id = '', ), 
                                            lag_enabled = True, 
                                            settings = equinix.services.fabricv4.models.port_settings.PortSettings(
                                                buyout = True, 
                                                view_port_permission = True, 
                                                place_vc_order_permission = True, 
                                                layer3_enabled = True, 
                                                shared_port_type = True, 
                                                shared_port_product = 'NETWORK_EDGE', 
                                                package_type = 'STANDARD', ), 
                                            physical_port_quantity = 56, 
                                            additional_info = [
                                                equinix.services.fabricv4.models.port_additional_info.PortAdditionalInfo(
                                                    key = '', 
                                                    value = '', )
                                                ], 
                                            physical_ports = [
                                                equinix.services.fabricv4.models.physical_port.PhysicalPort(
                                                    href = '', 
                                                    id = 56, 
                                                    interface_speed = 0, 
                                                    interface_type = '', 
                                                    uuid = '', 
                                                    notifications = [
                                                        equinix.services.fabricv4.models.port_notification.PortNotification(
                                                            type = 'NOTIFICATION', 
                                                            registered_users = [
                                                                ''
                                                                ], )
                                                        ], 
                                                    order = equinix.services.fabricv4.models.port_order.PortOrder(
                                                        purchase_order = equinix.services.fabricv4.models.port_order_purchase_order.PortOrder_purchaseOrder(
                                                            number = '', 
                                                            amount = '', 
                                                            start_date = '', 
                                                            end_date = '', 
                                                            attachment_id = '', 
                                                            selection_type = 'EXEMPTION', ), 
                                                        order_id = '', 
                                                        customer_reference_id = '', 
                                                        order_number = '', 
                                                        uuid = '', 
                                                        signature = equinix.services.fabricv4.models.port_order_signature.PortOrder_signature(
                                                            signatory = 'DELEGATE', 
                                                            delegate = equinix.services.fabricv4.models.port_order_signature_delegate.PortOrder_signature_delegate(
                                                                first_name = '', 
                                                                last_name = '', 
                                                                email = '', ), ), ), 
                                                    loas = [
                                                        equinix.services.fabricv4.models.port_loa.PortLoa(
                                                            uuid = '', 
                                                            href = '', )
                                                        ], )
                                                ], ), 
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
                                            connections_count = 0, 
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
                                        link_protocol = equinix.services.fabricv4.models.simplified_link_protocol.SimplifiedLinkProtocol(
                                            vlan_tag = 2, 
                                            vlan_s_tag = 2, 
                                            vlan_c_tag = 2, ), 
                                        virtual_device = equinix.services.fabricv4.models.virtual_device.VirtualDevice(
                                            href = '', 
                                            uuid = '', 
                                            name = '', ), 
                                        interface = equinix.services.fabricv4.models.interface.Interface(
                                            href = '', 
                                            uuid = '', 
                                            id = 56, 
                                            project_id = '', ), 
                                        network = equinix.services.fabricv4.models.simplified_network.SimplifiedNetwork(
                                            href = 'https://api.equinix.com/fabric/v4/networks/92dc376a-a932-43aa-a6a2-c806dedbd784', 
                                            uuid = '92dc376a-a932-43aa-a6a2-c806dedbd784', 
                                            name = 'My EVPLAN Network', 
                                            links = [
                                                equinix.services.fabricv4.models.link.Link(
                                                    href = '', 
                                                    rel = '', 
                                                    method = '', 
                                                    content_type = '', 
                                                    authenticate = True, )
                                                ], 
                                            scope = 'REGIONAL', ), 
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
                                            uuid = '', ), ), ), 
                                z_side = equinix.services.fabricv4.models.fabric_connection_access_point.fabricConnectionAccessPoint(), )
                            ], 
                        ipv4 = {"primary":"10.0.0.1","secondary":"10.0.0.2","networkMask":"255.255.255.240","defaultGateway":"10.0.0.3"}, 
                        ntp_advanced_configuration = [
                            equinix.services.fabricv4.models.md5.md5(
                                key_number = 10, 
                                key = '0123456789', )
                            ], 
                        ptp_advanced_configuration = equinix.services.fabricv4.models.ptp_advance_configuration.ptpAdvanceConfiguration(
                            time_scale = 'ARB', 
                            domain = 0, 
                            priority1 = 128, 
                            priority2 = 128, 
                            log_announce_interval = 1, 
                            log_sync_interval = -4, 
                            log_delay_req_interval = -4, 
                            transport_mode = 'MULTICAST', 
                            grant_time = 300, ), 
                        project = equinix.services.fabricv4.models.project.Project(
                            project_id = '44f4c4f8-2f39-494e-838c-d8e640591be5', ), 
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
                        order = equinix.services.fabricv4.models.precision_time_order.precisionTimeOrder(
                            purchase_order_number = '', 
                            customer_reference_number = '', 
                            order_number = '', ), 
                        pricing = equinix.services.fabricv4.models.precision_time_price.precisionTimePrice(
                            currency = '', 
                            charges = [
                                equinix.services.fabricv4.models.price_charge.PriceCharge(
                                    price = 0, )
                                ], ), 
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
                            deleted_date_time = '2020-11-06T07:00Z', ), )
                    ]
            )
        else:
            return ServiceSearchResponse(
        )
        """

    def testServiceSearchResponse(self):
        """Test ServiceSearchResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
