# coding: utf-8

"""
    Metal API

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.metalv1.models.invitation1 import Invitation1

class TestInvitation1(unittest.TestCase):
    """Invitation1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Invitation1:
        """Test Invitation1
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Invitation1`
        """
        model = Invitation1()
        if include_optional:
            return Invitation1(
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                href = '',
                id = '',
                invitation = equinix.services.metalv1.models.href.Href(
                    href = '', ),
                invited_by = equinix.services.metalv1.models.href.Href(
                    href = '', ),
                invitee = '',
                nonce = '',
                organization = equinix.services.metalv1.models.href.Href(
                    href = '', ),
                projects = [
                    equinix.services.metalv1.models.href.Href(
                        href = '', )
                    ],
                roles = [
                    'admin'
                    ],
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return Invitation1(
        )
        """

    def testInvitation1(self):
        """Test Invitation1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()