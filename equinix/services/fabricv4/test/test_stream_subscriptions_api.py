# coding: utf-8

"""
    Equinix Fabric API v4

    Equinix Fabric is an advanced software-defined interconnection solution that enables you to directly, securely and dynamically connect to distributed infrastructure and digital ecosystems on platform Equinix via a single port, Customers can use Fabric to connect to: </br> 1. Cloud Service Providers - Clouds, network and other service providers.  </br> 2. Enterprises - Other Equinix customers, vendors and partners.  </br> 3. Myself - Another customer instance deployed at Equinix. </br> </br> <b>Integrations (SDKs, Tools) links:</b> </br> <a href=\"https://deploy.equinix.com/labs/fabric-java\\\">Fabric Java SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-go\\\">Fabric Go SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-python\\\">Fabric Python SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-provider-equinix\\\">Equinix Terraform Provider</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-equinix-fabric\\\">Fabric Terraform Modules</a> </br> <a href=\"https://deploy.equinix.com/labs/pulumi-provider-equinix/\">Equinix Pulumi Provider</a> </br>

    The version of the OpenAPI document: 4.20
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.fabricv4.api.stream_subscriptions_api import StreamSubscriptionsApi


class TestStreamSubscriptionsApi(unittest.TestCase):
    """StreamSubscriptionsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = StreamSubscriptionsApi()

    def tearDown(self) -> None:
        pass

    def test_create_stream_subscriptions(self) -> None:
        """Test case for create_stream_subscriptions

        Create Subscription
        """
        pass

    def test_delete_stream_subscription_by_uuid(self) -> None:
        """Test case for delete_stream_subscription_by_uuid

        Delete Subscription
        """
        pass

    def test_get_stream_subscription_by_uuid(self) -> None:
        """Test case for get_stream_subscription_by_uuid

        Get Subscription
        """
        pass

    def test_get_stream_subscriptions(self) -> None:
        """Test case for get_stream_subscriptions

        Get Subscriptions
        """
        pass

    def test_update_stream_subscription_by_uuid(self) -> None:
        """Test case for update_stream_subscription_by_uuid

        Update Subscription
        """
        pass


if __name__ == '__main__':
    unittest.main()
