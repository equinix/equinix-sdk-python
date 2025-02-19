# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.fabricv4.models.network_post_request import NetworkPostRequest

class TestNetworkPostRequest(unittest.TestCase):
    """NetworkPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NetworkPostRequest:
        """Test NetworkPostRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NetworkPostRequest`
        """
        model = NetworkPostRequest()
        if include_optional:
            return NetworkPostRequest(
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
                    ]
            )
        else:
            return NetworkPostRequest(
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
        )
        """

    def testNetworkPostRequest(self):
        """Test NetworkPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
