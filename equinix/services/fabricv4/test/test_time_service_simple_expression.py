# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)
"""

import unittest

from equinix.services.fabricv4.models.time_service_simple_expression import TimeServiceSimpleExpression

class TestTimeServiceSimpleExpression(unittest.TestCase):
    """TimeServiceSimpleExpression unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TimeServiceSimpleExpression:
        """Test TimeServiceSimpleExpression
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TimeServiceSimpleExpression`
        """
        model = TimeServiceSimpleExpression()
        if include_optional:
            return TimeServiceSimpleExpression(
                var_property = '/name',
                operator = '=',
                values = [
                    'FabricPrecisionTimeService-1'
                    ]
            )
        else:
            return TimeServiceSimpleExpression(
        )
        """

    def testTimeServiceSimpleExpression(self):
        """Test TimeServiceSimpleExpression"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
