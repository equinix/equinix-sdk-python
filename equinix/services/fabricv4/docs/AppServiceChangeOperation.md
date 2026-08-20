# AppServiceChangeOperation

App Service change operation data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | [**PrecisionTimeChangeOperationOp**](PrecisionTimeChangeOperationOp.md) |  | 
**path** | [**AppServiceChangeOperationPath**](AppServiceChangeOperationPath.md) |  | 
**value** | **object** | new value for updated parameter | 

## Example

```python
from equinix.services.fabricv4.models.app_service_change_operation import AppServiceChangeOperation

# TODO update the JSON string below
json = "{}"
# create an instance of AppServiceChangeOperation from a JSON string
app_service_change_operation_instance = AppServiceChangeOperation.from_json(json)
# print the JSON string representation of the object
print(AppServiceChangeOperation.to_json())

# convert the object into a dict
app_service_change_operation_dict = app_service_change_operation_instance.to_dict()
# create an instance of AppServiceChangeOperation from a dict
app_service_change_operation_from_dict = AppServiceChangeOperation.from_dict(app_service_change_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


