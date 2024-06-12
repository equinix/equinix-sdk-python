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
hardware_reservation_id = os.environ["METAL_HARDWARE_RESERVATION_ID"]


hwr_api = metalv1.HardwareReservationsApi(client)
resp = hwr_api.find_hardware_reservation_by_id(hardware_reservation_id)

print(resp)

