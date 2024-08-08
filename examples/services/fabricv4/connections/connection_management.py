import json
import time


from icecream import ic
from examples.services.fabricv4.utils import utils
from examples.services.fabricv4.oauth2 import configure_client_credentials
from examples.services import fabricv4
from equinix.services import fabricv4


def create_fcr_connection(fcr_uuid, fcr2colo_request):
    """
        Create a connection for a Fabric Cloud Router (FCR) within the Equinix Fabric environment.

        This method handles the process of establishing a connection between a Fabric Cloud Router (FCR) and a
        colocation or another FCR within the Equinix Fabric. It generates the connection request payload,
        sends the request to the Equinix Fabric API, and returns the unique identifier (UUID) of the created connection.

        Returns:
            str: The UUID of the newly created connection, which can be used for further operations like querying the connection
                 status, updating, or deleting the connection.

        Example Usage:
            fcr_uuid = "1234-abcd-5678-efgh"
            fcr2colo_request = FCRConnectionRequest(...)  # An instance of a request object with necessary attributes.
            connection_uuid = create_fcr_connection(fcr_uuid, fcr2colo_request)
            print(f"Created FCR Connection UUID: {connection_uuid}")
        """
    utils.pr_purple('\nFCR Connection Request Payload:\n')
    ic(fcr2colo_request.to_json())
    client = configure_client_credentials.get_equinix_fabric_client()
    connections = fabricv4.ConnectionsApi(client)
    response = dict(connections.create_connection(fcr2colo_request))
    pretty_json = json.dumps(response, indent=4, default=utils.custom_serializer)
    time.sleep(20)
    utils.pr_cyan('\nFCR Connection response\n')
    ic(pretty_json)
    utils.pr_cyan('\nfcr_conn_response = '+response['uuid'])
    return response['uuid']


def configure_routing_protocol(connection_uuid,routing_protocol_request):
    """
        Configures a routing protocol for a specified connection in the Equinix Fabric.

        This method sets up a routing protocol for the given connection UUID using the
        specified routing protocol request. The method leverages the Equinix Fabric API
        to create the routing protocol associated with the connection. The response from
        the API is formatted and printed for verification.

        This would configure a BGP routing protocol for the specified connection, using
        the provided ASNs and authentication key, and then print the response from the
        Equinix Fabric API.
        """
    rp_type = fabricv4.RoutingProtocolBase(routing_protocol_request)
    client = configure_client_credentials.get_equinix_fabric_client()
    routing_protocol = fabricv4.RoutingProtocolsApi(client)
    response = dict(routing_protocol.create_connection_routing_protocol(connection_uuid, rp_type))
    json_formatted_str = json.dumps(response, indent=4, default=utils.custom_serializer)
    time.sleep(15)
    ic('\nconfigure routing protocol = ', json_formatted_str)
    ic('\nrouting protocol configured successful\n')


def get_connection_details_by_uuid(fcr_uuid):
    """
        Retrieve connection details using the unique identifier (UUID) of a Fabric Cloud Router (FCR) connection.

        This method interacts with the Equinix Fabric API to fetch detailed information about a specific connection
        identified by its UUID. The response is then formatted into a JSON string for easier readability and logged
        for debugging purposes.
        """
    client = configure_client_credentials.get_equinix_fabric_client()
    cloudrouterapicall = fabricv4.ConnectionsApi(client)
    response = dict(cloudrouterapicall.get_connection_by_uuid(fcr_uuid))
    json_formatted_str = json.dumps(response, indent=4, default=utils.custom_serializer)
    time.sleep(15)
    ic('\nget connection details response = ', json_formatted_str)
    ic('\ngot connection details successful\n')


def update_connection_details_by_uuid(connection_uuid,update_payload):
    """
        Updates the details of an existing connection in Equinix Fabric using its UUID.

        This method sends an update request to the Equinix Fabric API to modify the details of a
        connection specified by its UUID. The updated details are provided through the update_payload
        parameter. After the update, the method formats the response into a JSON string and logs
        the updated connection details.
        """
    client = configure_client_credentials.get_equinix_fabric_client()
    cloudrouterapicall = fabricv4.ConnectionsApi(client)
    response = dict(cloudrouterapicall.update_connection_by_uuid(connection_uuid,update_payload))
    json_formatted_str = json.dumps(response, indent=4, default=utils.custom_serializer)
    time.sleep(15)
    ic('\nupdate connection details = ', json_formatted_str)
    ic('\nconnections details updated successful\n')


def delete_connection(con_uuid):
    """
        Deletes a connection from the Equinix Fabric using the connection UUID.

        This method interacts with the Equinix Fabric API to delete a specified connection.
        The method retrieves a configured client for the Equinix Fabric, utilizes the
        ConnectionsApi to perform the deletion, and then logs the response.
        """
    client = configure_client_credentials.get_equinix_fabric_client()
    connections = fabricv4.ConnectionsApi(client)
    response = connections.delete_connection_by_uuid_with_http_info(con_uuid).json
    pretty_json = json.dumps(response, indent=4, default=utils.custom_serializer)
    time.sleep(15)
    ic('\ndelete connection response = ', pretty_json)
    ic('\nConnection Deleted Successfully\n')
