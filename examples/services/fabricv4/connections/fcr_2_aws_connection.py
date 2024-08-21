import time
import os

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

    Construct a `CloudRouterPostRequest` object using the `module.CloudRouterPostRequest` class.
    This object contains the details required to create the Fabric Cloud Router.
    """

    utils.pr_yellow('\nCreate Fabric Cloud Router')
    fcr_request = CloudRouterPostRequest(
        type="XF_ROUTER",
        name="fcrtoawsfcr_01",
        location={"metro_code": "SV"},
        package={"code": "STANDARD"},
        order={"purchase_order_number": "1-1453534"},
        project={"project_id": "xxxx22-xxxx-xxxx-xxxx"},
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
        Create a Fabric Cloud Router (FCR) to AWS Connection.
        
        This method creates a connection from an Equinix Fabric Cloud Router (FCR) to an AWS service provider using 
        the Equinix API. The connection is established by specifying various parameters such as connection type, 
        bandwidth, redundancy priority, and the details of both the A-side (Cloud Router) and Z-side (AWS service 
        provider).
        """
    utils.pr_yellow('\nCreate Fabric Cloud Router to AWS Connection')
    fcr2aws_request = ConnectionPostRequest(
        type="IP_VC",
        name="fcr2aws_conn_python_01",
        bandwidth=50,
        redundancy={
            "priority": "PRIMARY"
        },
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
                "type": "SP",
                "profile": {
                    "type": "L2_PROFILE",
                    "uuid": "3435fefrr-4534ffvrt-45345dvff-cvvvv"
                },
                "location": {
                    "metroCode": "SV"
                },
                "sellerRegion": "us-west-1",
                "authenticationKey": os.getenv("AWS_AUTH_KEY")
            }
        },
        project={"project_id": "xxxx22-xxxx-xxxx-xxxx"},
        notifications=[
            {
                "type": "ALL",
                "emails": [
                    "test@test.com"
                ]
            }
        ]
    )
    fcr2aws = connection_management.create_fcr_connection(fcr_uuid, fcr2aws_request)

    """Configures a routing protocol for a Fabric Cloud Router (FCR) to AWS connection identified by the provided 
    connection UUID.

        This method is designed to configure the routing protocol details for an existing connection between a Fabric 
        Cloud Router and AWS. It uses the `connection_uuid` to identify the connection and applies the specified 
        routing protocol settings.

        The routing protocol configuration includes the following details:
        - Protocol Type: DIRECT
        - Direct IPv4 Configuration: Specifies the Equinix Interface IP (equinixIfaceIp) with the value '99.65.179.45/30'.
    """
    utils.pr_yellow('\nConfigure Routing Protocol Detail by UUID')
    routing_protocol_request = RoutingProtocolDirectType(
        type="DIRECT",
        directIpv4={
            "equinixIfaceIp": 'ip'
        }
    )
    connection_management.configure_routing_protocol(fcr2aws, routing_protocol_request)

    """
    Accepts an AWS connection from the Equinix Fabric using the AWS_ACCESS_KEY and AWS_SECRET_KEY.

    This method updates the connection details of an existing AWS connection in the Equinix Fabric by using the 
    provided AWS credentials. It performs the following steps:
    
    1. Displays a message indicating that the name details will be updated using the Connection UUID. 
    2. Constructs a `ConnectionChangeOperation` object that specifies the operation to add AWS credentials to the 
    connection. 
    3. The `ConnectionChangeOperation` object is populated with AWS_ACCESS_KEY and AWS_SECRET_KEY fetched from the 
    environment variables. 

    Environment Variables:
    - AWS_ACCESS_KEY: The AWS access key required to authenticate the connection.
    - AWS_SECRET_KEY: The AWS secret key required to authenticate the connection.
    """
    utils.pr_yellow('\nAccepting AWS Connection using AWS_ACCESS_KEY and AWS_SECRET_KEY')
    aws_accept_connection = [module.ConnectionChangeOperation(
        op="add",
        path="",
        value={
            "additionalInfo": [
                {
                    "key": "accessKey",
                    "value": os.getenv("AWS_ACCESS_KEY")
                },
                {
                    "key": "secretKey",
                    "value": os.getenv("AWS_SECRET_KEY")
                }
            ]
        }
    )
    ]
    connection_management.update_connection_details_by_uuid(fcr2aws, aws_accept_connection)

    """
    Retrieves the connection details for a Fabric Cloud Router (FCR) to AWS connection by its UUID.
    This method is primarily used to fetch detailed information about a specific connection between 
    a Fabric Cloud Router and AWS, using the connection's unique identifier (UUID). 
    """
    utils.pr_yellow('\nGet FCR2AWS Connection Details by UUID')
    time.sleep(120)
    connection_management.get_connection_details_by_uuid(fcr2aws)

    """
    Deletes a Fabric Cloud Router (FCR) to AWS connection.

    This function performs the following steps:
    1. Prints a message indicating that the deletion of the Fabric Cloud Router 
       to AWS connection is about to begin. The message is printed in yellow for visibility.
    2. Calls the `delete_connection` method from the `connection_management` module 
       to delete the specified Fabric Cloud Router to AWS connection.
    """
    utils.pr_yellow('\nDelete Fabric Cloud Router to AWS Connection')
    time.sleep(20)
    connection_management.delete_connection(fcr2aws)

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
