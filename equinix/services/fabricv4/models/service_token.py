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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from equinix.services.fabricv4.models.changelog import Changelog
from equinix.services.fabricv4.models.project import Project
from equinix.services.fabricv4.models.service_token_connection import ServiceTokenConnection
from equinix.services.fabricv4.models.service_token_state import ServiceTokenState
from equinix.services.fabricv4.models.service_token_type import ServiceTokenType
from equinix.services.fabricv4.models.simplified_account import SimplifiedAccount
from equinix.services.fabricv4.models.simplified_notification import SimplifiedNotification
from typing import Optional, Set
from typing_extensions import Self

class ServiceToken(BaseModel):
    """
    Create Service Tokens (v4) generates Equinix Fabric service tokens. These tokens authorize users to access protected resources and services. The tokens remove sensitive content from the environment, rather than just masking it, making the protected data impossible to unencrypt or decrypt. Resource owners can distribute the tokens to trusted partners and vendors, allowing selected third parties to work directly with Equinix network assets.
    """ # noqa: E501
    type: Optional[ServiceTokenType] = None
    href: Optional[StrictStr] = Field(default=None, description="An absolute URL that is the subject of the link's context.")
    expiry: Optional[StrictInt] = None
    uuid: Optional[StrictStr] = Field(default=None, description="Equinix-assigned service token identifier")
    issuer_side: Optional[StrictStr] = Field(default=None, description="information about token side", alias="issuerSide")
    name: Optional[StrictStr] = Field(default=None, description="Customer-provided service token name")
    description: Optional[StrictStr] = Field(default=None, description="Customer-provided service token description")
    expiration_date_time: Optional[datetime] = Field(default=None, description="Expiration date and time of the service token.", alias="expirationDateTime")
    connection: Optional[ServiceTokenConnection] = None
    state: Optional[ServiceTokenState] = None
    notifications: Optional[List[SimplifiedNotification]] = Field(default=None, description="Service token related notifications")
    account: Optional[SimplifiedAccount] = None
    changelog: Optional[Changelog] = None
    project: Optional[Project] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["type", "href", "expiry", "uuid", "issuerSide", "name", "description", "expirationDateTime", "connection", "state", "notifications", "account", "changelog", "project"]

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
        """Create an instance of ServiceToken from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "href",
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of connection
        if self.connection:
            _dict['connection'] = self.connection.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in notifications (list)
        _items = []
        if self.notifications:
            for _item_notifications in self.notifications:
                if _item_notifications:
                    _items.append(_item_notifications.to_dict())
            _dict['notifications'] = _items
        # override the default output from pydantic by calling `to_dict()` of account
        if self.account:
            _dict['account'] = self.account.to_dict()
        # override the default output from pydantic by calling `to_dict()` of changelog
        if self.changelog:
            _dict['changelog'] = self.changelog.to_dict()
        # override the default output from pydantic by calling `to_dict()` of project
        if self.project:
            _dict['project'] = self.project.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ServiceToken from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "href": obj.get("href"),
            "expiry": obj.get("expiry"),
            "uuid": obj.get("uuid"),
            "issuerSide": obj.get("issuerSide"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "expirationDateTime": obj.get("expirationDateTime"),
            "connection": ServiceTokenConnection.from_dict(obj["connection"]) if obj.get("connection") is not None else None,
            "state": obj.get("state"),
            "notifications": [SimplifiedNotification.from_dict(_item) for _item in obj["notifications"]] if obj.get("notifications") is not None else None,
            "account": SimplifiedAccount.from_dict(obj["account"]) if obj.get("account") is not None else None,
            "changelog": Changelog.from_dict(obj["changelog"]) if obj.get("changelog") is not None else None,
            "project": Project.from_dict(obj["project"]) if obj.get("project") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


