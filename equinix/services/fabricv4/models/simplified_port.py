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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from equinix.services.fabricv4.models.package import Package
from equinix.services.fabricv4.models.physical_port import PhysicalPort
from equinix.services.fabricv4.models.port_additional_info import PortAdditionalInfo
from equinix.services.fabricv4.models.port_demarcation_point import PortDemarcationPoint
from equinix.services.fabricv4.models.port_device import PortDevice
from equinix.services.fabricv4.models.port_encapsulation import PortEncapsulation
from equinix.services.fabricv4.models.port_interface import PortInterface
from equinix.services.fabricv4.models.port_operation import PortOperation
from equinix.services.fabricv4.models.port_redundancy import PortRedundancy
from equinix.services.fabricv4.models.port_service_type import PortServiceType
from equinix.services.fabricv4.models.port_settings import PortSettings
from equinix.services.fabricv4.models.port_state import PortState
from equinix.services.fabricv4.models.port_tether import PortTether
from equinix.services.fabricv4.models.port_type import PortType
from equinix.services.fabricv4.models.project import Project
from equinix.services.fabricv4.models.simplified_account import SimplifiedAccount
from equinix.services.fabricv4.models.simplified_location import SimplifiedLocation
from typing import Optional, Set
from typing_extensions import Self

class SimplifiedPort(BaseModel):
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
    project: Optional[Project] = None
    state: Optional[PortState] = None
    operation: Optional[PortOperation] = None
    account: Optional[SimplifiedAccount] = None
    service_type: Optional[PortServiceType] = Field(default=None, alias="serviceType")
    bandwidth: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="Equinix assigned response attribute for Port bandwidth in Mbps")
    available_bandwidth: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="Equinix assigned response attribute for Port available bandwidth in Mbps", alias="availableBandwidth")
    used_bandwidth: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="Equinix assigned response attribute for Port used bandwidth in Mbps", alias="usedBandwidth")
    location: Optional[SimplifiedLocation] = None
    device: Optional[PortDevice] = None
    interface: Optional[PortInterface] = None
    tether: Optional[PortTether] = None
    demarcation_point: Optional[PortDemarcationPoint] = Field(default=None, alias="demarcationPoint")
    redundancy: Optional[PortRedundancy] = None
    encapsulation: Optional[PortEncapsulation] = None
    lag_enabled: Optional[StrictBool] = Field(default=None, description="If LAG enabled", alias="lagEnabled")
    package: Optional[Package] = None
    settings: Optional[PortSettings] = None
    physical_port_quantity: Optional[StrictInt] = Field(default=None, description="Number of physical ports", alias="physicalPortQuantity")
    additional_info: Optional[List[PortAdditionalInfo]] = Field(default=None, description="Port additional information", alias="additionalInfo")
    physical_ports: Optional[List[PhysicalPort]] = Field(default=None, description="Physical ports that implement this port", alias="physicalPorts")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["href", "type", "id", "uuid", "name", "description", "physicalPortsSpeed", "connectionsCount", "project", "state", "operation", "account", "serviceType", "bandwidth", "availableBandwidth", "usedBandwidth", "location", "device", "interface", "tether", "demarcationPoint", "redundancy", "encapsulation", "lagEnabled", "package", "settings", "physicalPortQuantity", "additionalInfo", "physicalPorts"]

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
        """Create an instance of SimplifiedPort from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of operation
        if self.operation:
            _dict['operation'] = self.operation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of account
        if self.account:
            _dict['account'] = self.account.to_dict()
        # override the default output from pydantic by calling `to_dict()` of location
        if self.location:
            _dict['location'] = self.location.to_dict()
        # override the default output from pydantic by calling `to_dict()` of device
        if self.device:
            _dict['device'] = self.device.to_dict()
        # override the default output from pydantic by calling `to_dict()` of interface
        if self.interface:
            _dict['interface'] = self.interface.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tether
        if self.tether:
            _dict['tether'] = self.tether.to_dict()
        # override the default output from pydantic by calling `to_dict()` of demarcation_point
        if self.demarcation_point:
            _dict['demarcationPoint'] = self.demarcation_point.to_dict()
        # override the default output from pydantic by calling `to_dict()` of redundancy
        if self.redundancy:
            _dict['redundancy'] = self.redundancy.to_dict()
        # override the default output from pydantic by calling `to_dict()` of encapsulation
        if self.encapsulation:
            _dict['encapsulation'] = self.encapsulation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of package
        if self.package:
            _dict['package'] = self.package.to_dict()
        # override the default output from pydantic by calling `to_dict()` of settings
        if self.settings:
            _dict['settings'] = self.settings.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in additional_info (list)
        _items = []
        if self.additional_info:
            for _item_additional_info in self.additional_info:
                if _item_additional_info:
                    _items.append(_item_additional_info.to_dict())
            _dict['additionalInfo'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in physical_ports (list)
        _items = []
        if self.physical_ports:
            for _item_physical_ports in self.physical_ports:
                if _item_physical_ports:
                    _items.append(_item_physical_ports.to_dict())
            _dict['physicalPorts'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SimplifiedPort from a dict"""
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
            "project": Project.from_dict(obj["project"]) if obj.get("project") is not None else None,
            "state": obj.get("state"),
            "operation": PortOperation.from_dict(obj["operation"]) if obj.get("operation") is not None else None,
            "account": SimplifiedAccount.from_dict(obj["account"]) if obj.get("account") is not None else None,
            "serviceType": obj.get("serviceType"),
            "bandwidth": obj.get("bandwidth"),
            "availableBandwidth": obj.get("availableBandwidth"),
            "usedBandwidth": obj.get("usedBandwidth"),
            "location": SimplifiedLocation.from_dict(obj["location"]) if obj.get("location") is not None else None,
            "device": PortDevice.from_dict(obj["device"]) if obj.get("device") is not None else None,
            "interface": PortInterface.from_dict(obj["interface"]) if obj.get("interface") is not None else None,
            "tether": PortTether.from_dict(obj["tether"]) if obj.get("tether") is not None else None,
            "demarcationPoint": PortDemarcationPoint.from_dict(obj["demarcationPoint"]) if obj.get("demarcationPoint") is not None else None,
            "redundancy": PortRedundancy.from_dict(obj["redundancy"]) if obj.get("redundancy") is not None else None,
            "encapsulation": PortEncapsulation.from_dict(obj["encapsulation"]) if obj.get("encapsulation") is not None else None,
            "lagEnabled": obj.get("lagEnabled"),
            "package": Package.from_dict(obj["package"]) if obj.get("package") is not None else None,
            "settings": PortSettings.from_dict(obj["settings"]) if obj.get("settings") is not None else None,
            "physicalPortQuantity": obj.get("physicalPortQuantity"),
            "additionalInfo": [PortAdditionalInfo.from_dict(_item) for _item in obj["additionalInfo"]] if obj.get("additionalInfo") is not None else None,
            "physicalPorts": [PhysicalPort.from_dict(_item) for _item in obj["physicalPorts"]] if obj.get("physicalPorts") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


