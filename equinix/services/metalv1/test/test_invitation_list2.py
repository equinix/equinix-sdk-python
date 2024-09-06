# coding: utf-8

"""
    Metal API

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.metalv1.models.invitation_list2 import InvitationList2

class TestInvitationList2(unittest.TestCase):
    """InvitationList2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InvitationList2:
        """Test InvitationList2
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InvitationList2`
        """
        model = InvitationList2()
        if include_optional:
            return InvitationList2(
                href = '',
                invitations = [
                    equinix.services.metalv1.models.membership.Membership(
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        href = '', 
                        id = '', 
                        project = equinix.services.metalv1.models.href.Href(
                            href = '', ), 
                        roles = [
                            ''
                            ], 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        user = equinix.services.metalv1.models.href.Href(
                            href = '', ), )
                    ]
            )
        else:
            return InvitationList2(
        )
        """

    def testInvitationList2(self):
        """Test InvitationList2"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
