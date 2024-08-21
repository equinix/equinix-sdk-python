import json
import time

from icecream import ic
from examples.services.fabricv4.utils import utils
from examples.services.fabricv4.oauth2 import configure_client_credentials
from examples.services import fabricv4
from equinix.services import fabricv4

"""
    Create a Fabric Cloud Router (FCR) using the provided request payload.
"""


def create_fcr(fcr_request):
    utils.pr_purple('\nCreate FCR request payload:\n')
    ic(fcr_request.to_json())
    client = configure_client_credentials.get_equinix_fabric_client()
    cloudrouterapicall = fabricv4.CloudRoutersApi(client)
    response = cloudrouterapicall.create_cloud_router(fcr_request).to_json()
    json_resp = json.loads(response)
    json_formatted_str = json.dumps(json_resp, sort_keys=True, indent=4)
    time.sleep(15)
    utils.pr_cyan('\nCloud router creation response\n')
    ic(json_formatted_str)
    utils.pr_cyan('\nconnection_uuid = ' + json_resp['uuid'])
    return json_resp['uuid']


"""
    Retrieve the details of an existing Fabric Cloud Router (FCR) by its UUID.
"""


def get_fcr_uuid(fcr_uuid):
    client = configure_client_credentials.get_equinix_fabric_client()
    cloudrouterapicall = fabricv4.CloudRoutersApi(client)
    response = cloudrouterapicall.get_cloud_router_by_uuid(fcr_uuid).to_json()
    json_resp = json.loads(response)
    json_formatted_str = json.dumps(json_resp, sort_keys=True, indent=4)
    time.sleep(15)
    ic('\nget FCR response = ', json_formatted_str)
    ic('\nFCR Get Successfully\n')


"""
    Update an existing Fabric Cloud Router (FCR) using the provided UUID and update payload.
"""


def update_fcr_by_uuid(fcr_uuid, update_payload):
    client = configure_client_credentials.get_equinix_fabric_client()
    cloudrouterapicall = fabricv4.CloudRoutersApi(client)
    response = cloudrouterapicall.update_cloud_router_by_uuid(fcr_uuid, update_payload).to_json()
    json_resp = json.loads(response)
    json_formatted_str = json.dumps(json_resp, sort_keys=True, indent=4)
    time.sleep(15)
    ic('\nupdate FCR response = ', json_formatted_str)
    ic('\nFCR updated Successfully\n')


"""
    Delete an existing Fabric Cloud Router (FCR) using the provided UUID.
"""


def delete_fcr(fcr_uuid):
    client = configure_client_credentials.get_equinix_fabric_client()
    cloudrouterapicall = fabricv4.CloudRoutersApi(client)
    response = cloudrouterapicall.delete_cloud_router_by_uuid(fcr_uuid)
    time.sleep(15)
    ic('\ndelete FCR response = ', response)
    ic('\nFCR Deleted Successfully\n')
