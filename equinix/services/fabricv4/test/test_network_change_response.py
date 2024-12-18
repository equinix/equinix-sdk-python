# coding: utf-8

"""
    Equinix Fabric API v4

    Equinix Fabric is an advanced software-defined interconnection solution that enables you to directly, securely and dynamically connect to distributed infrastructure and digital ecosystems on platform Equinix via a single port, Customers can use Fabric to connect to: </br> 1. Cloud Service Providers - Clouds, network and other service providers.  </br> 2. Enterprises - Other Equinix customers, vendors and partners.  </br> 3. Myself - Another customer instance deployed at Equinix. </br> </br> <b>Integrations (SDKs, Tools) links:</b> </br> <a href=\"https://deploy.equinix.com/labs/fabric-java\\\">Fabric Java SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-go\\\">Fabric Go SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-python\\\">Fabric Python SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-provider-equinix\\\">Equinix Terraform Provider</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-equinix-fabric\\\">Fabric Terraform Modules</a> </br> <a href=\"https://deploy.equinix.com/labs/pulumi-provider-equinix/\">Equinix Pulumi Provider</a> </br>

    The version of the OpenAPI document: 4.18
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.fabricv4.models.network_change_response import NetworkChangeResponse

class TestNetworkChangeResponse(unittest.TestCase):
    """NetworkChangeResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NetworkChangeResponse:
        """Test NetworkChangeResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NetworkChangeResponse`
        """
        model = NetworkChangeResponse()
        if include_optional:
            return NetworkChangeResponse(
                pagination = equinix.services.fabricv4.models.pagination.Pagination(
                    offset = 0, 
                    limit = 0, 
                    total = 0, 
                    next = '', 
                    previous = '', ),
                data = [
                    equinix.services.fabricv4.models.network_change.NetworkChange(
                        href = 'https://api.equinix.com/fabric/v4/networks/2a4fb415-5a7f-436f-bae6-02f5e403deec/changes/4b17da68-3d6b-436d-9c8f-2105f3b950d9', 
                        uuid = '4b17da68-3d6b-436d-9c8f-2105f3b950d9', 
                        type = 'NETWORK_CREATION', 
                        status = 'APPROVED', 
                        created_date_time = '2020-11-06T07:00Z', 
                        updated_date_time = '2020-11-06T07:00Z', 
                        data = [
                            equinix.services.fabricv4.models.network_change_operation.NetworkChangeOperation(
                                op = 'replace', 
                                path = '/name', 
                                value = equinix.services.fabricv4.models.value.value(), )
                            ], )
                    ]
            )
        else:
            return NetworkChangeResponse(
        )
        """

    def testNetworkChangeResponse(self):
        """Test NetworkChangeResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
