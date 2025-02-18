# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)
"""

import unittest

from equinix.services.fabricv4.models.port_order_signature_delegate import PortOrderSignatureDelegate

class TestPortOrderSignatureDelegate(unittest.TestCase):
    """PortOrderSignatureDelegate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PortOrderSignatureDelegate:
        """Test PortOrderSignatureDelegate
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PortOrderSignatureDelegate`
        """
        model = PortOrderSignatureDelegate()
        if include_optional:
            return PortOrderSignatureDelegate(
                first_name = '',
                last_name = '',
                email = ''
            )
        else:
            return PortOrderSignatureDelegate(
        )
        """

    def testPortOrderSignatureDelegate(self):
        """Test PortOrderSignatureDelegate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
