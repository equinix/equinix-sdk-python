# coding: utf-8

"""
    Equinix Fabric API v4

    Equinix Fabric is an advanced software-defined interconnection solution that enables you to directly, securely and dynamically connect to distributed infrastructure and digital ecosystems on platform Equinix via a single port, Customers can use Fabric to connect to: </br> 1. Cloud Service Providers - Clouds, network and other service providers.  </br> 2. Enterprises - Other Equinix customers, vendors and partners.  </br> 3. Myself - Another customer instance deployed at Equinix. </br> </br> <b>Integrations (SDKs, Tools) links:</b> </br> <a href=\"https://deploy.equinix.com/labs/fabric-java\\\">Fabric Java SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-go\\\">Fabric Go SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-python\\\">Fabric Python SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-provider-equinix\\\">Equinix Terraform Provider</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-equinix-fabric\\\">Fabric Terraform Modules</a> </br> <a href=\"https://deploy.equinix.com/labs/pulumi-provider-equinix/\">Equinix Pulumi Provider</a> </br>

    The version of the OpenAPI document: 4.20
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from equinix.services.fabricv4.models.changelog import Changelog
from equinix.services.fabricv4.models.stream_subscription_filter import StreamSubscriptionFilter
from equinix.services.fabricv4.models.stream_subscription_selector import StreamSubscriptionSelector
from equinix.services.fabricv4.models.stream_subscription_sink import StreamSubscriptionSink
from equinix.services.fabricv4.models.stream_subscription_state import StreamSubscriptionState
from equinix.services.fabricv4.models.stream_subscription_type import StreamSubscriptionType
from typing import Optional, Set
from typing_extensions import Self

class StreamSubscription(BaseModel):
    """
    Stream Subscription object
    """ # noqa: E501
    href: Optional[StrictStr] = Field(default=None, description="Stream Subscription URI")
    uuid: Optional[StrictStr] = Field(default=None, description="Equinix-assigned access point identifier")
    type: Optional[StreamSubscriptionType] = None
    name: Optional[StrictStr] = Field(default=None, description="Customer-provided subscription name")
    description: Optional[StrictStr] = Field(default=None, description="Customer-provided subscription description")
    state: Optional[StreamSubscriptionState] = None
    enabled: Optional[StrictBool] = Field(default=None, description="Stream subscription enabled status")
    filters: Optional[StreamSubscriptionFilter] = None
    metric_selector: Optional[StreamSubscriptionSelector] = Field(default=None, alias="metricSelector")
    event_selector: Optional[StreamSubscriptionSelector] = Field(default=None, alias="eventSelector")
    sink: Optional[StreamSubscriptionSink] = None
    change_log: Optional[Changelog] = Field(default=None, alias="changeLog")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["href", "uuid", "type", "name", "description", "state", "enabled", "filters", "metricSelector", "eventSelector", "sink", "changeLog"]

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
        """Create an instance of StreamSubscription from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of filters
        if self.filters:
            _dict['filters'] = self.filters.to_dict()
        # override the default output from pydantic by calling `to_dict()` of metric_selector
        if self.metric_selector:
            _dict['metricSelector'] = self.metric_selector.to_dict()
        # override the default output from pydantic by calling `to_dict()` of event_selector
        if self.event_selector:
            _dict['eventSelector'] = self.event_selector.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sink
        if self.sink:
            _dict['sink'] = self.sink.to_dict()
        # override the default output from pydantic by calling `to_dict()` of change_log
        if self.change_log:
            _dict['changeLog'] = self.change_log.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of StreamSubscription from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "href": obj.get("href"),
            "uuid": obj.get("uuid"),
            "type": obj.get("type"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "state": obj.get("state"),
            "enabled": obj.get("enabled"),
            "filters": StreamSubscriptionFilter.from_dict(obj["filters"]) if obj.get("filters") is not None else None,
            "metricSelector": StreamSubscriptionSelector.from_dict(obj["metricSelector"]) if obj.get("metricSelector") is not None else None,
            "eventSelector": StreamSubscriptionSelector.from_dict(obj["eventSelector"]) if obj.get("eventSelector") is not None else None,
            "sink": StreamSubscriptionSink.from_dict(obj["sink"]) if obj.get("sink") is not None else None,
            "changeLog": Changelog.from_dict(obj["changeLog"]) if obj.get("changeLog") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


