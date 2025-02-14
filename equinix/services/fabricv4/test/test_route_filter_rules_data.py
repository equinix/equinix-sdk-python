# coding: utf-8

"""
    Equinix Fabric API v4

    Equinix Fabric is an advanced software-defined interconnection solution that enables you to directly, securely and dynamically connect to distributed infrastructure and digital ecosystems on platform Equinix via a single port, Customers can use Fabric to connect to: </br> 1. Cloud Service Providers - Clouds, network and other service providers.  </br> 2. Enterprises - Other Equinix customers, vendors and partners.  </br> 3. Myself - Another customer instance deployed at Equinix. </br> </br> <b>Integrations (SDKs, Tools) links:</b> </br> <a href=\"https://deploy.equinix.com/labs/fabric-java\\\">Fabric Java SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-go\\\">Fabric Go SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-python\\\">Fabric Python SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-provider-equinix\\\">Equinix Terraform Provider</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-equinix-fabric\\\">Fabric Terraform Modules</a> </br> <a href=\"https://deploy.equinix.com/labs/pulumi-provider-equinix/\">Equinix Pulumi Provider</a> </br>

    Generated by OpenAPI Generator (https://openapi-generator.tech)
"""


import unittest

from equinix.services.fabricv4.models.route_filter_rules_data import RouteFilterRulesData

class TestRouteFilterRulesData(unittest.TestCase):
    """RouteFilterRulesData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RouteFilterRulesData:
        """Test RouteFilterRulesData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RouteFilterRulesData`
        """
        model = RouteFilterRulesData()
        if include_optional:
            return RouteFilterRulesData(
                href = 'https://api.equinix.com/fabric/v4/routeFilters/695a8471-6595-4ac6-a2f4-b3d96ed3a59d/routeFilterRules/65b025ef-022b-4180-85cf-82cfc1ab655b',
                type = 'BGP_IPv4_PREFIX_FILTER_RULE',
                uuid = '65b025ef-022b-4180-85cf-82cfc1ab655b',
                name = 'Private-subnet-filter-2',
                description = '',
                state = 'PROVISIONING',
                prefix_match = 'orlonger',
                change = equinix.services.fabricv4.models.route_filter_rules_change.RouteFilterRulesChange(
                    uuid = '', 
                    type = 'BGP_IPv4_PREFIX_FILTER_RULE_UPDATE', 
                    href = '', ),
                action = 'PERMIT',
                prefix = '192.168.0.0/24',
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
                    deleted_date_time = '2020-11-06T07:00Z', )
            )
        else:
            return RouteFilterRulesData(
        )
        """

    def testRouteFilterRulesData(self):
        """Test RouteFilterRulesData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
