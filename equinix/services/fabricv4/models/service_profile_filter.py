# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)
"""

from __future__ import annotations
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Optional
from equinix.services.fabricv4.models.service_profile_and_filter import ServiceProfileAndFilter
from equinix.services.fabricv4.models.service_profile_simple_expression import ServiceProfileSimpleExpression
from typing import Union, Any, List, Set, TYPE_CHECKING, Optional, Dict
from typing_extensions import Literal, Self
from pydantic import Field

SERVICEPROFILEFILTER_ANY_OF_SCHEMAS = ["ServiceProfileAndFilter", "ServiceProfileSimpleExpression"]

class ServiceProfileFilter(BaseModel):
    """
    ServiceProfileFilter
    """

    # data type: ServiceProfileSimpleExpression
    anyof_schema_1_validator: Optional[ServiceProfileSimpleExpression] = None
    # data type: ServiceProfileAndFilter
    anyof_schema_2_validator: Optional[ServiceProfileAndFilter] = None
    if TYPE_CHECKING:
        actual_instance: Optional[Union[ServiceProfileAndFilter, ServiceProfileSimpleExpression]] = None
    else:
        actual_instance: Any = None
    any_of_schemas: Set[str] = { "ServiceProfileAndFilter", "ServiceProfileSimpleExpression" }

    model_config = {
        "validate_assignment": True,
        "protected_namespaces": (),
    }

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_anyof(cls, v):
        instance = ServiceProfileFilter.model_construct()
        error_messages = []
        # validate data type: ServiceProfileSimpleExpression
        if not isinstance(v, ServiceProfileSimpleExpression):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ServiceProfileSimpleExpression`")
        else:
            return v

        # validate data type: ServiceProfileAndFilter
        if not isinstance(v, ServiceProfileAndFilter):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ServiceProfileAndFilter`")
        else:
            return v

        if error_messages:
            # no match
            raise ValueError("No match found when setting the actual_instance in ServiceProfileFilter with anyOf schemas: ServiceProfileAndFilter, ServiceProfileSimpleExpression. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Dict[str, Any]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        # anyof_schema_1_validator: Optional[ServiceProfileSimpleExpression] = None
        try:
            instance.actual_instance = ServiceProfileSimpleExpression.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_2_validator: Optional[ServiceProfileAndFilter] = None
        try:
            instance.actual_instance = ServiceProfileAndFilter.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))

        if error_messages:
            # no match
            raise ValueError("No match found when deserializing the JSON string into ServiceProfileFilter with anyOf schemas: ServiceProfileAndFilter, ServiceProfileSimpleExpression. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], ServiceProfileAndFilter, ServiceProfileSimpleExpression]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


