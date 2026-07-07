from __future__ import annotations

import json
import os
import random
from functools import lru_cache
from pathlib import Path
from typing import Dict, Optional

from .users import UserData, UserName

TEST_DATA_ENV_VAR = "TEST_DATA_UAT_USERS"
TEST_DATA_FILE_VAR = "TEST_DATA_FILE"
ENV_URL_VAR = "ENV_URL"
DEFAULT_DATA_FILES = ("env.json", "file.json")

_REPO_ROOT = Path(__file__).resolve().parents[4]


def data_file_path() -> Optional[Path]:
    explicit = os.getenv(TEST_DATA_FILE_VAR)
    if explicit:
        path = Path(explicit)
        return path if path.is_file() else None
    for base in (Path.cwd(), _REPO_ROOT):
        for name in DEFAULT_DATA_FILES:
            candidate = base / name
            if candidate.is_file():
                return candidate
    return None


@lru_cache(maxsize=1)
def _load_document() -> dict:
    raw = os.getenv(TEST_DATA_ENV_VAR)
    if raw:
        return json.loads(raw)
    path = data_file_path()
    if path is not None:
        return json.loads(path.read_text())
    raise RuntimeError(
        f"No test data found. Set {TEST_DATA_ENV_VAR}, or provide a JSON file "
        f"(one of {DEFAULT_DATA_FILES} in the repo root, or {TEST_DATA_FILE_VAR})."
    )


def test_data_available() -> bool:
    return bool(os.getenv(TEST_DATA_ENV_VAR)) or data_file_path() is not None


def env_url() -> str:
    url = os.getenv(ENV_URL_VAR)
    if not url and test_data_available():
        doc = _load_document()
        url = doc.get("envUrl") or doc.get("env_url") or doc.get(ENV_URL_VAR)
    if not url:
        raise RuntimeError(
            f"No base URL set. Provide {ENV_URL_VAR} (e.g. https://api.equinix.com) "
            f"or an 'envUrl' key in the test-data document."
        )
    return url.rstrip("/")


def env_url_available() -> bool:
    try:
        return bool(env_url())
    except RuntimeError:
        return False


_META_KEYS = {ENV_URL_VAR, "envUrl", "env_url"}


def _as_dict(value):
    if isinstance(value, str):
        value = json.loads(value)
    return value


@lru_cache(maxsize=1)
def _load_users() -> Dict[str, UserData]:
    document = _load_document()

    if isinstance(document, list) or "users" in document:
        users = document.get("users", document) if isinstance(document, dict) else document
        users = _as_dict(users)
        if isinstance(users, dict):
            users = users.get("users", [])
        return {u["name"]: UserData.from_json(u) for u in users}

    result: Dict[str, UserData] = {}
    for name, value in document.items():
        if name in _META_KEYS:
            continue
        entry = _as_dict(value)
        if isinstance(entry, dict):
            result[name] = UserData.from_json(entry, name=name)
    return result


def get_user_data(user_name: UserName) -> UserData:
    users = _load_users()
    try:
        return users[user_name.value]
    except KeyError as exc:
        raise LookupError(
            f"User '{user_name.value}' not found in test data "
            f"(available: {sorted(users)})"
        ) from exc


def get_random_vlan_number() -> int:
    return random.randint(1, 3999)
