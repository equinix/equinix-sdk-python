# LoaActionResponse

Action Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Action URI | [optional] 
**uuid** | **str** | Action Identifier | [optional] 
**state** | [**LoaActionState**](LoaActionState.md) |  | [optional] 
**type** | [**LoaActionType**](LoaActionType.md) |  | [optional] 
**data** | [**LoaActionData**](LoaActionData.md) |  | [optional] 
**change_log** | [**LoaChangelog**](LoaChangelog.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.loa_action_response import LoaActionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LoaActionResponse from a JSON string
loa_action_response_instance = LoaActionResponse.from_json(json)
# print the JSON string representation of the object
print(LoaActionResponse.to_json())

# convert the object into a dict
loa_action_response_dict = loa_action_response_instance.to_dict()
# create an instance of LoaActionResponse from a dict
loa_action_response_from_dict = LoaActionResponse.from_dict(loa_action_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


