# AppServiceChange

Current state of latest AppService change

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Uniquely identifies a change | [optional] 
**type** | [**AppServiceChangeType**](AppServiceChangeType.md) |  | 
**status** | [**PortChangeStatus**](PortChangeStatus.md) |  | [optional] 
**created_date_time** | **datetime** | Set when change flow starts | [optional] 
**updated_date_time** | **datetime** | Set when change object is updated | 
**data** | [**List[AppServiceChangeOperation]**](AppServiceChangeOperation.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.app_service_change import AppServiceChange

# TODO update the JSON string below
json = "{}"
# create an instance of AppServiceChange from a JSON string
app_service_change_instance = AppServiceChange.from_json(json)
# print the JSON string representation of the object
print(AppServiceChange.to_json())

# convert the object into a dict
app_service_change_dict = app_service_change_instance.to_dict()
# create an instance of AppServiceChange from a dict
app_service_change_from_dict = AppServiceChange.from_dict(app_service_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


