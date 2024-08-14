# coding: utf-8

"""
    Equinix Fabric API v4

    Equinix Fabric is an advanced software-defined interconnection solution that enables you to directly, securely and dynamically connect to distributed infrastructure and digital ecosystems on platform Equinix via a single port, Customers can use Fabric to connect to: </br> 1. Cloud Service Providers - Clouds, network and other service providers.  </br> 2. Enterprises - Other Equinix customers, vendors and partners.  </br> 3. Myself - Another customer instance deployed at Equinix. </br> </br> <b>Integrations (SDKs, Tools) links:</b> </br> <a href=\"https://deploy.equinix.com/labs/fabric-java\\\">Fabric Java SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-go\\\">Fabric Go SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-provider-equinix\\\">Equinix Terraform Provider</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-equinix-fabric\\\">Fabric Terraform Modules</a> </br> <a href=\"https://deploy.equinix.com/labs/pulumi-provider-equinix/\">Equinix Pulumi Provider</a> </br>

    The version of the OpenAPI document: 4.15
    Contact: api-support@equinix.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.fabricv4.models.all_physical_ports_response import AllPhysicalPortsResponse

class TestAllPhysicalPortsResponse(unittest.TestCase):
    """AllPhysicalPortsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AllPhysicalPortsResponse:
        """Test AllPhysicalPortsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AllPhysicalPortsResponse`
        """
        model = AllPhysicalPortsResponse()
        if include_optional:
            return AllPhysicalPortsResponse(
                pagination = equinix.services.fabricv4.models.pagination.Pagination(
                    offset = 0, 
                    limit = 0, 
                    total = 0, 
                    next = '', 
                    previous = '', ),
                data = [
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
                        notifications = [
                            equinix.services.fabricv4.models.port_notification.PortNotification(
                                type = 'NOTIFICATION', 
                                registered_users = [
                                    ''
                                    ], )
                            ], 
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
                            customer_reference_id = '', 
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
            return AllPhysicalPortsResponse(
        )
        """

    def testAllPhysicalPortsResponse(self):
        """Test AllPhysicalPortsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
