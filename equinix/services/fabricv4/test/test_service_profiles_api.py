# coding: utf-8

"""
    Equinix Fabric API v4

    Equinix Fabric is an advanced software-defined interconnection solution that enables you to directly, securely and dynamically connect to distributed infrastructure and digital ecosystems on platform Equinix via a single port, Customers can use Fabric to connect to: </br> 1. Cloud Service Providers - Clouds, network and other service providers.  </br> 2. Enterprises - Other Equinix customers, vendors and partners.  </br> 3. Myself - Another customer instance deployed at Equinix. </br> </br> <b>Integrations (SDKs, Tools) links:</b> </br> <a href=\"https://deploy.equinix.com/labs/fabric-java\\\">Fabric Java SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-go\\\">Fabric Go SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-provider-equinix\\\">Equinix Terraform Provider</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-equinix-fabric\\\">Fabric Terraform Modules</a> </br> <a href=\"https://deploy.equinix.com/labs/pulumi-provider-equinix/\">Equinix Pulumi Provider</a> </br>

    The version of the OpenAPI document: 4.15
    Contact: api-support@equinix.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.fabricv4.api.service_profiles_api import ServiceProfilesApi


class TestServiceProfilesApi(unittest.TestCase):
    """ServiceProfilesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ServiceProfilesApi()

    def tearDown(self) -> None:
        pass

    def test_create_service_profile(self) -> None:
        """Test case for create_service_profile

        Create Profile
        """
        pass

    def test_delete_service_profile_by_uuid(self) -> None:
        """Test case for delete_service_profile_by_uuid

        Delete Profile
        """
        pass

    def test_get_service_profile_by_uuid(self) -> None:
        """Test case for get_service_profile_by_uuid

        Get Profile
        """
        pass

    def test_get_service_profile_metros_by_uuid(self) -> None:
        """Test case for get_service_profile_metros_by_uuid

        Get Profile Metros
        """
        pass

    def test_get_service_profiles(self) -> None:
        """Test case for get_service_profiles

        Get all Profiles
        """
        pass

    def test_put_service_profile_by_uuid(self) -> None:
        """Test case for put_service_profile_by_uuid

        Replace Profile
        """
        pass

    def test_search_service_profiles(self) -> None:
        """Test case for search_service_profiles

        Profile Search
        """
        pass

    def test_update_service_profile_by_uuid(self) -> None:
        """Test case for update_service_profile_by_uuid

        Update Profile
        """
        pass


if __name__ == '__main__':
    unittest.main()
