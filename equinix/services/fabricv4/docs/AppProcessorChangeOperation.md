# AppProcessorChangeOperation

App Processor change operation data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | [**AppDomainChangeOperationOp**](AppDomainChangeOperationOp.md) |  | 
**path** | [**AppProcessorChangeOperationPath**](AppProcessorChangeOperationPath.md) |  | 
**value** | **object** | new value for updated parameter | 

## Example

```python
from equinix.services.fabricv4.models.app_processor_change_operation import AppProcessorChangeOperation

# TODO update the JSON string below
json = "{}"
# create an instance of AppProcessorChangeOperation from a JSON string
app_processor_change_operation_instance = AppProcessorChangeOperation.from_json(json)
# print the JSON string representation of the object
print(AppProcessorChangeOperation.to_json())

# convert the object into a dict
app_processor_change_operation_dict = app_processor_change_operation_instance.to_dict()
# create an instance of AppProcessorChangeOperation from a dict
app_processor_change_operation_from_dict = AppProcessorChangeOperation.from_dict(app_processor_change_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


