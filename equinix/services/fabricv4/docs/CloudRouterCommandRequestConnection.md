# CloudRouterCommandRequestConnection

Connection object for Cloud Router Command

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Connection UUID | 

## Example

```python
from equinix.services.fabricv4.models.cloud_router_command_request_connection import CloudRouterCommandRequestConnection

# TODO update the JSON string below
json = "{}"
# create an instance of CloudRouterCommandRequestConnection from a JSON string
cloud_router_command_request_connection_instance = CloudRouterCommandRequestConnection.from_json(json)
# print the JSON string representation of the object
print(CloudRouterCommandRequestConnection.to_json())

# convert the object into a dict
cloud_router_command_request_connection_dict = cloud_router_command_request_connection_instance.to_dict()
# create an instance of CloudRouterCommandRequestConnection from a dict
cloud_router_command_request_connection_from_dict = CloudRouterCommandRequestConnection.from_dict(cloud_router_command_request_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


