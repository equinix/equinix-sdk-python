# coding: utf-8

"""
    Metal API

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.metalv1.models.component import Component

class TestComponent(unittest.TestCase):
    """Component unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Component:
        """Test Component
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Component`
        """
        model = Component()
        if include_optional:
            return Component(
                checksum = '',
                component = 'bmc',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                filename = '',
                href = '',
                model = [
                    'romed8hm3'
                    ],
                repository_url = '',
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                upstream_url = '',
                uuid = '0516463a-47ee-4809-9a66-ece8c740eed9',
                vendor = 'equinix',
                version = '1.5.0'
            )
        else:
            return Component(
        )
        """

    def testComponent(self):
        """Test Component"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
