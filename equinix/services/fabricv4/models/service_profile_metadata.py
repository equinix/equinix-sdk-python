# coding: utf-8

"""
    Equinix Fabric API v4

    Equinix Fabric is an advanced software-defined interconnection solution that enables you to directly, securely and dynamically connect to distributed infrastructure and digital ecosystems on platform Equinix via a single port, Customers can use Fabric to connect to: </br> 1. Cloud Service Providers - Clouds, network and other service providers.  </br> 2. Enterprises - Other Equinix customers, vendors and partners.  </br> 3. Myself - Another customer instance deployed at Equinix. </br> </br> <b>Integrations (SDKs, Tools) links:</b> </br> <a href=\"https://deploy.equinix.com/labs/fabric-java\\\">Fabric Java SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-go\\\">Fabric Go SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/equinix-sdk-python\\\">Fabric Python SDK</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-provider-equinix\\\">Equinix Terraform Provider</a> </br> <a href=\"https://deploy.equinix.com/labs/terraform-equinix-fabric\\\">Fabric Terraform Modules</a> </br> <a href=\"https://deploy.equinix.com/labs/pulumi-provider-equinix/\">Equinix Pulumi Provider</a> </br>

    The version of the OpenAPI document: 4.17
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ServiceProfileMetadata(BaseModel):
    """
    Metadata. Response attribute. Ignored on request payload.
    """ # noqa: E501
    props: Optional[StrictStr] = None
    reg_ex: Optional[StrictStr] = Field(default=None, alias="regEx")
    reg_ex_msg: Optional[StrictStr] = Field(default=None, alias="regExMsg")
    vlan_range_max_value: Optional[StrictInt] = Field(default=None, alias="vlanRangeMaxValue")
    vlan_range_min_value: Optional[StrictInt] = Field(default=None, alias="vlanRangeMinValue")
    max_qinq: Optional[StrictStr] = Field(default=None, alias="maxQinq")
    max_dot1q: Optional[StrictInt] = Field(default=None, alias="maxDot1q")
    variable_billing: Optional[StrictBool] = Field(default=None, alias="variableBilling")
    global_organization: Optional[StrictStr] = Field(default=None, alias="globalOrganization")
    limit_auth_key_conn: Optional[StrictBool] = Field(default=None, alias="limitAuthKeyConn")
    allow_secondary_location: Optional[StrictBool] = Field(default=None, alias="allowSecondaryLocation")
    redundant_profile_id: Optional[StrictStr] = Field(default=None, alias="redundantProfileId")
    allow_vc_migration: Optional[StrictBool] = Field(default=None, alias="allowVcMigration")
    connection_editable: Optional[StrictBool] = Field(default=None, alias="connectionEditable")
    release_vlan: Optional[StrictBool] = Field(default=None, alias="releaseVlan")
    max_connections_on_port: Optional[StrictInt] = Field(default=None, alias="maxConnectionsOnPort")
    port_assignment_strategy: Optional[StrictStr] = Field(default=None, alias="portAssignmentStrategy")
    eqx_managed_port: Optional[StrictBool] = Field(default=None, alias="eqxManagedPort")
    connection_name_editable: Optional[StrictBool] = Field(default=None, alias="connectionNameEditable")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["props", "regEx", "regExMsg", "vlanRangeMaxValue", "vlanRangeMinValue", "maxQinq", "maxDot1q", "variableBilling", "globalOrganization", "limitAuthKeyConn", "allowSecondaryLocation", "redundantProfileId", "allowVcMigration", "connectionEditable", "releaseVlan", "maxConnectionsOnPort", "portAssignmentStrategy", "eqxManagedPort", "connectionNameEditable"]

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
        """Create an instance of ServiceProfileMetadata from a JSON string"""
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
        """Create an instance of ServiceProfileMetadata from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "props": obj.get("props"),
            "regEx": obj.get("regEx"),
            "regExMsg": obj.get("regExMsg"),
            "vlanRangeMaxValue": obj.get("vlanRangeMaxValue"),
            "vlanRangeMinValue": obj.get("vlanRangeMinValue"),
            "maxQinq": obj.get("maxQinq"),
            "maxDot1q": obj.get("maxDot1q"),
            "variableBilling": obj.get("variableBilling"),
            "globalOrganization": obj.get("globalOrganization"),
            "limitAuthKeyConn": obj.get("limitAuthKeyConn"),
            "allowSecondaryLocation": obj.get("allowSecondaryLocation"),
            "redundantProfileId": obj.get("redundantProfileId"),
            "allowVcMigration": obj.get("allowVcMigration"),
            "connectionEditable": obj.get("connectionEditable"),
            "releaseVlan": obj.get("releaseVlan"),
            "maxConnectionsOnPort": obj.get("maxConnectionsOnPort"),
            "portAssignmentStrategy": obj.get("portAssignmentStrategy"),
            "eqxManagedPort": obj.get("eqxManagedPort"),
            "connectionNameEditable": obj.get("connectionNameEditable")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


