# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.fabricv4.models.connection_invitation import ConnectionInvitation

class TestConnectionInvitation(unittest.TestCase):
    """ConnectionInvitation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConnectionInvitation:
        """Test ConnectionInvitation
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConnectionInvitation`
        """
        model = ConnectionInvitation()
        if include_optional:
            return ConnectionInvitation(
                email = 'test@equinix.com',
                message = 'Hello, Please accept my invitation',
                ctr_draft_order_id = ''
            )
        else:
            return ConnectionInvitation(
        )
        """

    def testConnectionInvitation(self):
        """Test ConnectionInvitation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
