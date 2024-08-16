# coding: utf-8

"""
    Equinix Fabric API v4

    Equinix Fabric is an advanced software-defined interconnection solution that enables you to directly, securely and dynamically connect to distributed infrastructure and digital ecosystems on platform Equinix via a single port, Customers can use Fabric to connect to: </br> 1. Cloud Service Providers - Clouds, network and other service providers.  </br> 2. Enterprises - Other Equinix customers, vendors and partners.  </br> 3. Myself - Another customer instance deployed at Equinix. </br> </br> <b>Integrations (SDKs, Tools) links:</b> </br> <a href=\"https://deploy.equinix.com/labs/fabric-java\\\">Fabric Java SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-go\\\">Fabric Go SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-provider-equinix\\\">Equinix Terraform Provider</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-equinix-fabric\\\">Fabric Terraform Modules</a> </br> <a href=\"https://deploy.equinix.com/labs/pulumi-provider-equinix/\">Equinix Pulumi Provider</a> </br>

    The version of the OpenAPI document: 4.15
    Contact: api-support@equinix.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.fabricv4.models.link_protocol_qinq import LinkProtocolQinq

class TestLinkProtocolQinq(unittest.TestCase):
    """LinkProtocolQinq unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LinkProtocolQinq:
        """Test LinkProtocolQinq
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LinkProtocolQinq`
        """
        model = LinkProtocolQinq()
        if include_optional:
            return LinkProtocolQinq(
                type = 'UNTAGGED',
                inner_tag_protocol_id = 56,
                outer_tag_protocol_id = 56,
                vlan_c_tag = 56,
                vlan_s_tag = 56,
                vlan_c_tag_min = 56,
                vlan_c_tag_max = 56,
                sub_interface = 56
            )
        else:
            return LinkProtocolQinq(
                inner_tag_protocol_id = 56,
                outer_tag_protocol_id = 56,
                vlan_c_tag = 56,
                vlan_s_tag = 56,
        )
        """

    def testLinkProtocolQinq(self):
        """Test LinkProtocolQinq"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
