# coding: utf-8

"""
    Metal API

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.metalv1.api.events_api import EventsApi


class TestEventsApi(unittest.TestCase):
    """EventsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = EventsApi()

    def tearDown(self) -> None:
        pass

    def test_find_device_events(self) -> None:
        """Test case for find_device_events

        Retrieve device's events
        """
        pass

    def test_find_device_events_all_pages(self):
        """Test case for find_device_events_all_pages

        Retrieve device's events  # noqa: E501
        """
        pass

    def test_find_event_by_id(self) -> None:
        """Test case for find_event_by_id

        Retrieve an event
        """
        pass

    def test_find_events(self) -> None:
        """Test case for find_events

        Retrieve current user's events
        """
        pass

    def test_find_events_all_pages(self):
        """Test case for find_events_all_pages

        Retrieve current user's events  # noqa: E501
        """
        pass

    def test_find_interconnection_events(self) -> None:
        """Test case for find_interconnection_events

        Retrieve interconnection events
        """
        pass

    def test_find_interconnection_events_all_pages(self):
        """Test case for find_interconnection_events_all_pages

        Retrieve interconnection events  # noqa: E501
        """
        pass

    def test_find_interconnection_port_events(self) -> None:
        """Test case for find_interconnection_port_events

        Retrieve interconnection port events
        """
        pass

    def test_find_organization_events(self) -> None:
        """Test case for find_organization_events

        Retrieve organization's events
        """
        pass

    def test_find_organization_events_all_pages(self):
        """Test case for find_organization_events_all_pages

        Retrieve organization's events  # noqa: E501
        """
        pass

    def test_find_project_events(self) -> None:
        """Test case for find_project_events

        Retrieve project's events
        """
        pass

    def test_find_project_events_all_pages(self):
        """Test case for find_project_events_all_pages

        Retrieve project's events  # noqa: E501
        """
        pass

    def test_find_virtual_circuit_events(self) -> None:
        """Test case for find_virtual_circuit_events

        Retrieve virtual circuit events
        """
        pass

    def test_find_vrf_route_events(self) -> None:
        """Test case for find_vrf_route_events

        Retrieve VRF route events
        """
        pass


if __name__ == '__main__':
    unittest.main()
