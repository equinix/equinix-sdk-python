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
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from equinix.services.fabricv4.models.fabric_cloud_router_price import FabricCloudRouterPrice
from equinix.services.fabricv4.models.ip_block_price import IpBlockPrice
from equinix.services.fabricv4.models.price_category import PriceCategory
from equinix.services.fabricv4.models.price_charge import PriceCharge
from equinix.services.fabricv4.models.price_term_length import PriceTermLength
from equinix.services.fabricv4.models.product_type import ProductType
from equinix.services.fabricv4.models.simplified_account import SimplifiedAccount
from equinix.services.fabricv4.models.virtual_connection_price import VirtualConnectionPrice
from equinix.services.fabricv4.models.virtual_port_price import VirtualPortPrice
from typing import Optional, Set
from typing_extensions import Self

class Price(BaseModel):
    """
    Price
    """ # noqa: E501
    href: Optional[StrictStr] = Field(default=None, description="An absolute URL that returns specified pricing data")
    type: Optional[ProductType] = None
    code: Optional[StrictStr] = Field(default=None, description="Equinix-assigned product code")
    name: Optional[StrictStr] = Field(default=None, description="Full product name")
    description: Optional[StrictStr] = Field(default=None, description="Product description")
    account: Optional[SimplifiedAccount] = None
    charges: Optional[List[PriceCharge]] = None
    currency: Optional[StrictStr] = Field(default=None, description="Product offering price currency")
    term_length: Optional[PriceTermLength] = Field(default=None, alias="termLength")
    catgory: Optional[PriceCategory] = None
    connection: Optional[VirtualConnectionPrice] = None
    ip_block: Optional[IpBlockPrice] = Field(default=None, alias="ipBlock")
    router: Optional[FabricCloudRouterPrice] = None
    port: Optional[VirtualPortPrice] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["href", "type", "code", "name", "description", "account", "charges", "currency", "termLength", "catgory", "connection", "ipBlock", "router", "port"]

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
        """Create an instance of Price from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of account
        if self.account:
            _dict['account'] = self.account.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in charges (list)
        _items = []
        if self.charges:
            for _item in self.charges:
                if _item:
                    _items.append(_item.to_dict())
            _dict['charges'] = _items
        # override the default output from pydantic by calling `to_dict()` of connection
        if self.connection:
            _dict['connection'] = self.connection.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ip_block
        if self.ip_block:
            _dict['ipBlock'] = self.ip_block.to_dict()
        # override the default output from pydantic by calling `to_dict()` of router
        if self.router:
            _dict['router'] = self.router.to_dict()
        # override the default output from pydantic by calling `to_dict()` of port
        if self.port:
            _dict['port'] = self.port.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Price from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "href": obj.get("href"),
            "type": obj.get("type"),
            "code": obj.get("code"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "account": SimplifiedAccount.from_dict(obj["account"]) if obj.get("account") is not None else None,
            "charges": [PriceCharge.from_dict(_item) for _item in obj["charges"]] if obj.get("charges") is not None else None,
            "currency": obj.get("currency"),
            "termLength": obj.get("termLength"),
            "catgory": obj.get("catgory"),
            "connection": VirtualConnectionPrice.from_dict(obj["connection"]) if obj.get("connection") is not None else None,
            "ipBlock": IpBlockPrice.from_dict(obj["ipBlock"]) if obj.get("ipBlock") is not None else None,
            "router": FabricCloudRouterPrice.from_dict(obj["router"]) if obj.get("router") is not None else None,
            "port": VirtualPortPrice.from_dict(obj["port"]) if obj.get("port") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


