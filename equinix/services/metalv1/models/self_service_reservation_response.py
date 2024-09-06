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
from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from equinix.services.metalv1.models.create_self_service_reservation_request_period import CreateSelfServiceReservationRequestPeriod
from equinix.services.metalv1.models.self_service_reservation_item_response import SelfServiceReservationItemResponse
from typing import Optional, Set
from typing_extensions import Self

class SelfServiceReservationResponse(BaseModel):
    """
    SelfServiceReservationResponse
    """ # noqa: E501
    created_at: Optional[datetime] = None
    href: Optional[StrictStr] = None
    item: Optional[List[SelfServiceReservationItemResponse]] = None
    notes: Optional[StrictStr] = None
    organization: Optional[StrictStr] = None
    organization_id: Optional[StrictStr] = None
    period: Optional[CreateSelfServiceReservationRequestPeriod] = None
    project: Optional[StrictStr] = None
    project_id: Optional[StrictStr] = None
    start_date: Optional[datetime] = None
    status: Optional[StrictStr] = None
    total_cost: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["created_at", "href", "item", "notes", "organization", "organization_id", "period", "project", "project_id", "start_date", "status", "total_cost"]

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
        """Create an instance of SelfServiceReservationResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in item (list)
        _items = []
        if self.item:
            for _item in self.item:
                if _item:
                    _items.append(_item.to_dict())
            _dict['item'] = _items
        # override the default output from pydantic by calling `to_dict()` of period
        if self.period:
            _dict['period'] = self.period.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SelfServiceReservationResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in SelfServiceReservationResponse) in the input: " + _key)

        _obj = cls.model_validate({
            "created_at": obj.get("created_at"),
            "href": obj.get("href"),
            "item": [SelfServiceReservationItemResponse.from_dict(_item) for _item in obj["item"]] if obj.get("item") is not None else None,
            "notes": obj.get("notes"),
            "organization": obj.get("organization"),
            "organization_id": obj.get("organization_id"),
            "period": CreateSelfServiceReservationRequestPeriod.from_dict(obj["period"]) if obj.get("period") is not None else None,
            "project": obj.get("project"),
            "project_id": obj.get("project_id"),
            "start_date": obj.get("start_date"),
            "status": obj.get("status"),
            "total_cost": obj.get("total_cost")
        })
        return _obj


