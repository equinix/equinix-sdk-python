from examples.services.fabricv4.utils import utils
from equinix.services import fabricv4
import cloud_router_management


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
        name="Python_FCR",
        location={"metro_code": "SV"},
        package={"code": "STANDARD"},
        order={"purchase_order_number": "1-14535"},
        project={"project_id": "123456877663"},
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
    Retrieve the details of a Fabric Cloud Router using its UUID.

    This method fetches and returns the detailed information associated with a specific
    Fabric Cloud Router, identified by its UUID. It interacts with the Equinix Fabric API
    to retrieve the cloud router's data, such as its configuration, status, and related
    connections.
    """

    utils.pr_yellow('\nGet Fabric Cloud Router Details by UUID')
    cloud_router_management.get_fcr_uuid(fcr_uuid)

    """
    Updates the name of a Fabric Cloud Router (FCR) using its UUID.
    
    This method performs an update operation on a specified Fabric Cloud Router by replacing
    the current name with a new one. It leverages the Equinix Fabric API to execute this change.
    """

    update_name = [CloudRouterChangeOperation(
        op="replace",
        path="/name",
        value="panthers-test-updated1"
    )]
    cloud_router_management.update_fcr_by_uuid(fcr_uuid,update_name)

    """
    Deletes a Fabric Cloud Router (FCR) with the specified UUID.

    This method handles the deletion of a Fabric Cloud Router by calling the
    relevant function in the `cloud_router_management` module. It first prints
    a message to the console indicating the start of the deletion process,
    using a yellow color for emphasis. After that, it proceeds to delete the
    specified Fabric Cloud Router.
    
    """
    utils.pr_yellow('\nDelete Fabric Cloud Router')
    cloud_router_management.delete_fcr(fcr_uuid)

