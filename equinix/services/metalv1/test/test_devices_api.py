# coding: utf-8

"""
    Metal API

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.metalv1.api.devices_api import DevicesApi


class TestDevicesApi(unittest.TestCase):
    """DevicesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DevicesApi()

    def tearDown(self) -> None:
        pass

    def test_create_bgp_session(self) -> None:
        """Test case for create_bgp_session

        Create a BGP session
        """
        pass

    def test_create_device(self) -> None:
        """Test case for create_device

        Create a device
        """
        pass

    def test_create_ip_assignment(self) -> None:
        """Test case for create_ip_assignment

        Create an ip assignment
        """
        pass

    def test_delete_device(self) -> None:
        """Test case for delete_device

        Delete the device
        """
        pass

    def test_find_bgp_sessions(self) -> None:
        """Test case for find_bgp_sessions

        Retrieve all BGP sessions
        """
        pass

    def test_find_device_by_id(self) -> None:
        """Test case for find_device_by_id

        Retrieve a device
        """
        pass

    def test_find_device_customdata(self) -> None:
        """Test case for find_device_customdata

        Retrieve the custom metadata of an instance
        """
        pass

    def test_find_device_metadata_by_id(self) -> None:
        """Test case for find_device_metadata_by_id

        Retrieve metadata
        """
        pass

    def test_find_device_userdata_by_id(self) -> None:
        """Test case for find_device_userdata_by_id

        Retrieve userdata
        """
        pass

    def test_find_instance_bandwidth(self) -> None:
        """Test case for find_instance_bandwidth

        Retrieve an instance bandwidth
        """
        pass

    def test_find_ip_assignment_customdata(self) -> None:
        """Test case for find_ip_assignment_customdata

        Retrieve the custom metadata of an IP Assignment
        """
        pass

    def test_find_ip_assignments(self) -> None:
        """Test case for find_ip_assignments

        Retrieve all ip assignments
        """
        pass

    def test_find_organization_devices(self) -> None:
        """Test case for find_organization_devices

        Retrieve all devices of an organization
        """
        pass

    def test_find_organization_devices_all_pages(self):
        """Test case for find_organization_devices_all_pages

        Retrieve all devices of an organization  # noqa: E501
        """
        pass

    def test_find_project_devices(self) -> None:
        """Test case for find_project_devices

        Retrieve all devices of a project
        """
        pass

    def test_find_project_devices_all_pages(self):
        """Test case for find_project_devices_all_pages

        Retrieve all devices of a project  # noqa: E501
        """
        pass

    def test_find_traffic(self) -> None:
        """Test case for find_traffic

        Retrieve device traffic
        """
        pass

    def test_get_bgp_neighbor_data(self) -> None:
        """Test case for get_bgp_neighbor_data

        Retrieve BGP neighbor data for this device
        """
        pass

    def test_get_device_firmware_sets(self) -> None:
        """Test case for get_device_firmware_sets

        Get Device's associated Firmware Set
        """
        pass

    def test_get_device_health_rollup(self) -> None:
        """Test case for get_device_health_rollup

        Get Device's Health Status
        """
        pass

    def test_perform_action(self) -> None:
        """Test case for perform_action

        Perform an action
        """
        pass

    def test_update_device(self) -> None:
        """Test case for update_device

        Update the device
        """
        pass


if __name__ == '__main__':
    unittest.main()
