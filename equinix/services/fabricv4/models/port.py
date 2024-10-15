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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from equinix.services.fabricv4.models.changelog import Changelog
from equinix.services.fabricv4.models.package import Package
from equinix.services.fabricv4.models.physical_port import PhysicalPort
from equinix.services.fabricv4.models.port_additional_info import PortAdditionalInfo
from equinix.services.fabricv4.models.port_bmmr_type import PortBmmrType
from equinix.services.fabricv4.models.port_connectivity_source_type import PortConnectivitySourceType
from equinix.services.fabricv4.models.port_demarcation_point import PortDemarcationPoint
from equinix.services.fabricv4.models.port_device import PortDevice
from equinix.services.fabricv4.models.port_encapsulation import PortEncapsulation
from equinix.services.fabricv4.models.port_interface import PortInterface
from equinix.services.fabricv4.models.port_lag import PortLag
from equinix.services.fabricv4.models.port_loa import PortLoa
from equinix.services.fabricv4.models.port_notification import PortNotification
from equinix.services.fabricv4.models.port_operation import PortOperation
from equinix.services.fabricv4.models.port_order import PortOrder
from equinix.services.fabricv4.models.port_physical_ports_type import PortPhysicalPortsType
from equinix.services.fabricv4.models.port_redundancy import PortRedundancy
from equinix.services.fabricv4.models.port_service_type import PortServiceType
from equinix.services.fabricv4.models.port_settings import PortSettings
from equinix.services.fabricv4.models.port_state import PortState
from equinix.services.fabricv4.models.port_type import PortType
from equinix.services.fabricv4.models.project import Project
from equinix.services.fabricv4.models.simplified_account import SimplifiedAccount
from equinix.services.fabricv4.models.simplified_location import SimplifiedLocation
from typing import Optional, Set
from typing_extensions import Self

