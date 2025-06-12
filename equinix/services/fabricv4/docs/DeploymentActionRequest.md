# DeploymentActionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**DeploymentActionType**](DeploymentActionType.md) |  | 
**data** | [**List[ActionRequest]**](ActionRequest.md) |  | 

## Example

```python
from equinix.services.fabricv4.models.deployment_action_request import DeploymentActionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentActionRequest from a JSON string
deployment_action_request_instance = DeploymentActionRequest.from_json(json)
# print the JSON string representation of the object
print(DeploymentActionRequest.to_json())

# convert the object into a dict
deployment_action_request_dict = deployment_action_request_instance.to_dict()
# create an instance of DeploymentActionRequest from a dict
deployment_action_request_from_dict = DeploymentActionRequest.from_dict(deployment_action_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


