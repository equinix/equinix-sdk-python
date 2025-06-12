# ActionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**AWSPermissionType**](AWSPermissionType.md) |  | 
**role_arn** | **str** |  | 
**region** | **str** |  | 
**deployment_properties** | [**TopologyProperties**](TopologyProperties.md) |  | 
**project_id** | **str** |  | 
**provider_id** | **str** |  | 
**pool_id** | **str** |  | 

## Example

```python
from equinix.services.fabricv4.models.action_request import ActionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ActionRequest from a JSON string
action_request_instance = ActionRequest.from_json(json)
# print the JSON string representation of the object
print(ActionRequest.to_json())

# convert the object into a dict
action_request_dict = action_request_instance.to_dict()
# create an instance of ActionRequest from a dict
action_request_from_dict = ActionRequest.from_dict(action_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


