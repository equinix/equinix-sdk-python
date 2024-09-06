# coding: utf-8

"""
    Metal API

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from equinix.services.metalv1.models.ip_assignment import IPAssignment
from equinix.services.metalv1.models.ip_reservation import IPReservation
from equinix.services.metalv1.models.vrf_ip_reservation import VrfIpReservation
from pydantic import StrictStr, Field
from typing import Union, List, Optional, Dict
from typing_extensions import Literal, Self

FINDIPADDRESSBYID200RESPONSE_ONE_OF_SCHEMAS = ["IPAssignment", "IPReservation", "VrfIpReservation"]

class FindIPAddressById200Response(BaseModel):
    """
    FindIPAddressById200Response
    """
    # data type: IPAssignment
    oneof_schema_1_validator: Optional[IPAssignment] = None
    # data type: IPReservation
    oneof_schema_2_validator: Optional[IPReservation] = None
    # data type: VrfIpReservation
    oneof_schema_3_validator: Optional[VrfIpReservation] = None
    actual_instance: Optional[Union[IPAssignment, IPReservation, VrfIpReservation]] = None
    one_of_schemas: List[str] = Field(default=Literal["IPAssignment", "IPReservation", "VrfIpReservation"])

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


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
    def actual_instance_must_validate_oneof(cls, v):
        instance = FindIPAddressById200Response.model_construct()
        error_messages = []
        match = 0
        # validate data type: IPAssignment
        if not isinstance(v, IPAssignment):
            error_messages.append(f"Error! Input type `{type(v)}` is not `IPAssignment`")
        else:
            match += 1
        # validate data type: IPReservation
        if not isinstance(v, IPReservation):
            error_messages.append(f"Error! Input type `{type(v)}` is not `IPReservation`")
        else:
            match += 1
        # validate data type: VrfIpReservation
        if not isinstance(v, VrfIpReservation):
            error_messages.append(f"Error! Input type `{type(v)}` is not `VrfIpReservation`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in FindIPAddressById200Response with oneOf schemas: IPAssignment, IPReservation, VrfIpReservation. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in FindIPAddressById200Response with oneOf schemas: IPAssignment, IPReservation, VrfIpReservation. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into IPAssignment
        try:
            instance.actual_instance = IPAssignment.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into IPReservation
        try:
            instance.actual_instance = IPReservation.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into VrfIpReservation
        try:
            instance.actual_instance = VrfIpReservation.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into FindIPAddressById200Response with oneOf schemas: IPAssignment, IPReservation, VrfIpReservation. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into FindIPAddressById200Response with oneOf schemas: IPAssignment, IPReservation, VrfIpReservation. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Optional[Union[Dict[str, Any], IPAssignment, IPReservation, VrfIpReservation]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


