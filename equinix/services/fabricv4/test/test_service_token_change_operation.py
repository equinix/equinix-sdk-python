# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.fabricv4.models.service_token_change_operation import ServiceTokenChangeOperation

class TestServiceTokenChangeOperation(unittest.TestCase):
    """ServiceTokenChangeOperation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServiceTokenChangeOperation:
        """Test ServiceTokenChangeOperation
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServiceTokenChangeOperation`
        """
        model = ServiceTokenChangeOperation()
        if include_optional:
            return ServiceTokenChangeOperation(
                op = 'replace',
                path = '/expirationDateTime',
                value = None
            )
        else:
            return ServiceTokenChangeOperation(
                op = 'replace',
                path = '/expirationDateTime',
                value = None,
        )
        """

    def testServiceTokenChangeOperation(self):
        """Test ServiceTokenChangeOperation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
