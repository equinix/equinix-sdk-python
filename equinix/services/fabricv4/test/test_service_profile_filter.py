# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)
"""

import unittest

from equinix.services.fabricv4.models.service_profile_filter import ServiceProfileFilter

class TestServiceProfileFilter(unittest.TestCase):
    """ServiceProfileFilter unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServiceProfileFilter:
        """Test ServiceProfileFilter
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServiceProfileFilter`
        """
        model = ServiceProfileFilter()
        if include_optional:
            return ServiceProfileFilter(
                var_property = '/name',
                operator = '=',
                values = [
                    'ServiceProfile-1'
                    ],
                var_and = [
                    equinix.services.fabricv4.models.service_profile_simple_expression.ServiceProfileSimpleExpression(
                        property = '/name', 
                        operator = '=', 
                        values = [
                            'ServiceProfile-1'
                            ], )
                    ]
            )
        else:
            return ServiceProfileFilter(
        )
        """

    def testServiceProfileFilter(self):
        """Test ServiceProfileFilter"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
