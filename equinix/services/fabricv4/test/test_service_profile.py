# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.fabricv4.models.service_profile import ServiceProfile

class TestServiceProfile(unittest.TestCase):
    """ServiceProfile unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServiceProfile:
        """Test ServiceProfile
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServiceProfile`
        """
        model = ServiceProfile()
        if include_optional:
            return ServiceProfile(
                state = 'ACTIVE',
                account = None,
                project = equinix.services.fabricv4.models.project.Project(
                    project_id = '44f4c4f8-2f39-494e-838c-d8e640591be5', ),
                change_log = None,
                href = '',
                type = 'L2_PROFILE',
                name = 'Sample Service Profile',
                uuid = '',
                description = 'offering connectivity to my-network',
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
                        location = equinix.services.fabricv4.models.simplified_location.SimplifiedLocation(
                            metro_href = 'https://api.equinix.com/fabric/v4/metros/AM', 
                            region = 'AMER, APAC, EMEA', 
                            metro_name = 'Amsterdam', 
                            metro_code = 'AM', 
                            ibx = 'AM1', ), 
                        seller_region = '', 
                        seller_region_description = '', 
                        cross_connect_id = '', )
                    ],
                virtual_devices = [
                    equinix.services.fabricv4.models.service_profile_access_point_vd.ServiceProfileAccessPointVD(
                        type = 'VD', 
                        uuid = '94662143-e21b-4098-bfcf-e9416f47eae1', 
                        location = equinix.services.fabricv4.models.simplified_location.SimplifiedLocation(
                            metro_href = 'https://api.equinix.com/fabric/v4/metros/AM', 
                            region = 'AMER, APAC, EMEA', 
                            metro_name = 'Amsterdam', 
                            metro_code = 'AM', 
                            ibx = 'AM1', ), 
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
                project_id = ''
            )
        else:
            return ServiceProfile(
        )
        """

    def testServiceProfile(self):
        """Test ServiceProfile"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
