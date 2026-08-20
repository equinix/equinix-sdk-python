# EnvironmentActionResponse

Response from environment action <sup color='red'>Beta</sup></font>

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Environment action URI | [optional] [readonly] 
**type** | [**EnvironmentActionTypeEnum**](EnvironmentActionTypeEnum.md) |  | [optional] 
**uuid** | **str** | Equinix-assigned action identifier | [optional] 
**state** | [**EnvironmentActionStateEnum**](EnvironmentActionStateEnum.md) |  | [optional] 
**key_details** | [**ActivationKeyDetails**](ActivationKeyDetails.md) |  | [optional] 
**change_log** | [**Changelog**](Changelog.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.environment_action_response import EnvironmentActionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentActionResponse from a JSON string
environment_action_response_instance = EnvironmentActionResponse.from_json(json)
# print the JSON string representation of the object
print(EnvironmentActionResponse.to_json())

# convert the object into a dict
environment_action_response_dict = environment_action_response_instance.to_dict()
# create an instance of EnvironmentActionResponse from a dict
environment_action_response_from_dict = EnvironmentActionResponse.from_dict(environment_action_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


