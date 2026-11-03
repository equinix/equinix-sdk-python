# Change

Current state of latest connection change

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Uniquely identifies a change | [optional] 
**type** | [**ChangeType**](ChangeType.md) |  | 
**status** | [**ChangeStatus**](ChangeStatus.md) |  | [optional] 
**created_date_time** | **datetime** | Set when change flow starts | 
**updated_date_time** | **datetime** | Set when change object is updated | [optional] 
**information** | **str** | Additional information | [optional] 
**data** | [**ConnectionChangeOperation**](ConnectionChangeOperation.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.change import Change

# TODO update the JSON string below
json = "{}"
# create an instance of Change from a JSON string
change_instance = Change.from_json(json)
# print the JSON string representation of the object
print(Change.to_json())

# convert the object into a dict
change_dict = change_instance.to_dict()
# create an instance of Change from a dict
change_from_dict = Change.from_dict(change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


