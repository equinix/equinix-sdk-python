# coding: utf-8

"""
    Metal API

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.metalv1.models.project_update_input import ProjectUpdateInput

class TestProjectUpdateInput(unittest.TestCase):
    """ProjectUpdateInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProjectUpdateInput:
        """Test ProjectUpdateInput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProjectUpdateInput`
        """
        model = ProjectUpdateInput()
        if include_optional:
            return ProjectUpdateInput(
                backend_transfer_enabled = True,
                customdata = None,
                href = '',
                name = '0',
                payment_method_id = '',
                tags = [
                    ''
                    ]
            )
        else:
            return ProjectUpdateInput(
        )
        """

    def testProjectUpdateInput(self):
        """Test ProjectUpdateInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
