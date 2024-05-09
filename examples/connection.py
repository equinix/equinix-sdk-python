#!/usr/bin/env python3

# Example of hardware_reservation resource fetch

import os
import time

from equinix.services import metalv1


def get_equinix_metal_client(api_token):
    conf = metalv1.Configuration(
        host="https://api.equinix.com/metal/v1"
    )
    conf.api_key['x_auth_token'] = api_token
    conf.debug=  True
    return metalv1.ApiClient(conf)


client = get_equinix_metal_client(os.environ["METAL_AUTH_TOKEN"])


org_api = metalv1.InterconnectionsApi(client)
resp = org_api.project_list_interconnections_all_pages("126d9a9d-f425-47a8-97ad-537185b5bebe")

print(resp)

