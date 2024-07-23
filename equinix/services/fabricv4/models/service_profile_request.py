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
from equinix.services.fabricv4.models.custom_field import CustomField
from equinix.services.fabricv4.models.marketing_info import MarketingInfo
from equinix.services.fabricv4.models.project import Project
from equinix.services.fabricv4.models.service_metro import ServiceMetro
from equinix.services.fabricv4.models.service_profile_access_point_colo import ServiceProfileAccessPointCOLO
from equinix.services.fabricv4.models.service_profile_access_point_type import ServiceProfileAccessPointType
from equinix.services.fabricv4.models.service_profile_access_point_vd import ServiceProfileAccessPointVD
from equinix.services.fabricv4.models.service_profile_type_enum import ServiceProfileTypeEnum
from equinix.services.fabricv4.models.service_profile_visibility_enum import ServiceProfileVisibilityEnum
from equinix.services.fabricv4.models.simplified_notification import SimplifiedNotification
from typing import Optional, Set
from typing_extensions import Self

class ServiceProfileRequest(BaseModel):
    """
    Service Profile is a software definition for a named provider service and it's network connectivity requirements. This includes the basic marketing information and one or more sets of access points (a set per each access point type) fulfilling the provider service. 
    """ # noqa: E501
    project: Optional[Project] = None
    href: Optional[StrictStr] = Field(default=None, description="Service Profile URI response attribute")
    type: ServiceProfileTypeEnum
    name: Annotated[str, Field(strict=True, max_length=50)] = Field(description="Customer-assigned service profile name")
    uuid: Optional[StrictStr] = Field(default=None, description="Equinix-assigned service profile identifier")
    description: StrictStr = Field(description="User-provided service description should be of maximum length 375")
    notifications: Optional[List[SimplifiedNotification]] = Field(default=None, description="Recipients of notifications on service profile change")
    tags: Optional[List[StrictStr]] = None
    visibility: Optional[ServiceProfileVisibilityEnum] = None
    allowed_emails: Optional[List[StrictStr]] = Field(default=None, alias="allowedEmails")
    access_point_type_configs: Optional[Annotated[List[ServiceProfileAccessPointType], Field(min_length=1)]] = Field(default=None, alias="accessPointTypeConfigs")
    custom_fields: Optional[List[CustomField]] = Field(default=None, alias="customFields")
    marketing_info: Optional[MarketingInfo] = Field(default=None, alias="marketingInfo")
    ports: Optional[List[ServiceProfileAccessPointCOLO]] = None
    virtual_devices: Optional[List[ServiceProfileAccessPointVD]] = Field(default=None, alias="virtualDevices")
    metros: Optional[List[ServiceMetro]] = Field(default=None, description="Derived response attribute.")
    self_profile: Optional[StrictBool] = Field(default=None, description="response attribute indicates whether the profile belongs to the same organization as the api-invoker.", alias="selfProfile")
    project_id: Optional[StrictStr] = Field(default=None, alias="projectId")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["href", "type", "name", "uuid", "description", "notifications", "tags", "visibility", "allowedEmails", "accessPointTypeConfigs", "customFields", "marketingInfo", "ports", "virtualDevices", "metros", "selfProfile", "projectId"]

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
        """Create an instance of ServiceProfileRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in notifications (list)
        _items = []
        if self.notifications:
            for _item in self.notifications:
                if _item:
                    _items.append(_item.to_dict())
            _dict['notifications'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in access_point_type_configs (list)
        _items = []
        if self.access_point_type_configs:
            for _item in self.access_point_type_configs:
                if _item:
                    _items.append(_item.to_dict())
            _dict['accessPointTypeConfigs'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in custom_fields (list)
        _items = []
        if self.custom_fields:
            for _item in self.custom_fields:
                if _item:
                    _items.append(_item.to_dict())
            _dict['customFields'] = _items
        # override the default output from pydantic by calling `to_dict()` of marketing_info
        if self.marketing_info:
            _dict['marketingInfo'] = self.marketing_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in ports (list)
        _items = []
        if self.ports:
            for _item in self.ports:
                if _item:
                    _items.append(_item.to_dict())
            _dict['ports'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in virtual_devices (list)
        _items = []
        if self.virtual_devices:
            for _item in self.virtual_devices:
                if _item:
                    _items.append(_item.to_dict())
            _dict['virtualDevices'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in metros (list)
        _items = []
        if self.metros:
            for _item in self.metros:
                if _item:
                    _items.append(_item.to_dict())
            _dict['metros'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ServiceProfileRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "href": obj.get("href"),
            "type": obj.get("type"),
            "name": obj.get("name"),
            "uuid": obj.get("uuid"),
            "description": obj.get("description"),
            "notifications": [SimplifiedNotification.from_dict(_item) for _item in obj["notifications"]] if obj.get("notifications") is not None else None,
            "tags": obj.get("tags"),
            "visibility": obj.get("visibility"),
            "allowedEmails": obj.get("allowedEmails"),
            "accessPointTypeConfigs": [ServiceProfileAccessPointType.from_dict(_item) for _item in obj["accessPointTypeConfigs"]] if obj.get("accessPointTypeConfigs") is not None else None,
            "customFields": [CustomField.from_dict(_item) for _item in obj["customFields"]] if obj.get("customFields") is not None else None,
            "marketingInfo": MarketingInfo.from_dict(obj["marketingInfo"]) if obj.get("marketingInfo") is not None else None,
            "ports": [ServiceProfileAccessPointCOLO.from_dict(_item) for _item in obj["ports"]] if obj.get("ports") is not None else None,
            "virtualDevices": [ServiceProfileAccessPointVD.from_dict(_item) for _item in obj["virtualDevices"]] if obj.get("virtualDevices") is not None else None,
            "metros": [ServiceMetro.from_dict(_item) for _item in obj["metros"]] if obj.get("metros") is not None else None,
            "selfProfile": obj.get("selfProfile"),
            "projectId": obj.get("projectId")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


