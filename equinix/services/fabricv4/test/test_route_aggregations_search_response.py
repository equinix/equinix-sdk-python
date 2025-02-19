# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.fabricv4.models.route_aggregations_search_response import RouteAggregationsSearchResponse

class TestRouteAggregationsSearchResponse(unittest.TestCase):
    """RouteAggregationsSearchResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RouteAggregationsSearchResponse:
        """Test RouteAggregationsSearchResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RouteAggregationsSearchResponse`
        """
        model = RouteAggregationsSearchResponse()
        if include_optional:
            return RouteAggregationsSearchResponse(
                pagination = equinix.services.fabricv4.models.pagination.Pagination(
                    offset = 0, 
                    limit = 0, 
                    total = 0, 
                    next = '', 
                    previous = '', ),
                data = [
                    equinix.services.fabricv4.models.route_aggregations_data.RouteAggregationsData(
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
                            deleted_date_time = '2020-11-06T07:00Z', ), )
                    ]
            )
        else:
            return RouteAggregationsSearchResponse(
        )
        """

    def testRouteAggregationsSearchResponse(self):
        """Test RouteAggregationsSearchResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
