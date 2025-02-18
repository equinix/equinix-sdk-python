# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)
"""

import unittest

from equinix.services.fabricv4.models.metrics import Metrics

class TestMetrics(unittest.TestCase):
    """Metrics unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Metrics:
        """Test Metrics
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Metrics`
        """
        model = Metrics()
        if include_optional:
            return Metrics(
                interval_end_timestamp = '2020-11-06T07:00Z',
                max = 1.337,
                mean = 1.337
            )
        else:
            return Metrics(
        )
        """

    def testMetrics(self):
        """Test Metrics"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
