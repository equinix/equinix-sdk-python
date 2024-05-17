# coding: utf-8

"""
    Metal API

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.metalv1.models.attribute_data import AttributeData

class TestAttributeData(unittest.TestCase):
    """AttributeData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AttributeData:
        """Test AttributeData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AttributeData`
        """
        model = AttributeData()
        if include_optional:
            return AttributeData(
                href = '',
                latest = True,
                model = '',
                plan = '',
                vendor = ''
            )
        else:
            return AttributeData(
        )
        """

    def testAttributeData(self):
        """Test AttributeData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
