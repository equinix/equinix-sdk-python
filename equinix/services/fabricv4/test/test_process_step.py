# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.fabricv4.models.process_step import ProcessStep

class TestProcessStep(unittest.TestCase):
    """ProcessStep unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProcessStep:
        """Test ProcessStep
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProcessStep`
        """
        model = ProcessStep()
        if include_optional:
            return ProcessStep(
                title = '',
                sub_title = '',
                description = ''
            )
        else:
            return ProcessStep(
        )
        """

    def testProcessStep(self):
        """Test ProcessStep"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
