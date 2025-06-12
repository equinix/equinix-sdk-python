# CloudRouterCommandTracerouteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**output** | **str** |  | [optional] 
**output_structured_traceroute** | [**OutputStructuredTraceroute**](OutputStructuredTraceroute.md) |  | [optional] 
**errors** | [**List[Error]**](Error.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cloud_router_command_traceroute_response import CloudRouterCommandTracerouteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CloudRouterCommandTracerouteResponse from a JSON string
cloud_router_command_traceroute_response_instance = CloudRouterCommandTracerouteResponse.from_json(json)
# print the JSON string representation of the object
print(CloudRouterCommandTracerouteResponse.to_json())

# convert the object into a dict
cloud_router_command_traceroute_response_dict = cloud_router_command_traceroute_response_instance.to_dict()
# create an instance of CloudRouterCommandTracerouteResponse from a dict
cloud_router_command_traceroute_response_from_dict = CloudRouterCommandTracerouteResponse.from_dict(cloud_router_command_traceroute_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


