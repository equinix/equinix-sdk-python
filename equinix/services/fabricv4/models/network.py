# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from equinix.services.fabricv4.models.changelog import Changelog
from equinix.services.fabricv4.models.link import Link
from equinix.services.fabricv4.models.network_operation import NetworkOperation
from equinix.services.fabricv4.models.network_scope import NetworkScope
from equinix.services.fabricv4.models.network_state import NetworkState
from equinix.services.fabricv4.models.network_type import NetworkType
from equinix.services.fabricv4.models.project import Project
from equinix.services.fabricv4.models.simplified_account import SimplifiedAccount
from equinix.services.fabricv4.models.simplified_location import SimplifiedLocation
from equinix.services.fabricv4.models.simplified_network_change import SimplifiedNetworkChange
from equinix.services.fabricv4.models.simplified_notification import SimplifiedNotification
from typing import Optional, Set
from typing_extensions import Self

class Network(BaseModel):
    """
    Network specification
    """ # noqa: E501
    type: NetworkType
    name: StrictStr = Field(description="Customer-provided network name")
    scope: NetworkScope
    location: Optional[SimplifiedLocation] = None
    project: Optional[Project] = None
    notifications: List[SimplifiedNotification] = Field(description="Preferences for notifications on network configuration or status changes")
    href: StrictStr = Field(description="Network URI")
    uuid: StrictStr = Field(description="Equinix-assigned network identifier")
    state: NetworkState
    connections_count: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="number of connections created on the network", alias="connectionsCount")
    account: Optional[SimplifiedAccount] = None
    change: Optional[SimplifiedNetworkChange] = None
    operation: Optional[NetworkOperation] = None
    change_log: Changelog = Field(alias="changeLog")
    links: Optional[List[Link]] = Field(default=None, description="Network sub-resources links")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["type", "name", "scope", "location", "project", "notifications", "href", "uuid", "state", "connectionsCount", "account", "change", "operation", "changeLog", "links"]

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
        """Create an instance of Network from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "href",
            "links",
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
        # override the default output from pydantic by calling `to_dict()` of project
        if self.project:
            _dict['project'] = self.project.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in notifications (list)
        _items = []
        if self.notifications:
            for _item_notifications in self.notifications:
                if _item_notifications:
                    _items.append(_item_notifications.to_dict())
            _dict['notifications'] = _items
        # override the default output from pydantic by calling `to_dict()` of account
        if self.account:
            _dict['account'] = self.account.to_dict()
        # override the default output from pydantic by calling `to_dict()` of change
        if self.change:
            _dict['change'] = self.change.to_dict()
        # override the default output from pydantic by calling `to_dict()` of operation
        if self.operation:
            _dict['operation'] = self.operation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of change_log
        if self.change_log:
            _dict['changeLog'] = self.change_log.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item_links in self.links:
                if _item_links:
                    _items.append(_item_links.to_dict())
            _dict['links'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Network from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "name": obj.get("name"),
            "scope": obj.get("scope"),
            "location": SimplifiedLocation.from_dict(obj["location"]) if obj.get("location") is not None else None,
            "project": Project.from_dict(obj["project"]) if obj.get("project") is not None else None,
            "notifications": [SimplifiedNotification.from_dict(_item) for _item in obj["notifications"]] if obj.get("notifications") is not None else None,
            "href": obj.get("href"),
            "uuid": obj.get("uuid"),
            "state": obj.get("state"),
            "connectionsCount": obj.get("connectionsCount"),
            "account": SimplifiedAccount.from_dict(obj["account"]) if obj.get("account") is not None else None,
            "change": SimplifiedNetworkChange.from_dict(obj["change"]) if obj.get("change") is not None else None,
            "operation": NetworkOperation.from_dict(obj["operation"]) if obj.get("operation") is not None else None,
            "changeLog": Changelog.from_dict(obj["changeLog"]) if obj.get("changeLog") is not None else None,
            "links": [Link.from_dict(_item) for _item in obj["links"]] if obj.get("links") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


