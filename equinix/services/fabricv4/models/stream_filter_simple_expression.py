# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)
"""

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class StreamFilterSimpleExpression(BaseModel):
    """
    StreamFilterSimpleExpression
    """ # noqa: E501
    var_property: Optional[StrictStr] = Field(default=None, description="Possible field names to use on filters:  * `/subject` - subject  * `/type` - type ", alias="property")
    operator: Optional[StrictStr] = Field(default=None, description="Possible operators to use on filters:  * `=` - equal  * `in` - in  * `LIKE` - case-sensitive like  * `ILIKE` - case-insensitive like ")
    values: Optional[List[StrictStr]] = Field(default=None, description="### Supported event or metric names to use on filters with property /type:   * `*` - all events or metrics   * `equinix.fabric.port.*` - port events or metrics   * `equinix.fabric.connection.*` - connection events or metrics   * `equinix.fabric.router.*` - cloud router events   * `equinix.fabric.metro.*` - metro metrics   * `equinix.fabric.network.*` - network events   * `equinix.fabric.service_token.*` - service token events   * `equinix.network_edge.*` - network edge events   * `equinix.network_edge.acl.*` - network edge acl events   * `equinix.network_edge.device.*` - network edge device events   * `equinix.access_manager.*` - identity access manager events   * `equinix.access_manager.user.role.*` - identity access manager user role events ### Supported event or metric names to use on filters with property /subject:   * `*` - all events or metrics   * `/fabric/v4/ports/<uuid>` - port events or metrics   * `/fabric/v4/connections/<uuid>` - connection events or metrics   * `/fabric/v4/routers/<uuid>` - cloud router events   * `/fabric/v4/metros/<metroCode>` - metro metrics   * `/fabric/v4/networks/<uuid>` - network events   * `/fabric/v4/tokens/<uuid>` - service token events   * `/ne/v1/acl/<uuid>` - network edge acl events   * `/ne/v1/devices/<uuid>` - network edge device events   * `/am/v2/users/<uuid>/roleAssignments/<uuid>` - identity access manager events ")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["property", "operator", "values"]

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
        """Create an instance of StreamFilterSimpleExpression from a JSON string"""
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
        """Create an instance of StreamFilterSimpleExpression from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "property": obj.get("property"),
            "operator": obj.get("operator"),
            "values": obj.get("values")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


