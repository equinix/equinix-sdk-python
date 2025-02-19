# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.fabricv4.models.bgp_actions_bulk_data import BGPActionsBulkData

class TestBGPActionsBulkData(unittest.TestCase):
    """BGPActionsBulkData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BGPActionsBulkData:
        """Test BGPActionsBulkData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BGPActionsBulkData`
        """
        model = BGPActionsBulkData()
        if include_optional:
            return BGPActionsBulkData(
                pagination = equinix.services.fabricv4.models.pagination.Pagination(
                    offset = 0, 
                    limit = 0, 
                    total = 0, 
                    next = '', 
                    previous = '', ),
                data = [
                    equinix.services.fabricv4.models.bgp_action_data.BGPActionData(
                        href = 'https://api.equinix.com/fabric/v4/connections/81331c52-04c0-4656-a4a7-18c52669348f/routingProtocols/69762051-85ed-4d13-b6b4-e32e93c672b5/actions', 
                        uuid = 'c9b8e7a2-f3b1-4576-a4a9-1366a63df170', 
                        type = 'CLEAR_BGPIPV4', 
                        description = '', 
                        state = 'PENDING', 
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
                            deleted_date_time = '2020-11-06T07:00Z', ), )
                    ]
            )
        else:
            return BGPActionsBulkData(
        )
        """

    def testBGPActionsBulkData(self):
        """Test BGPActionsBulkData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
