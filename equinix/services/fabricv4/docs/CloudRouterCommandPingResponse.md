# CloudRouterCommandPingResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**output** | **str** |  | [optional] 
**output_structured_ping** | [**OutputStructuredPing**](OutputStructuredPing.md) |  | [optional] 
**errors** | [**List[Error]**](Error.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cloud_router_command_ping_response import CloudRouterCommandPingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CloudRouterCommandPingResponse from a JSON string
cloud_router_command_ping_response_instance = CloudRouterCommandPingResponse.from_json(json)
# print the JSON string representation of the object
print(CloudRouterCommandPingResponse.to_json())

# convert the object into a dict
cloud_router_command_ping_response_dict = cloud_router_command_ping_response_instance.to_dict()
# create an instance of CloudRouterCommandPingResponse from a dict
cloud_router_command_ping_response_from_dict = CloudRouterCommandPingResponse.from_dict(cloud_router_command_ping_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


