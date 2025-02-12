# coding: utf-8

"""
    Equinix Fabric API v4

    Equinix Fabric is an advanced software-defined interconnection solution that enables you to directly, securely and dynamically connect to distributed infrastructure and digital ecosystems on platform Equinix via a single port, Customers can use Fabric to connect to: </br> 1. Cloud Service Providers - Clouds, network and other service providers.  </br> 2. Enterprises - Other Equinix customers, vendors and partners.  </br> 3. Myself - Another customer instance deployed at Equinix. </br> </br> <b>Integrations (SDKs, Tools) links:</b> </br> <a href=\"https://deploy.equinix.com/labs/fabric-java\\\">Fabric Java SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-go\\\">Fabric Go SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-python\\\">Fabric Python SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-provider-equinix\\\">Equinix Terraform Provider</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-equinix-fabric\\\">Fabric Terraform Modules</a> </br> <a href=\"https://deploy.equinix.com/labs/pulumi-provider-equinix/\">Equinix Pulumi Provider</a> </br>

    The version of the OpenAPI document: 4.20
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.fabricv4.models.route_aggregations_data import RouteAggregationsData

class TestRouteAggregationsData(unittest.TestCase):
    """RouteAggregationsData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RouteAggregationsData:
        """Test RouteAggregationsData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RouteAggregationsData`
        """
        model = RouteAggregationsData()
        if include_optional:
            return RouteAggregationsData(
                href = 'https://api.equinix.com/fabric/v4/routeAggregations/695a8471-6595-4ac6-a2f4-b3d96ed3a59d',
                type = 'BGP_IPv4_PREFIX_AGGREGATION',
                uuid = '695a8471-6595-4ac6-a2f4-b3d96ed3a59d',
                name = 'My-direct-route-1',
                description = '',
                state = 'PROVISIONING',
                change = equinix.services.fabricv4.models.route_aggregations_change.RouteAggregationsChange(
                    uuid = '', 
                    type = 'BGP_IPv4_PREFIX_AGGREGATION_UPDATE', 
                    href = '', ),
                connections_count = 0,
                rules_count = 0,
                project = equinix.services.fabricv4.models.route_aggregations_data_project.RouteAggregationsData_project(
                    project_id = '44f4c4f8-2f39-494e-838c-d8e640591be5', 
                    href = '', ),
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
                    deleted_date_time = '2020-11-06T07:00Z', )
            )
        else:
            return RouteAggregationsData(
        )
        """

    def testRouteAggregationsData(self):
        """Test RouteAggregationsData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
