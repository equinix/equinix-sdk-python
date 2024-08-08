import time
import os

from examples.services.fabricv4.utils import utils
from equinix.services import fabricv4 as module
from examples.services.fabricv4.cloud_router import cloud_router_management
from examples.services.fabricv4.connections import connection_management

if __name__ == "__main__":
    """
        Create a Fabric Cloud Router (FCR) using the Equinix Fabric API.
    
        This method sends a request to create a new Fabric Cloud Router with specified configurations 
        such as router type, name, location, package, and associated project and account details. 
        Notifications are also configured to receive updates regarding the router.
    
        Construct a `CloudRouterPostRequest` object using the `module.CloudRouterPostRequest` class.
        This object contains the details required to create the Fabric Cloud Router.
        """
    utils.pr_yellow('\nCreate Fabric Cloud Router')
    fcr_request = module.CloudRouterPostRequest(
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

        This method creates a connection from an Equinix Fabric Cloud Router (FCR) to an Azure service provider using 
        the Equinix API. The connection is established by specifying various parameters such as connection type, 
        bandwidth, redundancy priority, and the details of both the A-side (Cloud Router) and Z-side (Azure service 
        provider).
        """
    utils.pr_yellow('\nCreate Fabric Cloud Router to Azure Connection')
    fcr2azure_request = module.ConnectionPostRequest(
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

    """Configures a routing protocol for a Fabric Cloud Router (FCR) to Azure connection identified by the provided 
    connection UUID.

        This method is designed to configure the routing protocol details for an existing connection between a Fabric 
        Cloud Router and Azure. It uses the `connection_uuid` to identify the connection and applies the specified 
        routing protocol settings.

        The routing protocol configuration includes the following details:
        - Protocol Type: DIRECT
        - Direct IPv4 Configuration: Specifies the Equinix Interface IP (equinixIfaceIp) with the value '99.65.179.45/30'.
    """
    utils.pr_yellow('\nConfigure Routing Protocol Detail by UUID')
    routing_protocol_request = module.RoutingProtocolDirectType(
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

    This function performs the following steps:
    1. Prints a message indicating that the deletion of the Fabric Cloud Router 
       to Azure connection is about to begin. The message is printed in yellow for visibility.
    2. Calls the `delete_connection` method from the `connection_management` module 
       to delete the specified Fabric Cloud Router to Azure connection.
    """
    utils.pr_yellow('\nDelete Fabric Cloud Router to Azure Connection')
    time.sleep(20)
    connection_management.delete_connection(fcr2azure)

    """
    Deletes a Fabric Cloud Router (FCR) with the specified UUID.

    This method handles the deletion of a Fabric Cloud Router by calling the
    relevant function in the `cloud_router_management` module. It first prints
    a message to the console indicating the start of the deletion process,
    using a yellow color for emphasis. After that, it proceeds to delete the
    specified Fabric Cloud Router.
    """
    utils.pr_yellow('\nDelete Fabric Cloud Router')
    time.sleep(20)
    cloud_router_management.delete_fcr(fcr_uuid)
