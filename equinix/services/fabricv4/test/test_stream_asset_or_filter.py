# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.fabricv4.models.stream_asset_or_filter import StreamAssetOrFilter

class TestStreamAssetOrFilter(unittest.TestCase):
    """StreamAssetOrFilter unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StreamAssetOrFilter:
        """Test StreamAssetOrFilter
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StreamAssetOrFilter`
        """
        model = StreamAssetOrFilter()
        if include_optional:
            return StreamAssetOrFilter(
                var_or = [
                    equinix.services.fabricv4.models.stream_asset_simple_expression.StreamAssetSimpleExpression(
                        property = '/name', 
                        operator = '=', 
                        values = [
                            'FabricStreamAsset-1'
                            ], )
                    ]
            )
        else:
            return StreamAssetOrFilter(
        )
        """

    def testStreamAssetOrFilter(self):
        """Test StreamAssetOrFilter"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
