# AppLinkChange

Current state of latest AppLink change

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Uniquely identifies a change | [optional] 
**type** | [**AppLinkChangeType**](AppLinkChangeType.md) |  | 
**status** | [**PortChangeStatus**](PortChangeStatus.md) |  | [optional] 
**created_date_time** | **datetime** | Set when change flow starts | [optional] 
**updated_date_time** | **datetime** | Set when change object is updated | 
**data** | [**List[AppLinkChangeOperation]**](AppLinkChangeOperation.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.app_link_change import AppLinkChange

# TODO update the JSON string below
json = "{}"
# create an instance of AppLinkChange from a JSON string
app_link_change_instance = AppLinkChange.from_json(json)
# print the JSON string representation of the object
print(AppLinkChange.to_json())

# convert the object into a dict
app_link_change_dict = app_link_change_instance.to_dict()
# create an instance of AppLinkChange from a dict
app_link_change_from_dict = AppLinkChange.from_dict(app_link_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


