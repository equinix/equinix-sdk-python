# CloudRouterCommandRequestPayload

Fabric Cloud Router Command Request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination** | **str** | Fabric Cloud Router Ping or Traceroute Command Destination | 
**source_connection** | [**CloudRouterCommandRequestConnection**](CloudRouterCommandRequestConnection.md) |  | 
**timeout** | **int** | Timeout in seconds for Fabric Cloud Router Command:   - For &#x60;PING_COMMAND&#x60;: Packet timeout duration. The default value is 5.   - For &#x60;TRACEROUTE_COMMAND&#x60;: Probe timeout duration.     The default value is 2 and it is not configurable.  | [optional] 
**data_bytes** | **int** | Ping Command DataBytes.  This field is only applicable for commands of type &#x60;PING_COMMAND&#x60;.  | [optional] [default to 64]
**probes** | **int** | Number of probes for Fabric Cloud Router Traceroute Command. This field is only applicable for commands of type &#x60;TRACEROUTE_COMMAND&#x60; and is not configurable.  | [optional] [default to 3]
**hops_max** | **int** | Maximum number of hops for the traceroute command. This field is only applicable for commands of type &#x60;TRACEROUTE_COMMAND&#x60;.  | [optional] [default to 20]

## Example

```python
from equinix.services.fabricv4.models.cloud_router_command_request_payload import CloudRouterCommandRequestPayload

# TODO update the JSON string below
json = "{}"
# create an instance of CloudRouterCommandRequestPayload from a JSON string
cloud_router_command_request_payload_instance = CloudRouterCommandRequestPayload.from_json(json)
# print the JSON string representation of the object
print(CloudRouterCommandRequestPayload.to_json())

# convert the object into a dict
cloud_router_command_request_payload_dict = cloud_router_command_request_payload_instance.to_dict()
# create an instance of CloudRouterCommandRequestPayload from a dict
cloud_router_command_request_payload_from_dict = CloudRouterCommandRequestPayload.from_dict(cloud_router_command_request_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


