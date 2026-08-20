# AppDomainChangeOperation

App Domain change operation data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | [**PrecisionTimeChangeOperationOp**](PrecisionTimeChangeOperationOp.md) |  | 
**path** | [**AppDomainChangeOperationPath**](AppDomainChangeOperationPath.md) |  | 
**value** | **object** | new value for updated parameter | 

## Example

```python
from equinix.services.fabricv4.models.app_domain_change_operation import AppDomainChangeOperation

# TODO update the JSON string below
json = "{}"
# create an instance of AppDomainChangeOperation from a JSON string
app_domain_change_operation_instance = AppDomainChangeOperation.from_json(json)
# print the JSON string representation of the object
print(AppDomainChangeOperation.to_json())

# convert the object into a dict
app_domain_change_operation_dict = app_domain_change_operation_instance.to_dict()
# create an instance of AppDomainChangeOperation from a dict
app_domain_change_operation_from_dict = AppDomainChangeOperation.from_dict(app_domain_change_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


