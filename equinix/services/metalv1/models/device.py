# coding: utf-8

"""
    Metal API

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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from equinix.services.metalv1.models.device_actions_inner import DeviceActionsInner
from equinix.services.metalv1.models.device_created_by import DeviceCreatedBy
from equinix.services.metalv1.models.device_metro import DeviceMetro
from equinix.services.metalv1.models.device_project_lite import DeviceProjectLite
from equinix.services.metalv1.models.event import Event
from equinix.services.metalv1.models.facility import Facility
from equinix.services.metalv1.models.href import Href
from equinix.services.metalv1.models.ip_assignment import IPAssignment
from equinix.services.metalv1.models.operating_system import OperatingSystem
from equinix.services.metalv1.models.plan import Plan
from equinix.services.metalv1.models.project import Project
from equinix.services.metalv1.models.storage import Storage
from typing import Optional, Set
from typing_extensions import Self

class Device(BaseModel):
    """
    Device
    """ # noqa: E501
    actions: Optional[List[DeviceActionsInner]] = Field(default=None, description="Actions supported by the device instance.")
    always_pxe: Optional[StrictBool] = None
    billing_cycle: Optional[StrictStr] = None
    bonding_mode: Optional[StrictInt] = None
    created_at: Optional[datetime] = None
    created_by: Optional[DeviceCreatedBy] = None
    customdata: Optional[Dict[str, Any]] = None
    description: Optional[StrictStr] = None
    facility: Optional[Facility] = None
    firmware_set_id: Optional[StrictStr] = Field(default=None, description="The UUID of the firmware set to associate with the device.")
    hardware_reservation: Optional[HardwareReservation] = None
    hostname: Optional[StrictStr] = None
    href: Optional[StrictStr] = None
    id: Optional[StrictStr] = None
    image_url: Optional[StrictStr] = None
    ip_addresses: Optional[List[IPAssignment]] = None
    ipxe_script_url: Optional[StrictStr] = None
    iqn: Optional[StrictStr] = None
    locked: Optional[StrictBool] = Field(default=None, description="Prevents accidental deletion of this resource when set to true.")
    metro: Optional[DeviceMetro] = None
    network_frozen: Optional[StrictBool] = Field(default=None, description="Whether network mode changes such as converting to/from Layer2 or Layer3 networking, bonding or disbonding network interfaces are permitted for the device.")
    network_ports: Optional[List[Port]] = Field(default=None, description="By default, servers at Equinix Metal are configured in a “bonded” mode using LACP (Link Aggregation Control Protocol). Each 2-NIC server is configured with a single bond (namely bond0) with both interfaces eth0 and eth1 as members of the bond in a default Layer 3 mode. Some device plans may have a different number of ports and bonds available.")
    operating_system: Optional[OperatingSystem] = None
    plan: Optional[Plan] = None
    project: Optional[Project] = None
    project_lite: Optional[DeviceProjectLite] = None
    provisioning_events: Optional[List[Event]] = None
    provisioning_percentage: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Only visible while device provisioning")
    root_password: Optional[StrictStr] = Field(default=None, description="Root password is automatically generated when server is provisioned and it is removed after 24 hours")
    short_id: Optional[StrictStr] = None
    sos: Optional[StrictStr] = Field(default=None, description="Hostname used to connect to the instance via the SOS (Serial over SSH) out-of-band console.")
    spot_instance: Optional[StrictBool] = Field(default=None, description="Whether or not the device is a spot instance.")
    spot_price_max: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The maximum price per hour you are willing to pay to keep this spot instance.  If you are outbid, the termination will be set allowing two minutes before shutdown.")
    ssh_keys: Optional[List[Href]] = None
    state: Optional[StrictStr] = Field(default=None, description="The current state the instance is in.  * When an instance is initially created it will be in the `queued` state until it is picked up by the provisioner. * Once provisioning has begun on the instance it's state will move to `provisioning`. * When an instance is deleted, it will move to `deprovisioning` state until the deprovision is completed and the instance state moves to `deleted`. * If an instance fails to provision or deprovision it will move to `failed` state. * Once an instance has completed provisioning it will move to `active` state. * If an instance is currently powering off or powering on it will move to `powering_off` or `powering_on` states respectively.  * When the instance is powered off completely it will move to the `inactive` state. * When an instance is powered on completely it will move to the `active` state. * Using the reinstall action to install a new OS on the instance will cause the instance state to change to `reinstalling`. * When the reinstall action is complete the instance will move to `active` state.")
    storage: Optional[Storage] = None
    switch_uuid: Optional[StrictStr] = Field(default=None, description="Switch short id. This can be used to determine if two devices are connected to the same switch, for example.")
    tags: Optional[List[StrictStr]] = None
    termination_time: Optional[datetime] = Field(default=None, description="When the device will be terminated. If you don't supply timezone info, the timestamp is assumed to be in UTC.  This is commonly set in advance for ephemeral spot market instances but this field may also be set with on-demand and reservation instances to automatically delete the resource at a given time. The termination time can also be used to release a hardware reservation instance at a given time, keeping the reservation open for other uses.  On a spot market device, the termination time will be set automatically when outbid.")
    updated_at: Optional[datetime] = None
    user: Optional[StrictStr] = None
    userdata: Optional[StrictStr] = None
    volumes: Optional[List[Href]] = None
    __properties: ClassVar[List[str]] = ["actions", "always_pxe", "billing_cycle", "bonding_mode", "created_at", "created_by", "customdata", "description", "facility", "firmware_set_id", "hardware_reservation", "hostname", "href", "id", "image_url", "ip_addresses", "ipxe_script_url", "iqn", "locked", "metro", "network_frozen", "network_ports", "operating_system", "plan", "project", "project_lite", "provisioning_events", "provisioning_percentage", "root_password", "short_id", "sos", "spot_instance", "spot_price_max", "ssh_keys", "state", "storage", "switch_uuid", "tags", "termination_time", "updated_at", "user", "userdata", "volumes"]

    @field_validator('state')
    def state_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['queued', 'provisioning', 'deprovisioning', 'reinstalling', 'active', 'inactive', 'failed', 'powering_on', 'powering_off', 'deleted']):
            raise ValueError("must be one of enum values ('queued', 'provisioning', 'deprovisioning', 'reinstalling', 'active', 'inactive', 'failed', 'powering_on', 'powering_off', 'deleted')")
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
        """Create an instance of Device from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in actions (list)
        _items = []
        if self.actions:
            for _item in self.actions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['actions'] = _items
        # override the default output from pydantic by calling `to_dict()` of created_by
        if self.created_by:
            _dict['created_by'] = self.created_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of facility
        if self.facility:
            _dict['facility'] = self.facility.to_dict()
        # override the default output from pydantic by calling `to_dict()` of hardware_reservation
        if self.hardware_reservation:
            _dict['hardware_reservation'] = self.hardware_reservation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in ip_addresses (list)
        _items = []
        if self.ip_addresses:
            for _item in self.ip_addresses:
                if _item:
                    _items.append(_item.to_dict())
            _dict['ip_addresses'] = _items
        # override the default output from pydantic by calling `to_dict()` of metro
        if self.metro:
            _dict['metro'] = self.metro.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in network_ports (list)
        _items = []
        if self.network_ports:
            for _item in self.network_ports:
                if _item:
                    _items.append(_item.to_dict())
            _dict['network_ports'] = _items
        # override the default output from pydantic by calling `to_dict()` of operating_system
        if self.operating_system:
            _dict['operating_system'] = self.operating_system.to_dict()
        # override the default output from pydantic by calling `to_dict()` of plan
        if self.plan:
            _dict['plan'] = self.plan.to_dict()
        # override the default output from pydantic by calling `to_dict()` of project
        if self.project:
            _dict['project'] = self.project.to_dict()
        # override the default output from pydantic by calling `to_dict()` of project_lite
        if self.project_lite:
            _dict['project_lite'] = self.project_lite.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in provisioning_events (list)
        _items = []
        if self.provisioning_events:
            for _item in self.provisioning_events:
                if _item:
                    _items.append(_item.to_dict())
            _dict['provisioning_events'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in ssh_keys (list)
        _items = []
        if self.ssh_keys:
            for _item in self.ssh_keys:
                if _item:
                    _items.append(_item.to_dict())
            _dict['ssh_keys'] = _items
        # override the default output from pydantic by calling `to_dict()` of storage
        if self.storage:
            _dict['storage'] = self.storage.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in volumes (list)
        _items = []
        if self.volumes:
            for _item in self.volumes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['volumes'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Device from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "actions": [DeviceActionsInner.from_dict(_item) for _item in obj["actions"]] if obj.get("actions") is not None else None,
            "always_pxe": obj.get("always_pxe"),
            "billing_cycle": obj.get("billing_cycle"),
            "bonding_mode": obj.get("bonding_mode"),
            "created_at": obj.get("created_at"),
            "created_by": DeviceCreatedBy.from_dict(obj["created_by"]) if obj.get("created_by") is not None else None,
            "customdata": obj.get("customdata"),
            "description": obj.get("description"),
            "facility": Facility.from_dict(obj["facility"]) if obj.get("facility") is not None else None,
            "firmware_set_id": obj.get("firmware_set_id"),
            "hardware_reservation": HardwareReservation.from_dict(obj["hardware_reservation"]) if obj.get("hardware_reservation") is not None else None,
            "hostname": obj.get("hostname"),
            "href": obj.get("href"),
            "id": obj.get("id"),
            "image_url": obj.get("image_url"),
            "ip_addresses": [IPAssignment.from_dict(_item) for _item in obj["ip_addresses"]] if obj.get("ip_addresses") is not None else None,
            "ipxe_script_url": obj.get("ipxe_script_url"),
            "iqn": obj.get("iqn"),
            "locked": obj.get("locked"),
            "metro": DeviceMetro.from_dict(obj["metro"]) if obj.get("metro") is not None else None,
            "network_frozen": obj.get("network_frozen"),
            "network_ports": [Port.from_dict(_item) for _item in obj["network_ports"]] if obj.get("network_ports") is not None else None,
            "operating_system": OperatingSystem.from_dict(obj["operating_system"]) if obj.get("operating_system") is not None else None,
            "plan": Plan.from_dict(obj["plan"]) if obj.get("plan") is not None else None,
            "project": Project.from_dict(obj["project"]) if obj.get("project") is not None else None,
            "project_lite": DeviceProjectLite.from_dict(obj["project_lite"]) if obj.get("project_lite") is not None else None,
            "provisioning_events": [Event.from_dict(_item) for _item in obj["provisioning_events"]] if obj.get("provisioning_events") is not None else None,
            "provisioning_percentage": obj.get("provisioning_percentage"),
            "root_password": obj.get("root_password"),
            "short_id": obj.get("short_id"),
            "sos": obj.get("sos"),
            "spot_instance": obj.get("spot_instance"),
            "spot_price_max": obj.get("spot_price_max"),
            "ssh_keys": [Href.from_dict(_item) for _item in obj["ssh_keys"]] if obj.get("ssh_keys") is not None else None,
            "state": obj.get("state"),
            "storage": Storage.from_dict(obj["storage"]) if obj.get("storage") is not None else None,
            "switch_uuid": obj.get("switch_uuid"),
            "tags": obj.get("tags"),
            "termination_time": obj.get("termination_time"),
            "updated_at": obj.get("updated_at"),
            "user": obj.get("user"),
            "userdata": obj.get("userdata"),
            "volumes": [Href.from_dict(_item) for _item in obj["volumes"]] if obj.get("volumes") is not None else None
        })
        return _obj

from equinix.services.metalv1.models.hardware_reservation import HardwareReservation
from equinix.services.metalv1.models.port import Port
# TODO: Rewrite to not use raise_errors
Device.model_rebuild(raise_errors=False)

