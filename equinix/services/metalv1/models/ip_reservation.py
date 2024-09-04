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
from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from equinix_metal.models.href import Href
from equinix_metal.models.ip_reservation_facility import IPReservationFacility
from equinix_metal.models.ip_reservation_metro import IPReservationMetro
from equinix_metal.models.metal_gateway_lite import MetalGatewayLite
from equinix_metal.models.project import Project
from typing import Optional, Set
from typing_extensions import Self

class IPReservation(BaseModel):
    """
    IPReservation
    """ # noqa: E501
    addon: Optional[StrictBool] = None
    address: Optional[StrictStr] = None
    address_family: Optional[StrictInt] = None
    assignments: Optional[List[Href]] = None
    available: Optional[StrictStr] = None
    bill: Optional[StrictBool] = None
    cidr: Optional[StrictInt] = None
    created_at: Optional[datetime] = None
    customdata: Optional[Dict[str, Any]] = None
    details: Optional[StrictStr] = None
    enabled: Optional[StrictBool] = None
    facility: Optional[IPReservationFacility] = None
    gateway: Optional[StrictStr] = None
    global_ip: Optional[StrictBool] = None
    href: Optional[StrictStr] = None
    id: Optional[StrictStr] = None
    manageable: Optional[StrictBool] = None
    management: Optional[StrictBool] = None
    metal_gateway: Optional[MetalGatewayLite] = None
    metro: Optional[IPReservationMetro] = None
    netmask: Optional[StrictStr] = None
    network: Optional[StrictStr] = None
    project: Optional[Project] = None
    project_lite: Optional[Href] = None
    public: Optional[StrictBool] = None
    requested_by: Optional[Href] = None
    state: Optional[StrictStr] = None
    tags: Optional[List[StrictStr]] = None
    type: StrictStr
    __properties: ClassVar[List[str]] = ["addon", "address", "address_family", "assignments", "available", "bill", "cidr", "created_at", "customdata", "details", "enabled", "facility", "gateway", "global_ip", "href", "id", "manageable", "management", "metal_gateway", "metro", "netmask", "network", "project", "project_lite", "public", "requested_by", "state", "tags", "type"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['global_ipv4', 'public_ipv4', 'private_ipv4', 'public_ipv6']):
            raise ValueError("must be one of enum values ('global_ipv4', 'public_ipv4', 'private_ipv4', 'public_ipv6')")
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
        """Create an instance of IPReservation from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in assignments (list)
        _items = []
        if self.assignments:
            for _item in self.assignments:
                if _item:
                    _items.append(_item.to_dict())
            _dict['assignments'] = _items
        # override the default output from pydantic by calling `to_dict()` of facility
        if self.facility:
            _dict['facility'] = self.facility.to_dict()
        # override the default output from pydantic by calling `to_dict()` of metal_gateway
        if self.metal_gateway:
            _dict['metal_gateway'] = self.metal_gateway.to_dict()
        # override the default output from pydantic by calling `to_dict()` of metro
        if self.metro:
            _dict['metro'] = self.metro.to_dict()
        # override the default output from pydantic by calling `to_dict()` of project
        if self.project:
            _dict['project'] = self.project.to_dict()
        # override the default output from pydantic by calling `to_dict()` of project_lite
        if self.project_lite:
            _dict['project_lite'] = self.project_lite.to_dict()
        # override the default output from pydantic by calling `to_dict()` of requested_by
        if self.requested_by:
            _dict['requested_by'] = self.requested_by.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IPReservation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "addon": obj.get("addon"),
            "address": obj.get("address"),
            "address_family": obj.get("address_family"),
            "assignments": [Href.from_dict(_item) for _item in obj["assignments"]] if obj.get("assignments") is not None else None,
            "available": obj.get("available"),
            "bill": obj.get("bill"),
            "cidr": obj.get("cidr"),
            "created_at": obj.get("created_at"),
            "customdata": obj.get("customdata"),
            "details": obj.get("details"),
            "enabled": obj.get("enabled"),
            "facility": IPReservationFacility.from_dict(obj["facility"]) if obj.get("facility") is not None else None,
            "gateway": obj.get("gateway"),
            "global_ip": obj.get("global_ip"),
            "href": obj.get("href"),
            "id": obj.get("id"),
            "manageable": obj.get("manageable"),
            "management": obj.get("management"),
            "metal_gateway": MetalGatewayLite.from_dict(obj["metal_gateway"]) if obj.get("metal_gateway") is not None else None,
            "metro": IPReservationMetro.from_dict(obj["metro"]) if obj.get("metro") is not None else None,
            "netmask": obj.get("netmask"),
            "network": obj.get("network"),
            "project": Project.from_dict(obj["project"]) if obj.get("project") is not None else None,
            "project_lite": Href.from_dict(obj["project_lite"]) if obj.get("project_lite") is not None else None,
            "public": obj.get("public"),
            "requested_by": Href.from_dict(obj["requested_by"]) if obj.get("requested_by") is not None else None,
            "state": obj.get("state"),
            "tags": obj.get("tags"),
            "type": obj.get("type")
        })
        return _obj


