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
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class SimplifiedAccountPortResponse(BaseModel):
    """
    Temporary SimplifiedAccount for PortResponse data mismatch of all strings in account
    """ # noqa: E501
    account_number: Optional[StrictStr] = Field(default=None, description="Account number", alias="accountNumber")
    org_id: Optional[StrictStr] = Field(default=None, description="Customer organization identifier", alias="orgId")
    reseller_account_number: Optional[StrictStr] = Field(default=None, description="Reseller account number", alias="resellerAccountNumber")
    reseller_org_id: Optional[StrictStr] = Field(default=None, description="Reseller customer organization identifier", alias="resellerOrgId")
    account_name: Optional[StrictStr] = Field(default=None, description="Account name", alias="accountName")
    organization_name: Optional[StrictStr] = Field(default=None, description="Customer organization name", alias="organizationName")
    global_org_id: Optional[StrictStr] = Field(default=None, description="Global organization identifier", alias="globalOrgId")
    global_organization_name: Optional[StrictStr] = Field(default=None, description="Global organization name", alias="globalOrganizationName")
    ucm_id: Optional[StrictStr] = Field(default=None, description="Account ucmId", alias="ucmId")
    global_cust_id: Optional[StrictStr] = Field(default=None, description="Account name", alias="globalCustId")
    reseller_account_name: Optional[StrictStr] = Field(default=None, description="Reseller account name", alias="resellerAccountName")
    reseller_ucm_id: Optional[StrictStr] = Field(default=None, description="Reseller account ucmId", alias="resellerUcmId")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["accountNumber", "accountName", "orgId", "organizationName", "globalOrgId", "globalOrganizationName", "ucmId", "globalCustId", "resellerAccountNumber", "resellerAccountName", "resellerUcmId", "resellerOrgId"]

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
        """Create an instance of SimplifiedAccountPortResponse from a JSON string"""
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
        """Create an instance of SimplifiedAccountPortResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accountNumber": obj.get("accountNumber"),
            "accountName": obj.get("accountName"),
            "orgId": obj.get("orgId"),
            "organizationName": obj.get("organizationName"),
            "globalOrgId": obj.get("globalOrgId"),
            "globalOrganizationName": obj.get("globalOrganizationName"),
            "ucmId": obj.get("ucmId"),
            "globalCustId": obj.get("globalCustId"),
            "resellerAccountNumber": obj.get("resellerAccountNumber"),
            "resellerAccountName": obj.get("resellerAccountName"),
            "resellerUcmId": obj.get("resellerUcmId"),
            "resellerOrgId": obj.get("resellerOrgId")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


