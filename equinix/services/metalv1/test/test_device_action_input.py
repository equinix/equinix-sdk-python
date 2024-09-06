# coding: utf-8

"""
    Metal API

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.metalv1.models.device_action_input import DeviceActionInput

class TestDeviceActionInput(unittest.TestCase):
    """DeviceActionInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceActionInput:
        """Test DeviceActionInput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceActionInput`
        """
        model = DeviceActionInput()
        if include_optional:
            return DeviceActionInput(
                deprovision_fast = True,
                force_delete = True,
                href = '',
                ipxe_script_url = '',
                operating_system = 'ubuntu_22_04',
                preserve_data = True,
                type = 'power_on'
            )
        else:
            return DeviceActionInput(
                type = 'power_on',
        )
        """

    def testDeviceActionInput(self):
        """Test DeviceActionInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
