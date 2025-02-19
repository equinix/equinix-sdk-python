# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.fabricv4.models.stream_subscription import StreamSubscription

class TestStreamSubscription(unittest.TestCase):
    """StreamSubscription unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StreamSubscription:
        """Test StreamSubscription
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StreamSubscription`
        """
        model = StreamSubscription()
        if include_optional:
            return StreamSubscription(
                href = 'https://api.equinix.com/fabric/v4/streams/d684aa26-8276-48b7-bb42-a6d9def0a418/subscriptions/3c9b8e7a2-f3b1-4576-a4a9-1366a63df170',
                uuid = 'c9b8e7a2-f3b1-4576-a4a9-1366a63df170',
                type = 'STREAM_SUBSCRIPTION',
                name = '',
                description = '',
                state = 'PROVISIONING',
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
                    host = '', ),
                change_log = equinix.services.fabricv4.models.changelog.Changelog(
                    created_by = 'johnsmith', 
                    created_by_full_name = 'John Smith', 
                    created_by_email = 'john.smith@example.com', 
                    created_date_time = '2020-11-06T07:00Z', 
                    updated_by = 'johnsmith', 
                    updated_by_full_name = 'John Smith', 
                    updated_by_email = 'john.smith@example.com', 
                    updated_date_time = '2020-11-06T07:00Z', 
                    deleted_by = 'johnsmith', 
                    deleted_by_full_name = 'John Smith', 
                    deleted_by_email = 'john.smith@example.com', 
                    deleted_date_time = '2020-11-06T07:00Z', )
            )
        else:
            return StreamSubscription(
        )
        """

    def testStreamSubscription(self):
        """Test StreamSubscription"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
