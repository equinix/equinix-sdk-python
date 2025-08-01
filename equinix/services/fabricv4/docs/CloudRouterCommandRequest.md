# CloudRouterCommandRequest

Fabric Cloud Router Command Request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination** | **str** | Fabric Cloud Router Ping Command Destination | 
**source_connection** | [**CloudRouterCommandRequestConnection**](CloudRouterCommandRequestConnection.md) |  | 
**timeout** | **int** | Timeout in seconds for Fabric Cloud Router Ping or Traceroute Command | [optional] 
**data_bytes** | **int** | Fabric Cloud Router Ping Command DataBytes | [optional] [default to 64]
**interval** | **int** | Time in milliseconds between sending each packet for Fabric Cloud Router Ping Command | [optional] [readonly] [default to 1000]
**count** | **int** | Total number of ping requests for Fabric Cloud Router Ping Command | [optional] [readonly] [default to 5]
**probes** | **int** | Number of probes to send for Fabric Cloud Router Traceroute Command | [optional] [default to 3]
**hops_max** | **int** | Maximum number of hops for Fabric Cloud Router Traceroute Command | [optional] [default to 20]

## Example

```python
from equinix.services.fabricv4.models.cloud_router_command_request import CloudRouterCommandRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CloudRouterCommandRequest from a JSON string
cloud_router_command_request_instance = CloudRouterCommandRequest.from_json(json)
# print the JSON string representation of the object
print(CloudRouterCommandRequest.to_json())

# convert the object into a dict
cloud_router_command_request_dict = cloud_router_command_request_instance.to_dict()
# create an instance of CloudRouterCommandRequest from a dict
cloud_router_command_request_from_dict = CloudRouterCommandRequest.from_dict(cloud_router_command_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


