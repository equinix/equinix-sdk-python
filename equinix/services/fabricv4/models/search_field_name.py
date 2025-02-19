# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class SearchFieldName(str, Enum):
    """
    Possible field names to use on filters
    """

    """
    allowed enum values
    """
    SLASH_IS_REMOTE = '/isRemote'
    SLASH_NAME = '/name'
    SLASH_UUID = '/uuid'
    SLASH_TYPE = '/type'
    SLASH_GEO_SCOPE = '/geoScope'
    SLASH_ACCOUNT_SLASH_ORG_ID = '/account/orgId'
    SLASH_A_SIDE_SLASH_ACCESS_POINT_SLASH_ACCOUNT_SLASH_ACCOUNT_NAME = '/aSide/accessPoint/account/accountName'
    SLASH_A_SIDE_SLASH_ACCESS_POINT_SLASH_ACCOUNT_SLASH_ACCOUNT_NUMBER = '/aSide/accessPoint/account/accountNumber'
    SLASH_A_SIDE_SLASH_ACCESS_POINT_SLASH_ROUTER_SLASH_UUID = '/aSide/accessPoint/router/uuid'
    SLASH_A_SIDE_SLASH_ACCESS_POINT_SLASH_LINK_PROTOCOL_SLASH_VLAN_C_TAG = '/aSide/accessPoint/linkProtocol/vlanCTag'
    SLASH_A_SIDE_SLASH_ACCESS_POINT_SLASH_LINK_PROTOCOL_SLASH_VLAN_S_TAG = '/aSide/accessPoint/linkProtocol/vlanSTag'
    SLASH_A_SIDE_SLASH_ACCESS_POINT_SLASH_LINK_PROTOCOL_SLASH_VLAN_TAG_MIN = '/aSide/accessPoint/linkProtocol/vlanTagMin'
    SLASH_A_SIDE_SLASH_ACCESS_POINT_SLASH_LINK_PROTOCOL_SLASH_VLAN_TAG_MAX = '/aSide/accessPoint/linkProtocol/vlanTagMax'
    SLASH_A_SIDE_SLASH_ACCESS_POINT_SLASH_LOCATION_SLASH_METRO_CODE = '/aSide/accessPoint/location/metroCode'
    SLASH_A_SIDE_SLASH_ACCESS_POINT_SLASH_LOCATION_SLASH_METRO_NAME = '/aSide/accessPoint/location/metroName'
    SLASH_A_SIDE_SLASH_ACCESS_POINT_SLASH_NAME = '/aSide/accessPoint/name'
    SLASH_A_SIDE_SLASH_ACCESS_POINT_SLASH_PORT_SLASH_UUID = '/aSide/accessPoint/port/uuid'
    SLASH_A_SIDE_SLASH_ACCESS_POINT_SLASH_PORT_SLASH_NAME = '/aSide/accessPoint/port/name'
    SLASH_A_SIDE_SLASH_ACCESS_POINT_SLASH_TYPE = '/aSide/accessPoint/type'
    SLASH_A_SIDE_SLASH_ACCESS_POINT_SLASH_VIRTUAL_DEVICE_SLASH_NAME = '/aSide/accessPoint/virtualDevice/name'
    SLASH_A_SIDE_SLASH_ACCESS_POINT_SLASH_VIRTUAL_DEVICE_SLASH_UUID = '/aSide/accessPoint/virtualDevice/uuid'
    SLASH_A_SIDE_SLASH_SERVICE_TOKEN_SLASH_UUID = '/aSide/serviceToken/uuid'
    SLASH_CHANGE_SLASH_STATUS = '/change/status'
    SLASH_OPERATION_SLASH_EQUINIX_STATUS = '/operation/equinixStatus'
    SLASH_OPERATION_SLASH_PROVIDER_STATUS = '/operation/providerStatus'
    SLASH_PROJECT_SLASH_PROJECT_ID = '/project/projectId'
    SLASH_REDUNDANCY_SLASH_GROUP = '/redundancy/group'
    SLASH_REDUNDANCY_SLASH_PRIORITY = '/redundancy/priority'
    SLASH_Z_SIDE_SLASH_ACCESS_POINT_SLASH_ACCOUNT_SLASH_ACCOUNT_NAME = '/zSide/accessPoint/account/accountName'
    SLASH_Z_SIDE_SLASH_ACCESS_POINT_SLASH_AUTHENTICATION_KEY = '/zSide/accessPoint/authenticationKey'
    SLASH_Z_SIDE_SLASH_ACCESS_POINT_SLASH_LINK_PROTOCOL_SLASH_VLAN_C_TAG = '/zSide/accessPoint/linkProtocol/vlanCTag'
    SLASH_Z_SIDE_SLASH_ACCESS_POINT_SLASH_LINK_PROTOCOL_SLASH_VLAN_S_TAG = '/zSide/accessPoint/linkProtocol/vlanSTag'
    SLASH_Z_SIDE_SLASH_ACCESS_POINT_SLASH_LINK_PROTOCOL_SLASH_VLAN_TAG_MIN = '/zSide/accessPoint/linkProtocol/vlanTagMin'
    SLASH_Z_SIDE_SLASH_ACCESS_POINT_SLASH_LINK_PROTOCOL_SLASH_VLAN_TAG_MAX = '/zSide/accessPoint/linkProtocol/vlanTagMax'
    SLASH_Z_SIDE_SLASH_ACCESS_POINT_SLASH_LOCATION_SLASH_METRO_CODE = '/zSide/accessPoint/location/metroCode'
    SLASH_Z_SIDE_SLASH_ACCESS_POINT_SLASH_LOCATION_SLASH_METRO_NAME = '/zSide/accessPoint/location/metroName'
    SLASH_Z_SIDE_SLASH_ACCESS_POINT_SLASH_NAME = '/zSide/accessPoint/name'
    SLASH_Z_SIDE_SLASH_ACCESS_POINT_SLASH_PORT_SLASH_UUID = '/zSide/accessPoint/port/uuid'
    SLASH_Z_SIDE_SLASH_ACCESS_POINT_SLASH_NETWORK_SLASH_UUID = '/zSide/accessPoint/network/uuid'
    SLASH_Z_SIDE_SLASH_ACCESS_POINT_SLASH_PORT_SLASH_NAME = '/zSide/accessPoint/port/name'
    SLASH_Z_SIDE_SLASH_ACCESS_POINT_SLASH_PROFILE_SLASH_UUID = '/zSide/accessPoint/profile/uuid'
    SLASH_Z_SIDE_SLASH_ACCESS_POINT_SLASH_TYPE = '/zSide/accessPoint/type'
    SLASH_Z_SIDE_SLASH_ACCESS_POINT_SLASH_VIRTUAL_DEVICE_SLASH_NAME = '/zSide/accessPoint/virtualDevice/name'
    SLASH_Z_SIDE_SLASH_ACCESS_POINT_SLASH_VIRTUAL_DEVICE_SLASH_UUID = '/zSide/accessPoint/virtualDevice/uuid'
    SLASH_Z_SIDE_SLASH_SERVICE_TOKEN_SLASH_UUID = '/zSide/serviceToken/uuid'
    SLASH_Z_SIDE_SLASH_INTERNET_ACCESS_SLASH_UUID = '/zSide/internetAccess/uuid'
    STAR = '*'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of SearchFieldName from a JSON string"""
        return cls(json.loads(json_str))


