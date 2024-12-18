# coding: utf-8

"""
    Equinix Fabric API v4

    Equinix Fabric is an advanced software-defined interconnection solution that enables you to directly, securely and dynamically connect to distributed infrastructure and digital ecosystems on platform Equinix via a single port, Customers can use Fabric to connect to: </br> 1. Cloud Service Providers - Clouds, network and other service providers.  </br> 2. Enterprises - Other Equinix customers, vendors and partners.  </br> 3. Myself - Another customer instance deployed at Equinix. </br> </br> <b>Integrations (SDKs, Tools) links:</b> </br> <a href=\"https://deploy.equinix.com/labs/fabric-java\\\">Fabric Java SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-go\\\">Fabric Go SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-python\\\">Fabric Python SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-provider-equinix\\\">Equinix Terraform Provider</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-equinix-fabric\\\">Fabric Terraform Modules</a> </br> <a href=\"https://deploy.equinix.com/labs/pulumi-provider-equinix/\">Equinix Pulumi Provider</a> </br>

    The version of the OpenAPI document: 4.18
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from equinix.services.fabricv4.models.connection_redundancy import ConnectionRedundancy
from equinix.services.fabricv4.models.connection_side import ConnectionSide
from equinix.services.fabricv4.models.connection_side_additional_info import ConnectionSideAdditionalInfo
from equinix.services.fabricv4.models.connection_type import ConnectionType
from equinix.services.fabricv4.models.end_customer import EndCustomer
from equinix.services.fabricv4.models.geo_scope_type import GeoScopeType
from equinix.services.fabricv4.models.marketplace_subscription import MarketplaceSubscription
from equinix.services.fabricv4.models.order import Order
from equinix.services.fabricv4.models.project import Project
from equinix.services.fabricv4.models.simplified_notification import SimplifiedNotification
from typing import Optional, Set
from typing_extensions import Self

class ConnectionPostRequest(BaseModel):
    """
    Create connection post request
    """ # noqa: E501
    type: ConnectionType
    name: StrictStr = Field(description="Customer-provided connection name")
    order: Optional[Order] = None
    notifications: List[SimplifiedNotification] = Field(description="Preferences for notifications on connection configuration or status changes")
    bandwidth: Annotated[int, Field(le=50000, strict=True, ge=0)] = Field(description="Connection bandwidth in Mbps")
    geo_scope: Optional[GeoScopeType] = Field(default=None, alias="geoScope")
    redundancy: Optional[ConnectionRedundancy] = None
    a_side: ConnectionSide = Field(alias="aSide")
    z_side: ConnectionSide = Field(alias="zSide")
    project: Optional[Project] = None
    additional_info: Optional[List[ConnectionSideAdditionalInfo]] = Field(default=None, description="Connection additional information", alias="additionalInfo")
    marketplace_subscription: Optional[MarketplaceSubscription] = Field(default=None, alias="marketplaceSubscription")
    end_customer: Optional[EndCustomer] = Field(default=None, alias="endCustomer")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["type", "name", "order", "notifications", "bandwidth", "geoScope", "redundancy", "aSide", "zSide", "project", "additionalInfo", "marketplaceSubscription", "endCustomer"]

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
        """Create an instance of ConnectionPostRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of order
        if self.order:
            _dict['order'] = self.order.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in notifications (list)
        _items = []
        if self.notifications:
            for _item in self.notifications:
                if _item:
                    _items.append(_item.to_dict())
            _dict['notifications'] = _items
        # override the default output from pydantic by calling `to_dict()` of redundancy
        if self.redundancy:
            _dict['redundancy'] = self.redundancy.to_dict()
        # override the default output from pydantic by calling `to_dict()` of a_side
        if self.a_side:
            _dict['aSide'] = self.a_side.to_dict()
        # override the default output from pydantic by calling `to_dict()` of z_side
        if self.z_side:
            _dict['zSide'] = self.z_side.to_dict()
        # override the default output from pydantic by calling `to_dict()` of project
        if self.project:
            _dict['project'] = self.project.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in additional_info (list)
        _items = []
        if self.additional_info:
            for _item in self.additional_info:
                if _item:
                    _items.append(_item.to_dict())
            _dict['additionalInfo'] = _items
        # override the default output from pydantic by calling `to_dict()` of marketplace_subscription
        if self.marketplace_subscription:
            _dict['marketplaceSubscription'] = self.marketplace_subscription.to_dict()
        # override the default output from pydantic by calling `to_dict()` of end_customer
        if self.end_customer:
            _dict['endCustomer'] = self.end_customer.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConnectionPostRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "name": obj.get("name"),
            "order": Order.from_dict(obj["order"]) if obj.get("order") is not None else None,
            "notifications": [SimplifiedNotification.from_dict(_item) for _item in obj["notifications"]] if obj.get("notifications") is not None else None,
            "bandwidth": obj.get("bandwidth"),
            "geoScope": obj.get("geoScope"),
            "redundancy": ConnectionRedundancy.from_dict(obj["redundancy"]) if obj.get("redundancy") is not None else None,
            "aSide": ConnectionSide.from_dict(obj["aSide"]) if obj.get("aSide") is not None else None,
            "zSide": ConnectionSide.from_dict(obj["zSide"]) if obj.get("zSide") is not None else None,
            "project": Project.from_dict(obj["project"]) if obj.get("project") is not None else None,
            "additionalInfo": [ConnectionSideAdditionalInfo.from_dict(_item) for _item in obj["additionalInfo"]] if obj.get("additionalInfo") is not None else None,
            "marketplaceSubscription": MarketplaceSubscription.from_dict(obj["marketplaceSubscription"]) if obj.get("marketplaceSubscription") is not None else None,
            "endCustomer": EndCustomer.from_dict(obj["endCustomer"]) if obj.get("endCustomer") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


