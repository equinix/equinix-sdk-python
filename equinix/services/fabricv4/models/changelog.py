# coding: utf-8

"""
    Equinix Fabric API v4

    Equinix Fabric is an advanced software-defined interconnection solution that enables you to directly, securely and dynamically connect to distributed infrastructure and digital ecosystems on platform Equinix via a single port, Customers can use Fabric to connect to: </br> 1. Cloud Service Providers - Clouds, network and other service providers.  </br> 2. Enterprises - Other Equinix customers, vendors and partners.  </br> 3. Myself - Another customer instance deployed at Equinix. </br> </br> <b>Integrations (SDKs, Tools) links:</b> </br> <a href=\"https://deploy.equinix.com/labs/fabric-java\\\">Fabric Java SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-go\\\">Fabric Go SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-python\\\">Fabric Python SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-provider-equinix\\\">Equinix Terraform Provider</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-equinix-fabric\\\">Fabric Terraform Modules</a> </br> <a href=\"https://deploy.equinix.com/labs/pulumi-provider-equinix/\">Equinix Pulumi Provider</a> </br>

    The version of the OpenAPI document: 4.18
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class Changelog(BaseModel):
    """
    Change log
    """ # noqa: E501
    created_by: Optional[StrictStr] = Field(default=None, description="Created by User Key", alias="createdBy")
    created_by_full_name: Optional[StrictStr] = Field(default=None, description="Created by User Full Name", alias="createdByFullName")
    created_by_email: Optional[StrictStr] = Field(default=None, description="Created by User Email Address", alias="createdByEmail")
    created_date_time: Optional[datetime] = Field(default=None, description="Created by Date and Time", alias="createdDateTime")
    updated_by: Optional[StrictStr] = Field(default=None, description="Updated by User Key", alias="updatedBy")
    updated_by_full_name: Optional[StrictStr] = Field(default=None, description="Updated by User Full Name", alias="updatedByFullName")
    updated_by_email: Optional[StrictStr] = Field(default=None, description="Updated by User Email Address", alias="updatedByEmail")
    updated_date_time: Optional[datetime] = Field(default=None, description="Updated by Date and Time", alias="updatedDateTime")
    deleted_by: Optional[StrictStr] = Field(default=None, description="Deleted by User Key", alias="deletedBy")
    deleted_by_full_name: Optional[StrictStr] = Field(default=None, description="Deleted by User Full Name", alias="deletedByFullName")
    deleted_by_email: Optional[StrictStr] = Field(default=None, description="Deleted by User Email Address", alias="deletedByEmail")
    deleted_date_time: Optional[datetime] = Field(default=None, description="Deleted by Date and Time", alias="deletedDateTime")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["createdBy", "createdByFullName", "createdByEmail", "createdDateTime", "updatedBy", "updatedByFullName", "updatedByEmail", "updatedDateTime", "deletedBy", "deletedByFullName", "deletedByEmail", "deletedDateTime"]

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
        """Create an instance of Changelog from a JSON string"""
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
        """Create an instance of Changelog from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "createdBy": obj.get("createdBy"),
            "createdByFullName": obj.get("createdByFullName"),
            "createdByEmail": obj.get("createdByEmail"),
            "createdDateTime": obj.get("createdDateTime"),
            "updatedBy": obj.get("updatedBy"),
            "updatedByFullName": obj.get("updatedByFullName"),
            "updatedByEmail": obj.get("updatedByEmail"),
            "updatedDateTime": obj.get("updatedDateTime"),
            "deletedBy": obj.get("deletedBy"),
            "deletedByFullName": obj.get("deletedByFullName"),
            "deletedByEmail": obj.get("deletedByEmail"),
            "deletedDateTime": obj.get("deletedDateTime")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


