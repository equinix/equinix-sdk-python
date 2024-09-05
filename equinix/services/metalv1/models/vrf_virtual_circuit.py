# coding: utf-8

"""
    Metal API

    # Introduction Equinix Metal provides a RESTful HTTP API which can be reached at <https://api.equinix.com/metal/v1>. This document describes the API and how to use it.  The API allows you to programmatically interact with all of your Equinix Metal resources, including devices, networks, addresses, organizations, projects, and your user account. Every feature of the Equinix Metal web interface is accessible through the API.  The API docs are generated from the Equinix Metal OpenAPI specification and are officially hosted at <https://deploy.equinix.com/developers/api/metal/>.  # Common Parameters  The Equinix Metal API uses a few methods to minimize network traffic and improve throughput. These parameters are not used in all API calls, but are used often enough to warrant their own section. Look for these parameters in the documentation for the API calls that support them.  ## Pagination  Pagination is used to limit the number of results returned in a single request. The API will return a maximum of 100 results per page. To retrieve additional results, you can use the `page` and `per_page` query parameters.  The `page` parameter is used to specify the page number. The first page is `1`. The `per_page` parameter is used to specify the number of results per page. The maximum number of results differs by resource type.  ## Sorting  Where offered, the API allows you to sort results by a specific field. To sort results use the `sort_by` query parameter with the root level field name as the value. The `sort_direction` parameter is used to specify the sort direction, either either `asc` (ascending) or `desc` (descending).  ## Filtering  Filtering is used to limit the results returned in a single request. The API supports filtering by certain fields in the response. To filter results, you can use the field as a query parameter.  For example, to filter the IP list to only return public IPv4 addresses, you can filter by the `type` field, as in the following request:  ```sh curl -H 'X-Auth-Token: my_authentication_token' \\   https://api.equinix.com/metal/v1/projects/id/ips?type=public_ipv4 ```  Only IP addresses with the `type` field set to `public_ipv4` will be returned.  ## Searching  Searching is used to find matching resources using multiple field comparissons. The API supports searching in resources that define this behavior. Currently the search parameter is only available on devices, ssh_keys, api_keys and memberships endpoints.  To search resources you can use the `search` query parameter.  ## Include and Exclude  For resources that contain references to other resources, sucha as a Device that refers to the Project it resides in, the Equinix Metal API will returns `href` values (API links) to the associated resource.  ```json {   ...   \"project\": {     \"href\": \"/metal/v1/projects/f3f131c8-f302-49ef-8c44-9405022dc6dd\"   } } ```  If you're going need the project details, you can avoid a second API request.  Specify the contained `href` resources and collections that you'd like to have included in the response using the `include` query parameter.  For example:  ```sh curl -H 'X-Auth-Token: my_authentication_token' \\   https://api.equinix.com/metal/v1/user?include=projects ```  The `include` parameter is generally accepted in `GET`, `POST`, `PUT`, and `PATCH` requests where `href` resources are presented.  To have multiple resources include, use a comma-separated list (e.g. `?include=emails,projects,memberships`).  ```sh curl -H 'X-Auth-Token: my_authentication_token' \\   https://api.equinix.com/metal/v1/user?include=emails,projects,memberships ```  You may also include nested associations up to three levels deep using dot notation (`?include=memberships.projects`):  ```sh curl -H 'X-Auth-Token: my_authentication_token' \\   https://api.equinix.com/metal/v1/user?include=memberships.projects ```  To exclude resources, and optimize response delivery, use the `exclude` query parameter. The `exclude` parameter is generally accepted in `GET`, `POST`, `PUT`, and `PATCH` requests for fields with nested object responses. When excluded, these fields will be replaced with an object that contains only an `href` field. 

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from equinix_metal.models.project import Project
from typing import Optional, Set
from typing_extensions import Self

class VrfVirtualCircuit(BaseModel):
    """
    VrfVirtualCircuit
    """ # noqa: E501
    created_at: Optional[datetime] = None
    customer_ip: Optional[StrictStr] = Field(default=None, description="An IPv4 address from the subnet that will be used on the Customer side. This parameter is optional, but if supplied, we will use the other usable IP address in the subnet as the Metal IP. By default, the last usable IP address in the subnet will be used.")
    customer_ipv6: Optional[StrictStr] = Field(default=None, description="An IPv6 address from the subnet IPv6 that will be used on the Customer side. This parameter is optional, but if supplied, we will use the other usable IP address in the subnet IPv6 as the Metal IPv6. By default, the last usable IP address in the subnet IPv6 will be used.")
    description: Optional[StrictStr] = None
    href: Optional[StrictStr] = None
    id: Optional[StrictStr] = None
    md5: Optional[StrictStr] = Field(default=None, description="The MD5 password for the BGP peering in plaintext (not a checksum).")
    metal_ip: Optional[StrictStr] = Field(default=None, description="An IPv4 address from the subnet that will be used on the Metal side. This parameter is optional, but if supplied, we will use the other usable IP address in the subnet as the Customer IP. By default, the first usable IP address in the subnet will be used.")
    metal_ipv6: Optional[StrictStr] = Field(default=None, description="An IPv6 address from the subnet IPv6 that will be used on the Metal side. This parameter is optional, but if supplied, we will use the other usable IPv6 address in the subnet IPv6 as the Customer IP. By default, the first usable IPv6 address in the subnet IPv6 will be used.")
    name: Optional[StrictStr] = None
    nni_vlan: Optional[StrictInt] = None
    peer_asn: Optional[Annotated[int, Field(le=4294967295, strict=True, ge=0)]] = Field(default=None, description="The peer ASN that will be used with the VRF on the Virtual Circuit.")
    port: Optional[InterconnectionPort] = None
    project: Optional[Project] = None
    speed: Optional[StrictInt] = Field(default=None, description="integer representing bps speed")
    status: Optional[StrictStr] = Field(default=None, description="The status changes of a VRF virtual circuit are generally the same as Virtual Circuits that aren't in a VRF. However, for VRF Virtual Circuits on Fabric VCs, the status will change to 'waiting_on_peering_details' once the Fabric service token associated with the virtual circuit has been redeemed on Fabric, and Metal has found the associated Fabric connection. At this point, users can update the subnet, MD5 password, customer IP and/or metal IP accordingly. For VRF Virtual Circuits on Dedicated Ports, we require all peering details to be set on creation of a VRF Virtual Circuit. The status will change to `changing_peering_details` whenever an active VRF Virtual Circuit has any of its peering details updated.")
    subnet: Optional[StrictStr] = Field(default=None, description="The /30 or /31 IPv4 subnet of one of the VRF IP Blocks that will be used with the VRF for the Virtual Circuit. This subnet does not have to be an existing VRF IP reservation, as we will create the VRF IP reservation on creation if it does not exist. The Metal IP and Customer IP must be IPs from this subnet. For /30 subnets, the network and broadcast IPs cannot be used as the Metal or Customer IP.")
    subnet_ipv6: Optional[StrictStr] = Field(default=None, description="The /126 or /127 IPv6 subnet of one of the VRF IP Blocks that will be used with the VRF for the Virtual Circuit. This subnet does not have to be an existing VRF IP reservation, as we will create the VRF IP reservation on creation if it does not exist. The Metal IPv6 and Customer IPv6 must be IPs from this subnet. For /126 subnets, the network and broadcast IPs cannot be used as the Metal IPv6 or Customer IPv6. The subnet specified must be contained within an already-defined IP Range for the VRF.")
    tags: Optional[List[StrictStr]] = None
    type: Optional[StrictStr] = None
    updated_at: Optional[datetime] = None
    vrf: Vrf
    __properties: ClassVar[List[str]] = ["created_at", "customer_ip", "customer_ipv6", "description", "href", "id", "md5", "metal_ip", "metal_ipv6", "name", "nni_vlan", "peer_asn", "port", "project", "speed", "status", "subnet", "subnet_ipv6", "tags", "type", "updated_at", "vrf"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['pending', 'waiting_on_peering_details', 'activating', 'changing_peering_details', 'deactivating', 'deleting', 'active', 'expired', 'activation_failed', 'changing_peering_details_failed', 'deactivation_failed', 'delete_failed']):
            raise ValueError("must be one of enum values ('pending', 'waiting_on_peering_details', 'activating', 'changing_peering_details', 'deactivating', 'deleting', 'active', 'expired', 'activation_failed', 'changing_peering_details_failed', 'deactivation_failed', 'delete_failed')")
        return value

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['vrf']):
            raise ValueError("must be one of enum values ('vrf')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of VrfVirtualCircuit from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of port
        if self.port:
            _dict['port'] = self.port.to_dict()
        # override the default output from pydantic by calling `to_dict()` of project
        if self.project:
            _dict['project'] = self.project.to_dict()
        # override the default output from pydantic by calling `to_dict()` of vrf
        if self.vrf:
            _dict['vrf'] = self.vrf.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of VrfVirtualCircuit from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "created_at": obj.get("created_at"),
            "customer_ip": obj.get("customer_ip"),
            "customer_ipv6": obj.get("customer_ipv6"),
            "description": obj.get("description"),
            "href": obj.get("href"),
            "id": obj.get("id"),
            "md5": obj.get("md5"),
            "metal_ip": obj.get("metal_ip"),
            "metal_ipv6": obj.get("metal_ipv6"),
            "name": obj.get("name"),
            "nni_vlan": obj.get("nni_vlan"),
            "peer_asn": obj.get("peer_asn"),
            "port": InterconnectionPort.from_dict(obj["port"]) if obj.get("port") is not None else None,
            "project": Project.from_dict(obj["project"]) if obj.get("project") is not None else None,
            "speed": obj.get("speed"),
            "status": obj.get("status"),
            "subnet": obj.get("subnet"),
            "subnet_ipv6": obj.get("subnet_ipv6"),
            "tags": obj.get("tags"),
            "type": obj.get("type"),
            "updated_at": obj.get("updated_at"),
            "vrf": Vrf.from_dict(obj["vrf"]) if obj.get("vrf") is not None else None
        })
        return _obj

from equinix_metal.models.interconnection_port import InterconnectionPort
from equinix_metal.models.vrf import Vrf
# TODO: Rewrite to not use raise_errors
VrfVirtualCircuit.model_rebuild(raise_errors=False)
