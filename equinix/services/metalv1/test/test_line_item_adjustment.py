# coding: utf-8

"""
    Metal API

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.metalv1.models.line_item_adjustment import LineItemAdjustment

class TestLineItemAdjustment(unittest.TestCase):
    """LineItemAdjustment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LineItemAdjustment:
        """Test LineItemAdjustment
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LineItemAdjustment`
        """
        model = LineItemAdjustment()
        if include_optional:
            return LineItemAdjustment(
                amount = 1.337,
                description = '',
                href = ''
            )
        else:
            return LineItemAdjustment(
        )
        """

    def testLineItemAdjustment(self):
        """Test LineItemAdjustment"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
