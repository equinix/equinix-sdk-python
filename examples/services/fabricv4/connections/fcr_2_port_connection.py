import time

from examples.services.fabricv4.utils import utils
from equinix.services import fabricv4
from examples.services.fabricv4.cloud_router import cloud_router_management
from examples.services.fabricv4.connections import connection_management

if __name__ == "__main__":
    """
    Create a Fabric Cloud Router (FCR) using the Equinix Fabric API.

    This method sends a request to create a new Fabric Cloud Router with specified configurations 
    such as router type, name, location, package, and associated project and account details. 
    Notifications are also configured to receive updates regarding the router.
    """
    utils.pr_yellow('\nCreate Fabric Cloud Router')
    fcr_request = CloudRouterPostRequest(
        type="XF_ROUTER",
        name="fcrtoportfcr_01",
        location={"metro_code": "SV"},
        package={"code": "STANDARD"},
        order={"purchase_order_number": "1-1453534"},
        project={"project_id": "1232432542545435"},
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
        Create a Fabric Cloud Router (FCR) to Colo Port Connection.
        
        This method creates a connection from an Equinix Fabric Cloud Router (FCR) to an Colo Equinix Port using 
        the Equinix API. The connection is established by specifying various parameters such as connection type, 
        bandwidth, redundancy priority, and the details of both the A-side (Cloud Router) and Z-side (Equinix Port).
        """
    utils.pr_yellow('\nCreate Fabric Cloud Router to Colo Connection')
    fcr2colo_request = ConnectionPostRequest(
        type="IP_VC",
        name="fcr2port_conn_python_01",
        bandwidth=10,
        a_side={
            "accessPoint": {
                "type": "CLOUD_ROUTER",
                "router": {
                    "uuid": fcr_uuid
                }
            }
        },
        z_side={
            "accessPoint": {
                "type": "COLO",
                "port": {
                    "uuid": "xxxx22-xxxx-xxxx-xxxx"
                },
                "linkProtocol": {
                    "type": "DOT1Q",
                    "vlanTag": 3200
                }
            }
        },
        project={"project_id": "1232432542545435"},
        notifications=[
            {
                "type": "ALL",
                "emails": [
                    "test@test.com"
                ]
            }
        ]
    )
    fcr2colo = connection_management.create_fcr_connection(fcr_uuid, fcr2colo_request)

    """
    Configures a routing protocol for a Fabric Cloud Router (FCR) to Port connection identified by the provided 
    connection UUID.
    """
    utils.pr_yellow('\nConfigure Routing Protocol Detail by UUID')
    routing_protocol_request = RoutingProtocolDirectType(
        type="DIRECT",
        directIpv4={
            "equinixIfaceIp": 'ip'
        }
    )
    connection_management.configure_routing_protocol(fcr2colo, routing_protocol_request)

    """
    Retrieves the connection details for a Fabric Cloud Router (FCR) to Port connection by its UUID.
    This method is primarily used to fetch detailed information about a specific connection between 
    a Fabric Cloud Router and Port, using the connection's unique identifier (UUID). 
    """
    utils.pr_yellow('\nGet FCR2Port Connection Details by UUID')
    connection_management.get_connection_details_by_uuid(fcr2colo)

    """
    Updates the name details of a connection using the provided Connection UUID.

    This function changes the name attribute of an existing connection name to "fcr2PortUpdate" 
    by performing a "replace" operation on the connection's name field. The connection is 
    identified by its UUID, passed as the `fcr2colo` parameter.
    """
    utils.pr_yellow('\nUpdate Name Details Using Connection_UUID')
    port_conn_name_update = [ConnectionChangeOperation(
            op="replace",
            path="/name",
            value="fcr2PortUpdate"
        )
    ]
    connection_management.update_connection_details_by_uuid(fcr2colo,port_conn_name_update)

    """
    Updates the bandwidth details of a connection using the provided Connection UUID.
    """
    utils.pr_yellow('\nUpdate Bandwidth Details Using Connection_UUID')
    port_conn_bandwidth_update = [ConnectionChangeOperation(
            op="replace",
            path="/bandwidth",
            value=50
        )
    ]
    connection_management.update_connection_details_by_uuid(fcr2colo,port_conn_bandwidth_update)

    """
    Deletes a Fabric Cloud Router (FCR) to Port Colo connection.
    """
    utils.pr_yellow('\nDelete Fabric Cloud Router to Colo Connection')
    time.sleep(60)
    connection_management.delete_connection(fcr2colo)

    """
    Deletes a Fabric Cloud Router (FCR) with the specified UUID.
    """
    utils.pr_yellow('\nDelete Fabric Cloud Router')
    cloud_router_management.delete_fcr(fcr_uuid)