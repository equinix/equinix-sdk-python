# coding: utf-8

"""
    Equinix Fabric API v4

    Equinix Fabric is an advanced software-defined interconnection solution that enables you to directly, securely and dynamically connect to distributed infrastructure and digital ecosystems on platform Equinix via a single port, Customers can use Fabric to connect to: </br> 1. Cloud Service Providers - Clouds, network and other service providers.  </br> 2. Enterprises - Other Equinix customers, vendors and partners.  </br> 3. Myself - Another customer instance deployed at Equinix. </br> </br> <b>Integrations (SDKs, Tools) links:</b> </br> <a href=\"https://deploy.equinix.com/labs/fabric-java\\\">Fabric Java SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-go\\\">Fabric Go SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-python\\\">Fabric Python SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-provider-equinix\\\">Equinix Terraform Provider</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-equinix-fabric\\\">Fabric Terraform Modules</a> </br> <a href=\"https://deploy.equinix.com/labs/pulumi-provider-equinix/\">Equinix Pulumi Provider</a> </br>

    The version of the OpenAPI document: 4.17
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
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StreamSubscription`
        """
        model = StreamSubscription()
        if include_optional:
            return StreamSubscription(
                href = 'https://api.equinix.com/fabric/v4/streamSubscription/3c9b8e7a2-f3b1-4576-a4a9-1366a63df170',
                uuid = 'c9b8e7a2-f3b1-4576-a4a9-1366a63df170',
                type = 'STREAM_SUBSCRIPTION',
                name = '',
                description = '',
                project = equinix.services.fabricv4.models.project.Project(
                    project_id = '44f4c4f8-2f39-494e-838c-d8e640591be5', ),
                state = 'PROVISIONING',
                enabled = True,
                stream = equinix.services.fabricv4.models.stream_target.StreamTarget(
                    uuid = '657400f8-d360-11e9-bb65-2a2ae2dbcce5', ),
                filters = equinix.services.fabricv4.models.stream_subscription_filter.StreamSubscriptionFilter(
                    and = [
                        equinix.services.fabricv4.models.stream_filter.StreamFilter()
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
                        api_key = '', ), 
                    settings = equinix.services.fabricv4.models.stream_subscription_sink_setting.StreamSubscriptionSinkSetting(
                        event_index = '', 
                        metric_index = '', 
                        source = '', 
                        application_key = '', ), ),
                changelog = equinix.services.fabricv4.models.changelog.Changelog(
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
