# AppProcessorChange

Current state of latest AppProcessor change

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Uniquely identifies a change | [optional] 
**type** | [**AppProcessorChangeType**](AppProcessorChangeType.md) |  | 
**status** | [**PortChangeStatus**](PortChangeStatus.md) |  | [optional] 
**created_date_time** | **datetime** | Set when change flow starts | [optional] 
**updated_date_time** | **datetime** | Set when change object is updated | 
**data** | [**List[AppProcessorChangeOperation]**](AppProcessorChangeOperation.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.app_processor_change import AppProcessorChange

# TODO update the JSON string below
json = "{}"
# create an instance of AppProcessorChange from a JSON string
app_processor_change_instance = AppProcessorChange.from_json(json)
# print the JSON string representation of the object
print(AppProcessorChange.to_json())

# convert the object into a dict
app_processor_change_dict = app_processor_change_instance.to_dict()
# create an instance of AppProcessorChange from a dict
app_processor_change_from_dict = AppProcessorChange.from_dict(app_processor_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


