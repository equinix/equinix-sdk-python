# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)
"""

import unittest

from equinix.services.fabricv4.models.stream_subscription_sink_setting import StreamSubscriptionSinkSetting

class TestStreamSubscriptionSinkSetting(unittest.TestCase):
    """StreamSubscriptionSinkSetting unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StreamSubscriptionSinkSetting:
        """Test StreamSubscriptionSinkSetting
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StreamSubscriptionSinkSetting`
        """
        model = StreamSubscriptionSinkSetting()
        if include_optional:
            return StreamSubscriptionSinkSetting(
                event_index = '',
                metric_index = '',
                source = '',
                application_key = '',
                event_uri = '',
                metric_uri = '',
                transform_alerts = True
            )
        else:
            return StreamSubscriptionSinkSetting(
        )
        """

    def testStreamSubscriptionSinkSetting(self):
        """Test StreamSubscriptionSinkSetting"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
