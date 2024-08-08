
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

       The method performs the following steps:
       1. Retrieves the `client_id` and `client_secret` from environment variables.
       2. Creates an `OAuth2Service` instance using the client credentials.
       3. Requests an access token using the `client_credentials` grant type.
       4. Configures the Equinix Fabric API client with the obtained access token.
       5. Returns the initialized `fabricv4.ApiClient` instance.

       Returns:
           fabricv4.ApiClient: An instance of `fabricv4.ApiClient` that is authenticated
           and ready to interact with the Equinix Fabric API.

       Raises:
           EnvironmentError: If the `EQUINIX_API_CLIENT_ID` or `EQUINIX_API_CLIENT_SECRET`
           environment variables are not set.
           OAuth2Error: If there is an error obtaining the access token from the OAuth2
           service.

       Example:
           To use this function, ensure that the environment variables are set and call
           it as follows:

           ```python
           client = get_equinix_fabric_client()
           # Now you can use `client` to interact with the Equinix Fabric API
           ```

       Note:
           This method is configured to work with the PROD (PRODUCTION)
           environment of the Equinix API. If you need to connect to a different
           environment, adjust the `access_token_url`, `authorize_url`, and `base_url`
           accordingly.

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