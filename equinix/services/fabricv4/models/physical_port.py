# coding: utf-8

"""
    Equinix Fabric API v4

    Equinix Fabric is an advanced software-defined interconnection solution that enables you to directly, securely and dynamically connect to distributed infrastructure and digital ecosystems on platform Equinix via a single port, Customers can use Fabric to connect to: </br> 1. Cloud Service Providers - Clouds, network and other service providers.  </br> 2. Enterprises - Other Equinix customers, vendors and partners.  </br> 3. Myself - Another customer instance deployed at Equinix. </br> </br> <b>Integrations (SDKs, Tools) links:</b> </br> <a href=\"https://deploy.equinix.com/labs/fabric-java\\\">Fabric Java SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-go\\\">Fabric Go SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-python\\\">Fabric Python SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-provider-equinix\\\">Equinix Terraform Provider</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-equinix-fabric\\\">Fabric Terraform Modules</a> </br> <a href=\"https://deploy.equinix.com/labs/pulumi-provider-equinix/\">Equinix Pulumi Provider</a> </br>

    The version of the OpenAPI document: 4.17
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
from equinix.services.fabricv4.models.physical_port_settings import PhysicalPortSettings
from equinix.services.fabricv4.models.physical_port_type import PhysicalPortType
from equinix.services.fabricv4.models.port_additional_info import PortAdditionalInfo
from equinix.services.fabricv4.models.port_demarcation_point import PortDemarcationPoint
from equinix.services.fabricv4.models.port_interface import PortInterface
from equinix.services.fabricv4.models.port_loa import PortLoa
from equinix.services.fabricv4.models.port_notification import PortNotification
from equinix.services.fabricv4.models.port_operation import PortOperation
from equinix.services.fabricv4.models.port_order import PortOrder
from equinix.services.fabricv4.models.port_state import PortState
from equinix.services.fabricv4.models.port_tether import PortTether
from equinix.services.fabricv4.models.simplified_account import SimplifiedAccount
from typing import Optional, Set
from typing_extensions import Self

class PhysicalPort(BaseModel):
    """
    Physical Port specification
    """ # noqa: E501
    href: Optional[StrictStr] = Field(default=None, description="Equinix assigned response attribute for an absolute URL that is the subject of the link's context.")
    type: Optional[PhysicalPortType] = None
    id: Optional[StrictInt] = Field(default=None, description="Equinix assigned response attribute for Physical Port Id")
    state: Optional[PortState] = None
    account: Optional[SimplifiedAccount] = None
    interface_speed: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="Physical Port Speed in Mbps", alias="interfaceSpeed")
    interface_type: Optional[StrictStr] = Field(default=None, description="Physical Port Interface Type", alias="interfaceType")
    uuid: Optional[StrictStr] = Field(default=None, description="Equinix assigned response attribute for physical port identifier")
    tether: Optional[PortTether] = None
    demarcation_point: Optional[PortDemarcationPoint] = Field(default=None, alias="demarcationPoint")
    settings: Optional[PhysicalPortSettings] = None
    interface: Optional[PortInterface] = None
    notifications: Optional[List[PortNotification]] = Field(default=None, description="Notification preferences")
    additional_info: Optional[List[PortAdditionalInfo]] = Field(default=None, description="Physical Port additional information", alias="additionalInfo")
    order: Optional[PortOrder] = None
    operation: Optional[PortOperation] = None
    loas: Optional[List[PortLoa]] = Field(default=None, description="Port Loas")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["href", "type", "id", "state", "account", "interfaceSpeed", "interfaceType", "uuid", "tether", "demarcationPoint", "settings", "interface", "notifications", "additionalInfo", "order", "operation", "loas"]

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
        """Create an instance of PhysicalPort from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of account
        if self.account:
            _dict['account'] = self.account.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tether
        if self.tether:
            _dict['tether'] = self.tether.to_dict()
        # override the default output from pydantic by calling `to_dict()` of demarcation_point
        if self.demarcation_point:
            _dict['demarcationPoint'] = self.demarcation_point.to_dict()
        # override the default output from pydantic by calling `to_dict()` of settings
        if self.settings:
            _dict['settings'] = self.settings.to_dict()
        # override the default output from pydantic by calling `to_dict()` of interface
        if self.interface:
            _dict['interface'] = self.interface.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in notifications (list)
        _items = []
        if self.notifications:
            for _item in self.notifications:
                if _item:
                    _items.append(_item.to_dict())
            _dict['notifications'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in additional_info (list)
        _items = []
        if self.additional_info:
            for _item in self.additional_info:
                if _item:
                    _items.append(_item.to_dict())
            _dict['additionalInfo'] = _items
        # override the default output from pydantic by calling `to_dict()` of order
        if self.order:
            _dict['order'] = self.order.to_dict()
        # override the default output from pydantic by calling `to_dict()` of operation
        if self.operation:
            _dict['operation'] = self.operation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in loas (list)
        _items = []
        if self.loas:
            for _item in self.loas:
                if _item:
                    _items.append(_item.to_dict())
            _dict['loas'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PhysicalPort from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "href": obj.get("href"),
            "type": obj.get("type"),
            "id": obj.get("id"),
            "state": obj.get("state"),
            "account": SimplifiedAccount.from_dict(obj["account"]) if obj.get("account") is not None else None,
            "interfaceSpeed": obj.get("interfaceSpeed"),
            "interfaceType": obj.get("interfaceType"),
            "uuid": obj.get("uuid"),
            "tether": PortTether.from_dict(obj["tether"]) if obj.get("tether") is not None else None,
            "demarcationPoint": PortDemarcationPoint.from_dict(obj["demarcationPoint"]) if obj.get("demarcationPoint") is not None else None,
            "settings": PhysicalPortSettings.from_dict(obj["settings"]) if obj.get("settings") is not None else None,
            "interface": PortInterface.from_dict(obj["interface"]) if obj.get("interface") is not None else None,
            "notifications": [PortNotification.from_dict(_item) for _item in obj["notifications"]] if obj.get("notifications") is not None else None,
            "additionalInfo": [PortAdditionalInfo.from_dict(_item) for _item in obj["additionalInfo"]] if obj.get("additionalInfo") is not None else None,
            "order": PortOrder.from_dict(obj["order"]) if obj.get("order") is not None else None,
            "operation": PortOperation.from_dict(obj["operation"]) if obj.get("operation") is not None else None,
            "loas": [PortLoa.from_dict(_item) for _item in obj["loas"]] if obj.get("loas") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


