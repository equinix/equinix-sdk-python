# AppDomainChange

Current state of latest AppDomain change

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Uniquely identifies a change | [optional] 
**type** | [**AppDomainChangeType**](AppDomainChangeType.md) |  | 
**status** | [**PortChangeStatus**](PortChangeStatus.md) |  | [optional] 
**created_date_time** | **datetime** | Set when change flow starts | [optional] 
**updated_date_time** | **datetime** | Set when change object is updated | 
**data** | [**List[AppDomainChangeOperation]**](AppDomainChangeOperation.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.app_domain_change import AppDomainChange

# TODO update the JSON string below
json = "{}"
# create an instance of AppDomainChange from a JSON string
app_domain_change_instance = AppDomainChange.from_json(json)
# print the JSON string representation of the object
print(AppDomainChange.to_json())

# convert the object into a dict
app_domain_change_dict = app_domain_change_instance.to_dict()
# create an instance of AppDomainChange from a dict
app_domain_change_from_dict = AppDomainChange.from_dict(app_domain_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


