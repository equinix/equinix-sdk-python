# coding: utf-8

"""
    Equinix Fabric API v4

    Equinix Fabric is an advanced software-defined interconnection solution that enables you to directly, securely and dynamically connect to distributed infrastructure and digital ecosystems on platform Equinix via a single port, Customers can use Fabric to connect to: </br> 1. Cloud Service Providers - Clouds, network and other service providers.  </br> 2. Enterprises - Other Equinix customers, vendors and partners.  </br> 3. Myself - Another customer instance deployed at Equinix. </br> </br> <b>Integrations (SDKs, Tools) links:</b> </br> <a href=\"https://deploy.equinix.com/labs/fabric-java\\\">Fabric Java SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-go\\\">Fabric Go SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-provider-equinix\\\">Equinix Terraform Provider</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-equinix-fabric\\\">Fabric Terraform Modules</a> </br> <a href=\"https://deploy.equinix.com/labs/pulumi-provider-equinix/\">Equinix Pulumi Provider</a> </br>

    The version of the OpenAPI document: 4.14
    Contact: api-support@equinix.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class SortBy(str, Enum):
    """
    Possible field names to use on sorting
    """

    """
    allowed enum values
    """
    SLASH_NAME = '/name'
    SLASH_DIRECTION = '/direction'
    SLASH_A_SIDE_SLASH_ACCESS_POINT_SLASH_NAME = '/aSide/accessPoint/name'
    SLASH_A_SIDE_SLASH_ACCESS_POINT_SLASH_TYPE = '/aSide/accessPoint/type'
    SLASH_A_SIDE_SLASH_ACCESS_POINT_SLASH_ACCOUNT_SLASH_ACCOUNT_NAME = '/aSide/accessPoint/account/accountName'
    SLASH_A_SIDE_SLASH_ACCESS_POINT_SLASH_LOCATION_SLASH_METRO_NAME = '/aSide/accessPoint/location/metroName'
    SLASH_A_SIDE_SLASH_ACCESS_POINT_SLASH_LOCATION_SLASH_METRO_CODE = '/aSide/accessPoint/location/metroCode'
    SLASH_A_SIDE_SLASH_ACCESS_POINT_SLASH_LINK_PROTOCOL_SLASH_VLAN_C_TAG = '/aSide/accessPoint/linkProtocol/vlanCTag'
    SLASH_A_SIDE_SLASH_ACCESS_POINT_SLASH_LINK_PROTOCOL_SLASH_VLAN_S_TAG = '/aSide/accessPoint/linkProtocol/vlanSTag'
    SLASH_Z_SIDE_SLASH_ACCESS_POINT_SLASH_NAME = '/zSide/accessPoint/name'
    SLASH_Z_SIDE_SLASH_ACCESS_POINT_SLASH_TYPE = '/zSide/accessPoint/type'
    SLASH_Z_SIDE_SLASH_ACCESS_POINT_SLASH_ACCOUNT_SLASH_ACCOUNT_NAME = '/zSide/accessPoint/account/accountName'
    SLASH_Z_SIDE_SLASH_ACCESS_POINT_SLASH_LOCATION_SLASH_METRO_NAME = '/zSide/accessPoint/location/metroName'
    SLASH_Z_SIDE_SLASH_ACCESS_POINT_SLASH_LOCATION_SLASH_METRO_CODE = '/zSide/accessPoint/location/metroCode'
    SLASH_Z_SIDE_SLASH_ACCESS_POINT_SLASH_LINK_PROTOCOL_SLASH_VLAN_C_TAG = '/zSide/accessPoint/linkProtocol/vlanCTag'
    SLASH_Z_SIDE_SLASH_ACCESS_POINT_SLASH_LINK_PROTOCOL_SLASH_VLAN_S_TAG = '/zSide/accessPoint/linkProtocol/vlanSTag'
    SLASH_Z_SIDE_SLASH_ACCESS_POINT_SLASH_AUTHENTICATION_KEY = '/zSide/accessPoint/authenticationKey'
    SLASH_BANDWIDTH = '/bandwidth'
    SLASH_GEO_SCOPE = '/geoScope'
    SLASH_UUID = '/uuid'
    SLASH_CHANGE_LOG_SLASH_CREATED_DATE_TIME = '/changeLog/createdDateTime'
    SLASH_CHANGE_LOG_SLASH_UPDATED_DATE_TIME = '/changeLog/updatedDateTime'
    SLASH_OPERATION_SLASH_EQUINIX_STATUS = '/operation/equinixStatus'
    SLASH_OPERATION_SLASH_PROVIDER_STATUS = '/operation/providerStatus'
    SLASH_REDUNDANCY_SLASH_PRIORITY = '/redundancy/priority'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of SortBy from a JSON string"""
        return cls(json.loads(json_str))

