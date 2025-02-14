# coding: utf-8

"""
    Equinix Fabric API v4

    Equinix Fabric is an advanced software-defined interconnection solution that enables you to directly, securely and dynamically connect to distributed infrastructure and digital ecosystems on platform Equinix via a single port, Customers can use Fabric to connect to: </br> 1. Cloud Service Providers - Clouds, network and other service providers.  </br> 2. Enterprises - Other Equinix customers, vendors and partners.  </br> 3. Myself - Another customer instance deployed at Equinix. </br> </br> <b>Integrations (SDKs, Tools) links:</b> </br> <a href=\"https://deploy.equinix.com/labs/fabric-java\\\">Fabric Java SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-go\\\">Fabric Go SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-python\\\">Fabric Python SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-provider-equinix\\\">Equinix Terraform Provider</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-equinix-fabric\\\">Fabric Terraform Modules</a> </br> <a href=\"https://deploy.equinix.com/labs/pulumi-provider-equinix/\">Equinix Pulumi Provider</a> </br>

    Generated by OpenAPI Generator (https://openapi-generator.tech)
"""


import unittest

from equinix.services.fabricv4.api.route_aggregation_rules_api import RouteAggregationRulesApi


class TestRouteAggregationRulesApi(unittest.TestCase):
    """RouteAggregationRulesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = RouteAggregationRulesApi()

    def tearDown(self) -> None:
        pass

    def test_create_route_aggregation_rule(self) -> None:
        """Test case for create_route_aggregation_rule

        Create RARule
        """
        pass

    def test_create_route_aggregation_rules_in_bulk(self) -> None:
        """Test case for create_route_aggregation_rules_in_bulk

        Bulk RARules
        """
        pass

    def test_delete_route_aggregation_rule_by_uuid(self) -> None:
        """Test case for delete_route_aggregation_rule_by_uuid

        DeleteRARule
        """
        pass

    def test_get_route_aggregation_rule_by_uuid(self) -> None:
        """Test case for get_route_aggregation_rule_by_uuid

        GetRARule By UUID
        """
        pass

    def test_get_route_aggregation_rule_change_by_uuid(self) -> None:
        """Test case for get_route_aggregation_rule_change_by_uuid

        Get Change By ID
        """
        pass

    def test_get_route_aggregation_rule_changes(self) -> None:
        """Test case for get_route_aggregation_rule_changes

        Get All Changes
        """
        pass

    def test_get_route_aggregation_rules(self) -> None:
        """Test case for get_route_aggregation_rules

        GetRARules
        """
        pass

    def test_patch_route_aggregation_rule_by_uuid(self) -> None:
        """Test case for patch_route_aggregation_rule_by_uuid

        PatchRARule
        """
        pass

    def test_replace_route_aggregation_rule_by_uuid(self) -> None:
        """Test case for replace_route_aggregation_rule_by_uuid

        ReplaceRARule
        """
        pass


if __name__ == '__main__':
    unittest.main()
