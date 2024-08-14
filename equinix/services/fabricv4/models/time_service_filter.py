# coding: utf-8

"""
    Equinix Fabric API v4

    Equinix Fabric is an advanced software-defined interconnection solution that enables you to directly, securely and dynamically connect to distributed infrastructure and digital ecosystems on platform Equinix via a single port, Customers can use Fabric to connect to: </br> 1. Cloud Service Providers - Clouds, network and other service providers.  </br> 2. Enterprises - Other Equinix customers, vendors and partners.  </br> 3. Myself - Another customer instance deployed at Equinix. </br> </br> <b>Integrations (SDKs, Tools) links:</b> </br> <a href=\"https://deploy.equinix.com/labs/fabric-java\\\">Fabric Java SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-go\\\">Fabric Go SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-provider-equinix\\\">Equinix Terraform Provider</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-equinix-fabric\\\">Fabric Terraform Modules</a> </br> <a href=\"https://deploy.equinix.com/labs/pulumi-provider-equinix/\">Equinix Pulumi Provider</a> </br>

    The version of the OpenAPI document: 4.15
    Contact: api-support@equinix.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Optional
from equinix.services.fabricv4.models.time_service_or_filter import TimeServiceOrFilter
from equinix.services.fabricv4.models.time_service_simple_expression import TimeServiceSimpleExpression
from typing import Union, Any, List, TYPE_CHECKING, Optional, Dict
from typing_extensions import Literal, Self
from pydantic import Field

TIMESERVICEFILTER_ANY_OF_SCHEMAS = ["TimeServiceOrFilter", "TimeServiceSimpleExpression"]

class TimeServiceFilter(BaseModel):
    """
    TimeServiceFilter
    """

    # data type: TimeServiceSimpleExpression
    anyof_schema_1_validator: Optional[TimeServiceSimpleExpression] = None
    # data type: TimeServiceOrFilter
    anyof_schema_2_validator: Optional[TimeServiceOrFilter] = None
    if TYPE_CHECKING:
        actual_instance: Optional[Union[TimeServiceOrFilter, TimeServiceSimpleExpression]] = None
    else:
        actual_instance: Any = None
    any_of_schemas: List[str] = Field(default=Literal["TimeServiceOrFilter", "TimeServiceSimpleExpression"])

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
        instance = TimeServiceFilter.model_construct()
        error_messages = []
        # validate data type: TimeServiceSimpleExpression
        if not isinstance(v, TimeServiceSimpleExpression):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TimeServiceSimpleExpression`")
        else:
            return v

        # validate data type: TimeServiceOrFilter
        if not isinstance(v, TimeServiceOrFilter):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TimeServiceOrFilter`")
        else:
            return v

        if error_messages:
            # no match
            raise ValueError("No match found when setting the actual_instance in TimeServiceFilter with anyOf schemas: TimeServiceOrFilter, TimeServiceSimpleExpression. Details: " + ", ".join(error_messages))
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
        # anyof_schema_1_validator: Optional[TimeServiceSimpleExpression] = None
        try:
            instance.actual_instance = TimeServiceSimpleExpression.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_2_validator: Optional[TimeServiceOrFilter] = None
        try:
            instance.actual_instance = TimeServiceOrFilter.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))

        if error_messages:
            # no match
            raise ValueError("No match found when deserializing the JSON string into TimeServiceFilter with anyOf schemas: TimeServiceOrFilter, TimeServiceSimpleExpression. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Optional[Union[Dict[str, Any], TimeServiceOrFilter, TimeServiceSimpleExpression]]:
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


