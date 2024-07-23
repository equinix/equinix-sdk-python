# coding: utf-8

"""
    Equinix Fabric API v4

    Equinix Fabric is an advanced software-defined interconnection solution that enables you to directly, securely and dynamically connect to distributed infrastructure and digital ecosystems on platform Equinix via a single port, Customers can use Fabric to connect to: </br> 1. Cloud Service Providers - Clouds, network and other service providers.  </br> 2. Enterprises - Other Equinix customers, vendors and partners.  </br> 3. Myself - Another customer instance deployed at Equinix. </br> </br> <b>Integrations (SDKs, Tools) links:</b> </br> <a href=\"https://deploy.equinix.com/labs/fabric-java\\\">Fabric Java SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-go\\\">Fabric Go SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-provider-equinix\\\">Equinix Terraform Provider</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-equinix-fabric\\\">Fabric Terraform Modules</a> </br> <a href=\"https://deploy.equinix.com/labs/pulumi-provider-equinix/\">Equinix Pulumi Provider</a> </br>

    The version of the OpenAPI document: 4.14
    Contact: api-support@equinix.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.fabricv4.models.simplified_port import SimplifiedPort

class TestSimplifiedPort(unittest.TestCase):
    """SimplifiedPort unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SimplifiedPort:
        """Test SimplifiedPort
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SimplifiedPort`
        """
        model = SimplifiedPort()
        if include_optional:
            return SimplifiedPort(
                type = 'XF_PORT',
                id = 56,
                href = '',
                uuid = '',
                name = '',
                description = '',
                physical_ports_speed = 0,
                connections_count = 0,
                project = equinix.services.fabricv4.models.project.Project(
                    project_id = '44f4c4f8-2f39-494e-838c-d8e640591be5', ),
                state = 'PENDING',
                cvp_id = '',
                operation = equinix.services.fabricv4.models.port_operation.PortOperation(
                    operational_status = 'UP', 
                    connection_count = 56, 
                    op_status_changed_at = '2020-11-06T07:00Z', ),
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
                service_type = 'EPL',
                bandwidth = 0,
                available_bandwidth = 0,
                used_bandwidth = 0,
                location = equinix.services.fabricv4.models.simplified_location.SimplifiedLocation(
                    region = 'AMER, APAC, EMEA', 
                    metro_name = 'Amsterdam', 
                    metro_code = 'AM', 
                    metro_href = 'https://api.equinix.com/fabric/v4/metros/AM', 
                    ibx = 'AM1', ),
                device = equinix.services.fabricv4.models.port_device.PortDevice(
                    name = '', 
                    redundancy = equinix.services.fabricv4.models.port_device_redundancy.PortDeviceRedundancy(
                        group = '', 
                        priority = 'PRIMARY', ), ),
                interface = equinix.services.fabricv4.models.port_interface.PortInterface(
                    type = '', 
                    if_index = '', 
                    name = '', ),
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
                    group = '', 
                    priority = 'PRIMARY', ),
                encapsulation = equinix.services.fabricv4.models.port_encapsulation.PortEncapsulation(
                    type = 'NULL', 
                    tag_protocol_id = '', ),
                lag_enabled = True,
                settings = equinix.services.fabricv4.models.port_settings.PortSettings(
                    product = '', 
                    buyout = True, 
                    view_port_permission = True, 
                    place_vc_order_permission = True, 
                    layer3_enabled = True, 
                    product_code = '', 
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
                        type = 'XF_PHYSICAL_PORT', 
                        id = 56, 
                        href = '', 
                        state = 'PENDING', 
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
                        interface_speed = 0, 
                        interface_type = '', 
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
                        additional_info = [
                            equinix.services.fabricv4.models.port_additional_info.PortAdditionalInfo(
                                key = '', 
                                value = '', )
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
                            order_number = '', 
                            uuid = '', 
                            signature = equinix.services.fabricv4.models.port_order_signature.PortOrder_signature(
                                signatory = 'DELEGATE', 
                                delegate = equinix.services.fabricv4.models.port_order_signature_delegate.PortOrder_signature_delegate(
                                    first_name = '', 
                                    last_name = '', 
                                    email = '', ), ), ), 
                        operation = equinix.services.fabricv4.models.port_operation.PortOperation(
                            operational_status = 'UP', 
                            connection_count = 56, 
                            op_status_changed_at = '2020-11-06T07:00Z', ), 
                        loas = [
                            equinix.services.fabricv4.models.port_loa.PortLoa(
                                uuid = '', 
                                href = '', )
                            ], )
                    ]
            )
        else:
            return SimplifiedPort(
        )
        """

    def testSimplifiedPort(self):
        """Test SimplifiedPort"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
