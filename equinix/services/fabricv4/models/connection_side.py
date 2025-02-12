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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from equinix.services.fabricv4.models.access_point import AccessPoint
from equinix.services.fabricv4.models.connection_company_profile import ConnectionCompanyProfile
from equinix.services.fabricv4.models.connection_invitation import ConnectionInvitation
from equinix.services.fabricv4.models.connection_side_additional_info import ConnectionSideAdditionalInfo
from equinix.services.fabricv4.models.internet_access import InternetAccess
from equinix.services.fabricv4.models.service_token import ServiceToken
from typing import Optional, Set
from typing_extensions import Self

class ConnectionSide(BaseModel):
    """
    Connection configuration object for each side of multi-segment connection
    """ # noqa: E501
    service_token: Optional[ServiceToken] = Field(default=None, alias="serviceToken")
    access_point: Optional[AccessPoint] = Field(default=None, alias="accessPoint")
    internet_access: Optional[InternetAccess] = Field(default=None, alias="internetAccess")
    company_profile: Optional[ConnectionCompanyProfile] = Field(default=None, alias="companyProfile")
    invitation: Optional[ConnectionInvitation] = None
    additional_info: Optional[List[ConnectionSideAdditionalInfo]] = Field(default=None, description="Any additional information, which is not part of connection metadata or configuration", alias="additionalInfo")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["serviceToken", "accessPoint", "internetAccess", "companyProfile", "invitation", "additionalInfo"]

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
        """Create an instance of ConnectionSide from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of service_token
        if self.service_token:
            _dict['serviceToken'] = self.service_token.to_dict()
        # override the default output from pydantic by calling `to_dict()` of access_point
        if self.access_point:
            _dict['accessPoint'] = self.access_point.to_dict()
        # override the default output from pydantic by calling `to_dict()` of internet_access
        if self.internet_access:
            _dict['internetAccess'] = self.internet_access.to_dict()
        # override the default output from pydantic by calling `to_dict()` of company_profile
        if self.company_profile:
            _dict['companyProfile'] = self.company_profile.to_dict()
        # override the default output from pydantic by calling `to_dict()` of invitation
        if self.invitation:
            _dict['invitation'] = self.invitation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in additional_info (list)
        _items = []
        if self.additional_info:
            for _item_additional_info in self.additional_info:
                if _item_additional_info:
                    _items.append(_item_additional_info.to_dict())
            _dict['additionalInfo'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConnectionSide from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "serviceToken": ServiceToken.from_dict(obj["serviceToken"]) if obj.get("serviceToken") is not None else None,
            "accessPoint": AccessPoint.from_dict(obj["accessPoint"]) if obj.get("accessPoint") is not None else None,
            "internetAccess": InternetAccess.from_dict(obj["internetAccess"]) if obj.get("internetAccess") is not None else None,
            "companyProfile": ConnectionCompanyProfile.from_dict(obj["companyProfile"]) if obj.get("companyProfile") is not None else None,
            "invitation": ConnectionInvitation.from_dict(obj["invitation"]) if obj.get("invitation") is not None else None,
            "additionalInfo": [ConnectionSideAdditionalInfo.from_dict(_item) for _item in obj["additionalInfo"]] if obj.get("additionalInfo") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


