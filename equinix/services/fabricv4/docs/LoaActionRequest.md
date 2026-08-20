# LoaActionRequest

Action Request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**LoaActionType**](LoaActionType.md) |  | 
**data** | [**LoaActionData**](LoaActionData.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.loa_action_request import LoaActionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LoaActionRequest from a JSON string
loa_action_request_instance = LoaActionRequest.from_json(json)
# print the JSON string representation of the object
print(LoaActionRequest.to_json())

# convert the object into a dict
loa_action_request_dict = loa_action_request_instance.to_dict()
# create an instance of LoaActionRequest from a dict
loa_action_request_from_dict = LoaActionRequest.from_dict(loa_action_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


