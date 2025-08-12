# CloudRouterCommandRequestResponse

Fabric Cloud Router Command Request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination** | **str** | Fabric Cloud Router Ping or Traceroute Command Destination | [optional] 
**source_connection** | [**CloudRouterCommandRequestConnection**](CloudRouterCommandRequestConnection.md) |  | [optional] 
**timeout** | **int** | Timeout in seconds for Fabric Cloud Router Command:   - For &#x60;PING_COMMAND&#x60;: Packet timeout duration. The default value is 5.   - For &#x60;TRACEROUTE_COMMAND&#x60;: Probe timeout duration.     The default value is 2 and it is not configurable.  | [optional] 
**data_bytes** | **int** | Ping Command DataBytes.  This field is only applicable for commands of type &#x60;PING_COMMAND&#x60;.  | [optional] [default to 64]
**interval** | **int** | Time in milliseconds between sending each packet. This field is only applicable for commands of type &#x60;PING_COMMAND&#x60;.  | [optional] [default to 1000]
**count** | **int** | Total number of ping requests. This field is only applicable for commands of type &#x60;PING_COMMAND&#x60;.  | [optional] [default to 5]
**probes** | **int** | Number of probes for Fabric Cloud Router Traceroute Command. This field is only applicable for commands of type &#x60;TRACEROUTE_COMMAND&#x60; and is not configurable.  | [optional] [default to 3]
**hops_max** | **int** | Maximum number of hops for the traceroute command. This field is only applicable for commands of type &#x60;TRACEROUTE_COMMAND&#x60;.  | [optional] [default to 20]

## Example

```python
from equinix.services.fabricv4.models.cloud_router_command_request_response import CloudRouterCommandRequestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CloudRouterCommandRequestResponse from a JSON string
cloud_router_command_request_response_instance = CloudRouterCommandRequestResponse.from_json(json)
# print the JSON string representation of the object
print(CloudRouterCommandRequestResponse.to_json())

# convert the object into a dict
cloud_router_command_request_response_dict = cloud_router_command_request_response_instance.to_dict()
# create an instance of CloudRouterCommandRequestResponse from a dict
cloud_router_command_request_response_from_dict = CloudRouterCommandRequestResponse.from_dict(cloud_router_command_request_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


