# EnvironmentActionRequest

Request payload for environment action

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**EnvironmentActionTypeEnum**](EnvironmentActionTypeEnum.md) |  | 
**key_details** | [**ActivationKeyDetails**](ActivationKeyDetails.md) |  | 

## Example

```python
from equinix.services.fabricv4.models.environment_action_request import EnvironmentActionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentActionRequest from a JSON string
environment_action_request_instance = EnvironmentActionRequest.from_json(json)
# print the JSON string representation of the object
print(EnvironmentActionRequest.to_json())

# convert the object into a dict
environment_action_request_dict = environment_action_request_instance.to_dict()
# create an instance of EnvironmentActionRequest from a dict
environment_action_request_from_dict = EnvironmentActionRequest.from_dict(environment_action_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


