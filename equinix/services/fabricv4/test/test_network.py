# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)
"""

import unittest

from equinix.services.fabricv4.models.network import Network

class TestNetwork(unittest.TestCase):
    """Network unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Network:
        """Test Network
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Network`
        """
        model = Network()
        if include_optional:
            return Network(
                type = 'EVPLAN',
                name = '',
                scope = 'REGIONAL',
                location = equinix.services.fabricv4.models.simplified_location.SimplifiedLocation(
                    metro_href = 'https://api.equinix.com/fabric/v4/metros/AM', 
                    region = 'AMER, APAC, EMEA', 
                    metro_name = 'Amsterdam', 
                    metro_code = 'AM', 
                    ibx = 'AM1', ),
                project = equinix.services.fabricv4.models.project.Project(
                    project_id = '44f4c4f8-2f39-494e-838c-d8e640591be5', ),
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
                href = 'https://api.equinix.com/fabric/v4/networks/92dc376a-a932-43aa-a6a2-c806dedbd784',
                uuid = '92dc376a-a932-43aa-a6a2-c806dedbd784',
                state = 'ACTIVE',
                connections_count = 1.337,
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
                change = equinix.services.fabricv4.models.simplified_network_change.SimplifiedNetworkChange(
                    href = 'https://api.equinix.com/fabric/v4/networks/2a4fb415-5a7f-436f-bae6-02f5e403deec/changes/4b17da68-3d6b-436d-9c8f-2105f3b950d9', 
                    uuid = '4b17da68-3d6b-436d-9c8f-2105f3b950d9', 
                    type = 'NETWORK_CREATION', ),
                operation = equinix.services.fabricv4.models.network_operation.NetworkOperation(
                    equinix_status = 'PROVISIONING', ),
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
                links = [
                    equinix.services.fabricv4.models.link.Link(
                        href = '', 
                        rel = '', 
                        method = '', 
                        content_type = '', 
                        authenticate = True, )
                    ]
            )
        else:
            return Network(
                type = 'EVPLAN',
                name = '',
                scope = 'REGIONAL',
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
                href = 'https://api.equinix.com/fabric/v4/networks/92dc376a-a932-43aa-a6a2-c806dedbd784',
                uuid = '92dc376a-a932-43aa-a6a2-c806dedbd784',
                state = 'ACTIVE',
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
        )
        """

    def testNetwork(self):
        """Test Network"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
