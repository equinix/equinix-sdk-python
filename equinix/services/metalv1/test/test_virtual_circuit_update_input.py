# coding: utf-8

"""
    Metal API

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.metalv1.models.virtual_circuit_update_input import VirtualCircuitUpdateInput

class TestVirtualCircuitUpdateInput(unittest.TestCase):
    """VirtualCircuitUpdateInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VirtualCircuitUpdateInput:
        """Test VirtualCircuitUpdateInput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VirtualCircuitUpdateInput`
        """
        model = VirtualCircuitUpdateInput()
        if include_optional:
            return VirtualCircuitUpdateInput(
                description = '',
                href = '',
                name = '',
                speed = '',
                tags = [
                    ''
                    ],
                vnid = '',
                customer_ip = '12.0.0.2',
                customer_ipv6 = '2604:1380:4641:a00::6',
                md5 = 'jUR,rZ#UM/?R,Fp^l6$ARjeJk C>i H\'qT\\{<?\'es#)#iK.YM{Rag2/!KB!k@5oXh.:Ts\";mGL,i&z5[P@M\"lzfB+Y,Twzfu~N^z\"mfqecVU{SE{QA<Y8XX0<}J;Krm9W\'g~?)DvDDL7BlwpCDcpNjORpuEG',
                metal_ip = '12.0.0.1',
                metal_ipv6 = '2604:1380:4641:a00::6',
                peer_asn = 65000,
                subnet = '12.0.0.0/30',
                subnet_ipv6 = '2604:1380:4641:a00::4/126'
            )
        else:
            return VirtualCircuitUpdateInput(
        )
        """

    def testVirtualCircuitUpdateInput(self):
        """Test VirtualCircuitUpdateInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
