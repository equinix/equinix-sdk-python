# coding: utf-8

"""
    Equinix Fabric API v4

    Equinix Fabric is an advanced software-defined interconnection solution that enables you to directly, securely and dynamically connect to distributed infrastructure and digital ecosystems on platform Equinix via a single port, Customers can use Fabric to connect to: </br> 1. Cloud Service Providers - Clouds, network and other service providers.  </br> 2. Enterprises - Other Equinix customers, vendors and partners.  </br> 3. Myself - Another customer instance deployed at Equinix. </br> </br> <b>Integrations (SDKs, Tools) links:</b> </br> <a href=\"https://deploy.equinix.com/labs/fabric-java\\\">Fabric Java SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-go\\\">Fabric Go SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-python\\\">Fabric Python SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-provider-equinix\\\">Equinix Terraform Provider</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-equinix-fabric\\\">Fabric Terraform Modules</a> </br> <a href=\"https://deploy.equinix.com/labs/pulumi-provider-equinix/\">Equinix Pulumi Provider</a> </br>

    The version of the OpenAPI document: 4.18
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.fabricv4.models.route_filters_change_operation import RouteFiltersChangeOperation

class TestRouteFiltersChangeOperation(unittest.TestCase):
    """RouteFiltersChangeOperation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RouteFiltersChangeOperation:
        """Test RouteFiltersChangeOperation
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RouteFiltersChangeOperation`
        """
        model = RouteFiltersChangeOperation()
        if include_optional:
            return RouteFiltersChangeOperation(
                op = 'add',
                path = '/',
                value = equinix.services.fabricv4.models.route_filters_base.RouteFiltersBase(
                    type = 'BGP_IPv4_PREFIX_FILTER', 
                    name = 'My-direct-route-1', 
                    description = '', 
                    project = equinix.services.fabricv4.models.project.Project(
                        project_id = '44f4c4f8-2f39-494e-838c-d8e640591be5', ), )
            )
        else:
            return RouteFiltersChangeOperation(
                op = 'add',
                path = '/',
                value = equinix.services.fabricv4.models.route_filters_base.RouteFiltersBase(
                    type = 'BGP_IPv4_PREFIX_FILTER', 
                    name = 'My-direct-route-1', 
                    description = '', 
                    project = equinix.services.fabricv4.models.project.Project(
                        project_id = '44f4c4f8-2f39-494e-838c-d8e640591be5', ), ),
        )
        """

    def testRouteFiltersChangeOperation(self):
        """Test RouteFiltersChangeOperation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
