# CloudRouterActionResponse

Cloud Router actions response object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**CloudRouterActionType**](CloudRouterActionType.md) |  | 
**uuid** | **str** |  | 
**description** | **str** |  | [optional] 
**state** | [**CloudRouterActionState**](CloudRouterActionState.md) |  | 
**change_log** | [**Changelog**](Changelog.md) |  | 
**href** | **str** |  | [optional] 
**connection** | [**RouterActionsConnection**](RouterActionsConnection.md) |  | [optional] 
**operation** | [**Operation**](Operation.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cloud_router_action_response import CloudRouterActionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CloudRouterActionResponse from a JSON string
cloud_router_action_response_instance = CloudRouterActionResponse.from_json(json)
# print the JSON string representation of the object
print(CloudRouterActionResponse.to_json())

# convert the object into a dict
cloud_router_action_response_dict = cloud_router_action_response_instance.to_dict()
# create an instance of CloudRouterActionResponse from a dict
cloud_router_action_response_form_dict = cloud_router_action_response.from_dict(cloud_router_action_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


