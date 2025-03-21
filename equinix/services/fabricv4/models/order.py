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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class Order(BaseModel):
    """
    Order
    """ # noqa: E501
    purchase_order_number: Optional[StrictStr] = Field(default=None, description="Purchase order number", alias="purchaseOrderNumber")
    customer_reference_number: Optional[StrictStr] = Field(default=None, description="Customer reference number", alias="customerReferenceNumber")
    billing_tier: Optional[StrictStr] = Field(default=None, description="Billing tier for connection bandwidth", alias="billingTier")
    order_id: Optional[StrictStr] = Field(default=None, description="Order Identification", alias="orderId")
    order_number: Optional[StrictStr] = Field(default=None, description="Order Reference Number", alias="orderNumber")
    term_length: Optional[Annotated[int, Field(le=36, strict=True, ge=1)]] = Field(default=1, description="Term length in months, valid values are 1, 12, 24, 36 where 1 is the default value (for on-demand case).", alias="termLength")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["purchaseOrderNumber", "customerReferenceNumber", "billingTier", "orderId", "orderNumber", "termLength"]

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
        """Create an instance of Order from a JSON string"""
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
        """Create an instance of Order from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "purchaseOrderNumber": obj.get("purchaseOrderNumber"),
            "customerReferenceNumber": obj.get("customerReferenceNumber"),
            "billingTier": obj.get("billingTier"),
            "orderId": obj.get("orderId"),
            "orderNumber": obj.get("orderNumber"),
            "termLength": obj.get("termLength") if obj.get("termLength") is not None else 1
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


