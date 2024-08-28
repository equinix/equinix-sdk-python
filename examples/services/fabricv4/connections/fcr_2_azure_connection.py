import time
import os

from equinix.services.fabricv4 import CloudRouterPostRequest, ConnectionPostRequest, RoutingProtocolDirectType
from examples.services.fabricv4.utils import utils
from examples.services.fabricv4.cloud_router import cloud_router_management
from examples.services.fabricv4.connections import connection_management

if __name__ == "__main__":
    """
    Create a Fabric Cloud Router (FCR) using the Equinix Fabric API.
    """
    utils.pr_yellow('\nCreate Fabric Cloud Router')
    fcr_request = CloudRouterPostRequest(
        type="XF_ROUTER",
        name="fcrtoazurefcr_01",
        location={"metro_code": "DC"},
        package={"code": "STANDARD"},
        order={"purchase_order_number": "1-1453534"},
        project={"project_id": "12354863434345"},
        account={"account_number": 123456},
        notifications=[
            {
                "type": "ALL",
                "emails": [
                    "test@test.com"
                ]
            }
        ]
    )
    fcr_uuid = cloud_router_management.create_fcr(fcr_request)

    """
    Create a Fabric Cloud Router (FCR) to Azure Connection.
    """
    utils.pr_yellow('\nCreate Fabric Cloud Router to Azure Connection')
    fcr2azure_request = ConnectionPostRequest(
        type="IP_VC",
        name="fcr2azure_conn_python_01",
        bandwidth=50,
        aSide={
            "accessPoint": {
                "type": "CLOUD_ROUTER",
                "router": {
                    "uuid": fcr_uuid
                }
            }
        },
        zSide={
            "accessPoint": {
                "type": "SP",
                "profile": {
                    "type": "L2_PROFILE",
                    "uuid": "xxxx22-xxxx-xxxx-xxxx"
                },
                "authenticationKey":  os.getenv("AZURE_AUTH_KEY"),
                "location": {
                    "metroCode": "DC"
                },
                "peeringType": "PRIVATE"
            }
        },
        order={"purchaseOrderNumber": "1-129105284100"},
        project={"projectId": "124345345345345"},
        notifications=[
            {
                "type": "ALL",
                "emails": [
                    "panthersfcr@test.com"
                ]
            }
        ]
    )
    fcr2azure = connection_management.create_fcr_connection(fcr_uuid, fcr2azure_request)

    """
    Configures a routing protocol for a Fabric Cloud Router (FCR) to Azure connection identified by the provided 
    connection UUID.
    """
    utils.pr_yellow('\nConfigure Routing Protocol Detail by UUID')
    routing_protocol_request = RoutingProtocolDirectType(
        type="DIRECT",
        directIpv4={
            "equinixIfaceIp": 'ip'
        }
    )
    connection_management.configure_routing_protocol(fcr2azure, routing_protocol_request)

    """
    Retrieves the connection details for a Fabric Cloud Router (FCR) to Azure connection by its UUID.
    This method is primarily used to fetch detailed information about a specific connection between 
    a Fabric Cloud Router and Azure, using the connection's unique identifier (UUID). 
    """
    utils.pr_yellow('\nGet FCR2Azure Connection Details by UUID')
    time.sleep(120)
    connection_management.get_connection_details_by_uuid(fcr2azure)

    """
    Deletes a Fabric Cloud Router (FCR) to Azure connection.
    """
    utils.pr_yellow('\nDelete Fabric Cloud Router to Azure Connection')
    time.sleep(20)
    connection_management.delete_connection(fcr2azure)

    """
    Deletes a Fabric Cloud Router (FCR) with the specified UUID.
    """
    utils.pr_yellow('\nDelete Fabric Cloud Router')
    time.sleep(20)
    cloud_router_management.delete_fcr(fcr_uuid)
