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

from equinix.services.fabricv4.models.route_filter_rules_change_data import RouteFilterRulesChangeData

class TestRouteFilterRulesChangeData(unittest.TestCase):
    """RouteFilterRulesChangeData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RouteFilterRulesChangeData:
        """Test RouteFilterRulesChangeData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RouteFilterRulesChangeData`
        """
        model = RouteFilterRulesChangeData()
        if include_optional:
            return RouteFilterRulesChangeData(
                status = 'COMPLETED',
                created_by = '',
                created_date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_by = '',
                updated_date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                data = equinix.services.fabricv4.models.route_filter_rules_change_operation.RouteFilterRulesChangeOperation(
                    op = 'add', 
                    path = '/', 
                    value = equinix.services.fabricv4.models.route_filter_rules_base.RouteFilterRulesBase(
                        name = 'Private-subnet-filter', 
                        description = '', 
                        prefix = '192.168.0.0/24', 
                        prefix_match = 'orlonger', ), ),
                uuid = '',
                type = 'BGP_IPv4_PREFIX_FILTER_RULE_UPDATE',
                href = ''
            )
        else:
            return RouteFilterRulesChangeData(
                uuid = '',
                type = 'BGP_IPv4_PREFIX_FILTER_RULE_UPDATE',
        )
        """

    def testRouteFilterRulesChangeData(self):
        """Test RouteFilterRulesChangeData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
