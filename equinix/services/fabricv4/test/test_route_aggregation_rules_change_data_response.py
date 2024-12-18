# coding: utf-8

"""
    Equinix Fabric API v4

    Equinix Fabric is an advanced software-defined interconnection solution that enables you to directly, securely and dynamically connect to distributed infrastructure and digital ecosystems on platform Equinix via a single port, Customers can use Fabric to connect to: </br> 1. Cloud Service Providers - Clouds, network and other service providers.  </br> 2. Enterprises - Other Equinix customers, vendors and partners.  </br> 3. Myself - Another customer instance deployed at Equinix. </br> </br> <b>Integrations (SDKs, Tools) links:</b> </br> <a href=\"https://deploy.equinix.com/labs/fabric-java\\\">Fabric Java SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-go\\\">Fabric Go SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-python\\\">Fabric Python SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-provider-equinix\\\">Equinix Terraform Provider</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-equinix-fabric\\\">Fabric Terraform Modules</a> </br> <a href=\"https://deploy.equinix.com/labs/pulumi-provider-equinix/\">Equinix Pulumi Provider</a> </br>

    The version of the OpenAPI document: 4.18
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.fabricv4.models.route_aggregation_rules_change_data_response import RouteAggregationRulesChangeDataResponse

class TestRouteAggregationRulesChangeDataResponse(unittest.TestCase):
    """RouteAggregationRulesChangeDataResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RouteAggregationRulesChangeDataResponse:
        """Test RouteAggregationRulesChangeDataResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RouteAggregationRulesChangeDataResponse`
        """
        model = RouteAggregationRulesChangeDataResponse()
        if include_optional:
            return RouteAggregationRulesChangeDataResponse(
                pagination = equinix.services.fabricv4.models.pagination.Pagination(
                    offset = 0, 
                    limit = 0, 
                    total = 0, 
                    next = '', 
                    previous = '', ),
                data = [
                    equinix.services.fabricv4.models.route_aggregation_rules_change_data.RouteAggregationRulesChangeData(
                        status = 'COMPLETED', 
                        created_by = '', 
                        created_date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_by = '', 
                        updated_date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        data = equinix.services.fabricv4.models.route_aggregation_rules_change_operation.RouteAggregationRulesChangeOperation(
                            op = 'add', 
                            path = '/', 
                            value = equinix.services.fabricv4.models.route_aggregation_rules_base.RouteAggregationRulesBase(
                                name = 'Private-subnet-Aggregation', 
                                description = '', 
                                prefix = '192.168.0.0/24', ), ), )
                    ]
            )
        else:
            return RouteAggregationRulesChangeDataResponse(
        )
        """

    def testRouteAggregationRulesChangeDataResponse(self):
        """Test RouteAggregationRulesChangeDataResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
