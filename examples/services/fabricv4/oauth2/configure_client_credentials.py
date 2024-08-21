
import os
import json

from rauth import OAuth2Service
from equinix.services import fabricv4


def get_equinix_fabric_client():
    """
       Initializes and returns an Equinix Fabric API client using OAuth2 authentication.

       This method is designed to authenticate with the Equinix Fabric API using OAuth2
       client credentials flow. It retrieves the client ID and client secret from the
       environment variables `EQUINIX_API_CLIENTID` and `EQUINIX_API_CLIENTSECRET`. These
       credentials are then used to obtain an OAuth2 access token, which is subsequently
       used to configure the Equinix Fabric API client.
       """

    client_id = os.getenv("EQUINIX_API_CLIENT_ID")
    client_secret = os.getenv("EQUINIX_API_CLIENT_SECRET")

    oauth2_service = OAuth2Service(
        name="Fabricv4",
        client_id=client_id,
        client_secret=client_secret,
        access_token_url="https://api.equinix.com/oauth2/v1/token",
        authorize_url="https://api.equinix.com/oauth2/v1/token",
        base_url="https://api.equinix.com/",
    )

    data = {
        'code': 'Fabricv4',  # specific to my app
        'grant_type': 'client_credentials',  # generally required!
    }

    oauth2_session = oauth2_service.get_auth_session(data=data, decoder=json.loads)
    conf = fabricv4.Configuration(
        host="https://api.equinix.com/",
    )

    conf.access_token = oauth2_session.access_token
    return fabricv4.ApiClient(conf)