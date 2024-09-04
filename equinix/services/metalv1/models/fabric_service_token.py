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
from typing import Optional, Set
from typing_extensions import Self

class FabricServiceToken(BaseModel):
    """
    FabricServiceToken
    """ # noqa: E501
    expires_at: Optional[datetime] = Field(default=None, description="The expiration date and time of the Fabric service token. Once a service token is expired, it is no longer redeemable.")
    href: Optional[StrictStr] = None
    id: Optional[StrictStr] = Field(default=None, description="The UUID that can be used on the Fabric Portal to redeem either an A-Side or Z-Side Service Token. For Fabric VCs (Metal Billed), this UUID will represent an A-Side Service Token, which will allow interconnections to be made from Equinix Metal to other Service Providers on Fabric. For Fabric VCs (Fabric Billed), this UUID will represent a Z-Side Service Token, which will allow interconnections to be made to connect an owned Fabric Port or  Virtual Device to Equinix Metal.")
    max_allowed_speed: Optional[StrictInt] = Field(default=None, description="The maximum speed that can be selected on the Fabric Portal when configuring a interconnection with either  an A-Side or Z-Side Service Token. For Fabric VCs (Metal Billed), this is what the billing is based off of, and can be one of the following options, '50mbps', '200mbps', '500mbps', '1gbps', '2gbps', '5gbps' or '10gbps'. For Fabric VCs (Fabric Billed), this will default to 10Gbps.")
    role: Optional[StrictStr] = Field(default=None, description="Either primary or secondary, depending on which interconnection the service token is associated to.")
    service_token_type: Optional[StrictStr] = Field(default=None, description="Either 'a_side' or 'z_side', depending on which type of Fabric VC was requested.")
    state: Optional[StrictStr] = Field(default=None, description="The state of the service token that corresponds with the service token state on Fabric. An 'inactive' state refers to a token that has not been redeemed yet on the Fabric side, an 'active' state refers to a token that has already been redeemed, and an 'expired' state refers to a token that has reached its expiry time.")
    __properties: ClassVar[List[str]] = ["expires_at", "href", "id", "max_allowed_speed", "role", "service_token_type", "state"]

    @field_validator('role')
    def role_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['primary', 'secondary']):
            raise ValueError("must be one of enum values ('primary', 'secondary')")
        return value

    @field_validator('service_token_type')
    def service_token_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['a_side', 'z_side']):
            raise ValueError("must be one of enum values ('a_side', 'z_side')")
        return value

    @field_validator('state')
    def state_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['inactive', 'active', 'expired']):
            raise ValueError("must be one of enum values ('inactive', 'active', 'expired')")
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
        """Create an instance of FabricServiceToken from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FabricServiceToken from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "expires_at": obj.get("expires_at"),
            "href": obj.get("href"),
            "id": obj.get("id"),
            "max_allowed_speed": obj.get("max_allowed_speed"),
            "role": obj.get("role"),
            "service_token_type": obj.get("service_token_type"),
            "state": obj.get("state")
        })
        return _obj


