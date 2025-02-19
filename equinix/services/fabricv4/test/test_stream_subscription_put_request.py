# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.fabricv4.models.stream_subscription_put_request import StreamSubscriptionPutRequest

class TestStreamSubscriptionPutRequest(unittest.TestCase):
    """StreamSubscriptionPutRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StreamSubscriptionPutRequest:
        """Test StreamSubscriptionPutRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StreamSubscriptionPutRequest`
        """
        model = StreamSubscriptionPutRequest()
        if include_optional:
            return StreamSubscriptionPutRequest(
                name = '',
                description = '',
                enabled = True,
                filters = equinix.services.fabricv4.models.stream_subscription_filter.StreamSubscriptionFilter(
                    and = [
                        equinix.services.fabricv4.models.stream_filter.StreamFilter()
                        ], ),
                metric_selector = equinix.services.fabricv4.models.stream_subscription_selector.StreamSubscriptionSelector(
                    include = [
                        'equinix.fabric.connection.*'
                        ], 
                    except = [
                        'equinix.fabric.connection.*'
                        ], ),
                event_selector = equinix.services.fabricv4.models.stream_subscription_selector.StreamSubscriptionSelector(
                    include = [
                        'equinix.fabric.connection.*'
                        ], 
                    except = [
                        'equinix.fabric.connection.*'
                        ], ),
                sink = equinix.services.fabricv4.models.stream_subscription_sink.StreamSubscriptionSink(
                    uri = '', 
                    type = 'DATADOG', 
                    batch_enabled = False, 
                    batch_size_max = 56, 
                    batch_wait_time_max = 56, 
                    credential = equinix.services.fabricv4.models.stream_subscription_sink_credential.StreamSubscriptionSinkCredential(
                        access_token = '', 
                        integration_key = '', 
                        api_key = '', 
                        username = '', 
                        password = '', ), 
                    settings = equinix.services.fabricv4.models.stream_subscription_sink_setting.StreamSubscriptionSinkSetting(
                        event_index = '', 
                        metric_index = '', 
                        source = '', 
                        application_key = '', 
                        event_uri = '', 
                        metric_uri = '', 
                        transform_alerts = True, ), 
                    host = '', )
            )
        else:
            return StreamSubscriptionPutRequest(
        )
        """

    def testStreamSubscriptionPutRequest(self):
        """Test StreamSubscriptionPutRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
