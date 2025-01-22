# coding: utf-8

"""
    Equinix Fabric API v4

    Equinix Fabric is an advanced software-defined interconnection solution that enables you to directly, securely and dynamically connect to distributed infrastructure and digital ecosystems on platform Equinix via a single port, Customers can use Fabric to connect to: </br> 1. Cloud Service Providers - Clouds, network and other service providers.  </br> 2. Enterprises - Other Equinix customers, vendors and partners.  </br> 3. Myself - Another customer instance deployed at Equinix. </br> </br> <b>Integrations (SDKs, Tools) links:</b> </br> <a href=\"https://deploy.equinix.com/labs/fabric-java\\\">Fabric Java SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-go\\\">Fabric Go SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-python\\\">Fabric Python SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-provider-equinix\\\">Equinix Terraform Provider</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-equinix-fabric\\\">Fabric Terraform Modules</a> </br> <a href=\"https://deploy.equinix.com/labs/pulumi-provider-equinix/\">Equinix Pulumi Provider</a> </br>

    The version of the OpenAPI document: 4.18
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.fabricv4.models.access_point_selector import AccessPointSelector

class TestAccessPointSelector(unittest.TestCase):
    """AccessPointSelector unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AccessPointSelector:
        """Test AccessPointSelector
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AccessPointSelector`
        """
        model = AccessPointSelector()
        if include_optional:
            return AccessPointSelector(
                type = 'COLO',
                hide_asset_info = True,
                port = equinix.services.fabricv4.models.simplified_metadata_entity.SimplifiedMetadataEntity(
                    href = '', 
                    uuid = '', 
                    type = '', 
                    cvp_id = 56, 
                    bandwidth = 1.337, 
                    port_name = '', 
                    encapsulation_protocol_type = '', 
                    account_name = '', 
                    priority = '', 
                    location = equinix.services.fabricv4.models.simplified_location.SimplifiedLocation(
                        metro_href = 'https://api.equinix.com/fabric/v4/metros/AM', 
                        region = 'AMER, APAC, EMEA', 
                        metro_name = 'Amsterdam', 
                        metro_code = 'AM', 
                        ibx = 'AM1', ), ),
                link_protocol = equinix.services.fabricv4.models.simplified_link_protocol.SimplifiedLinkProtocol(
                    type = 'UNTAGGED', 
                    vlan_tag = 2, 
                    vlan_s_tag = 2, 
                    vlan_c_tag = 2, ),
                virtual_device = equinix.services.fabricv4.models.simplified_virtual_device.SimplifiedVirtualDevice(
                    href = '', 
                    uuid = '', 
                    type = 'EDGE', 
                    name = '', 
                    cluster = '', ),
                interface = equinix.services.fabricv4.models.virtual_device_interface.VirtualDeviceInterface(
                    type = 'NETWORK', 
                    id = 56, 
                    uuid = '', ),
                network = equinix.services.fabricv4.models.simplified_token_network.SimplifiedTokenNetwork(
                    href = '', 
                    uuid = '', 
                    type = 'EVPLAN', 
                    name = '', 
                    scope = 'LOCAL', 
                    location = equinix.services.fabricv4.models.simplified_location.SimplifiedLocation(
                        metro_href = 'https://api.equinix.com/fabric/v4/metros/AM', 
                        region = 'AMER, APAC, EMEA', 
                        metro_name = 'Amsterdam', 
                        metro_code = 'AM', 
                        ibx = 'AM1', ), )
            )
        else:
            return AccessPointSelector(
        )
        """

    def testAccessPointSelector(self):
        """Test AccessPointSelector"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
