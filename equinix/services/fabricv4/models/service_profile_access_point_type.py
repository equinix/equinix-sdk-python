# coding: utf-8

"""
    Equinix Fabric API v4

    Equinix Fabric is an advanced software-defined interconnection solution that enables you to directly, securely and dynamically connect to distributed infrastructure and digital ecosystems on platform Equinix via a single port, Customers can use Fabric to connect to: </br> 1. Cloud Service Providers - Clouds, network and other service providers.  </br> 2. Enterprises - Other Equinix customers, vendors and partners.  </br> 3. Myself - Another customer instance deployed at Equinix. </br> </br> <b>Integrations (SDKs, Tools) links:</b> </br> <a href=\"https://deploy.equinix.com/labs/fabric-java\\\">Fabric Java SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-go\\\">Fabric Go SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-provider-equinix\\\">Equinix Terraform Provider</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-equinix-fabric\\\">Fabric Terraform Modules</a> </br> <a href=\"https://deploy.equinix.com/labs/pulumi-provider-equinix/\">Equinix Pulumi Provider</a> </br>

    The version of the OpenAPI document: 4.14
    Contact: api-support@equinix.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from equinix.services.fabricv4.models.service_profile_access_point_type_colo import ServiceProfileAccessPointTypeCOLO
from equinix.services.fabricv4.models.service_profile_access_point_type_vd import ServiceProfileAccessPointTypeVD
from pydantic import StrictStr, Field
from typing import Union, List, Optional, Dict
from typing_extensions import Literal, Self

SERVICEPROFILEACCESSPOINTTYPE_ONE_OF_SCHEMAS = ["ServiceProfileAccessPointTypeCOLO", "ServiceProfileAccessPointTypeVD"]

class ServiceProfileAccessPointType(BaseModel):
    """
    Access Point Type
    """
    # data type: ServiceProfileAccessPointTypeCOLO
    oneof_schema_1_validator: Optional[ServiceProfileAccessPointTypeCOLO] = None
    # data type: ServiceProfileAccessPointTypeVD
    oneof_schema_2_validator: Optional[ServiceProfileAccessPointTypeVD] = None
    actual_instance: Optional[Union[ServiceProfileAccessPointTypeCOLO, ServiceProfileAccessPointTypeVD]] = None
    one_of_schemas: List[str] = Field(default=Literal["ServiceProfileAccessPointTypeCOLO", "ServiceProfileAccessPointTypeVD"])

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
        instance = ServiceProfileAccessPointType.model_construct()
        error_messages = []
        match = 0
        # validate data type: ServiceProfileAccessPointTypeCOLO
        if not isinstance(v, ServiceProfileAccessPointTypeCOLO):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ServiceProfileAccessPointTypeCOLO`")
        else:
            match += 1
        # validate data type: ServiceProfileAccessPointTypeVD
        if not isinstance(v, ServiceProfileAccessPointTypeVD):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ServiceProfileAccessPointTypeVD`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in ServiceProfileAccessPointType with oneOf schemas: ServiceProfileAccessPointTypeCOLO, ServiceProfileAccessPointTypeVD. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in ServiceProfileAccessPointType with oneOf schemas: ServiceProfileAccessPointTypeCOLO, ServiceProfileAccessPointTypeVD. Details: " + ", ".join(error_messages))
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

        # deserialize data into ServiceProfileAccessPointTypeCOLO
        try:
            instance.actual_instance = ServiceProfileAccessPointTypeCOLO.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ServiceProfileAccessPointTypeVD
        try:
            instance.actual_instance = ServiceProfileAccessPointTypeVD.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into ServiceProfileAccessPointType with oneOf schemas: ServiceProfileAccessPointTypeCOLO, ServiceProfileAccessPointTypeVD. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into ServiceProfileAccessPointType with oneOf schemas: ServiceProfileAccessPointTypeCOLO, ServiceProfileAccessPointTypeVD. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Optional[Union[Dict[str, Any], ServiceProfileAccessPointTypeCOLO, ServiceProfileAccessPointTypeVD]]:
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


