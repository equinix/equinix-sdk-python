# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)
"""

import unittest

from equinix.services.fabricv4.models.subscription_asset import SubscriptionAsset

class TestSubscriptionAsset(unittest.TestCase):
    """SubscriptionAsset unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SubscriptionAsset:
        """Test SubscriptionAsset
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SubscriptionAsset`
        """
        model = SubscriptionAsset()
        if include_optional:
            return SubscriptionAsset(
                type = '',
                package = equinix.services.fabricv4.models.subscription_router_package_type.SubscriptionRouterPackageType(
                    code = 'ADVANCED', ),
                bandwidth = 56
            )
        else:
            return SubscriptionAsset(
        )
        """

    def testSubscriptionAsset(self):
        """Test SubscriptionAsset"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