class Port(BaseModel):
    """
    Port specification
    """ # noqa: E501
    href: Optional[StrictStr] = Field(default=None, description="Equinix assigned response attribute for an absolute URL that is the subject of the link's context.")
    type: Optional[PortType] = None
    id: Optional[StrictInt] = Field(default=None, description="Equinix assigned response attribute for Port Id")
    uuid: Optional[StrictStr] = Field(default=None, description="Equinix assigned response attribute for  port identifier")
    name: Optional[StrictStr] = Field(default=None, description="Equinix assigned response attribute for Port name")
    description: Optional[StrictStr] = Field(default=None, description="Equinix assigned response attribute for Port description")
    physical_ports_speed: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="Physical Ports Speed in Mbps", alias="physicalPortsSpeed")
    connections_count: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="Equinix assigned response attribute for Connection count", alias="connectionsCount")
    physical_ports_type: Optional[PortPhysicalPortsType] = Field(default=None, alias="physicalPortsType")
    physical_ports_count: Optional[StrictInt] = Field(default=None, alias="physicalPortsCount")
    connectivity_source_type: Optional[PortConnectivitySourceType] = Field(default=None, alias="connectivitySourceType")
    bmmr_type: Optional[PortBmmrType] = Field(default=None, alias="bmmrType")
    project: Optional[Project] = None
    state: Optional[PortState] = None
    order: Optional[PortOrder] = None
    operation: Optional[PortOperation] = None
    account: Optional[SimplifiedAccount] = None
    change_log: Optional[Changelog] = Field(default=None, alias="changeLog")
    service_type: Optional[PortServiceType] = Field(default=None, alias="serviceType")
    bandwidth: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="Equinix assigned response attribute for Port bandwidth in Mbps")
    available_bandwidth: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="Equinix assigned response attribute for Port available bandwidth in Mbps", alias="availableBandwidth")
    used_bandwidth: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="Equinix assigned response attribute for Port used bandwidth in Mbps", alias="usedBandwidth")
    location: Optional[SimplifiedLocation] = None
    device: Optional[PortDevice] = None
    interface: Optional[PortInterface] = None
    demarcation_point_ibx: Optional[StrictStr] = Field(default=None, description="A-side/Equinix ibx", alias="demarcationPointIbx")
    tether_ibx: Optional[StrictStr] = Field(default=None, description="z-side/Equinix ibx", alias="tetherIbx")
    demarcation_point: Optional[PortDemarcationPoint] = Field(default=None, alias="demarcationPoint")
    redundancy: Optional[PortRedundancy] = None
    encapsulation: Optional[PortEncapsulation] = None
    lag_enabled: Optional[StrictBool] = Field(default=None, description="If LAG enabled", alias="lagEnabled")
    lag: Optional[PortLag] = None
    asn: Optional[StrictInt] = Field(default=None, description="Port ASN")
    package: Optional[Package] = None
    settings: Optional[PortSettings] = None
    physical_port_quantity: Optional[StrictInt] = Field(default=None, description="Number of physical ports", alias="physicalPortQuantity")
    notifications: Optional[List[PortNotification]] = Field(default=None, description="Notification preferences")
    additional_info: Optional[List[PortAdditionalInfo]] = Field(default=None, description="Port additional information", alias="additionalInfo")
    physical_ports: Optional[List[PhysicalPort]] = Field(default=None, description="Physical ports that implement this port", alias="physicalPorts")
    loas: Optional[List[PortLoa]] = Field(default=None, description="Port Loas")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["href", "type", "id", "uuid", "name", "description", "physicalPortsSpeed", "connectionsCount", "physicalPortsType", "physicalPortsCount", "connectivitySourceType", "bmmrType", "project", "state", "order", "operation", "account", "changeLog", "serviceType", "bandwidth", "availableBandwidth", "usedBandwidth", "location", "device", "interface", "demarcationPointIbx", "tetherIbx", "demarcationPoint", "redundancy", "encapsulation", "lagEnabled", "lag", "asn", "package", "settings", "physicalPortQuantity", "notifications", "additionalInfo", "physicalPorts", "loas"]

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
        """Create an instance of Port from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of project
        if self.project:
            _dict['project'] = self.project.to_dict()
        # override the default output from pydantic by calling `to_dict()` of order
        if self.order:
            _dict['order'] = self.order.to_dict()
        # override the default output from pydantic by calling `to_dict()` of operation
        if self.operation:
            _dict['operation'] = self.operation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of account
        if self.account:
            _dict['account'] = self.account.to_dict()
        # override the default output from pydantic by calling `to_dict()` of change_log
        if self.change_log:
            _dict['changeLog'] = self.change_log.to_dict()
        # override the default output from pydantic by calling `to_dict()` of location
        if self.location:
            _dict['location'] = self.location.to_dict()
        # override the default output from pydantic by calling `to_dict()` of device
        if self.device:
            _dict['device'] = self.device.to_dict()
        # override the default output from pydantic by calling `to_dict()` of interface
        if self.interface:
            _dict['interface'] = self.interface.to_dict()
        # override the default output from pydantic by calling `to_dict()` of demarcation_point
        if self.demarcation_point:
            _dict['demarcationPoint'] = self.demarcation_point.to_dict()
        # override the default output from pydantic by calling `to_dict()` of redundancy
        if self.redundancy:
            _dict['redundancy'] = self.redundancy.to_dict()
        # override the default output from pydantic by calling `to_dict()` of encapsulation
        if self.encapsulation:
            _dict['encapsulation'] = self.encapsulation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of lag
        if self.lag:
            _dict['lag'] = self.lag.to_dict()
        # override the default output from pydantic by calling `to_dict()` of package
        if self.package:
            _dict['package'] = self.package.to_dict()
        # override the default output from pydantic by calling `to_dict()` of settings
        if self.settings:
            _dict['settings'] = self.settings.to_dict()
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
        # override the default output from pydantic by calling `to_dict()` of each item in physical_ports (list)
        _items = []
        if self.physical_ports:
            for _item in self.physical_ports:
                if _item:
                    _items.append(_item.to_dict())
            _dict['physicalPorts'] = _items
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
        """Create an instance of Port from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "href": obj.get("href"),
            "type": obj.get("type"),
            "id": obj.get("id"),
            "uuid": obj.get("uuid"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "physicalPortsSpeed": obj.get("physicalPortsSpeed"),
            "connectionsCount": obj.get("connectionsCount"),
            "physicalPortsType": obj.get("physicalPortsType"),
            "physicalPortsCount": obj.get("physicalPortsCount"),
            "connectivitySourceType": obj.get("connectivitySourceType"),
            "bmmrType": obj.get("bmmrType"),
            "project": Project.from_dict(obj["project"]) if obj.get("project") is not None else None,
            "state": obj.get("state"),
            "order": PortOrder.from_dict(obj["order"]) if obj.get("order") is not None else None,
            "operation": PortOperation.from_dict(obj["operation"]) if obj.get("operation") is not None else None,
            "account": SimplifiedAccount.from_dict(obj["account"]) if obj.get("account") is not None else None,
            "changeLog": Changelog.from_dict(obj["changeLog"]) if obj.get("changeLog") is not None else None,
            "serviceType": obj.get("serviceType"),
            "bandwidth": obj.get("bandwidth"),
            "availableBandwidth": obj.get("availableBandwidth"),
            "usedBandwidth": obj.get("usedBandwidth"),
            "location": SimplifiedLocation.from_dict(obj["location"]) if obj.get("location") is not None else None,
            "device": PortDevice.from_dict(obj["device"]) if obj.get("device") is not None else None,
            "interface": PortInterface.from_dict(obj["interface"]) if obj.get("interface") is not None else None,
            "demarcationPointIbx": obj.get("demarcationPointIbx"),
            "tetherIbx": obj.get("tetherIbx"),
            "demarcationPoint": PortDemarcationPoint.from_dict(obj["demarcationPoint"]) if obj.get("demarcationPoint") is not None else None,
            "redundancy": PortRedundancy.from_dict(obj["redundancy"]) if obj.get("redundancy") is not None else None,
            "encapsulation": PortEncapsulation.from_dict(obj["encapsulation"]) if obj.get("encapsulation") is not None else None,
            "lagEnabled": obj.get("lagEnabled"),
            "lag": PortLag.from_dict(obj["lag"]) if obj.get("lag") is not None else None,
            "asn": obj.get("asn"),
            "package": Package.from_dict(obj["package"]) if obj.get("package") is not None else None,
            "settings": PortSettings.from_dict(obj["settings"]) if obj.get("settings") is not None else None,
            "physicalPortQuantity": obj.get("physicalPortQuantity"),
            "notifications": [PortNotification.from_dict(_item) for _item in obj["notifications"]] if obj.get("notifications") is not None else None,
            "additionalInfo": [PortAdditionalInfo.from_dict(_item) for _item in obj["additionalInfo"]] if obj.get("additionalInfo") is not None else None,
            "physicalPorts": [PhysicalPort.from_dict(_item) for _item in obj["physicalPorts"]] if obj.get("physicalPorts") is not None else None,
            "loas": [PortLoa.from_dict(_item) for _item in obj["loas"]] if obj.get("loas") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


