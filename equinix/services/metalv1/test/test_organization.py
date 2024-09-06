# coding: utf-8

"""
    Metal API

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.metalv1.models.organization import Organization

class TestOrganization(unittest.TestCase):
    """Organization unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Organization:
        """Test Organization
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Organization`
        """
        model = Organization()
        if include_optional:
            return Organization(
                address = equinix.services.metalv1.models.address.Address(
                    address2 = '', 
                    city = '', 
                    coordinates = equinix.services.metalv1.models.coordinates.Coordinates(
                        href = '', 
                        latitude = '', 
                        longitude = '', ), 
                    country = '', 
                    href = '', 
                    state = '', 
                    zip_code = '', ),
                billing_address = equinix.services.metalv1.models.address.Address(
                    address = '', 
                    address2 = '', 
                    city = '', 
                    coordinates = equinix.services.metalv1.models.coordinates.Coordinates(
                        href = '', 
                        latitude = '', 
                        longitude = '', ), 
                    country = '', 
                    href = '', 
                    state = '', 
                    zip_code = '', ),
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                credit_amount = 1.337,
                customdata = equinix.services.metalv1.models.customdata.customdata(),
                description = '',
                enforce_2fa_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                href = '',
                id = '',
                logo = '',
                members = [
                    equinix.services.metalv1.models.href.Href(
                        href = '', )
                    ],
                memberships = [
                    equinix.services.metalv1.models.href.Href(
                        href = '', )
                    ],
                name = '',
                projects = [
                    equinix.services.metalv1.models.href.Href(
                        href = '', )
                    ],
                terms = 56,
                twitter = '',
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                website = ''
            )
        else:
            return Organization(
        )
        """

    def testOrganization(self):
        """Test Organization"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
