# coding: utf-8

"""
    Metal API

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.metalv1.models.metadata_network_network import MetadataNetworkNetwork

class TestMetadataNetworkNetwork(unittest.TestCase):
    """MetadataNetworkNetwork unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MetadataNetworkNetwork:
        """Test MetadataNetworkNetwork
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MetadataNetworkNetwork`
        """
        model = MetadataNetworkNetwork()
        if include_optional:
            return MetadataNetworkNetwork(
                bonding = equinix.services.metalv1.models.metadata_network_network_bonding.Metadata_network_network_bonding(
                    href = '', 
                    link_aggregation = '', 
                    mac = '', 
                    mode = 56, ),
                href = ''
            )
        else:
            return MetadataNetworkNetwork(
        )
        """

    def testMetadataNetworkNetwork(self):
        """Test MetadataNetworkNetwork"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
