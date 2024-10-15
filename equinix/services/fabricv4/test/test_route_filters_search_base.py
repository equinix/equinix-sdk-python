# coding: utf-8

"""
    Equinix Fabric API v4

    Equinix Fabric is an advanced software-defined interconnection solution that enables you to directly, securely and dynamically connect to distributed infrastructure and digital ecosystems on platform Equinix via a single port, Customers can use Fabric to connect to: </br> 1. Cloud Service Providers - Clouds, network and other service providers.  </br> 2. Enterprises - Other Equinix customers, vendors and partners.  </br> 3. Myself - Another customer instance deployed at Equinix. </br> </br> <b>Integrations (SDKs, Tools) links:</b> </br> <a href=\"https://deploy.equinix.com/labs/fabric-java\\\">Fabric Java SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-go\\\">Fabric Go SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-python\\\">Fabric Python SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-provider-equinix\\\">Equinix Terraform Provider</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-equinix-fabric\\\">Fabric Terraform Modules</a> </br> <a href=\"https://deploy.equinix.com/labs/pulumi-provider-equinix/\">Equinix Pulumi Provider</a> </br>

    The version of the OpenAPI document: 4.17
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.fabricv4.models.route_filters_search_base import RouteFiltersSearchBase

class TestRouteFiltersSearchBase(unittest.TestCase):
    """RouteFiltersSearchBase unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RouteFiltersSearchBase:
        """Test RouteFiltersSearchBase
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RouteFiltersSearchBase`
        """
        model = RouteFiltersSearchBase()
        if include_optional:
            return RouteFiltersSearchBase(
                filter = equinix.services.fabricv4.models.route_filters_search_base_filter.RouteFiltersSearchBase_filter(
                    and = [
                        equinix.services.fabricv4.models.route_filters_search_filter_item.RouteFiltersSearchFilterItem(
                            property = '/type', 
                            operator = '', 
                            values = [
                                ''
                                ], )
                        ], ),
                pagination = equinix.services.fabricv4.models.pagination.Pagination(
                    offset = 0, 
                    limit = 0, 
                    total = 0, 
                    next = '', 
                    previous = '', ),
                sort = [
                    equinix.services.fabricv4.models.sort_item.SortItem(
                        property = '/changeLog/updatedDateTime', 
                        direction = 'DESC', )
                    ]
            )
        else:
            return RouteFiltersSearchBase(
        )
        """

    def testRouteFiltersSearchBase(self):
        """Test RouteFiltersSearchBase"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
