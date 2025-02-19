# coding: utf-8

"""
    Metal API

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.metalv1.models.batch import Batch

class TestBatch(unittest.TestCase):
    """Batch unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Batch:
        """Test Batch
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Batch`
        """
        model = Batch()
        if include_optional:
            return Batch(
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                devices = [
                    equinix.services.metalv1.models.href.Href(
                        href = '', )
                    ],
                error_messages = [
                    ''
                    ],
                href = '',
                id = '',
                project = equinix.services.metalv1.models.href.Href(
                    href = '', ),
                quantity = 56,
                state = '',
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return Batch(
        )
        """

    def testBatch(self):
        """Test Batch"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
