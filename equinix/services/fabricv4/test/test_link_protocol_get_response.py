# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.fabricv4.models.link_protocol_get_response import LinkProtocolGetResponse

class TestLinkProtocolGetResponse(unittest.TestCase):
    """LinkProtocolGetResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LinkProtocolGetResponse:
        """Test LinkProtocolGetResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LinkProtocolGetResponse`
        """
        model = LinkProtocolGetResponse()
        if include_optional:
            return LinkProtocolGetResponse(
                pagination = equinix.services.fabricv4.models.pagination.Pagination(
                    offset = 0, 
                    limit = 0, 
                    total = 0, 
                    next = '', 
                    previous = '', ),
                data = [
                    equinix.services.fabricv4.models.link_protocol_response.LinkProtocolResponse(
                        href = '', 
                        uuid = '92dc376a-a932-43aa-a6a2-c806dedbd784', 
                        state = 'RESERVED', 
                        type = 'UNTAGGED', 
                        vlan_tag = 20, 
                        vni = 20, 
                        vlan_tag_min = 20, 
                        vlan_tag_max = 200, 
                        vlan_s_tag = 20, 
                        vlan_c_tag = 20, 
                        vlan_c_tag_min = 20, 
                        vlan_c_tag_max = 200, 
                        sub_interface = equinix.services.fabricv4.models.sub_interface.SubInterface(
                            name = '', 
                            unit = 200, ), 
                        asset = equinix.services.fabricv4.models.link_protocol_connection.LinkProtocolConnection(
                            href = '', 
                            uuid = 'cd67f685-41b0-1b07-6de0-320a5c00abe', 
                            bandwidth = 100, ), 
                        service_token = equinix.services.fabricv4.models.link_protocol_service_token.LinkProtocolServiceToken(
                            href = '', 
                            uuid = 'cd67f685-41b0-1b07-6de0-0320a5c00abe', 
                            bandwidth = 1000, ), 
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
            return LinkProtocolGetResponse(
        )
        """

    def testLinkProtocolGetResponse(self):
        """Test LinkProtocolGetResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
