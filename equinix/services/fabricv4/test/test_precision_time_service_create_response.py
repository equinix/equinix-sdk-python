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

from equinix.services.fabricv4.models.precision_time_service_create_response import PrecisionTimeServiceCreateResponse

class TestPrecisionTimeServiceCreateResponse(unittest.TestCase):
    """PrecisionTimeServiceCreateResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PrecisionTimeServiceCreateResponse:
        """Test PrecisionTimeServiceCreateResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PrecisionTimeServiceCreateResponse`
        """
        model = PrecisionTimeServiceCreateResponse()
        if include_optional:
            return PrecisionTimeServiceCreateResponse(
                type = 'NTP',
                href = '',
                uuid = '',
                name = '',
                description = '',
                state = 'PROVISIONED',
                package = {"href":"https://api.equinix.com/fabric/v4/timeServicePackage/NTP_STANDARD","code":"NTP_STANDARD","type":"TIME_SERVICE_PACKAGE","bandwidth":10,"accuracyUnit":"microseconds","accuracySla":50,"accuracyAvgMin":1,"accuracyAvgMax":10,"clientsPerSecondMax":100,"redundancySupported":true,"multiSubnetSupported":true,"changeLog":{"createdDateTime":"2023-05-16T07:50:49.749Z","updatedDateTime":"2023-05-17T07:50:49.749Z"}},
                connections = [
                    {"uuid":"095be615-a8ad-4c33-8e9c-c7612fbf6c9f"}
                    ],
                ipv4 = {"primary":"10.0.0.1","secondary":"10.0.0.2","networkMask":"255.255.255.240","defaultGateway":"10.0.0.3"},
                account = {"accountNumber":123456},
                advance_configuration = equinix.services.fabricv4.models.advance_configuration.advanceConfiguration(
                    ntp = [
                        equinix.services.fabricv4.models.md5.md5(
                            type = 'ASCII', 
                            id = '', 
                            password = '', )
                        ], 
                    ptp = equinix.services.fabricv4.models.ptp_advance_configuration.ptpAdvanceConfiguration(
                        time_scale = 'ARB', 
                        domain = 0, 
                        priority1 = 0, 
                        priority2 = 0, 
                        log_announce_interval = 0, 
                        log_sync_interval = 0, 
                        log_delay_req_interval = 0, 
                        transport_mode = 'Multicast', 
                        grant_time = 300, ), ),
                project = equinix.services.fabricv4.models.project.Project(
                    project_id = '44f4c4f8-2f39-494e-838c-d8e640591be5', )
            )
        else:
            return PrecisionTimeServiceCreateResponse(
                type = 'NTP',
                href = '',
                uuid = '',
                state = 'PROVISIONED',
                package = {"href":"https://api.equinix.com/fabric/v4/timeServicePackage/NTP_STANDARD","code":"NTP_STANDARD","type":"TIME_SERVICE_PACKAGE","bandwidth":10,"accuracyUnit":"microseconds","accuracySla":50,"accuracyAvgMin":1,"accuracyAvgMax":10,"clientsPerSecondMax":100,"redundancySupported":true,"multiSubnetSupported":true,"changeLog":{"createdDateTime":"2023-05-16T07:50:49.749Z","updatedDateTime":"2023-05-17T07:50:49.749Z"}},
                ipv4 = {"primary":"10.0.0.1","secondary":"10.0.0.2","networkMask":"255.255.255.240","defaultGateway":"10.0.0.3"},
        )
        """

    def testPrecisionTimeServiceCreateResponse(self):
        """Test PrecisionTimeServiceCreateResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()