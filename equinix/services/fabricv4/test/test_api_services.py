# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.fabricv4.models.api_services import ApiServices

class TestApiServices(unittest.TestCase):
    """ApiServices unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiServices:
        """Test ApiServices
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiServices`
        """
        model = ApiServices()
        if include_optional:
            return ApiServices(
                route = '',
                status = '',
                changed_date_time = ''
            )
        else:
            return ApiServices(
        )
        """

    def testApiServices(self):
        """Test ApiServices"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
