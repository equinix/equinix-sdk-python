# coding: utf-8

"""
    Metal API

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.metalv1.api.interconnections_api import InterconnectionsApi


class TestInterconnectionsApi(unittest.TestCase):
    """InterconnectionsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = InterconnectionsApi()

    def tearDown(self) -> None:
        pass

    def test_create_interconnection_port_virtual_circuit(self) -> None:
        """Test case for create_interconnection_port_virtual_circuit

        Create a new Virtual Circuit
        """
        pass

    def test_create_organization_interconnection(self) -> None:
        """Test case for create_organization_interconnection

        Request a new interconnection for the organization
        """
        pass

    def test_create_project_interconnection(self) -> None:
        """Test case for create_project_interconnection

        Request a new interconnection for the project's organization
        """
        pass

    def test_delete_interconnection(self) -> None:
        """Test case for delete_interconnection

        Delete interconnection
        """
        pass

    def test_delete_virtual_circuit(self) -> None:
        """Test case for delete_virtual_circuit

        Delete a virtual circuit
        """
        pass

    def test_get_interconnection(self) -> None:
        """Test case for get_interconnection

        Get interconnection
        """
        pass

    def test_get_interconnection_metros(self) -> None:
        """Test case for get_interconnection_metros

        Get connectivity to network provider by metro
        """
        pass

    def test_get_interconnection_port(self) -> None:
        """Test case for get_interconnection_port

        Get a interconnection port
        """
        pass

    def test_get_interconnection_pricing(self) -> None:
        """Test case for get_interconnection_pricing

        Get Interconnection Pricing
        """
        pass

    def test_get_virtual_circuit(self) -> None:
        """Test case for get_virtual_circuit

        Get a virtual circuit
        """
        pass

    def test_list_interconnection_port_virtual_circuits(self) -> None:
        """Test case for list_interconnection_port_virtual_circuits

        List a interconnection port's virtual circuits
        """
        pass

    def test_list_interconnection_ports(self) -> None:
        """Test case for list_interconnection_ports

        List a interconnection's ports
        """
        pass

    def test_list_interconnection_virtual_circuits(self) -> None:
        """Test case for list_interconnection_virtual_circuits

        List a interconnection's virtual circuits
        """
        pass

    def test_organization_list_interconnections(self) -> None:
        """Test case for organization_list_interconnections

        List organization connections
        """
        pass

    def test_project_list_interconnections(self) -> None:
        """Test case for project_list_interconnections

        List project connections
        """
        pass

    def test_project_list_interconnections_all_pages(self):
        """Test case for project_list_interconnections_all_pages

        List project connections  # noqa: E501
        """
        pass

    def test_update_interconnection(self) -> None:
        """Test case for update_interconnection

        Update interconnection
        """
        pass

    def test_update_virtual_circuit(self) -> None:
        """Test case for update_virtual_circuit

        Update a virtual circuit
        """
        pass


if __name__ == '__main__':
    unittest.main()
