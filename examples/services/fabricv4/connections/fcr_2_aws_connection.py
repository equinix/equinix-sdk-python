import time
import os

from equinix.services.fabricv4 import (CloudRouterPostRequest, ConnectionPostRequest,
                                       RoutingProtocolDirectType, ConnectionChangeOperation)
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
    """
    utils.pr_yellow('\nAccepting AWS Connection using AWS_ACCESS_KEY and AWS_SECRET_KEY')
    aws_accept_connection = [ConnectionChangeOperation(
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
    """
    utils.pr_yellow('\nDelete Fabric Cloud Router to AWS Connection')
    time.sleep(20)
    connection_management.delete_connection(fcr2aws)

    """
    Deletes a Fabric Cloud Router (FCR) with the specified UUID.
    """
    utils.pr_yellow('\nDelete Fabric Cloud Router')
    time.sleep(20)
    cloud_router_management.delete_fcr(fcr_uuid)
