# CloudRouterActionRequest

Cloud Router action request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**CloudRouterActionType**](CloudRouterActionType.md) |  | 

## Example

```python
from equinix.services.fabricv4.models.cloud_router_action_request import CloudRouterActionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CloudRouterActionRequest from a JSON string
cloud_router_action_request_instance = CloudRouterActionRequest.from_json(json)
# print the JSON string representation of the object
print(CloudRouterActionRequest.to_json())

# convert the object into a dict
cloud_router_action_request_dict = cloud_router_action_request_instance.to_dict()
# create an instance of CloudRouterActionRequest from a dict
cloud_router_action_request_from_dict = CloudRouterActionRequest.from_dict(cloud_router_action_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


