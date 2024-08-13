# coding: utf-8

"""
    Equinix Fabric API v4

    Equinix Fabric is an advanced software-defined interconnection solution that enables you to directly, securely and dynamically connect to distributed infrastructure and digital ecosystems on platform Equinix via a single port, Customers can use Fabric to connect to: </br> 1. Cloud Service Providers - Clouds, network and other service providers.  </br> 2. Enterprises - Other Equinix customers, vendors and partners.  </br> 3. Myself - Another customer instance deployed at Equinix. </br> </br> <b>Integrations (SDKs, Tools) links:</b> </br> <a href=\"https://deploy.equinix.com/labs/fabric-java\\\">Fabric Java SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-go\\\">Fabric Go SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-provider-equinix\\\">Equinix Terraform Provider</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-equinix-fabric\\\">Fabric Terraform Modules</a> </br> <a href=\"https://deploy.equinix.com/labs/pulumi-provider-equinix/\">Equinix Pulumi Provider</a> </br>

    The version of the OpenAPI document: 4.15
    Contact: api-support@equinix.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from equinix.services.fabricv4.models.changelog import Changelog
from equinix.services.fabricv4.models.cloud_router_access_point_state import CloudRouterAccessPointState
from equinix.services.fabricv4.models.cloud_router_change import CloudRouterChange
from equinix.services.fabricv4.models.cloud_router_post_request_package import CloudRouterPostRequestPackage
from equinix.services.fabricv4.models.cloud_router_post_request_type import CloudRouterPostRequestType
from equinix.services.fabricv4.models.marketplace_subscription import MarketplaceSubscription
from equinix.services.fabricv4.models.order import Order
from equinix.services.fabricv4.models.project import Project
from equinix.services.fabricv4.models.simplified_account import SimplifiedAccount
from equinix.services.fabricv4.models.simplified_location_without_ibx import SimplifiedLocationWithoutIBX
from equinix.services.fabricv4.models.simplified_notification import SimplifiedNotification
from typing import Optional, Set
from typing_extensions import Self

class CloudRouter(BaseModel):
    """
    Fabric Cloud Router object
    """ # noqa: E501
    href: Optional[StrictStr] = Field(default=None, description="Cloud Routers URI")
    uuid: Optional[StrictStr] = Field(default=None, description="Equinix-assigned access point identifier")
    name: Optional[StrictStr] = Field(default=None, description="Customer-provided Cloud Router name")
    state: Optional[CloudRouterAccessPointState] = None
    equinix_asn: Optional[StrictInt] = Field(default=None, description="Equinix ASN", alias="equinixAsn")
    bgp_ipv4_routes_count: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="Access point used and maximum number of IPv4 BGP routes", alias="bgpIpv4RoutesCount")
    bgp_ipv6_routes_count: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="Access point used and maximum number of IPv6 BGP routes", alias="bgpIpv6RoutesCount")
    connections_count: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="Number of connections associated with this Access point", alias="connectionsCount")
    distinct_ipv4_prefixes_count: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="Number of distinct ipv4 routes", alias="distinctIpv4PrefixesCount")
    distinct_ipv6_prefixes_count: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="Number of distinct ipv6 routes", alias="distinctIpv6PrefixesCount")
    marketplace_subscription: Optional[MarketplaceSubscription] = Field(default=None, alias="marketplaceSubscription")
    change_log: Optional[Changelog] = Field(default=None, alias="changeLog")
    change: Optional[CloudRouterChange] = None
    type: Optional[CloudRouterPostRequestType] = None
    location: Optional[SimplifiedLocationWithoutIBX] = None
    package: Optional[CloudRouterPostRequestPackage] = None
    order: Optional[Order] = None
    project: Optional[Project] = None
    account: Optional[SimplifiedAccount] = None
    notifications: Optional[List[SimplifiedNotification]] = Field(default=None, description="Preferences for notifications on connection configuration or status changes")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["type", "name", "location", "package", "order", "project", "account", "notifications", "marketplaceSubscription"]

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
        """Create an instance of CloudRouter from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "href",
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of location
        if self.location:
            _dict['location'] = self.location.to_dict()
        # override the default output from pydantic by calling `to_dict()` of package
        if self.package:
            _dict['package'] = self.package.to_dict()
        # override the default output from pydantic by calling `to_dict()` of order
        if self.order:
            _dict['order'] = self.order.to_dict()
        # override the default output from pydantic by calling `to_dict()` of project
        if self.project:
            _dict['project'] = self.project.to_dict()
        # override the default output from pydantic by calling `to_dict()` of account
        if self.account:
            _dict['account'] = self.account.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in notifications (list)
        _items = []
        if self.notifications:
            for _item in self.notifications:
                if _item:
                    _items.append(_item.to_dict())
            _dict['notifications'] = _items
        # override the default output from pydantic by calling `to_dict()` of marketplace_subscription
        if self.marketplace_subscription:
            _dict['marketplaceSubscription'] = self.marketplace_subscription.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CloudRouter from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "name": obj.get("name"),
            "location": SimplifiedLocationWithoutIBX.from_dict(obj["location"]) if obj.get("location") is not None else None,
            "package": CloudRouterPostRequestPackage.from_dict(obj["package"]) if obj.get("package") is not None else None,
            "order": Order.from_dict(obj["order"]) if obj.get("order") is not None else None,
            "project": Project.from_dict(obj["project"]) if obj.get("project") is not None else None,
            "account": SimplifiedAccount.from_dict(obj["account"]) if obj.get("account") is not None else None,
            "notifications": [SimplifiedNotification.from_dict(_item) for _item in obj["notifications"]] if obj.get("notifications") is not None else None,
            "marketplaceSubscription": MarketplaceSubscription.from_dict(obj["marketplaceSubscription"]) if obj.get("marketplaceSubscription") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


