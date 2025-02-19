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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from equinix.services.fabricv4.models.ptp_advance_configuration_log_announce_interval import PtpAdvanceConfigurationLogAnnounceInterval
from equinix.services.fabricv4.models.ptp_advance_configuration_log_delay_req_interval import PtpAdvanceConfigurationLogDelayReqInterval
from equinix.services.fabricv4.models.ptp_advance_configuration_log_sync_interval import PtpAdvanceConfigurationLogSyncInterval
from equinix.services.fabricv4.models.ptp_advance_configuration_time_scale import PtpAdvanceConfigurationTimeScale
from equinix.services.fabricv4.models.ptp_advance_configuration_transport_mode import PtpAdvanceConfigurationTransportMode
from typing import Optional, Set
from typing_extensions import Self

class PtpAdvanceConfiguration(BaseModel):
    """
    PTP Advanced Configuration.
    """ # noqa: E501
    time_scale: Optional[PtpAdvanceConfigurationTimeScale] = Field(default=None, alias="timeScale")
    domain: Optional[Annotated[int, Field(le=127, strict=True, ge=0)]] = Field(default=None, description="The PTP domain value.")
    priority1: Optional[Annotated[int, Field(le=248, strict=True, ge=0)]] = Field(default=None, description="The priority1 value determines the best primary clock, Lower value indicates higher priority.")
    priority2: Optional[Annotated[int, Field(le=248, strict=True, ge=0)]] = Field(default=None, description="The priority2 value differentiates and prioritizes the primary clock to avoid confusion when priority1-value is the same for different primary clocks in a network.")
    log_announce_interval: Optional[PtpAdvanceConfigurationLogAnnounceInterval] = Field(default=None, alias="logAnnounceInterval")
    log_sync_interval: Optional[PtpAdvanceConfigurationLogSyncInterval] = Field(default=None, alias="logSyncInterval")
    log_delay_req_interval: Optional[PtpAdvanceConfigurationLogDelayReqInterval] = Field(default=None, alias="logDelayReqInterval")
    transport_mode: Optional[PtpAdvanceConfigurationTransportMode] = Field(default=None, alias="transportMode")
    grant_time: Optional[Annotated[int, Field(le=7200, strict=True, ge=30)]] = Field(default=None, description="Unicast Grant Time in seconds. For Multicast and Hybrid transport modes, grant time defaults to 300 seconds. For Unicast mode, grant time can be between 30 to 7200.", alias="grantTime")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["timeScale", "domain", "priority1", "priority2", "logAnnounceInterval", "logSyncInterval", "logDelayReqInterval", "transportMode", "grantTime"]

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
        """Create an instance of PtpAdvanceConfiguration from a JSON string"""
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
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PtpAdvanceConfiguration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "timeScale": obj.get("timeScale"),
            "domain": obj.get("domain"),
            "priority1": obj.get("priority1"),
            "priority2": obj.get("priority2"),
            "logAnnounceInterval": obj.get("logAnnounceInterval"),
            "logSyncInterval": obj.get("logSyncInterval"),
            "logDelayReqInterval": obj.get("logDelayReqInterval"),
            "transportMode": obj.get("transportMode"),
            "grantTime": obj.get("grantTime")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


