from __future__ import annotations

from typing import Dict

import requests

# Import from submodules: the fabricv4 package root re-exports a model named
# Configuration that shadows the HTTP-client Configuration.
from equinix.services.fabricv4.api_client import ApiClient
from equinix.services.fabricv4.configuration import Configuration

from . import http_logging, utils
from .users import UserName

_clients: Dict[UserName, ApiClient] = {}


def _request_access_token(base_url: str, client_id: str, client_secret: str) -> str:
    response = requests.post(
        f"{base_url}/oauth2/v1/token",
        json={
            "client_id": client_id,
            "client_secret": client_secret,
            "grant_type": "client_credentials",
        },
        headers={"Content-Type": "application/json"},
        timeout=60,
    )
    response.raise_for_status()
    return response.json()["access_token"]


def generate(user_name: UserName) -> ApiClient:
    base_url = utils.env_url()
    user = utils.get_user_data(user_name)

    access_token = _request_access_token(base_url, user.client_id, user.client_secret)

    configuration = Configuration(host=base_url, access_token=access_token)
    api_client = ApiClient(configuration)
    http_logging.enable(api_client)

    _clients[user_name] = api_client
    return api_client


def get_api_client(user_name: UserName) -> ApiClient:
    if user_name in _clients:
        return _clients[user_name]
    return generate(user_name)
