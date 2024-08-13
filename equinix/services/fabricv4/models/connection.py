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
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from equinix.services.fabricv4.models.change import Change
from equinix.services.fabricv4.models.changelog import Changelog
from equinix.services.fabricv4.models.connection_direction import ConnectionDirection
from equinix.services.fabricv4.models.connection_operation import ConnectionOperation
from equinix.services.fabricv4.models.connection_redundancy import ConnectionRedundancy
from equinix.services.fabricv4.models.connection_side import ConnectionSide
from equinix.services.fabricv4.models.connection_side_additional_info import ConnectionSideAdditionalInfo
from equinix.services.fabricv4.models.connection_state import ConnectionState
from equinix.services.fabricv4.models.connection_type import ConnectionType
from equinix.services.fabricv4.models.geo_scope_type import GeoScopeType
from equinix.services.fabricv4.models.order import Order
from equinix.services.fabricv4.models.project import Project
from equinix.services.fabricv4.models.simplified_account import SimplifiedAccount
from equinix.services.fabricv4.models.simplified_notification import SimplifiedNotification
from typing import Optional, Set
from typing_extensions import Self

class Connection(BaseModel):
    """
    Connection specification
    """ # noqa: E501
    type: ConnectionType
    href: Optional[StrictStr] = Field(default=None, description="Connection URI")
    uuid: Optional[StrictStr] = Field(default=None, description="Equinix-assigned connection identifier")
    name: StrictStr = Field(description="Customer-provided connection name")
    description: Optional[StrictStr] = Field(default=None, description="Customer-provided connection description")
    state: Optional[ConnectionState] = None
    change: Optional[Change] = None
    operation: Optional[ConnectionOperation] = None
    order: Optional[Order] = None
    notifications: Optional[List[SimplifiedNotification]] = Field(default=None, description="Preferences for notifications on connection configuration or status changes")
    account: Optional[SimplifiedAccount] = None
    change_log: Optional[Changelog] = Field(default=None, alias="changeLog")
    bandwidth: Annotated[int, Field(le=10000, strict=True, ge=0)] = Field(description="Connection bandwidth in Mbps")
    geo_scope: Optional[GeoScopeType] = Field(default=None, alias="geoScope")
    redundancy: Optional[ConnectionRedundancy] = None
    is_remote: Optional[StrictBool] = Field(default=None, description="Connection property derived from access point locations", alias="isRemote")
    direction: Optional[ConnectionDirection] = None
    a_side: ConnectionSide = Field(alias="aSide")
    z_side: ConnectionSide = Field(alias="zSide")
    additional_info: Optional[List[ConnectionSideAdditionalInfo]] = Field(default=None, description="Connection additional information", alias="additionalInfo")
    project: Optional[Project] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["type", "href", "uuid", "name", "description", "state", "change", "operation", "order", "notifications", "account", "changeLog", "bandwidth", "geoScope", "redundancy", "isRemote", "direction", "aSide", "zSide", "additionalInfo", "project"]

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
        """Create an instance of Connection from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of change
        if self.change:
            _dict['change'] = self.change.to_dict()
        # override the default output from pydantic by calling `to_dict()` of operation
        if self.operation:
            _dict['operation'] = self.operation.to_dict()
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
        # override the default output from pydantic by calling `to_dict()` of account
        if self.account:
            _dict['account'] = self.account.to_dict()
        # override the default output from pydantic by calling `to_dict()` of change_log
        if self.change_log:
            _dict['changeLog'] = self.change_log.to_dict()
        # override the default output from pydantic by calling `to_dict()` of redundancy
        if self.redundancy:
            _dict['redundancy'] = self.redundancy.to_dict()
        # override the default output from pydantic by calling `to_dict()` of a_side
        if self.a_side:
            _dict['aSide'] = self.a_side.to_dict()
        # override the default output from pydantic by calling `to_dict()` of z_side
        if self.z_side:
            _dict['zSide'] = self.z_side.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in additional_info (list)
        _items = []
        if self.additional_info:
            for _item in self.additional_info:
                if _item:
                    _items.append(_item.to_dict())
            _dict['additionalInfo'] = _items
        # override the default output from pydantic by calling `to_dict()` of project
        if self.project:
            _dict['project'] = self.project.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Connection from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "href": obj.get("href"),
            "uuid": obj.get("uuid"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "state": obj.get("state"),
            "change": Change.from_dict(obj["change"]) if obj.get("change") is not None else None,
            "operation": ConnectionOperation.from_dict(obj["operation"]) if obj.get("operation") is not None else None,
            "order": Order.from_dict(obj["order"]) if obj.get("order") is not None else None,
            "notifications": [SimplifiedNotification.from_dict(_item) for _item in obj["notifications"]] if obj.get("notifications") is not None else None,
            "account": SimplifiedAccount.from_dict(obj["account"]) if obj.get("account") is not None else None,
            "changeLog": Changelog.from_dict(obj["changeLog"]) if obj.get("changeLog") is not None else None,
            "bandwidth": obj.get("bandwidth"),
            "geoScope": obj.get("geoScope"),
            "redundancy": ConnectionRedundancy.from_dict(obj["redundancy"]) if obj.get("redundancy") is not None else None,
            "isRemote": obj.get("isRemote"),
            "direction": obj.get("direction"),
            "aSide": ConnectionSide.from_dict(obj["aSide"]) if obj.get("aSide") is not None else None,
            "zSide": ConnectionSide.from_dict(obj["zSide"]) if obj.get("zSide") is not None else None,
            "additionalInfo": [ConnectionSideAdditionalInfo.from_dict(_item) for _item in obj["additionalInfo"]] if obj.get("additionalInfo") is not None else None,
            "project": Project.from_dict(obj["project"]) if obj.get("project") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

