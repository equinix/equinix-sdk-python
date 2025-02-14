# coding: utf-8

"""
    Equinix Fabric API v4

    Equinix Fabric is an advanced software-defined interconnection solution that enables you to directly, securely and dynamically connect to distributed infrastructure and digital ecosystems on platform Equinix via a single port, Customers can use Fabric to connect to: </br> 1. Cloud Service Providers - Clouds, network and other service providers.  </br> 2. Enterprises - Other Equinix customers, vendors and partners.  </br> 3. Myself - Another customer instance deployed at Equinix. </br> </br> <b>Integrations (SDKs, Tools) links:</b> </br> <a href=\"https://deploy.equinix.com/labs/fabric-java\\\">Fabric Java SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-go\\\">Fabric Go SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-python\\\">Fabric Python SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-provider-equinix\\\">Equinix Terraform Provider</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-equinix-fabric\\\">Fabric Terraform Modules</a> </br> <a href=\"https://deploy.equinix.com/labs/pulumi-provider-equinix/\">Equinix Pulumi Provider</a> </br>

    Generated by OpenAPI Generator (https://openapi-generator.tech)
"""


import unittest

from equinix.services.fabricv4.models.route_aggregation_rules_post_request import RouteAggregationRulesPostRequest

class TestRouteAggregationRulesPostRequest(unittest.TestCase):
    """RouteAggregationRulesPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RouteAggregationRulesPostRequest:
        """Test RouteAggregationRulesPostRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RouteAggregationRulesPostRequest`
        """
        model = RouteAggregationRulesPostRequest()
        if include_optional:
            return RouteAggregationRulesPostRequest(
                data = [
                    equinix.services.fabricv4.models.route_aggregation_rules_base.RouteAggregationRulesBase(
                        name = 'Private-subnet-Aggregation', 
                        description = '', 
                        prefix = '192.168.0.0/24', )
                    ]
            )
        else:
            return RouteAggregationRulesPostRequest(
        )
        """

    def testRouteAggregationRulesPostRequest(self):
        """Test RouteAggregationRulesPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
