from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Optional


class UserName(str, Enum):
    PANTHERS_FCR = "fcr"
    PANTHERS_FNV = "fnv"


@dataclass
class Resources:
    ports: List[str] = field(default_factory=list)
    connections: List[str] = field(default_factory=list)
    raw: Dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_json(cls, data: Optional[Dict[str, Any]]) -> "Resources":
        data = data or {}
        return cls(
            ports=list(data.get("ports") or []),
            connections=list(data.get("connections") or []),
            raw=data,
        )

    def get(self, name: str) -> list:
        return list(self.raw.get(name) or [])


@dataclass
class UserData:
    name: str
    client_id: str
    client_secret: str
    project_id: Optional[str] = None
    account_number: Optional[str] = None
    account_number_eia: Optional[str] = None
    ia_profile_uuid: Optional[str] = None
    resources: Resources = field(default_factory=Resources)

    @classmethod
    def from_json(cls, data: Dict[str, Any], name: Optional[str] = None) -> "UserData":
        def pick(*keys, default=None):
            for key in keys:
                if key in data:
                    return data[key]
            return default

        def str_or_none(v):
            return str(v) if v is not None else None

        return cls(
            name=name or pick("name"),
            client_id=pick("client_id", "clientId"),
            client_secret=pick("client_secret", "clientSecret"),
            project_id=pick("projectId", "project_id"),
            account_number=str_or_none(pick("accountNumber", "account_number")),
            account_number_eia=str_or_none(pick("accountNumberEIA", "account_number_eia")),
            ia_profile_uuid=pick("iaProfileUuid", "ia_profile_uuid"),
            resources=Resources.from_json(pick("resources")),
        )
