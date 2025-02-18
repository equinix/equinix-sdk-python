# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)
"""

import unittest

from equinix.services.fabricv4.models.json_patch_operation import JsonPatchOperation

class TestJsonPatchOperation(unittest.TestCase):
    """JsonPatchOperation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> JsonPatchOperation:
        """Test JsonPatchOperation
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `JsonPatchOperation`
        """
        model = JsonPatchOperation()
        if include_optional:
            return JsonPatchOperation(
                op = 'add',
                path = '',
                value = equinix.services.fabricv4.models.value.value()
            )
        else:
            return JsonPatchOperation(
                op = 'add',
                path = '',
                value = equinix.services.fabricv4.models.value.value(),
        )
        """

    def testJsonPatchOperation(self):
        """Test JsonPatchOperation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
